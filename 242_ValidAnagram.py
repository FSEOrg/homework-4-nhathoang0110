import collections
class Solution:
    
    """
    đơn giản tạo tuple chứa 26 phần tử là số lượng các chữ cái xuất hiện
    time: O(độ dài string)
    space: số lượng chữ cái    
    """
    
           
    def get_tuple(self, s:str):
        a = [0] * 26
        counter = collections.Counter()
        for i in s:
            a[ord(i) - ord('a')] += 1
        return tuple(a)    
        
            
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_tuple(s) == self.get_tuple(t)
        
        
 