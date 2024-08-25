import csv
import math
import os
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams


class Setting:
    def __init__(self):
        self.metaphor = None
        self.guidance_approach = None
        self.intensity = None
        self.layout = None
        self.participants = None


def distance(x1, y1, x2, y2):
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dis


def file_processor(folder_name, new_setting, index, gender):
    new_center = [0, 0]
    new_radius = 0
    counter_outside = 0
    counter_inside = 0
    percentage_inside = []
    dir_list = os.listdir("./Outputs_copy/" + folder_name)
    for filename in dir_list:
        temp_setting = Setting()
        with open("./Outputs_copy/" + folder_name + "/" + filename, 'r') as f:
            a_y = None
            b_x = None
            center = None
            target = None
            for line in f:
                arr = line.strip('\n').split(" ")
                if arr[0] == 'metaphor:':
                    temp_setting.metaphor = arr[1]
                elif arr[0] == 'guidance_approach:':
                    temp_setting.guidance_approach = arr[1]
                elif arr[0] == 'intensity:':
                    temp_setting.intensity = arr[1]
                elif arr[0] == 'layout:':
                    temp_setting.layout = arr[1]
                elif arr[0] == 'Time':
                    pass
                elif arr[0] == 'Target':
                    data_real = line.replace('[', ' ').replace(']', ' ').strip().split(" ")
                    data_real = list(filter(None, data_real))
                    if temp_setting.layout == new_setting.layout and temp_setting.guidance_approach == new_setting.guidance_approach \
                            and temp_setting.metaphor == new_setting.metaphor:
                        new_center[0] = (float(data_real[2]) - center[0]) / (b_x - center[0]) * 35
                        new_center[1] = (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35
                        new_radius = distance(new_center[0], new_center[1], 0, 0)
                        new_radius *= 1.2
                elif arr[0] == 'Theta:':
                    pass
                elif arr[0] == 'Center:':
                    center = [float(arr[1]), float(arr[2])]
                elif arr[0] == 'A':
                    a_y = float(arr[3])
                elif arr[0] == 'B':
                    b_x = float(arr[2])
                elif arr[0] == '----':
                    if counter_outside + counter_inside > 0:
                        percentage_inside.append(counter_inside / (counter_outside + counter_inside))
                    counter_outside = 0
                    counter_inside = 0

                elif arr[0] == '****':
                    counter_outside = 0
                    counter_inside = 0

                else:
                    data_real = line.split(',')
                    if temp_setting.layout == new_setting.layout and temp_setting.guidance_approach == new_setting.guidance_approach \
                            and temp_setting.metaphor == new_setting.metaphor:

                        if temp_setting.layout == 'vertical':
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

    return percentage_inside


def setting_setter(setting, inp):
    if inp <= 7:
        setting.metaphor = 'push'
    else:
        setting.metaphor = 'pull'
    if inp % 8 < 4:
        setting.guidance_approach = 'two_tactor'
    else:
        setting.guidance_approach = 'worst_axis'
    if inp % 4 < 2:
        setting.intensity = 'linear'
    else:
        setting.intensity = 'zone'
    if inp % 2 == 0:
        setting.layout = 'vertical'
    else:
        setting.layout = 'horizontal'


palette = [
    'blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray',
    'olive', 'cyan', 'magenta', 'lime', 'teal', 'lavender', 'maroon', 'gold',
    'navy', 'salmon', 'darkgreen', 'indigo', 'darkorange', 'steelblue',
    'crimson', 'orchid', 'darkcyan', 'sienna', 'slategray', 'darkviolet', 'tomato', 'dodgerblue'
]

# Shades of Blue
blue_colors = [
    '#003f5c', '#004b6e', '#005682', '#006196', '#006ca9',
    '#0078bb', '#0083cd', '#008fdf', '#009bf2', '#00a7ff',
    '#33adff', '#66b3ff', '#99b9ff', '#ccbeff', '#ffccff'
]

# Shades of Red
red_colors = [
    '#67001f', '#800026', '#990029', '#b2002d', '#cc0033',
    '#e50038', '#ff003d', '#ff1947', '#ff3351', '#ff4e5c',
    '#ff6866', '#ff8170', '#ff9b7a', '#ffb584', '#ffcf8f'
]

participants = ['P1_H', 'P1', 'P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P4_H', 'P4_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P7',
                'P7_V', 'P8_H', 'P8_V_2', 'P9_H', 'P9_V', 'P10_H', 'P10_V', 'P11_H', 'P11_V', 'P12_H', 'P12_V', 'P14_H',
                'P14_V', 'P15_H', 'P15_V', 'P16_H', 'P16_V', 'P17_H', 'P17_V', 'P18_H', 'P18_V', 'P19_H', 'P19_V',
                'P20_V', 'P20_H', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H', 'P23_V']
male_participants = ['P1_H', 'P1', 'P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P8_H', 'P8_V_2',
                     'P9_H', 'P9_V', 'P11_H', 'P11_V', 'P15_H', 'P15_V', 'P18_H', 'P18_V', 'P20_V', 'P20_H']
female_participants = ['P4_H', 'P4_V', 'P7', 'P7_V', 'P10_H', 'P10_V', 'P12_H', 'P12_V', 'P14_H', 'P14_V', 'P16_H',
                       'P16_V', 'P17_H', 'P17_V', 'P19_H', 'P19_V', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H',
                       'P23_V']
# gender = input("Please enetr gender: ")
with open('zone_calculation/total_zone.csv', 'w', newline='') as f:
    f.write('')
with open('zone_calculation/female_zone.csv', 'w', newline='') as f:
    f.write('')
with open('zone_calculation/male_zone.csv', 'w', newline='') as f:
    f.write('')

for sets in range(16):
    rcParams['axes.titlepad'] = 20
    # counter = 0
    male_counter = 0
    female_counter = 0
    print(sets)
    new_setting = Setting()
    setting_setter(new_setting, sets)
    total_condition_percentage = []
    male_total_percentage = []
    female_total_percentage = []
    for p in participants:
        percentage = file_processor(p, new_setting, sets, 'male')
        total_condition_percentage.extend(percentage)
        if p in male_participants:
            male_total_percentage.extend(percentage)
        else:
            female_total_percentage.extend(percentage)

    with open('zone_calculation/total_zone.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(total_condition_percentage)

    with open('zone_calculation/female_zone.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(female_total_percentage)

    with open('zone_calculation/male_zone.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(male_total_percentage)
