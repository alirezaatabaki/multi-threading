from threading import Thread, RLock

lock = RLock()

num = 0


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


def both():
    add()
    subtract()


t1 = Thread(target=both)


t1.start()


t1.join()


print(num)
print('Done ...')
