class Solution:
    def topK(self, nums, k): 
        num_count = {} 
        n = len(nums) 
        for i in range(n): 
            if nums[i] in num_count: 
                num_count[nums[i]] += 1 
            else: 
                num_count[nums[i]] = 1 
        unique_counts = [0] * (len(num_count)) 
        j = 0 
        for num in num_count:
            unique_counts[j] = [num, num_count[num]]
            j += 1 
        unique_counts = sorted(unique_counts, key=lambda x: x[0], reverse=True) 
        unique_counts = sorted(unique_counts, key=lambda x: x[1], reverse=True) 
        result = [] 
        for i in range(k): 
            result.append(unique_counts[i][0])
        return result