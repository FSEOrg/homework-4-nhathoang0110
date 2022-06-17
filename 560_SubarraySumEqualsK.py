from collections import defaultdict
class Solution:
    
    
    """
    
    Ý tưởng thông thường 2 vòng for bị time limit
    
    Ý tưởng tối ưu: chạy for loop tính sum hiện tại bằng thì count tăng lên 1. 
                        Đồng thời tạo 1 dict lưu số phần tử của từng sum xuất hiện. 
                        Nếu có một giá trị nào đó bằng sum hiện tại - k  thì count tăng lên bằng số lượng xuất hiện 
                        của hiệu đó.
    
    """
    
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prevSum = defaultdict(lambda : 0)
        
        out = 0
        
        currSum = 0
        
        for i in range(len(nums)):
            
            currSum += nums[i]
            
            if currSum == k:
                out += 1
            
            if (currSum - k)  in prevSum:
                out += prevSum[currSum - k]
            
            prevSum[currSum] += 1
            
        return out
            
        
        
        