#!/bin/bash
#BVH_FOLDER="/home/erick/MotionProjs/lafan1/"
#FBX_FOLDER="/home/erick/MotionProjs/lafan1_fbx/"

#BVH_FOLDER="/home/erick/MotionProjs/zeggs/for_tpose/"
#FBX_FOLDER="/home/erick/MotionProjs/zeggs_tpose/"

#BVH_FOLDER="/home/erick/MotionProjs/cmu_balance_bvh/"
BVH_FOLDER="/home/erick/MotionProjs/cmu_temp/"
FBX_FOLDER="/home/erick/MotionProjs/cmu_balance_fbx/"

SCRIPT_PATH="/home/erick/MotionProjs/BlenderProjects/transform_cmu_bvh_to_fbx/BlenderScriptProject/convert_fbx.py"
for f in $(find $BVH_FOLDER -name '*.bvh')
do
  echo "Processing $f";
  /home/erick/Software/blender-3.4.1-linux-x64/blender -b --python $SCRIPT_PATH -- "$f" "$BVH_FOLDER" "$FBX_FOLDER";
done

echo "Finished"
