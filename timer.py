from threading import Thread
from time import sleep


class Timer:
    def __init__(self, seconds: int) -> None:
        self.seconds: int = seconds

    def timer(self) -> None:
        """
        function of the timer
        """

        while self.seconds > 0:
            sleep(1)
            self.seconds -= 1

    def start_timer(self) -> None:
        """
        starts the timer with Thread
        """
        Thread(target=self.timer).start()

    def format_time(self) -> str:
        """
        formats the time

        :return: seconds in the format of HH:MM:SS
        """
        local_hours = self.seconds // 3600
        local_minutes = self.seconds % 3600 // 60
        local_seconds = self.seconds % 3600 % 60
        return f"{local_hours:02d}:{local_minutes:02d}:{local_seconds:02d}"
