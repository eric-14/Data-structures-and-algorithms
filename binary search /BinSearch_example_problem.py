# implemet a fast integer square root function that takes in a 32-bit unsigned integer and return another 
# 32-bit unsigned integer that is the floor of the square rrot of the nput

def sqrt(input):
    i = 0
    n = input - 1

    while( i <= n):
        m = int(i+ (n-i)/2)
        if(i==m):
            print("input a valid square")
            break
        if(m*m < input):
            i = m
        elif(m*m == input):
            return m
        else:
            n =m 
        
print("sqrt====>>",sqrt(21))