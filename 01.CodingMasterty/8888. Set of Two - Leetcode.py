
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        num2=target-nums[i]
        if num2 in dict :
            return [i,dict[num2]]
        dict[nums[i]]=i

