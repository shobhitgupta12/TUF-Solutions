class Solution:
    def countFrequencies(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num]=1
        ans =[]     

        for num in freq:
            ans.append([num, freq[num]])
        return ans    