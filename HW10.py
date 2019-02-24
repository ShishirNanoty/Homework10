import itertools as it
import threading
import time as x

#Define function for generating thread
def gen_thread():
    print('\nThread1 is asleep\n')
    x.sleep(5)                  #Add delay
    print('\nThread1 is awake now\n')

# Initializing thread
t1 = threading.Thread(target = gen_thread)
t1.start()

#main
#Here we compute time taken to find all possible combinations for given logic
start = x.time()
k = [1,2,3,4,5,6]
a_sum = []
s = int(input('Enter sum>>'))
print('\nTop face of 2 dices thrown individually')
print(list(it.product(k,repeat = 2)))
for i in it.product(k, repeat=2):
    if sum(i) == s:
        a_sum.append(i)
print('\nPossible combinations for given sum', a_sum)
end = x.time()
print('\nTotal time for main loop to execute ' + str(int(end-start))+ ' seconds')
