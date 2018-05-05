import multiprocessing
import time
def add():
    while True:
        print (1)
        time.sleep(3)

def sud():
     while True:
        print(0)
        time.sleep(3)
if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=add)
    p = multiprocessing.Process(name='p', target=sud)
    p1.start()
    p.start()