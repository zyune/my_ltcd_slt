class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        result = [0]*len(height)
        left = 0
        right = len(height)-1
        area = 0
        while left < right:

            if (right-left)*min(height[left], height[right]) > area:
                area = (right-left)*min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right = right - 1

        return area


if __name__ == '__main__':
    a = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(a.maxArea(height))
