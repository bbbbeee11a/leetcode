import sys
input = sys.stdin.readline

class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     max_container = 0

    #     for l in range(len(height)):
    #         for r in range(l, len(height)):
    #             w = r - l
    #             h = min(height[l], height[r])
    #             max_container = max(max_container, w * h)
        
    #     return max_container

    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        l, r = 0, len(height) - 1

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_container = max(max_container, w * h)

            # 더 작은 쪽의 포인터를 이동
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_container

        