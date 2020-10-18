from threading import Thread, Lock

# Create thread-safe program

num = 0  # shared resource
lock = Lock()

"""
use lock with lock() and release()
"""
# def add():
#     global num
#     lock.acquire()
#     for _ in range(100000):
#         num += 1
#     lock.release()

# def subtract():
#     global num
#     lock.acquire()
#     for _ in range(100000):
#         num -= 1
#     lock.release()

###########
"""
Use Lock with context manager
"""


def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print('Done ...')
