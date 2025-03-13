class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if nums == 0 and nums < 3:
            return []

        nums.sort()
        res = set() #using hash map to remove the duplicates

        #Here we are taking the first number and comparing with the 2 pointer i.e left and right; l & r
        for i in range(len(nums)-2):    
            l = i+1
            r = len(nums)-1
            while l < r: 
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif total<0:
                    l += 1
                elif total>0:
                    r -= 1
        return [list(triple) for triple in res]
        