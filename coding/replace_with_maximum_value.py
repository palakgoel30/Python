class Solution():
    def replaceWithMaxValue(self,nums):
        nums1 = []
        for i in range(len(nums)):
            if(i+1 < len(nums)):
                max_value = max(nums[i+1::])
                if(nums[i+1] <= max_value):
                    nums1.append(max_value)
            else:
                nums1.append(0)
        return nums1

nums = [2,3,2,12,3,1] #Output : 12,12,12,3,1,0
obj = Solution()
print(obj.replaceWithMaxValue(nums))