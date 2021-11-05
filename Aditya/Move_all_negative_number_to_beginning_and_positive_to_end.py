def rearrange(arr):
    low=0
    high=len(arr)-1
    while(low<=high):
        if arr[low]<0 and arr[high]<0:       #when both left and right value are -ve  
            low+=1
        elif arr[low]<0 and arr[high]>0:     #when left value is -ve and right value is +ve  
            low+=1
            high-=1
        elif arr[low]>0 and arr[high]<0:     #when left value is +ve and right value is -ve 
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
        else:                                #when both left and right value are +ve
            high-=1
    return arr
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print(rearrange(arr))