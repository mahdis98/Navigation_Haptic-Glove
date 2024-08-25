import csv
import math
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def distance(x1, y1, x2, y2):
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dis


def file_processor(folder_name, gender):
    dir_list = os.listdir("./Outputs_copy/" + folder_name)
    num = 1
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
            new_center = [0, 0]
            target = [0, 0]
            new_radius = 0
            counter_outside = 0
            counter_inside = 0
            percentage_inside = []
            b_x = 0
            a_y = 0
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
                    data_real = line.replace('[', ' ').replace(']', ' ').strip().split(" ")
                    data_real = list(filter(None, data_real))
                    new_center[0] = (float(data_real[2]) - center[0]) / (b_x - center[0]) * 35 / 2
                    new_center[1] = (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35 / 2
                    new_radius = distance(new_center[0], new_center[1], 0, 0)
                    new_radius *= 1.2
                    target[0] = (float(data_real[2]) - center[0]) / (b_x - center[0]) * 35
                    target[1] = (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35
                elif arr[0] == 'Theta:':
                    pass
                elif arr[0] == 'Center:':
                    center = [float(arr[1]), float(arr[2])]
                elif arr[0] == 'A':
                    A_coordinates = [float(arr[2]), float(arr[3])]
                    a_y = A_coordinates[1]
                elif arr[0] == 'B':
                    B_coordinates = [float(arr[2]), float(arr[3])]
                    b_x = B_coordinates[0]
                elif arr[0] == '----':
                    if coordinates:
                        total_distance, speed, acc, jerk = distance_calculator(coordinates,
                                                                               abs(center[1] - A_coordinates[1]),
                                                                               abs(center[0] - B_coordinates[0]),
                                                                               time_array)
                        percentage = -1
                        if counter_outside + counter_inside > 0:
                            percentage = counter_inside / (counter_outside + counter_inside)
                        counter_outside = 0
                        counter_inside = 0
                        if percentage < 0.1:
                            xs = [(c[0] - center[0]) / (b_x - center[0]) * 35 for c in coordinates]
                            ys = [(c[1] - center[1]) / (a_y - center[1]) * 35 for c in coordinates]
                            circle = Circle((new_center[0], new_center[1]), new_radius, color="#aaaaaa")
                            f, a = plt.subplots()
                            a.add_patch(circle)
                            a.scatter(x=xs, y=ys)
                            a.scatter([0, target[0]], [0, target[1]], color='k')
                            a.scatter([new_center[0]], [new_center[1]], color='r')

                            plt.title(layout + " " + metaphor + " " + intensity + " " + guidance_approach + " " + str(percentage))
                            plt.show()
                            plt.close()
                        if total_distance != 0:
                            count = count + 1
                            with open("zone_calculation/total.csv", 'a', newline='') as f:
                                filewriter = csv.writer(f)
                                filewriter.writerow(
                                    [folder_name, layout, metaphor, intensity, guidance_approach, total_distance,
                                     round(speed, 2), round(acc, 2), round(jerk, 2), int(percentage * 100),
                                     round(time, 2), gender, layout + "_" + metaphor, layout + "_" + guidance_approach, metaphor + "_" + guidance_approach])

                        coordinates = []
                        time_array = []
                        num += 1
                elif arr[0] == '****':
                    coordinates = []
                    time_array = []
                    counter_outside = 0
                    counter_inside = 0
                else:
                    data_real = line.split(',')

                    # print(arr[0])
                    # print(center)
                    if layout is None:
                        pass
                    elif layout == 'vertical':
                        coordinates.append([float(data_real[1]), float(data_real[2])])
                        time_array.append(float(data_real[0]))
                    else:
                        coordinates.append([float(data_real[1]), float(data_real[3])])
                        time_array.append(float(data_real[0]))

                    if layout is None:
                        pass
                    elif layout == 'vertical':
                        if -2 < (float(data_real[1]) - center[0]) / (b_x - center[0]) < 2 and -2 < (
                                float(data_real[2]) - center[1]) / (a_y - center[1]) < 2:
                            zone_x = (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35
                            zone_y = (float(data_real[2]) - center[1]) / (a_y - center[1]) * 35
                            if distance(zone_x, zone_y, new_center[0], new_center[1]) < new_radius:
                                counter_inside += 1
                            else:
                                counter_outside += 1
                    else:
                        if -2 < (float(data_real[1]) - center[0]) / (b_x - center[0]) < 2 and -2 < (
                                float(data_real[3]) - center[1]) / (a_y - center[1]) < 2:

                            zone_x = (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35
                            zone_y = (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35
                            if distance(zone_x, zone_y, new_center[0], new_center[1]) < new_radius:
                                counter_inside += 1
                            else:
                                counter_outside += 1


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

    return round(total_distance, 2), np.percentile(np_speed_array, 50), np.percentile(np_acceleration_array,
                                                                                      50), np.percentile(
        np_jerk_array, 50)


participants = ['P1_H', 'P1', 'P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P4_H', 'P4_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P7',
                'P7_V', 'P8_H', 'P8_V_2', 'P9_H', 'P9_V', 'P10_H', 'P10_V', 'P11_H', 'P11_V', 'P12_H', 'P12_V', 'P14_H',
                'P14_V', 'P15_H', 'P15_V', 'P16_H', 'P16_V', 'P17_H', 'P17_V', 'P18_H', 'P18_V', 'P19_H', 'P19_V',
                'P20_V', 'P20_H', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H', 'P23_V']
male_participants = ['P1_H', 'P1', 'P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P8_H', 'P8_V_2',
                     'P9_H', 'P9_V', 'P11_H', 'P11_V', 'P15_H', 'P15_V', 'P18_H', 'P18_V', 'P20_V', 'P20_H']
female_participants = ['P4_H', 'P4_V', 'P7', 'P7_V', 'P10_H', 'P10_V', 'P12_H', 'P12_V', 'P14_H', 'P14_V', 'P16_H',
                       'P16_V', 'P17_H', 'P17_V', 'P19_H', 'P19_V', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H',
                       'P23_V']
with open('zone_calculation/total.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Participant", "Layout", "metaphor", "intensity", "guidance approach", "total_distance",
                     "speed", "acceleration", "jerk", "in zone percentage", "total time", "Gender", "Layout Metaphor", "Layout Approach", "Metaphor Approach"])
for p in participants:
    if p in male_participants:
        file_processor(p, "Male")
    else:
        file_processor(p, "Female")
# file_processor("./Outputs/P23_H/P23_H_horizontal_12-13-23_16-16-09.txt")
