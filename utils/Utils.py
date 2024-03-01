import time
import memory_profiler as mem_profile

class Utils:
    def __init__(self):
        pass

    # Measure the time and memory usage of a function
    def measure_function(func, *args, **kwargs):
        mem_before = mem_profile.memory_usage()

        # Function to measure
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        mem_after = mem_profile.memory_usage()
        print("Memory used: " + str(mem_after[0] - mem_before[0]) + " MB")
        print("Time taken: " + str(end_time - start_time) + " seconds" + "\n")