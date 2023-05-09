#!/bin/bash
BVH_FOLDER="/home/erick/MotionProjs/Bandai-Namco-Research-Motiondataset/dataset/Bandai-Namco-Research-Motiondataset-2/data/"
FBX_FOLDER="/home/erick/MotionProjs/bandai_namco_fbx/"

SCRIPT_PATH="/home/erick/MotionProjs/BlenderProjects/transform_cmu_bvh_to_fbx/BlenderScriptProject/bandai_namco_transform.py"
for f in $(find $BVH_FOLDER -name '*.bvh')
do
  echo "Processing $f";
  /home/erick/Software/blender-3.4.1-linux-x64/blender -b --python $SCRIPT_PATH -- "$f" "$BVH_FOLDER" "$FBX_FOLDER";
done

echo "Finished"