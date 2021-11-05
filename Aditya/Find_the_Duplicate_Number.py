def check_duplicate(nums):
    dict={}
    visited=[False]*(len(nums))
    for i in nums:
        if visited[i]:                 
            return i
        else:
            visited[i]=True
    return -1
nums = [1,3,4,2,2]
print(check_duplicate(nums))