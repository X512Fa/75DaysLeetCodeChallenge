class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for val in nums:
            if val in store:
                return True
            store.add(val)
        return False