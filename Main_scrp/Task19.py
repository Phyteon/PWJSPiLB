import matplotlib.pyplot as plt
import threading
import cv2 as cv
import time

start = time.time()


def histogram(image, i, histr):
    histr[i] = (cv.calcHist([image], [i], None, [256], [0, 256]))


def main():
    path = r'images\image.jpg'
    image = cv.imread(path)
    col = ('b', 'g', 'r')
    histr = [0, 0, 0]

    threads = list()
    for i in range(3):
        t = threading.Thread(target=histogram, args=(image, i, histr,))
        threads.append(t)
        t.start()

    for i, thread in enumerate(threads):
        thread.join()
        plt.plot(histr[i], color=col[i])

    plt.title("Histogram")
    plt.grid(True)
    plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start))