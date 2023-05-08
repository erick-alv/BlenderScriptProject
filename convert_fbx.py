import sys
import bpy
import os


def transform_to_fbx(bvh_in_filename, fbx_out_filename):
    armature_name = os.path.basename(bvh_in_filename)[:-4]  # name of armature in blender when importing

    # Import the BVH file
    bpy.ops.import_anim.bvh(filepath=bvh_in_filename, filter_glob="*.bvh", global_scale=1, frame_start=1, use_fps_scale=True,
                            use_cyclic=False, rotate_mode='NATIVE', axis_forward='-Z', axis_up='Y')
    #  Export as FBX file
    bpy.ops.export_scene.fbx(filepath=fbx_out_filename, axis_forward='-Z', axis_up='Y', object_types={'ARMATURE'})

    ## DELETE object so ot is not exported in next iteration
    if bpy.context.object.mode == 'EDIT':
        bpy.ops.object.mode_set(mode='OBJECT')


#Get command line arguments
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

transform_to_fbx(bvh_in, fbx_out)