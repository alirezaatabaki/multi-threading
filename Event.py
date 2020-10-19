from threading import Event, Thread
from time import sleep


def first(f, s):
    sleep(10)
    print("Fisrt is ready ...")
    f.set()
    s.wait()
    print("Frist is working ...")
    f.clear()


def second(f, s):
    print("Second is ready ...")
    s.set()
    f.wait()
    print("Second is working ...")
    s.clear()


f = Event()
s = Event()

t1 = Thread(target=first, args=(f, s))
t2 = Thread(target=second, args=(f, s))

t1.start()
t2.start()
