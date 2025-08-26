# Last updated: 8/26/2025, 7:31:30 PM
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+2) 
        for l, r, seats in bookings:
            diff[l] += seats
            diff[r+1] -= seats
        for i in range(1, len(diff)):
            diff[i] = diff[i-1] + diff[i]
        return diff[1:-1]
            
        

        
