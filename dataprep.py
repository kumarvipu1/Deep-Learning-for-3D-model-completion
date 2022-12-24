import numpy as np
import open3d as o3d
import copy
import os
import pickle


def load_annotation(root_label):
    subfolder1 = root_label
    annotation = []
    i = 0
    for items in os.listdir(subfolder1):
        label_path1 = os.path.join(root_label, items).replace('\\', '/')
        subfolder2 = [k.name for k in os.scandir(label_path1) if k.is_dir()]
        for files in subfolder2:
            label_path2 = os.path.join(label_path1, files).replace('\\', '/')
            print(label_path2)
            for files2 in os.listdir(label_path2):
                if i <= 100:
                    print(files2)
                    file_path = os.path.join(label_path2, files2).replace('\\', '/')
                    filename = file_path.replace('.obj', '.obj' + '\n')
                    annotation.append(filename)
                    i += 1
                else:
                    i = 0
                    break
    with open("dataset_new.txt", "w") as output:
        for element in annotation:
            output.write(element)
        output.close()

    return annotation

def read_paths(source_file):
    file = open(source_file, "r")
    content = file.read()
    content_list = content.split("\n")
    file.close()
    return content_list

def crop_mesh(mesh):
    mesh_cropped = copy.deepcopy(mesh)
    mesh_cropped.triangles = o3d.utility.Vector3iVector(
    np.asarray(mesh_cropped.triangles)[:len(mesh_cropped.triangles) // 2, :])
    mesh_cropped.triangle_normals = o3d.utility.Vector3dVector(
    np.asarray(mesh_cropped.triangle_normals)[:len(mesh_cropped.triangle_normals) // 2, :])
    return mesh_cropped

def build_dataset(source_file):
    dataset = {'X':[],'Y':[]}
    file_list = read_paths(source_file)
    for paths in file_list:
        print(paths)
        try:
            main_mesh = o3d.io.read_triangle_mesh(paths)
            main_pcd = main_mesh.sample_points_uniformly(number_of_points = 2000)
            main_pcd_array = np.asarray(main_pcd.points)
            cropped_mesh = crop_mesh(main_mesh)
            cropped_pcd  = cropped_mesh.sample_points_uniformly(number_of_points = 1000)
            cropped_pcd_array = np.asarray(cropped_pcd.points)
            dataset['Y'].append(main_pcd_array)
            dataset['X'].append(cropped_pcd_array)
        except:
            continue
    with open('pcd_dataset.pickle', 'wb') as handle:
        pickle.dump(dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return dataset