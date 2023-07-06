
from activities.activity import Activity
from constants.constants import *
from ui.components.component_factory import ComponentFactory
import random

import socket


class Haptic(Activity):

    TCP_IP = "172.16.1.2"

    TCP_PORT = 8888

    def __init__(self, body_point_array, ui, **kwargs) -> None:
        super().__init__(body_point_array, ui, **kwargs)

        cf = ComponentFactory(self.ui)

        self.persist = {}
        self.persist[SKELETON] = cf.new_skeleton(body_point_array)
        self.persist[TIMER] = cf.new_timer(0.3, -1.2, func=self.time_expire_func)

        stage_0 = {}
        stage_0["target_1"] = cf.new_button(50, (255, 0, 0, 120), random.uniform(-0.7, 0.7)*PIXEL_SCALE+PIXEL_X_OFFSET, random.uniform(0.0, -0.8)*PIXEL_SCALE+PIXEL_Y_OFFSET, precision=50, func=self.target_1_func, target_pts=[16])

        self.stages = [stage_0]
        self.stage = 0

        self.components = self.stages[self.stage]

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))

        mode = "push"

        pattern = '118'
        if mode == "push":
            self.commands = {'up':f'/buz2/{pattern}', 'down':f'/buz0/{pattern}', 'left':f'/buz1/{pattern}', 'right':f'/buz3/{pattern}key'}

        if mode == "pull":
            self.commands = {'up':f'/buz0/{pattern}', 'down':f'/buz2/{pattern}', 'left':f'/buz3/{pattern}', 'right':f'/buz1/{pattern}'}

        self.index = 0



    def time_expire_func(self) -> None:
        self.stage = 0
        self.change_stage()
        if CLOSE in self.funcs:
            for func in self.funcs[CLOSE]:
                func()
    
    def target_1_func(self) -> None:
        self.stages[0]["target_1"].set_pos(random.uniform(-0.7,0.7)*PIXEL_SCALE+PIXEL_X_OFFSET, random.uniform(0.0,-0.8)*PIXEL_SCALE+PIXEL_Y_OFFSET)
        for i in range(0, 200):
            self.s.send("/255/255/255/255\n".encode('ascii'))



    def handle_frame(self, **kwargs) -> None:
        super().handle_frame(**kwargs)

        self.index += 1

        x1 = (self.persist[SKELETON].skeleton_array[16][0])
        y1 = (self.persist[SKELETON].skeleton_array[16][1])

        x2 = self.stages[0]["target_1"].x_pos
        y2 = self.stages[0]["target_1"].y_pos

        vertical_dist = y1-y2
        horziontal_dist = x1-x2

        if abs(vertical_dist) > abs(horziontal_dist):
            if vertical_dist > 0:
                self.s.send("/255/125/125/125\n".encode('ascii'))
                self.s.send("/255/125/125/125\n".encode('ascii'))
                self.s.send("/255/125/125/125\n".encode('ascii'))
                self.s.send("/255/125/125/125\n".encode('ascii'))
            else:
                self.s.send("/125/255/125/125\n".encode('ascii'))
                self.s.send("/125/255/125/125\n".encode('ascii'))
                self.s.send("/125/255/125/125\n".encode('ascii'))
                self.s.send("/125/255/125/125\n".encode('ascii'))

        else:
            if horziontal_dist > 0:
                self.s.send("/125/125/255/125\n".encode('ascii'))
                self.s.send("/125/125/255/125\n".encode('ascii'))
                self.s.send("/125/125/255/125\n".encode('ascii'))
                self.s.send("/125/125/255/125\n".encode('ascii'))
            else:
                self.s.send("/125/125/125/255\n".encode('ascii'))
                self.s.send("/125/125/125/255\n".encode('ascii'))
                self.s.send("/125/125/125/255\n".encode('ascii'))
                self.s.send("/125/125/125/255\n".encode('ascii'))

        self.change_stage()