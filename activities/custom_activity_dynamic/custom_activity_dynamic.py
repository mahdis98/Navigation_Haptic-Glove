from pyqtgraph.functions import mkBrush
from activities.activity import Activity
from ui.components.component_factory import ComponentFactory
from PyQt5.QtGui import QFont
from constants.constants import *
import sys
import pandas as pd

class CustomActivityDynamic(Activity):
    """Activity that takes a custom file as the input and replays it for the user to replicate.

    Args:
        Activity ([type]): Abstract activity object
    """

    def __init__(self, body_point_array, ui, **kwargs) -> None:
        super().__init__(body_point_array, ui, **kwargs)

        cf = ComponentFactory(self.ui)
        # Initialize persistant component dict (Never dissapear reguardless of active stage)
        self.persist = {}
        self.persist[SKELETON] = cf.new_skeleton(body_point_array)
        self.persist[TIMER] = cf.new_timer(0.3, -1.2, font=QFont("Arial", 30), text="Time: ", starting_time=0, func=self.time_expire_func)
        self.persist["live_score"] = cf.new_live_score(-1, -1.2, font=QFont("Arial", 30), text="Score: ")

        # Initialize dict for stage 0 
        stage_0 = {}
        stage_0[START_TARGET] = cf.new_button(50, mkBrush(0, 255, 0, 120), 0, -0.6, func=self.start_button_func, target_pts=[16, 15])

        # Initialize path variable if specified in kwargs
        if "path" in kwargs:
            self.file_path = kwargs["path"]

        # Attempts to read point data from specified CSV, otherwise exits
        try:
            points_data = pd.read_csv(self.file_path)
        except:
            print("Cannot find csv file specified")
            sys.exit(1)

        # Set data for each point (based on https://google.github.io/mediapipe/images/mobile/pose_tracking_full_body_landmarks.png)
        self.lh_x_data = points_data["x15"]
        self.lh_y_data = points_data["y15"]

        self.rh_x_data = points_data["x16"]
        self.rh_y_data = points_data["y16"]

        self.ll_x_data = points_data["x27"]
        self.ll_y_data = points_data["y27"]

        self.rl_x_data = points_data["x28"]
        self.rl_y_data = points_data["y28"]
        
        # Index tracks point in the file for a specific group of buttons/points
        self.index = 0

        # Initialize stage 1 dict. This contains all the buttons
        stage_1 = {}
        stage_1["target_1"] = cf.new_button(50, mkBrush(255, 0, 0, 120),
                                                float(self.lh_x_data[self.index]), float(self.lh_y_data[self.index]),
                                                func=self.target_1_func, target_pts=[15], precision=0.1)

        stage_1["target_2"] = cf.new_button(50, mkBrush(0, 0, 255, 120),
                                                float(self.rh_x_data[self.index]), float(self.rh_y_data[self.index]),
                                                func=self.target_2_func, target_pts=[16], precision=0.1)

        stage_1["target_3"] = cf.new_button(50, mkBrush(100, 100, 0, 120),
                                                float(self.ll_x_data[self.index]), float(self.ll_y_data[self.index]),
                                                func=self.target_3_func, target_pts=[27], precision=0.1)

        stage_1["target_4"] = cf.new_button(50, mkBrush(0, 100, 100, 120),
                                                float(self.rl_x_data[self.index]), float(self.rl_y_data[self.index]),
                                                func=self.target_4_func, target_pts=[28], precision=0.1)

        # Initializes a dict of functions where various capabilities can be passed
        # i.e (Start logging, stop logging, etc.)
        if FUNCS in kwargs:
            self.funcs = kwargs[FUNCS]
        else:
            self.funcs = {}

        # List of stages to swap between and what stage to start at
        self.stages = [stage_0, stage_1]
        self.stage = 0

        # # Use this to start at stage 1
        # self.stage = 1
        # self.persist[TIMER].set_timer(100)

        # Set the active components to the dict of the initial stage
        self.components = self.stages[self.stage]

    def time_expire_func(self) -> None:
        if self.stage == 1:
            self.stage = 0
            self.index = 0
            self.change_stage()
            if CLOSE in self.funcs:
                for func in self.funcs[CLOSE]:
                    func()
    
    def target_1_func(self) -> None:
        self.stages[1]["target_1"].clicked = True
        self.stages[1]["target_1"].change_color(mkBrush(0, 255, 0, 120))
        self.persist["live_score"].add_score(1)

    def target_2_func(self) -> None:
        self.stages[1]["target_2"].clicked = True
        self.stages[1]["target_2"].change_color(mkBrush(0, 255, 0, 120))
        self.persist["live_score"].add_score(1)

    def target_3_func(self) -> None:
        self.stages[1]["target_3"].clicked = True
        self.stages[1]["target_3"].change_color(mkBrush(0, 255, 0, 120))
        self.persist["live_score"].add_score(1)

    def target_4_func(self) -> None:
        self.stages[1]["target_4"].clicked = True
        self.stages[1]["target_4"].change_color(mkBrush(0, 255, 0, 120))
        self.persist["live_score"].add_score(1)

    def start_button_func(self) -> None:
        """
        Defines what should happen when the start button is pressed. In this
        case, it sets the timer to 100, increments the stage, creates new logs,
        starts the logs, and activates the stage change.
        """
        if self.stage == 0:
            self.persist[TIMER].set_timer(100)
            self.stage = self.stage + 1
            if NEW_LOG in self.funcs:
                for func in self.funcs[NEW_LOG]:
                    func()
            if START_LOGGING in self.funcs:
                for func in self.funcs[START_LOGGING]:
                    func()
            self.change_stage()

    def handle_frame(self, **kwargs) -> None:
        """
        Defines what should happen at the end of a frame. In this case, it
        resets all the buttons to no longer be clicked.
        """
        super().handle_frame(**kwargs)
        if not self.stages[1]["target_1"].clicked:
            self.stages[1]["target_1"].change_color(mkBrush(255, 0, 0, 120))
        if not self.stages[1]["target_2"].clicked:
            self.stages[1]["target_2"].change_color(mkBrush(255, 0, 0, 120))
        if not self.stages[1]["target_3"].clicked:
            self.stages[1]["target_3"].change_color(mkBrush(255, 0, 0, 120))
        if not self.stages[1]["target_4"].clicked:
            self.stages[1]["target_4"].change_color(mkBrush(255, 0, 0, 120))
        
        self.stages[1]["target_1"].clicked = False
        self.stages[1]["target_2"].clicked = False
        self.stages[1]["target_3"].clicked = False
        self.stages[1]["target_4"].clicked = False

        self.index += 1
        self.stages[1]["target_1"].set_pos(float(self.lh_x_data[self.index]), float(self.lh_y_data[self.index]))
        self.stages[1]["target_2"].set_pos(float(self.rh_x_data[self.index]), float(self.rh_y_data[self.index]))
        self.stages[1]["target_3"].set_pos(float(self.ll_x_data[self.index]), float(self.ll_y_data[self.index]))
        self.stages[1]["target_4"].set_pos(float(self.rl_x_data[self.index]), float(self.rl_y_data[self.index]))



