import os
import re
import matplotlib.pyplot as plt
import numpy as np


class Setting:
    def __init__(self):
        self.metaphor = None
        self.guidance_approach = None
        self.intensity = None
        self.layout = None
        self.participants = None


def file_processor(folder_name, new_setting, color):
    check_first = False
    coords_x = []
    temp_x = []
    coords_y = []
    temp_y = []
    target_x = []
    temp_target_x = []
    target_y = []
    temp_target_y = []
    previous_line = []
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
                    if len(target_x) > 0:
                        break
                    temp_x = []
                    temp_y = []
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
                                temp_x.append(
                                    (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35)
                                temp_y.append(
                                    (float(data_real[2]) - center[1]) / (a_y - center[1]) * 35)
                        else:
                            if -2 < (float(data_real[1]) - center[0]) / (b_x - center[0]) < 2 and -2 < (
                                    float(data_real[3]) - center[1]) / (a_y - center[1]) < 2:
                                temp_x.append(
                                    (float(data_real[1]) - center[0]) / (b_x - center[0]) * 35)
                                temp_y.append(
                                    (float(data_real[3]) - center[1]) / (a_y - center[1]) * 35)
                previous_line = arr[0]

    if len(coords_x) > 1 and check_first is False:
        check_first = True
        plt.scatter(coords_x, coords_y, s=2, alpha=0.3, c=color, zorder=1)
        plt.xlabel("Hand X Position (cm)")
        plt.ylabel("Hand Y Position (cm)")
        plt.scatter(target_x, target_y, s=6, alpha=0.7, c='red')
        return
        # Scatter target points if needed
        # center = (0.5, 0.5)
        radius = 0.4
        theta = np.linspace(0, (3 / 4) * np.pi, 100)
        x_circle = center[0] + radius * np.cos(theta)
        y_circle = center[1] + radius * np.sin(theta)
        # plt.plot(x_circle, y_circle, color='red', label='Half Circle', zorder=2)
        plt.plot(center[0], center[1], color='black', zorder=2)

        # Add a white background to make sure the circle is not obscured
        plt.fill_between(x_circle, y_circle, color='white')

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
check_target_counter = False
for sets in range(16):
    if sets == 4:
        # counter = 0
        new_setting = Setting()
        plt.xlim(left=-50, right=50)
        plt.ylim(bottom=-50, top=50)
        setting_setter(new_setting, sets)
        plt.title(
            new_setting.layout + " " + new_setting.metaphor + " " + new_setting.intensity + " " + new_setting.guidance_approach)
        plt.plot()
        for p in participants:
            if p == 'P1' and check_target_counter is False:
                check_target_counter = True
                check = file_processor(p, new_setting, 'green')

        # center = (0, 0)
        # radius = 35
        # theta = np.linspace(-np.pi / 4, np.pi / 2, 100)
        # x_circle = center[0] + radius * np.cos(theta)
        # y_circle = center[1] + radius * np.sin(theta)
        # plt.plot(x_circle, y_circle, color='k', linewidth=2, label='Half Circle', zorder=2)
        plt.scatter([0], [0], s=20, zorder=2, c='k')
        plt.axis('square')
        plt.xlim(-60, 60)
        plt.ylim(-60, 60)
        plt.savefig('Sample_figures/setting_' + str(sets) + '.png', transparent=True)
        plt.close()
