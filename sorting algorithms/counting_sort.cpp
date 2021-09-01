
// it assumes that each of the n input elements is an integer in the range of 0 toK , for some integer k.
// Determines, for each input element x, the number of elements less than x .
// it uses this information to place element x directly into its position in the output array 
// Numbers with the same value appear in the output array in the same order as they do  in the input array.

// Stability of the count sort ony comes into consideration when using satellite data.
#include <iomanip>
using std::setw;

#include <iostream>
using namespace std;


int* counting_sort(int sort_arr[],int output[],int len){
    int count_arr[len];

    for(int i =0;i<=len;i++){
        count_arr[i]=0;
    }
    
    for(int m = 0; m < len; m++){
        count_arr[sort_arr[m]]++;
    }
   
    for(int x=1; x < len; x++){
        count_arr[x] += count_arr[x-1];
    }
    for(int z =0;z< len;z++){
        output[count_arr[sort_arr[z]] - 1] = sort_arr[z];
        count_arr[sort_arr[z]]--;
        
    }
    
   
    return output; 

}
int main(){
    
    int sort_arr[] = {2,5,3,0,2,3,0,3};
    int len = sizeof(sort_arr)/sizeof(*sort_arr);
    int output[len];

    int* out;

    out = counting_sort(sort_arr,output,len);

    for(int i=0; i< len;i++){
        cout<<out[i]<<endl;
    }
    

    
}