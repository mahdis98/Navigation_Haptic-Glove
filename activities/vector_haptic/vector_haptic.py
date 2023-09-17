import numpy as np
from activities.activity import Activity
from constants.constants import *
from feedback.auditory import ComputerSoundFeedback
from feedback.haptic_glove import HapticGlove


class VectorHaptic(Activity):
    MOTORS = np.array([np.array([0, 0, 1]), np.array([0, 0, -1]), np.array([0, -1, 0]),
                       np.array([0, 1, 0])])  # array of motor positions

    def __init__(self, body_point_array, ui, **kwargs) -> None:
        super().__init__(body_point_array, ui, **kwargs)

        self.body_point_array = body_point_array
        self.components = []
        self.index = 0

        self.current_pos = np.array([0, 0, 0])  # Current Pos
        self.goal_position = np.array([0, 1, 1])  # Goal Pos

        print("Before connection")
        self.glove = HapticGlove("192.168.1.4", 8888)
        self.glove.connect()
        print("Glove connected!")
        self.auditory = ComputerSoundFeedback()

    def time_expire_func(self) -> None:
        self.stage = 0
        self.change_stage()
        if CLOSE in self.funcs:
            for func in self.funcs[CLOSE]:
                func()

    def handle_frame(self, metaphor: str = "pull", guidance_approach: str = "two-tactor", intensity: str = "linear",
                     layout: str = "vertical", **kwargs) -> None:
        super().handle_frame(**kwargs)

        goal = ()
        radius = 0
        alpha = 0

        if "radius" in kwargs:
            radius = kwargs['radius']
        if "alpha" in kwargs:
            alpha = kwargs['alpha']
        if "goal" in kwargs:
            goal = kwargs['goal']
        if "turn_off" in kwargs and kwargs['turn_off']:
            print("stop")
            self.glove.stop_feedback()
        elif len(goal) > 0:
            self.index += 1
            if layout == "horizontal":
                self.current_pos = [self.body_point_array[0], self.body_point_array[2]]
            else:
                self.current_pos = [self.body_point_array[0], self.body_point_array[1]]
            self.goal_position = np.array([goal[0], goal[1]])

            if self.index > 300000:
                print("stop")
                self.glove.stop_feedback()
            else:
                self.glove.send_pull_feedback(self.current_pos, self.goal_position, alpha=alpha, radius=radius,
                                              metaphor=metaphor, guidance_approach=guidance_approach,
                                              intensity=intensity)
