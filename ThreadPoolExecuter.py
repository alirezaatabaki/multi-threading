from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def show(name):
    print(f'starting {name}')
    sleep(3)
    print(f'finishing {name}\n')


with ThreadPoolExecutor(max_workers=2) as executer:
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
    executer.map(show, names)

print('Done')
