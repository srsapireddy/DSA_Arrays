def findPair(nums,target):

    nums.sort()
    low = 0 
    high = len(nums) - 1

    while low < high:
        if nums[low] + nums[high] == target:
            print("Pair Found:", (num[low],num[high]))
            return

        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
    
    print("Pair Not Found")

num = [-1,1,5,7,100]
target = 6

findPair(num,target)


        