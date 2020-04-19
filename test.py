# arr = []
# arr.append(['1', '5'])
# arr.append(['2', '3'])
# arr.append(['3', '1'])
# # for i in arr:
# #     print(i[0]," and ",i[1])
    
# # for i in range(len(arr)):
# #     print(arr[i][1])
# a = []
# b = False

# if b is False:
#     print(b)

import threading

def thread_callback(name, loop):
    for i in range(1, loop+1):
        print("%s: %i" % (name, i))


thr = threading.Thread(target=thread_callback, args=["Thread-1", 5])
thr.start()
