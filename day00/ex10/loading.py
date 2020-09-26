
from time import sleep
import time
# print(time.clock_gettime())
from sys import stdout
def ft_progress(listy):
	start = time.time()
	for i in listy:
		i += 1
		str = "ETA: {}s [ {}%][" + "=" * int(i/50) + "> ] {}/{} | elapsed time {:.2f}s"
		print(str.format(1,int((i/len(listy))*100),i,len(listy),time.time() - start),end="\r")
		yield i
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
	# print("|",end='\r')
print()
print(ret)