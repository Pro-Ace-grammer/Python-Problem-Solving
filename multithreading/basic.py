import threading
import time

def func(sec):
    print(f'Function will wait for {sec} seconds')
    time.sleep(sec)
    # print(f'Function stopping for {sec} seconds')

time1 = time.perf_counter()
# func(4)
# func(2)
# func(1)

t1 = threading.Thread(target=func,args=[4])
t3 = threading.Thread(target=func,args=[1])
t2 = threading.Thread(target=func,args=[2])
t1.start()
t2.start()
t3.start()

time2 = time.perf_counter()
print(time2-time1)