import bpy
import sys
import os
import glob



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
    # deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    # select the object
    bpy.data.objects[armature_name].select_set(True)
    # delete all selected objects
    bpy.ops.object.delete()






single_file = False

if single_file:
    bvh_in = ""
    fbx_out = ""
    transform_to_fbx(bvh_in, fbx_out)
else:

    # bvh_in_folder = "/home/erick/MotionProjs/cmu_bvh/"
    # fbx_out_folder = "/home/erick/MotionProjs/cmu_fbx/"
    bvh_in_folder = "/home/erick/MotionProjs/cmu_bvh/cmuconvert-mb2-46-56/"
    fbx_out_folder = "/home/erick/MotionProjs/cmu_fbx/cmuconvert-mb2-46-56/"
    keep_subfolders_structure = True

    bvh_files_list = glob.glob(glob.escape(bvh_in_folder) + "/**/*.bvh", recursive=True)
    for bvh_in in bvh_files_list:
        #print(bvh_in)
        if keep_subfolders_structure:
            rest_path = bvh_in[len(bvh_in_folder):]
            fbx_out = os.path.join(fbx_out_folder, rest_path)[:-3] + "fbx"
            dirs_out_path = os.path.dirname(fbx_out)
            if not os.path.exists(dirs_out_path):
                os.makedirs(dirs_out_path)
            #print(fbx_out)
            #print(dirs_out_path)

        else:
            fbx_out = os.path.join(fbx_out_folder, os.path.basename(bvh_in))[:-3] + "fbx"
            #print(fbx_out)
        transform_to_fbx(bvh_in, fbx_out)




print("!!!!!!!!!! Finished !!!!!!!!!!!!")