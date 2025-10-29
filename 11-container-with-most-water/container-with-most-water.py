class Solution:
    def maxArea(self, height: List[int]) -> int:
        right =0
        left=len(height)-1
        max_area=0
        while right<left:
            width= left-right
            current_height=min(height[left],height[right])
            area =width*current_height
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left-=1
            else :
                right+=1
        return max_area 
        