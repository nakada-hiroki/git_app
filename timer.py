import time

start_time = time.perf_counter()

print('hellow world')

end_time  = time.perf_counter()
execution_time = end_time - start_time

print(f"Program executed in: {execution_time: .5f} seconds")
print(start_time)
print(end_time)
