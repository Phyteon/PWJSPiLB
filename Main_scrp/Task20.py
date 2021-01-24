from Res.task20_func import Philosopher
import threading
import time


def main():

    forks = [threading.Semaphore() for n in range(5)]

    # Without deadlock
    philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('Finished')

    # With deadlock
    philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5], True) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('Finished')


if __name__ == '__main__':
    main()