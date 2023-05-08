import os
import glob

# bvh_in_folder = "/home/erick/MotionProjs/cmu_bvh/cmuconvert-mb-40-45/"
# fbx_out_folder = "/home/erick/MotionProjs/cmu_fbx/cmuconvert-mb-40-45"
# bvh_in_folder = "/home/erick/MotionProjs/lafan1/"
# fbx_out_folder = "/home/erick/MotionProjs/lafan1_fbx"
bvh_in_folder = "/home/erick/MotionProjs/cmu_bvh/"
fbx_out_folder = "/home/erick/MotionProjs/cmu_fbx/"

keep_subfolders_structure = True

bvh_files_list = glob.glob(glob.escape(bvh_in_folder) + "/**/*.bvh", recursive=True)
for bvh_in in bvh_files_list:
    rest_path = bvh_in[len(bvh_in_folder):]
    fbx_out = os.path.join(fbx_out_folder, rest_path)[:-3] + "fbx"
    #dirs_out_path = os.path.dirname(fbx_out)
    if not os.path.exists(fbx_out):
        print(f"This file does not exist:\n{fbx_out}")
