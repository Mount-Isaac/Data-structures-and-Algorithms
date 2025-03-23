def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
try:
    print(containsDuplicate([4,5,6]))
except TypeError as e:
    print(e)
