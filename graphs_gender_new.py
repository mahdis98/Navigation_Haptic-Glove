import math
import os
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib import patches
from matplotlib.patches import Circle

total_in = [0]
total_out = [0]


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


def file_processor(folder_name, new_setting, color, gender):
    coords_x = []
    coords_x_out = []
    temp_x = []
    temp_x_out = []
    coords_y = []
    coords_y_out = []
    temp_y = []
    temp_y_out = []
    target_x = []
    temp_target_x = []
    target_y = []
    temp_target_y = []
    new_center = [0, 0]
    new_radius = 0
    previous_line = []
    dir_list = os.listdir("./Outputs/" + folder_name)
    for filename in dir_list:
        temp_setting = Setting()
        with open("./Outputs/" + folder_name + "/" + filename, 'r') as f:
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
                    new_center[0] = (float(data_real[2]) - center[0]) / (b_x - center[0]) * 35 / 2
                    new_center[1] = (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35 / 2
                    # new_center[0] = (float(data_real[2]) - center[0]) / 2
                    # new_center[1] = (float(data_real[3]) - center[1]) / 2
                    new_radius = distance(new_center[0], new_center[1], 0, 0)
                    new_radius *= 1.15
                    if temp_setting.layout == new_setting.layout and temp_setting.guidance_approach == new_setting.guidance_approach \
                            and temp_setting.metaphor == new_setting.metaphor and temp_setting.intensity == new_setting.intensity:
                        temp_target_x.append(
                            (float(data_real[2]) - center[0]) / (b_x - center[0]) * 35)
                        temp_target_y.append(
                            (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35)
                elif arr[0] == 'Theta:':
                    pass
                elif arr[0] == 'Center:':
                    center = [float(arr[1]), float(arr[2])]
                elif arr[0] == 'A':
                    a_y = float(arr[3])
                elif arr[0] == 'B':
                    b_x = float(arr[2])
                elif arr[0] == '----':
                    coords_x.extend(temp_x)
                    coords_y.extend(temp_y)
                    target_x.extend(temp_target_x)
                    target_y.extend(temp_target_y)
                    coords_x_out.extend(temp_x_out)
                    coords_y_out.extend(temp_y_out)
                    plt.scatter(temp_x, temp_y, s=2, alpha=0.3, c='b', zorder=1)
                    plt.scatter(temp_x_out, temp_y_out, s=2, alpha=0.3, c='b', zorder=1)
                    plt.ylabel("Hand Y Position (cm)", fontsize=14)
                    plt.scatter([0], [0], s=20, zorder=2, c='k')
                    plt.scatter(temp_target_x, temp_target_y, s=20, zorder=2, c='r')
                    plt.axis('square')
                    plt.xlim(-60, 60)
                    plt.ylim(-60, 60)
                    plt.gcf().text(0.5, 0.01, "Hand X Position (cm)", ha='center', fontsize=14)
                    plt.title(
                        new_setting.layout + " " + new_setting.metaphor + " " + new_setting.intensity + " " +
                        new_setting.guidance_approach)
                    circle = Circle(new_center, new_radius, edgecolor='g', facecolor='none')
                    if temp_x:
                        print(len(temp_x)/(len(temp_x) + len(temp_x_out)))
                    # Get the current Axes and add the Circle patch to it
                    plt.gca().add_patch(circle)
                    plt.show()
                    plt.close()
                    temp_x = []
                    temp_y = []
                    temp_x_out = []
                    temp_y_out = []
                    temp_target_x = []
                    temp_target_y = []


                elif arr[0] == '****':
                    temp_x = []
                    temp_y = []

                else:
                    data_real = line.split(',')
                    if temp_setting.layout == new_setting.layout and temp_setting.guidance_approach == new_setting.guidance_approach \
                            and temp_setting.metaphor == new_setting.metaphor and temp_setting.intensity == new_setting.intensity:

                        if temp_setting.layout == 'vertical':
                            if -2 < (float(data_real[1]) - center[0]) / (b_x - center[0]) < 2 and -2 < (
                                    float(data_real[2]) - center[1]) / (a_y - center[1]) < 2:
                                zone_x = (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35
                                zone_y = (float(data_real[2]) - center[1]) / (a_y - center[1]) * 35
                                if distance(zone_x, zone_y, new_center[0], new_center[1]) < new_radius:
                                    temp_x.append(
                                        (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35)
                                    temp_y.append(
                                        (float(data_real[2]) - center[1]) / (a_y - center[1]) * 35)
                                else:
                                    temp_x_out.append(
                                        (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35)
                                    temp_y_out.append(
                                        (float(data_real[2]) - center[1]) / (a_y - center[1]) * 35)

                        else:
                            if -2 < (float(data_real[1]) - center[0]) / (b_x - center[0]) < 2 and -2 < (
                                    float(data_real[3]) - center[1]) / (a_y - center[1]) < 2:
                                zone_x = (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35
                                zone_y = (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35
                                if distance(zone_x, zone_y, new_center[0], new_center[1]) < new_radius:
                                    temp_x.append(
                                        (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35)
                                    temp_y.append(
                                        (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35)
                                else:
                                    temp_x_out.append(
                                        (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35)
                                    temp_y_out.append(
                                        (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35)
                previous_line = arr[0]

    if len(coords_x) > 1:
        total_in[0] += len(coords_x)
        total_out[0] += len(coords_x_out)
        if gender == 'male':
            plt.subplot(1, 2, 1)
            plt.scatter(coords_x, coords_y, s=2, alpha=0.3, c='g', zorder=1)
            plt.scatter(coords_x_out, coords_y_out, s=2, alpha=0.3, c=color, zorder=1)
            # plt.xlabel("Hand X Position (cm)", fontsize=14, labelpad=20)
            plt.ylabel("Hand Y Position (cm)", fontsize=14)
            # plt.scatter(target_x, target_y, s=6, alpha=0.7, c=color)  # Scatter target points if needed
            center = (0, 0)
            radius = 35
            theta = np.linspace(-np.pi / 3, np.pi / 2, 100)
            x_circle = center[0] + radius * np.cos(theta)
            y_circle = center[1] + radius * np.sin(theta)
            plt.plot(x_circle, y_circle, color='k', linewidth=2, label='Half Circle', zorder=2)
            plt.scatter([0], [0], s=20, zorder=2, c='k')
            plt.axis('square')
            plt.xlim(-60, 60)
            plt.ylim(-60, 60)

            # Add a white background to make sure the circle is not obscured
            # plt.fill_between(x_circle, y_circle, color='white')
        else:
            plt.subplot(1, 2, 2)
            plt.scatter(coords_x, coords_y, s=2, alpha=0.3, c='g', zorder=1)
            plt.scatter(coords_x_out, coords_y_out, s=2, alpha=0.3, c=color, zorder=1)
            # print(len(coords_x) / (len(coords_x) + len(coords_x_out)))
            # plt.xlabel("Hand X Position (cm)", fontsize=14)
            plt.ylabel("Hand Y Position (cm)", fontsize=14)
            # plt.scatter(target_x, target_y, s=6, alpha=0.7, c=color)  # Scatter target points if needed
            center = (0, 0)
            radius = 35
            theta = np.linspace(-np.pi / 3, np.pi / 2, 100)
            x_circle = center[0] + radius * np.cos(theta)
            y_circle = center[1] + radius * np.sin(theta)
            plt.plot(x_circle, y_circle, color='k', linewidth=2, label='Half Circle', zorder=2)
            plt.scatter([0], [0], s=20, zorder=2, c='k')
            plt.axis('square')
            plt.xlim(-60, 60)
            plt.ylim(-60, 60)
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
        return True
    else:
        return False


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
participants = ['pouyan_april_v']
male_participants = ['pouyan_april_v']
female_participants = []
# participants = ['P1_H', 'P1', 'P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P4_H', 'P4_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P7',
#                 'P7_V', 'P8_H', 'P8_V_2', 'P9_H', 'P9_V', 'P10_H', 'P10_V', 'P11_H', 'P11_V', 'P12_H', 'P12_V', 'P14_H',
#                 'P14_V', 'P15_H', 'P15_V', 'P16_H', 'P16_V', 'P17_H', 'P17_V', 'P18_H', 'P18_V', 'P19_H', 'P19_V',
#                 'P20_V', 'P20_H', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H', 'P23_V']
# male_participants = ['P1_H', 'P1', 'P2_V_3', 'P2_H', 'P3_H', 'P3_V', 'P5', 'P5_H', 'P6_H', 'P6_V', 'P8_H', 'P8_V_2',
#                      'P9_H', 'P9_V', 'P11_H', 'P11_V', 'P15_H', 'P15_V', 'P18_H', 'P18_V', 'P20_V', 'P20_H']
# female_participants = ['P4_H', 'P4_V', 'P7', 'P7_V', 'P10_H', 'P10_V', 'P12_H', 'P12_V', 'P14_H', 'P14_V', 'P16_H',
#                        'P16_V', 'P17_H', 'P17_V', 'P19_H', 'P19_V', 'P21_H', 'P21_V', 'P22_H', 'P22_V', 'P23_H',
#                        'P23_V']
# gender = input("Please enetr gender: ")
# for sets in range(16):
for sets in [14]:
    rcParams['axes.titlepad'] = 20
    # counter = 0
    male_counter = 0
    female_counter = 0
    print(sets)
    new_setting = Setting()
    plt.xlim(left=-50, right=50)
    plt.ylim(bottom=-50, top=50)
    setting_setter(new_setting, sets)
    plt.title(
        new_setting.layout + " " + new_setting.metaphor + " " + new_setting.intensity + " " + new_setting.guidance_approach)
    # plt.tight_layout(h_pad=10, w_pad=10)  # Adjust both h_pad and w_pad parameters
    # plt.plot()
    # plt.subplots_adjust(top=0.3)
    for p in participants:
        if p in male_participants:
            check = file_processor(p, new_setting, blue_colors[male_counter], 'male')
            if check:
                # print(p)
                male_counter += 1

        # Make sure to plot the circle after the scatter points
        # x_start, y_start = np.random.uniform(-50, 50, 2)
        # x_end, y_end = np.random.uniform(-50, 50, 2)
        # plt.plot([x_start, x_end], [y_start, y_end], color='blue', label='Random Line')

        elif p in female_participants:
            check = file_processor(p, new_setting, red_colors[female_counter], 'female')
            if check:
                female_counter += 1
    center = (0, 0)
    radius = 35
    theta = np.linspace(-np.pi / 3, np.pi / 2, 100)
    x_circle = center[0] + radius * np.cos(theta)
    y_circle = center[1] + radius * np.sin(theta)
    plt.plot(x_circle, y_circle, color='k', linewidth=2, label='Half Circle', zorder=2)
    plt.scatter([0], [0], s=20, zorder=2, c='k')
    plt.axis('square')
    plt.xlim(-60, 60)
    plt.ylim(-60, 60)
    plt.title(
        new_setting.layout + " " + new_setting.metaphor + " " + new_setting.intensity + " " +
        new_setting.guidance_approach)
    total_in[0] = 0
    total_out[0] = 0
    # plt.tight_layout(h_pad=10, w_pad=10)  # Adjust both h_pad and w_pad parameters
    # plt.xlabel("Hand X and Y Position (cm)", fontsize=14, labelpad=20)
    plt.gcf().text(0.5, 0.15, "Hand X Position (cm)", ha='center', fontsize=14)
    plt.ylabel("")  # Empty y-axis label
    plt.savefig('Gender_Figures/Separated2/pouyan_bad' + str(sets) + '.png')
    plt.close()
