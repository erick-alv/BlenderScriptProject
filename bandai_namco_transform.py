import os
import sys
import bpy
from bpy import context





def import_bvh(bvh_filename):
    # Import the BVH file
    bpy.ops.import_anim.bvh(filepath=bvh_filename, filter_glob="*.bvh", global_scale=1, frame_start=1,
                            use_fps_scale=True,
                            use_cyclic=False, rotate_mode='NATIVE', axis_forward='-Z', axis_up='Y')

def export_fbx(fbx_filename):
    #  Export as FBX file
    bpy.ops.export_scene.fbx(filepath=fbx_filename, axis_forward='-Z', axis_up='Y', object_types={'ARMATURE'})


def estimate_frames():
    # check if actions is empty
    if bpy.data.actions:

        # get all actions
        action_list = [action.frame_range for action in bpy.data.actions]

        # sort, remove doubles and create a set
        keys = (sorted(set([item for sublist in action_list for item in sublist])))

        return int(keys[0]), int(keys[-1])

    else:
        raise Exception("No Keyframes")





def transform(bvh_in_filename, fbx_out_filename):
    scene = context.scene

    def select_only(obj_name):
        for objt in scene.objects:
            objt.select_set(False)
        bpy.data.objects[obj_name].select_set(True)


    import_bvh(bvh_in)
    frame_begin, frame_end = estimate_frames()
    main_armature_name = os.path.basename(bvh_in_filename)[:-4]

    # deselect all to then select just one
    select_only(main_armature_name)
    context.view_layer.objects.active = bpy.data.objects[main_armature_name]
    # put in edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    # unparent and delete root bone
    bpy.data.objects[main_armature_name].data.edit_bones['Hips'].parent = None
    bpy.data.objects[main_armature_name].data.edit_bones.remove(
        bpy.data.objects[main_armature_name].data.edit_bones['joint_Root'])

    # deselect all to then select just one
    select_only(main_armature_name)
    # put in pose mode
    bpy.ops.object.mode_set(mode='POSE')
    # select Hips bone
    bpy.data.objects[main_armature_name].data.bones.active = \
        bpy.data.objects[main_armature_name].data.bones["Hips"]

    # Add constraint
    bpy.ops.pose.constraint_add_with_targets(type='COPY_TRANSFORMS')
    # Reimport to have whole reference motion
    import_bvh(bvh_in)
    ref_armature_name = os.path.basename(bvh_in_filename)[:-4]+".001"

    #select main armature and set targets
    select_only(main_armature_name)
    bpy.context.view_layer.objects.active = bpy.data.objects[main_armature_name]
    bpy.context.object.pose.bones["Hips"].constraints["Copy Transforms"].target = bpy.data.objects[
        ref_armature_name]
    bpy.context.object.pose.bones["Hips"].constraints["Copy Transforms"].subtarget = "Hips"
    #bake action for creating animation
    bpy.ops.nla.bake(frame_start=frame_begin, frame_end=frame_end, bake_types={'POSE'}, clear_constraints=True,
                     visual_keying=True, only_selected=False)

    # deleting other objects
    bpy.ops.object.mode_set(mode='OBJECT')
    select_only(ref_armature_name)
    bpy.ops.object.delete()

    # delete empty object created during
    select_only("Empty")
    bpy.ops.object.delete()

    select_only(main_armature_name)
    export_fbx(fbx_out_filename)

#todo estimate frames
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "—"
bvh_in = argv[0]
bvh_in_folder = argv[1]
fbx_out_folder = argv[2]
rest_path = bvh_in[len(bvh_in_folder):]
fbx_out = os.path.join(fbx_out_folder, rest_path)[:-3] + "fbx"

dirs_out_path = os.path.dirname(fbx_out)
if not os.path.exists(dirs_out_path):
    os.makedirs(dirs_out_path)

transform(bvh_in, fbx_out)

#### bpy.data.armatures.remove(bpy.data.armatures[0])
