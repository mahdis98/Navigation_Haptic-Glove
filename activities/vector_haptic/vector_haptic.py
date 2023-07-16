import math
import numpy as np
from activities.activity import Activity
from constants.constants import *
from feedback.auditory import ComputerSoundFeedback
from feedback.haptic_glove import HapticGlove
from ui.components.component_factory import ComponentFactory
import random
import socket


class VectorHaptic(Activity):
    MOTORS = np.array([np.array([0, 0, 1]), np.array([0, 0, -1]), np.array([0, -1, 0]),
                       np.array([0, 1, 0])])  # array of motor positions

    def __init__(self, body_point_array, ui, metaphor: str = "pull", guidance_approach: str = "two-tactor", **kwargs) -> None:
        super().__init__(body_point_array, ui, **kwargs)

        cf = ComponentFactory(self.ui)

        self.TARGETS = [[-0.55, -0.35], [0.55, -0.35], [0, -0.9], [0, 0.2]]

        self.persist = {}
        self.persist[SKELETON] = cf.new_skeleton(body_point_array)
        self.persist[TIMER] = cf.new_timer(0.3, -1.2, func=self.time_expire_func)

        stage_0 = {}
        # stage_0["target_1"] = cf.new_button(50, (255, 0, 0, 120), random.uniform(-0.7, 0.7)*PIXEL_SCALE+PIXEL_X_OFFSET, random.uniform(0.0, -0.8)*PIXEL_SCALE+PIXEL_Y_OFFSET, precision=50, func=self.target_1_func, target_pts=[15])
        random_target = random.choice(self.TARGETS)
        stage_0["target_1"] = cf.new_button(50, (255, 0, 0, 120), random_target[0] * PIXEL_SCALE + PIXEL_X_OFFSET,
                                            random_target[1] * PIXEL_SCALE + PIXEL_Y_OFFSET, precision=50,
                                            func=self.target_1_func, target_pts=[15])
        stage_0["bubble_1"] = cf.new_hand_bubble(0, 0, 15, 30, (255, 0, 0, 120))

        self.stages = [stage_0]
        self.stage = 0

        self.components = self.stages[self.stage]

        self.index = 0

        self.current_pos = np.array([0, 0, 0])  # Current Pos
        self.goal_position = np.array([0, 1, 1])  # Goal Pos

        self.glove = HapticGlove("192.168.1.4", 8888, metaphor=metaphor, guidance_approach=guidance_approach)
        self.glove.connect()

        self.auditory = ComputerSoundFeedback()

    def time_expire_func(self) -> None:
        self.stage = 0
        self.change_stage()
        if CLOSE in self.funcs:
            for func in self.funcs[CLOSE]:
                func()

    def target_1_func(self) -> None:
        old_coords = (self.stages[0]["target_1"].x_pos, self.stages[0]["target_1"].y_pos)
        # new_coords = (random.uniform(-0.7,0.7)*PIXEL_SCALE+PIXEL_X_OFFSET, random.uniform(0.0,-0.8)*PIXEL_SCALE+PIXEL_Y_OFFSET)
        # while old_coords[0] - new_coords[0] < 0.1 and old_coords[1] - new_coords[1] < 0.1:
        #     new_coords = (random.uniform(-0.7,0.7)*PIXEL_SCALE+PIXEL_X_OFFSET, random.uniform(0.0,-0.8)*PIXEL_SCALE+PIXEL_Y_OFFSET)

        # choosing from pre-determined targets
        random_target = random.choice(self.TARGETS)
        new_coords = (random_target[0] * PIXEL_SCALE + PIXEL_X_OFFSET, random_target[1] * PIXEL_SCALE + PIXEL_Y_OFFSET)

        self.stages[0]["target_1"].set_pos(new_coords[0], new_coords[1])
        self.auditory.beep()
        self.index = 0

    def handle_frame(self, **kwargs) -> None:
        super().handle_frame(**kwargs)

        # print(self.persist[SKELETON].skeleton_array)

        goal = (0, 0, 0)
        if "goal" in kwargs:
            goal = kwargs['goal']

        self.index += 1
        self.current_pos = np.array([self.persist[SKELETON].skeleton_array[KEY_POINT][0],
                                     self.persist[SKELETON].skeleton_array[KEY_POINT][1]])  # Current Pos
        # print(self.persist[SKELETON].skeleton_array[4])
        # self.goal_position = np.array([0, self.stages[0]["target_1"].x_pos, self.stages[0]["target_1"].y_pos])
        self.goal_position = np.array([goal[0]*PIXEL_SCALE+PIXEL_X_OFFSET, goal[1]*PIXEL_SCALE+PIXEL_X_OFFSET])

        if self.index > 300000:
            print("stop")
            self.glove.stop_feedback()
        else:
            self.glove.send_pull_feedback(self.current_pos, self.goal_position)

        self.change_stage()


