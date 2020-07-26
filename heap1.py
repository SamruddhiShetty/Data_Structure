heap=[]
def printmin():
    if len(heap)>=1:
        print(heap[0])

def heapify(index):
    lchild=2*index+1
    rchild=2*index+2
    y=index
    size=len(heap)
    if lchild<=size-1 and heap[lchild]<heap[y]:
        y=lchild
    if rchild<=size-1 and heap[rchild]<heap[y]:
        y=rchild
    if y!=index:
        heap[index], heap[y]=heap[y], heap[index]
        heapify(y)

def delete(x):
    index=heap.index(x)
    size=len(heap)
    heap[size-1], heap[index]=heap[index], heap[size-1]
    heap.pop()
    heapify(index)

def insert(x):
    heap.append(x)
    child=len(heap)-1
    parent=(child-1)//2
    while(parent>=0):
        if(heap[parent]>heap[child]):
            heap[parent], heap[child]=heap[child], heap[parent]
            child=parent
            parent=(child-1)//2
        else:
            break

q=int(input())
for _ in range(q):
    l=list(map(int, input().strip().split()))
    if l[0]==1:
        insert(l[1])
    elif l[0]==2:
        delete(l[1])
    else:
        printmin()
