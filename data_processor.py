import csv
import math
import os

import numpy as np
import matplotlib.pyplot as plt


def file_processor(folder_name):
    dir_list = os.listdir("./Outputs_copy/" + folder_name)
    for filename in dir_list:
        with open("./Outputs_copy/" + folder_name + "/" + filename, 'r') as f:
            print(filename)
            metaphor = None
            guidance_approach = None
            intensity = None
            layout = None
            time = None
            time_array = []
            A_coordinates = None
            B_coordinates = None
            center = None
            coordinates = []
            count = 0
            total_distance = 0
            for line in f:
                # print(line)
                arr = line.strip('\n').split(" ")
                if arr[0] == 'metaphor:':
                    metaphor = arr[1]
                elif arr[0] == 'guidance_approach:':
                    guidance_approach = arr[1]
                elif arr[0] == 'intensity:':
                    intensity = arr[1]
                elif arr[0] == 'layout:':
                    layout = arr[1]
                elif arr[0] == 'Time':
                    time = float(arr[3])
                elif arr[0] == 'Target':
                    pass
                elif arr[0] == 'Theta:':
                    pass
                elif arr[0] == 'Center:':
                    center = [float(arr[1]), float(arr[2])]
                elif arr[0] == 'A':
                    A_coordinates = [float(arr[2]), float(arr[3])]
                elif arr[0] == 'B':
                    B_coordinates = [float(arr[2]), float(arr[3])]
                elif arr[0] == '----':
                    if coordinates:
                        total_distance, speed, acc, jerk = distance_calculator(coordinates, abs(center[1] - A_coordinates[1]),
                                                             abs(center[0] - B_coordinates[0]), time_array)
                        if total_distance != 0:
                            count = count + 1
                            print("count: ", count, " distance: ", total_distance)
                            with open("total_speed_95.csv", 'a', newline='') as f:
                                filewriter = csv.writer(f)
                                filewriter.writerow([folder_name, layout, metaphor, intensity, guidance_approach, total_distance, round(speed, 2), round(acc, 2), round(jerk, 2)])

                        coordinates = []
                        time_array = []
                elif arr[0] == '****':
                    coordinates = []
                    time_array = []
                else:
                    data_real = line.split(',')

                    # print(arr[0])
                    if layout is None:
                        pass
                    elif layout == 'vertical':
                        coordinates.append([float(data_real[1]), float(data_real[2])])
                        time_array.append(float(data_real[0]))
                    else:
                        coordinates.append([float(data_real[1]), float(data_real[3])])
                        time_array.append(float(data_real[0]))


def distance_calculator(coordinates, distance_top, distance_right, time_array):
    total_distance = 0
    distance_array = []
    speed_array = []
    time_speed = []
    acceleration_array = []
    time_acc = []
    jerk_array = []
    for i in range(len(coordinates) - 1):
        delta_y = coordinates[i + 1][1] - coordinates[i][1]
        real_delta_y = (delta_y * 35) / distance_top
        delta_x = coordinates[i + 1][0] - coordinates[i][0]
        real_delta_x = (delta_x * 35) / distance_right
        distance = math.sqrt(real_delta_x ** 2 + real_delta_y ** 2)
        total_distance += distance
        distance_array.append(distance)
    for i in range(len(distance_array)):
        speed_moment = (distance_array[i]) / (time_array[i + 1] - time_array[i])
        speed_array.append(speed_moment)
        time_speed.append((time_array[i + 1] + time_array[i]) / 2)
    for i in range(len(speed_array) - 1):
        acceleration_moment = (speed_array[i + 1] - speed_array[i]) / (time_speed[i + 1] - time_speed[i])
        acceleration_array.append(acceleration_moment)
        time_acc.append((time_speed[i] + time_speed[i + 1]) / 2)
    for i in range(len(acceleration_array) - 1):
        jerk_moment = (acceleration_array[i + 1] - acceleration_array[i]) / (time_acc[i + 1] - time_acc[i])
        jerk_array.append(jerk_moment)

    # print(len(time_array))
    np_speed_array = np.array(speed_array)
    np_acceleration_array = np.array(acceleration_array)
    np_jerk_array = np.array(jerk_array)
    # plt.figure(1)
    # plt.subplot(311)
    # plt.plot([(time_array[i+1]+time_array[i])/2 for i in range(len(time_array)-1)], distance_array)
    # plt.subplot(312)
    # plt.plot(time_speed, speed_array)
    # plt.subplot(313)
    # plt.plot(time_acc, acceleration_array)
    # plt.show()

    return round(total_distance, 2), np.percentile(np_speed_array, 95), np.percentile(np_acceleration_array, 95), np.percentile(
        np_jerk_array, 95)



participants = ['P1_H', 'P1','P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P4_H', 'P4_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P7', 'P7_V', 'P8_H', 'P8_V_2', 'P9_H', 'P9_V', 'P10_H', 'P10_V', 'P11_H', 'P11_V', 'P12_H', 'P12_V', 'P14_H', 'P14_V', 'P15_H', 'P15_V', 'P16_H', 'P16_V', 'P17_H', 'P17_V', 'P18_H', 'P18_V', 'P19_H', 'P19_V', 'P20_V', 'P20_H', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H', 'P23_V']
for p in participants:
    file_processor(p)
# file_processor("./Outputs/P23_H/P23_H_horizontal_12-13-23_16-16-09.txt")
