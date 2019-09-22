#coding=utf-8
'''
n:数据量大小
k:桶的数量
In-place:占用常数内存，不占用额外内存
Out-place:占用额外内存

    排序算法    平均时间复杂度    最好情况下   最坏情况下      空间复杂度   排序方式    稳定性
1   冒泡排序    O(n^2)           O(n)         O(n^2)         O(1)         In-place   True
2   选择排序    O(n^2)           O(n^2)       O(n^2)         O(1)         In-place   False
3   插入排序    O(n^2)           O(n)         O(n^2)         O(1)         In-place   True
4   希尔排序    O(n log n)       O(n log^2 n) O(n log^2 n)   O(1)         In-place   False
5   归并排序    O(n log n)       O(n log n)q  O(n log n)     O(n)         Out-place  True
6   快速排序    O(n log n)       O(n log n)   O(n^2)         O(log n)     In-place   False
7   堆排序      O(n log n)       O(n log n)   O(n log n)     O(1)         In-place   False
8   计数排序    O(n + k)         O(n + k)     O(n + k)       O(k)         Out-place  True
9   桶排序      O(n + k)         O(n + k)     O(n^2)         O(n + k)     Out-place  True
10  基数排序    O(n * k)         O(n * k)     O(n * k)       O(n + k)     Out-place  True
'''
#   1.冒泡排序
def bubbleSort(l):
    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

#   2.选择排序
def selectSort(l):
    for i in range(len(l)-1):
        #   保存最小数值的索引
        minIndex = i
        for j in range(i+1,len(l)):
            if l[j] < l[minIndex]:
                minIndex = j
        #   如果i不是最小值，就把最小值换到i
        if i != minIndex:
            l[i],l[minIndex] = l[minIndex],l[i]
    return l

#   3.插入排序
def insertSort(l):
    for i in range(len(l)):
        preIndex = i-1
        current = l[i]
        while preIndex >= 0 and l[preIndex] > current:
            l[preIndex+1] = l[preIndex]
            preIndex-=1
        l[preIndex+1] = current
    return l

#   4.希尔排序
def shellSort(l):
    import math
    gap = 1
    while(gap<len(l)/3):
        gap = gap*3+1
    while gap>0:
        for i in range(gap,len(l)):
            temp = l[i]
            j = i-gap
            while j>=0 and l[j]>temp:
                l[j+gap] = l[j]
                j -= gap
            l[j+gap] = temp
        gap = math.floor(gap/3)
    return l

#   5.归并排序
def mergeSort(l):
    import math
    if(len(l)<2):
        return l
    middle = math.floor(len(l)/2)
    left, right = l[0:middle], l[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result

#   6.快速排序
def quickSort(l, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(l)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(l, left, right)
        quickSort(l, left, partitionIndex-1)
        quickSort(l, partitionIndex+1, right)
    return l

def partition(l, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if l[i] < l[pivot]:
            swap(l, i, index)
            index+=1
        i+=1
    swap(l,pivot,index-1)
    return index-1

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

#   7.堆排序
def buildMaxHeap(l):
    import math
    for i in range(math.floor(len(l)/2),-1,-1):
        heapify(l,i)

def heapify(l, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and l[left] > l[largest]:
        largest = left
    if right < arrLen and l[right] > l[largest]:
        largest = right

    if largest != i:
        swap(l, i, largest)
        heapify(l, largest)

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def heapSort(l):
    global arrLen
    arrLen = len(l)
    buildMaxHeap(l)
    for i in range(len(l)-1,0,-1):
        swap(l,0,i)
        arrLen -=1
        heapify(l, 0)
    return l

#   8.计数排序
def countingSort(l, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(l)
    for i in range(arrLen):
        if not bucket[l[i]]:
            bucket[l[i]]=0
        bucket[l[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            l[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return l

#   9.桶排序
#   桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要
#   做到这两点：在额外空间充足的情况下，尽量增大桶的数量使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中同时，对于桶
#   中元素的排序，选择何种比较排序算法对于性能的影响至关重要。最快：所有数据被均匀分配到每一个桶中；最慢：所有数据被分配到一个
#   桶中。

#   10.基数排序
#   基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串
#   （比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。


if __name__ == '__main__':
    l = [1,2,2,6,3,1,8,5,9,15,13,12]
    print('冒泡排序： ' + str(bubbleSort(l)))
    print('选择排序： ' + str(selectSort(l)))
    print('插入排序： ' + str(insertSort(l)))
    print('希尔排序： ' + str(shellSort(l)))
    print('归并排序： ' + str(mergeSort(l)))
    print('快速排序： ' + str(quickSort(l)))
    print('堆排序： ' + str(heapSort(l)))
    print('计数排序： ' + str(countingSort(l,20)))