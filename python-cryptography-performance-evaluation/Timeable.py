import time
import timeit

class Timeable:
    def executeTimedMilliseconds(self, function):
        timer = timeit.Timer(function, timer=time.perf_counter_ns)
        # TODO Implement free method to reset child class (free memory etc.) and then average multiple runs
        milliseconds = timer.timeit(number=1) / 1000000.0
        return milliseconds