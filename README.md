# BlenderScriptProject

## Description
In this repo we share the different scripts that we used to process the motion capture files with Blender for our project.

These scripts were developed for Blender 3.4.1. In order to use them change the path to the Blender executable in the corresponding file. 

## Usage

In this repo we have different .sh files and .py files. The idea is to use the .sh files which call the corresponding python scripts. In each .sh file adjust the paths to the folders and scripts accordingly to your setup. In the following we give a brief description of each file:
- [trim_bvh_motions.sh](trim_bvh_motions.sh): we used this file to extract from the bvh files the sections that we want. The script has a process list. In this list each string is a element. Each string contains the path to the bvh file, the keyframe where the section starts and the keyframe where the section ends (each one separated by a space).
- [batch_bvh2fbx.sh](batch_bvh2fbx.sh): we use this scrip to transform the files from bvh to fbx. WIth this script we transformed the files of the CMU, ZEGGS and LAFAN1 database.
- [batch_namco_transform.sh](batch_namco_transform.sh): we use this specifically for the motions of the Bandai-Namco-Research-Motiondataset. It also transform bvh files to fbx files.
