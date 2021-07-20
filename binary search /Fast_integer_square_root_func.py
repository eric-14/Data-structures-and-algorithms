
def sqrt(n):
    start = int(0.25*n)
    stop = int(n/2)
    for i in range(start,stop):
        if(int(i*i)==n):
            return i

print("sqrt====>>",sqrt(90000))

"""Impementation of binary search in java"""

# public class SquareRootBinarySearch {

# public static void main(String [] args)

# {

# int [] inputs = {18, 67, 54, 98, 13908};

# for(int input : inputs)

# {

# getSquareRoot(input);

# //System.out.println(“The Square Root of “+input + ” is :”+getSquareRoot(input));

# }

# }

# private static int getSquareRoot(int input) {

# int high = input;

# int low = 1;

# int delta = Integer.MAX_VALUE;

# int start = 0, end = 0;

# boolean canContinue = true;

# int result = 0;

# while ((low < high) && canContinue)

# {

# start = low;

# end = high;

# if (high – low <= 1)

# canContinue = false;

# int mid = low + (high-low)/2;

# //System.out.println(“Low is :”+low + ” and high is:”+high);

# int tempSquareRoot = mid * mid;

# int tempDelta = Math.abs(tempSquareRoot – input);

# if (delta > tempDelta)

# {

# delta = tempDelta;

# result = mid;

# }

# if (tempSquareRoot > input)

# {

# high = mid;

# }

# else

# {

# low = mid;

# }

# }

# System.out.println(“Square root of “+input +” is between “+start +” and “+end + ” AND RESULT IS: “+result);

# return 0;

# }

# }