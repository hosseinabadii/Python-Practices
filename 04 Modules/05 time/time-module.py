import time
import os
os.system("clear")
t1 = time.perf_counter()

# Current Local Time:
print('\n1. Local time with ctime():')
print(time.ctime())
print('\n2. Local time with asctime():')
print(time.asctime())
print('\n3. Local time with asctime(localtime()):')
print(time.asctime(time.localtime()))
print('\n4. Local time with strftime(localtime()):')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print('\n5. Local time with localtime():')
# print(time.localtime())
time.sleep(1)
print(f"\n{'=' * 50}")

# GMT time
print('\n1. GMT time with gmtime():')
print(time.gmtime())
print('\n2. GMT time with asctime(gmtime()):')
print(time.asctime(time.gmtime()))
print('\n3. GMT time with strftime(gmtime()):')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
time.sleep(1)
print(f"\n{'=' * 50}")

# Specific time tuple
time_tuple = (2023, 1, 20, 20, 30, 55, 0, 6, 0)
print('\n1. Specific time tuple with struct_time:')
print(time.struct_time(time_tuple))
print('\n2. Specific time tuple with asctime():')
print(time.asctime(time_tuple))
print('\n3. Specific time tuple with strftime():')
print(time.strftime('%Y-%m-%d %H:%M:%S', time_tuple))
time.sleep(1)
print(f"\n{'=' * 50}")

# Cunvert string time to struct_time
print("\nString Formatted Time to Structure Time:")
print(time.strptime('2023-03-01', '%Y-%m-%d'))
time.sleep(1)

t2 = time.perf_counter()
print(f"Performance time is {(t2 - t1):<7.3f}s")