import signal


def find_max_queens():
    try:
        a = 0
        while 1:
            #print '.'
            a += 1
    except Exception:
        return a


def handler(signum, frame):
    raise Exception("Timeout")


# Register the signal function handler
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1.9)


if __name__ == '__main__':
    print find_max_queens()
