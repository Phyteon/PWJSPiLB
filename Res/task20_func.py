import threading
import time


class Philosopher(threading.Thread):
    hungry = True

    def __init__(self, index, fork_left, fork_right, is_deadlock=False):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = fork_left
        self.rightFork = fork_right
        self.isDeadlock = is_deadlock

    def run(self):
        while self.hungry:
            time.sleep(2)
            print('%s is hungry' % self.index)
            if self.isDeadlock:
                self.deadlock()
            else:
                self.no_deadlock()

    def deadlock(self):
        fork1, fork2 = self.rightFork, self.leftFork
        while self.hungry:
            has1 = fork1.acquire()
            has2 = fork2.acquire()
            if has1 and has2:
                break
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def no_deadlock(self):
        fork1, fork2 = self.rightFork, self.leftFork
        while self.hungry:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print('%s will try other fork' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def eat(self):
        print('%s starts eating' % self.index)
        time.sleep(2)
        print('%s finishes eating and thinking' % self.index)