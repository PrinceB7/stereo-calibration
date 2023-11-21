import numpy as np

def read_camera_parameters(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
    rot_matrix = np.array([[float(val) for val in content[1].split()],
                                    [float(val) for val in content[2].split()],
                                    [float(val) for val in content[3].split()],
                                    [float(0), float(0), float(0)]])
    trans_matrix = np.array([[float(val) for val in content[5].split()],
                                    [float(val) for val in content[6].split()],
                                    [float(val) for val in content[7].split()],
                                    [float(1)]])
    return np.hstack((rot_matrix, trans_matrix))

rot_trans_matrix = read_camera_parameters("camera_parameters/camera1_rot_trans.dat")
print(rot_trans_matrix, "\n\n\n")

# rot_m = np.array([[0.938701213382821, -0.052012703909437075, -0.34078543194457256, 27.788358927077176], 
#                 [-0.008228204680483384, 0.9848901616164161, -0.1729845837030743, 16.185174814841595], 
#                 [0.3446336150774555, 0.16518489090476485, 0.9240896185843801, -19.03935160473833],
#                 [0, 0, 0, 1]])


# print(rot_m, "\n\n\n")