import threading
import time


class Timer:
    def __init__(self, timer_time: int) -> None:
        self.time: int = timer_time
