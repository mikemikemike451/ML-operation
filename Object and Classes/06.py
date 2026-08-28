from collections import deque

class TimeSeriesSmoother:
    def __init__(self, window_size):
        self.window_size = window_size 
        self.point = deque(maxlen=self.window_size)
    
    def add_point (self, value):
        self.point.append(value)

    def get_moving_average (self):
        average = sum(self.point) / len(self.point)
        return average

