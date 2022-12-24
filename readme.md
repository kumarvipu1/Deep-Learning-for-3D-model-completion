# Deep Learning for 3D model completion

## Requirements:
- tensorflow
- numpy
- open3d
- pickle

Custom Dataset Preparation:
1. Use the notebook “DatasetPrep” notebook for preparing custom dataset.
2. Store “.obj” files of 3D models in the folder structure as shown below.

Main_Folder:
|-Sub_Folder:
|-Object_Folder1:
|-File11.obj
|-File12.obj…..
|-Object_Folder2:
|-File21.obj
|-File22.obj

3. Run the function ‘load_annotation’ to generate dataset_new.txt file with annotations.
arguments for load_annotation; root_label : (String) path of the main folder.

4. Run ‘build_dataset’ function to generate ‘pcd_dataset.pickle’ file for training the model.
Arguments: String(path of dataset_new.txt file).
Note: This step is not mandatory. Use this only if you want to train the model on your own 3D objects,
else you can use the pcsd_dataset.pickle file already provided in the project pack.

Training:
1. Use ‘train’ notebook to train the model.
2. Use the dataset ‘pcd_dataset.pickle’ as input.
3. The script saves the model weight in .h5 format that can be loaded later for inferencing.
4. Customize ‘numEpoch’ variable to change the number of epochs.

Note: Pre-trained weights are included with the project pack. Training the model is not mandatory.

Inferencing:

Use inferencing notebook to predict complete model from an incomplete 3D object.

Replace input_object variable with the .obj file you want to predict the output for.

Run infer function.

Output.obj file will be saved in the rood directory for further reference.
Note: The model is trained on GPU, so inferencing using pre-trained weights will work on GPU enabled
PC only. You can custom train the model on CPU to suit your requirement.