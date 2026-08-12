import threading

counter = 0
mutex = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        mutex.acquire()    # Lock lo
        counter += 1       # Critical section
        mutex.release()    # Lock chhoddo

# Better way — context manager
def increment_safe():
    global counter
    for _ in range(100000):
        with mutex:        # Auto acquire + release
            counter += 1

t1 = threading.Thread(target=increment_safe)
t2 = threading.Thread(target=increment_safe)
t1.start(); t2.start()
t1.join(); t2.join()

print(counter)  # Always 200000 ✅