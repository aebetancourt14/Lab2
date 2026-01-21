import ctypes
import multiprocessing
import os
import time
_libInC = ctypes.CDLL('./libMyLib.so')
def addC_print(_i, a, b, time_started):
    val = ctypes.c_int32(_libInC.myAdd(a, b)).value #cast the result to a 32 bit integer
    end_time = time.time()
    print('CPU_{} Add: {} in {}'.format(_i, val, end_time - time_started))
    
def multC_print(_i, a, b, time_started):
    val = ctypes.c_int32(_libInC.myMultiply(a, b)).value #cast the result to a 32 bit integer
    end_time = time.time()
    print('CPU_{} Multiply: {} in {}'.format(_i, val, end_time - time_started))
procs = [] # a future list of all our processes

# Launch process1 on CPU0
p1_start = time.time()
p1 = multiprocessing.Process(target=addC_print, args=(0, 3, 5, p1_start)) # the first arg defines which CPU to run the 'target' on
os.system("taskset -p -c {} {}".format(0, p1.pid)) # taskset is an os command to pin the process to a specific CPU
p1.start() # start the process
procs.append(p1)

# Launch process2 on CPU1
p2_start = time.time()
p2 = multiprocessing.Process(target=multC_print, args=(1, 3, 5, p2_start)) # the first arg defines which CPU to run the 'target' on
os.system("taskset -p -c {} {}".format(1, p2.pid)) # taskset is an os command to pin the process to a specific CPU
p2.start() # start the process
procs.append(p2)

p1Name = p1.name # get process1 name
p2Name = p2.name # get process2 name

# Here we wait for process1 to finish then wait for process2 to finish
p1.join() # wait for process1 to finish
print('Process 1 with name, {}, is finished'.format(p1Name))

p2.join() # wait for process2 to finish
print('Process 2 with name, {}, is finished'.format(p2Name))
def addC_no_print(_i, a, b, returnValus):
    '''
    Params:
      _i   : Index of the process being run (0 or 1)
      a, b : Integers to add
      returnValues : Multiprocessing array in which we will store the result at index _i
    '''
    val = ctypes.c_int32(_libInC.myAdd(a, b)).value
    returnVals[_i]= val
    # TODO: add code here to pass val to correct position returnValues
    
    
    
def multC_no_print(_i, a, b, returnValus):
    '''
    Params:
      _i   : Index of the process being run (0 or 1)
      a, b : Integers to multiply
      returnValues : Multiprocessing array in which we will store the result at index _i
    '''
    val = ctypes.c_int32(_libInC.myMultiply(a, b)).value
    returnVals[_i]=val
    # TODO: add code here to pass val to correct position of returnValues
    
procs = []

# TODO: define returnValues here. Check the multiprocessing docs to see 
# about initializing an array object for 2 processes. 
# Note the data type that will be stored in the array
returnValues = multiprocessing.Array(ctypes.c_int32, 2 ) #2 elements, integer types array 


p1 = multiprocessing.Process(target=addC_no_print, args=(0, 3, 5, returnValues)) # the first arg defines which CPU to run the 'target' on
os.system("taskset -p -c {} {}".format(0, p1.pid)) # taskset is an os command to pin the process to a specific CPU
p1.start() # start the process
procs.append(p1)

p2 = multiprocessing.Process(target=multC_no_print, args=(1, 3, 5, returnValues)) # the first arg defines which CPU to run the 'target' on
os.system("taskset -p -c {} {}".format(1, p2.pid)) # taskset is an os command to pin the process to a specific CPU
p2.start() # start the process
procs.append(p2)

# Wait for the processes to finish
for p in procs:
    pName = p.name # get process name
    p.join() # wait for the process to finish
    print('{} is finished'.format(pName))

# TODO print the results that have been stored in returnValues
print("myAdd result:", returnValues[0])
print("myMultiply result:", returnValues[1])