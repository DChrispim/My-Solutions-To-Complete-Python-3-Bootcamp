
def spy_game(nums):
    clean_nums = [num for num in nums if num == 0 or num == 7]
    return (0,0,7) in [x for x in zip(clean_nums[:-1], clean_nums[1:], clean_nums[2:])]
