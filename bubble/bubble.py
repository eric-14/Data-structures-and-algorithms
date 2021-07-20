def bubble(array):
    for i in range(len(array)):
        for j in range(len(array)):
            m = len(array) -1 - j
            if array[m-1] > array[m]:
                if((m-1)==-1):continue
                temp = array[m-1]
                array[m-1] = array[m]
                array[m] = temp
    return array
print("Hey {}",bubble([8,7,6,5,4]))
# array =[8,7,6,5,4]
# print("len of array{}",range(len(array)))
# # for i in range(len(array)):
# #     print("hey {}",len(array)-i-1)
