
def has_nn(nums,n):
    return any(x == (n, n) for x in zip(nums[:-1], nums[1:]))
