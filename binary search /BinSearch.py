#typical divide and conquer algorithm 

class BinSearch:
    def Search(self,arr,K):
        i = 0
        n = len(arr)-1 
        while(i <= n):
            m = i + (n-1)/2
            if(arr[m] < K):
                i = m+1
            elif(arr[m]==K):
                return m
            else:
                u = m-1
        return -1
    

array1=[1,2,3,4,5,6,7,8,9]
z = 8
BinSearch = BinSearch()
print("Z ======>",BinSearch.Search(array1, z))
    