import time
import memory_profiler as mem_profile

class Utils:
    def __init__(self):
        pass

    # Measure the time and memory usage of a function
    def measure_function(func, *args, **kwargs):
        t1 = time.process_time()
        mem_before = mem_profile.memory_usage()

        # Function to measure
        func(*args, **kwargs)

        mem_after = mem_profile.memory_usage()
        t2 = time.process_time()
        print("Memory used: " + str(mem_after[0] - mem_before[0]) + " MB")
        print("Time taken: " + str(t2-t1) + " seconds"+"\n")