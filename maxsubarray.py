#Give integer array "nums" find contiguous subarray containing at least one number which has the largest sum

Input = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(self, nums: List[int]) -> int:
    # default max subarray is the first term of the array
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSub)
    return maxSub

print(maxSubArray(Input))