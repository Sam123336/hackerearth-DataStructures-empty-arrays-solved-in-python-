from collections import deque

n=int(input())
elements = input()
elements2= input()

my_list = list(map(int, elements.split()))[:n]
my_list2 = list(map(int, elements2.split()))[:n]

def rotate_array(arr):
    dq = deque(arr)
    dq.rotate(-1)
    return list(dq)

j=0
c=0
while len(my_list)!=0:
        
        while my_list[0]!= my_list2[0]:
                od=rotate_array(my_list)
                my_list=od
                c+=1
       
        if my_list2[0]==my_list[0]:
                my_list.pop(0)
                my_list2.pop(0)
                j+=1
print(c+j)
