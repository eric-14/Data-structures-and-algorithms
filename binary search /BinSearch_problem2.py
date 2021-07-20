# Write a method that takes a sorted array A of integers and a key k does not appear in A. Write down tests to verify your code 

def Search(arr,k):
    i = 0
    n = len(arr) -1

    while(i<=n):
        m = int(i +(n-i)/2)
        if(arr[m] < k):
            i = m
        elif(arr[m]>k):
            n = m
        elif(arr[m]==k):
            return m
    return -1


array1 = [1,2,3,4,4,4,4,5,6,7,7,7,8,9]

print("===========>>>>>>>>>",Search(array1,4))