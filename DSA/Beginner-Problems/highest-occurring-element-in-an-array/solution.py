class Solution:
    def mostFrequentElement(self, nums):
        freq ={}
        maxFreq = 0
        maxEle = 0
        for num in nums:
            if num in freq:
              freq[num] += 1
            else:
              freq[num] = 1

        for num in freq:
            if freq[num] > maxFreq:
               maxFreq = freq[num]
               maxEle = num
            elif freq[num]==maxFreq:
               maxEle = min(maxEle,num)
        return maxEle