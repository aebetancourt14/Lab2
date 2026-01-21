import threading
import time
from pynq.overlays.base import BaseOverlay
base = BaseOverlay("base.bit")
def blink(t, d, n):
    '''
    Function to blink the LEDs
    Params:
      t: number of times to blink the LED
      d: duration (in seconds) for the LED to be on/off
      n: index of the LED (0 to 3)
    '''
    for i in range(t):
        base.leds[n].toggle()
        time.sleep(d)
    base.leds[n].off()

def worker_t(_l, num):
    '''
    Worker function to try and acquire resource and blink the LED
    _l: threading lock (resource)
    num: index representing the LED and thread number.
    '''
    for i in range(4):
        using_resource = _l.acquire(True)    
        print("Worker {} has the lock".format(num))
        blink(50, 0.02, num)
        _l.release()
        time.sleep(0) # yeild
    print("Worker {} is done.".format(num))
        
# TODO: Write your code here
import threading
import time

def worker_t(_l0, _l1, num):
  
    for i in range(4):
        # lock ordering for every thread
        _l0.acquire(True)
        try:
            print(f"Worker {num} has lock0")
            blink(50, 0.02, num)

            _l1.acquire(True)
            try:
                print(f"Worker {num} has lock1")
                blink(5, 0.1, num)

            finally:
                _l1.release()

        finally:
            _l0.release()

        time.sleep(0)  # yield

    print(f"Worker {num} is done.")

# Initialize and launch the threads
threads = []
fork0 = threading.Lock()
fork1 = threading.Lock()

for i in range(2):
    t = threading.Thread(target=worker_t, args=(fork0, fork1, i))
    threads.append(t)
    t.start()

for t in threads:
    name = t.getName()
    t.join()
    print(f"{name} joined")

# Initialize and launch the threads
threads = []
fork = threading.Lock()
for i in range(2):
    t = threading.Thread(target=worker_t, args=(fork, i))
    threads.append(t)
    t.start()

for t in threads:
    name = t.getName()
    t.join()
    print('{} joined'.format(name))
    def worker_t(_l0, _l1, num):
    '''
    Worker function to try and acquire resource and blink the LED
    _l0: threading lock0 (resource0)
    _l1: threading lock1 (resource1)
    num: index representing the LED and thread number.
    init: which resource this thread starts with (0 or 1)
    '''
    using_resource0 = False
    using_resource1 = False
        
    for i in range(4):
        using_resource0 = _l0.acquire(True)
        if using_resource1:
            _l1.release()
        print("Worker {} has lock0".format(num))
        blink(50, 0.02, num)
    
        using_resource1 = _l1.acquire(True)
        if using_resource0:
            _l0.release()
        print("Worker {} has lock1".format(num))
        blink(5, 0.1, num)
        
        time.sleep(0) # yeild
    
    if using_resource0:
        _l0.release()
    if using_resource1:
        _l1.release()
    
    print("Worker {} is done.".format(num))
        
# Initialize and launch the threads
threads = []
fork = threading.Lock()
fork1 = threading.Lock()
for i in range(2):
    t = threading.Thread(target=worker_t, args=(fork, fork1, i))
    threads.append(t)
    t.start()

for t in threads:
    name = t.getName()
    t.join()
    print('{} joined'.format(name))
    def blink(t, d, n):
    for i in range(t):
        base.leds[n].toggle()
        time.sleep(d)
        
    base.leds[n].off()

def worker_t(_l, num):
    for i in range(10):
        resource_available = _l.acquire(False) # this is non-blocking acquire
        if resource_available:
            
            # write code to:
            # print message for having the key
            # blink for a while
            # release the key
            # give enough time to the other thread to grab the key
            
        else:
            # write code to:
            # print message for waiting for the key
            # blink for a while with a different rate
            # the timing between having the key + yield and waiting for the key should be adjusted so no thread get stuck in waiting
            
            
    print('worker {} is done.'.format(num))
        
threads = []
fork = threading.Lock()
for i in range(2):
    t = threading.Thread(target=worker_t, args=(fork, i))
    threads.append(t)
    t.start()

for t in threads:
    name = t.getName()
    t.join()
    print('{} joined'.format(name))