import time
# x = [1,2,4,6,10]
# for i in x:
#     time.sleep(5)
#     print(i*i)

sec = time.time()
struct = time.localtime(sec)
x=time.strftime('%d.%m.%Y %H:%M', struct)
print(x)