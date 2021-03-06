from time import sleep, perf_counter
from threading import Thread, current_thread

start = perf_counter()


def show(name, delay):
    print(f'starting {name}')
    print(current_thread())
    sleep(delay)
    print(f'finishing {name} \n')


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


t1 = ShowThread('one', 3)
t2 = ShowThread('two', 7)

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()
print(f'total time = {round(end - start)}')
