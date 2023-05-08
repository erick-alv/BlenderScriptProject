import sys
import bpy
import os

def trim_motion(bvh_in_filename, start_frame, end_frame, trimmed_path):
    bpy.ops.import_anim.bvh(filepath=bvh_in_filename, filter_glob="*.bvh", global_scale=1,
                            frame_start=1,
                            use_fps_scale=True,
                            use_cyclic=False,
                            rotate_mode='NATIVE')

    #for some reason when exporting the file blender is changing the orientation. Therefore apply here previously
    # the "counter-rotation"
    #rotation of -90 in x axis
    bpy.context.object.rotation_euler[0] = -1.5708
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    bpy.ops.export_anim.bvh(filepath=trimmed_path, frame_start=start_frame, frame_end=end_frame)


#Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "—"
#expects something like '*/40/40_11.bvh'
bvh_in = argv[0]
start_frame = int(argv[1])
end_frame = int(argv[2])
out_folder = argv[3]

#get output path
in_path_els = bvh_in.split(sep=os.sep)
if out_folder.endswith(os.sep):
    out_dir_path = out_folder #+ in_path_els[-2]
else:
    out_dir_path = out_folder + os.sep #+ in_path_els[-2]
if not os.path.exists(out_dir_path):
    os.makedirs(out_dir_path)

out_name = f"{in_path_els[-1][:-4]}_{start_frame}_{end_frame}.bvh"
trimmed_out = os.path.join(out_dir_path, out_name)

#bvh_in_filename = '/home/erick/MotionProjs/cmu_bvh/cmuconvert-mb2-40-45/40/40_11.bvh'
#start_frame = 38
#end_frame = 125
#trimmed_path = f'/home/erick/MotionProjs/40_11_{start_frame}_{end_frame}.bvh'

trim_motion(bvh_in, start_frame, end_frame, trimmed_out)