
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i] == nums[i+1]:
            return True

    return False
