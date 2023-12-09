def two_sum(nums, target):
    hm = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if hm.get(rem) != None:
            return [hm[rem], i]
        hm[nums[i]] = i


ip = input()
target = int(input())
nums = list(map(lambda x: int(x), ip.split(" ")))

print(two_sum(nums=nums, target=target))
