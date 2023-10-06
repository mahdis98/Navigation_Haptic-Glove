import math


def file_processor(filename):
    with open(filename, 'r') as f:
        metaphor = None
        guidance_approach = None
        intensity = None
        layout = None
        time = None
        A_coordinates = None
        B_coordinates = None
        center = None
        coordinates = []
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
                total_distance = distance_calculator(coordinates, abs(center[1] - A_coordinates[1]), abs(center[0] - B_coordinates[0]))
                print(total_distance)
                coordinates = []
            else:
                data_real = line.split(',')
                # print(arr[0])
                if layout is None:
                    pass
                elif layout == 'vertical':
                    coordinates.append([float(data_real[1]), float(data_real[2])])
                else:
                    coordinates.append([float(data_real[1]), float(data_real[3])])


def distance_calculator(coordinates, distance_top, distance_right):
    total_distance = 0
    for i in range(len(coordinates) - 1):
        delta_y = coordinates[i + 1][1] - coordinates[i][1]
        real_delta_y = (delta_y * 35) / distance_top
        delta_x = coordinates[i + 1][0] - coordinates[i][0]
        real_delta_x = (delta_x * 35) / distance_right
        distance = math.sqrt(real_delta_x ** 2 + real_delta_y ** 2)
        total_distance += distance
    return total_distance


# file_processor("./Outputs/Mahdis/Mahdis_vertical_10-06-23_11-19-48.txt")
