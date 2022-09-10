"""
def subarray(nums,target):
    nums.sort()
    print(nums)

    low = 0
    high = len(nums)-1

    while low < high:
        if nums[low] + nums[high] == 0:
            print("We have an subarray with zero sum")
            return print("Numbers defining subarray are:", (nums[low],nums[high]))

        if nums[low] + nums[high] < 0:
            low = low + 1
        else:
            high = high - 1
    print("We have no numbers defining subarrays which sum to 0")


nums = [4,2,-3,-1,7]
target = 0

subarray(nums,target)
"""

def subArray(nums):
    a = set()
    a.add(0)
    #print(a)

    total = 0

    for i in a:
        total = total + i
        if total in a:
            return True
        a.add(total)
    return False

nums = [4,2,-3,-1,7]
if subArray(nums):
    print('Sublist exists')
else:
    print('Sublist does not exist')