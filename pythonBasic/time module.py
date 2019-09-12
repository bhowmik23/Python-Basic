import time
initial =time.time()
# print(initial)
k=0
while(k<45):
    print("This is Biddut")
    # time.sleep(2)
    k+=1
print(time.time()-initial)
initial2= time.time()
for i in range(45):
    print("This is Biddut")
print(time.time()-initial2)

local_time = time.asctime(time.localtime(time.time()))
print(local_time)