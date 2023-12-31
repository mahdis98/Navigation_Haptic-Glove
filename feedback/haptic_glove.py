
import math
import socket
import numpy as np
from feedback.feedback_device import FeedbackDevice


class HapticGlove(FeedbackDevice):

    MOTORS = np.array([np.array([0,0,1]), np.array([0,0,-1]), np.array([0,-1,0]), np.array([0,1,0])]) #array of motor positions
    TIMEOUT = 10 # seconds
    MINIMUM_INTENSITY_MESSAGE = "/150/150/150/150"

    def __init__(self, tcp_ip: str, tcp_port: int, metaphor: str = "pull", guidance_approach: str = "two-tactor") -> None:
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.TIMEOUT)
        self.tcp_ip = tcp_ip
        self.tcp_port = tcp_port
        self.metaphor = metaphor
        self.guidance_approach = guidance_approach
    
    def connect(self) -> None:
        self.socket.connect((self.tcp_ip, self.tcp_port))
        self.socket.settimeout(None)

    def disconnect(self) -> None:
        self.socket.close()
    
    def send_push_feedback(self, message: np.array) -> None:
        for _ in range(0,10):
            self.socket.send(f'{message}\n'.encode('ascii'))

    def send_pull_feedback(self, current_pt: np.array, goal_pt: np.array):
        intensity = self.find_intensity_array(current_pt, goal_pt, self.MOTORS)
        message = self.make_message(intensity)

        for _ in range(0,10):
            self.socket.send(f'{message}\n'.encode('ascii'))
    
    def stop_feedback(self) -> None:
        for _ in range(0,10):
            self.socket.send(f'{self.MINIMUM_INTENSITY_MESSAGE}\n'.encode('ascii'))

    def make_message(self, vect) -> str:
        return f'/{vect[1]}/{vect[0]}/{vect[2]}/{vect[3]}'

    def find_distance(self, vector1, vector2, normalized=False):
        if normalized:
            vector1 = vector1 / np.linalg.norm(vector1)
            vector2 = vector2 / np.linalg.norm(vector2)
        diff = vector1 - vector2
        distance = np.linalg.norm(diff)
        return distance

    def map_to_range(self, x, in_min, in_max, out_min, out_max, bounded=False):
        output = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        if bounded:
            if output < out_min:
                output = out_min
            if output > out_max:
                output = out_max
        return output

    def reverse_map_to_range(self, x, in_min, in_max, out_min, out_max, bounded=False):
        output = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        if bounded:
            if output > out_min:
                output = out_min
            if output < out_max:
                output = out_max
        return output

    def find_intensity_array(self, current_pos, goal_pos, motor_positions) -> np.array:
        U = goal_pos - current_pos
        # print(f'Displacement vector: {U}')

        D = np.linalg.norm(U)
        # print(f'Distance from goal: {D}')


        I = self.map_to_range(D, 0, 0.6, 150, 255,  bounded=True)
        #print(f'Distance adjusted to range: {I}')

        motor_distance = [0.0,0.0,0.0,0.0]
        mapped = [0.59,0.59,0.59,0.59]

        min_distance_motor = -1
        min_distance = 3
        for i in range(0, len(motor_positions)):
            motor_distance[i] = self.find_distance(U, motor_positions[i], normalized=True)
            # two tactor vector
            mapped[i] = self.reverse_map_to_range(motor_distance[i], 0.0, math.sqrt(2), 1, .59, bounded=True)

            #worst axis first

        #     if motor_distance[i] < min_distance:
        #         min_distance = motor_distance[i]
        #         min_distance_motor = i

        # mapped[min_distance_motor] = 1

        

        #print(mapped)

        mapped = np.array(mapped)

        # print(f'Motor distances : {motor_distance}')
        #print(f'Motor intensity proportions: {mapped}')

        intensity = np.array(I * mapped).astype(int)
        # print(f'Motor intensity array: {intensity}')
        return intensity
