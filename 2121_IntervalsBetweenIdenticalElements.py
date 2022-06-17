"""

ý tưởng: đầu tiên lưu dict key là giá trị phần tử, value là các vị trí của nó

duyệt từng key, lấy ra mảng các vị trí. Giờ phải tính giá trị của từng vị trí ( tổng khoảng cách đến vị trí khác)
mà không được dùng 2 vòng for sẽ out time.

Ví dụ: 6 vị trí của giá trị n lần lượt là :  a b c d e f
Giá trị output của vị trí d sẽ là:   (d-a) + (d-b) + (d-c) + (e-d) + (f-d)
                                    = 3 * d - (a+b+c)  +  (e+f) - 2*d
                                    = vị trí của d * d - prefixSum  +  (sum - prefixSum - d) - (độ dài mảng - 1 - vị trí d)*d
nhờ vậy phép tính ở đây nếu 2 vòng lặp từ O(n^2) thành O(n)

Time:  O(n)
Space: O(n)

"""


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        prev = defaultdict(lambda : [])
        
        out = [0] * len(arr)
        
        for idx in range(len(arr)):
            prev[arr[idx]].append(idx)
        
        for key in list(prev.keys()):
            summ = 0
            for val in prev[key]:
                summ += val
            prefixSum = 0
            for idx, val in enumerate(prev[key]):
                out[val] =  idx * val - prefixSum + (summ - prefixSum - val) - (len(prev[key]) - 1 - idx) * val
                prefixSum = prefixSum + val
        return out
            
