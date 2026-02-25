# arr=[2,5,11,1,6,3]
n=int(input("Enter a number"))
arr=[]

for i in range(n):
    arr.append(int(input("Enter a number")))
for i in range(len(arr)):
    count=0
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            count+=1
    if count==len(arr)-i-1:
        print(arr[i])
# print(arr[len(arr)-1])
    