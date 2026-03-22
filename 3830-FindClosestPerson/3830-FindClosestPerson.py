# Last updated: 3/22/2026, 10:33:11 PM
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if abs(z-x)<abs(z-y):
            return 1
        elif abs(z-x)>abs(z-y):
            return 2
        else:
            return 0