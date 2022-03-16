import threading
from time import sleep


def print_square(num):
    print(f"Square : {num * num}")
    sleep(1)


def print_cube(num):
    print(f"Cube : {num * num * num}")
    t2 = threading.Thread(target=print_square, args=(20,))
    t2.start()
    t2.join()
    sleep(3)


if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(10,))

    t1.start()

    for i in range(1, 10):
        print(f'Value of i is {i}')

    t1.join()  # it blocks the main thread to wait for t1 to complete ... or it should throw error

    print('Done!')
