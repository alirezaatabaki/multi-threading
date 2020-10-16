from time import sleep, perf_counter

start = perf_counter()


def show(name):
    print(f'starting {name}')
    sleep(3)
    print(f'finishing {name}')


show('one')
show('two')

end = perf_counter()
print(f'total time = {round(end - start)}')
