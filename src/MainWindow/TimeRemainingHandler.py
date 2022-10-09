"""
    Utility class for getting the remaining time until program finishes.
    Uses average of time spent computing each image.
"""
import time, statistics


class TimeRemainingHandler:
    def __init__(self):
        self.cached_time_taken = []  # List of cached time taken

    # Return remaining time of algorithm (hh:mm:ss)
    def calculate_time_remaining(
        self, percentage_increment, percentage_left, time_taken
    ):
        self.cached_time_taken.append(time_taken)
        mean_time_taken = statistics.mean(self.cached_time_taken)

        # Time left to 100% completion of current operation
        time_left = percentage_left / percentage_increment * mean_time_taken

        formatted = time.strftime("%H:%M:%S", time.gmtime(time_left * 1.75))
        return "Time left: " + formatted

    # Remove cached vars
    def clear_cache(self):
        self.cached_time_taken.clear()
