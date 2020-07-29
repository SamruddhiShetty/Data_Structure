#application of heap here using heapq module
import heapq
#from heapq import heapify, heappush, heappop(also works)
l= [int(x) for x in input().split()]
cookies=[int(x) for x in input().split()]
n=l[0]
k=l[1]
heapq.heapify(cookies)#(here dont have to mention heapq, if imported already)
count=0
try:
    while cookies[0]<k:
        c1=heapq.heappop(cookies)
        c2=heapq.heappop(cookies)
        count +=1
        new=(c1)+(c2*2)
        heapq.heappush(cookies, new)
    print(count)

except:
    print(-1)
