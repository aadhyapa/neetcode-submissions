"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        def checkConflict(meetings, interval):
            if len(meetings) == 0:
                return True
            return meetings[-1].end <= interval.start
            

        rooms = [[]]
        intervals.sort(key = lambda i: i.start)
    
        for i in range(len(intervals)):
            roomNo = 0
            assigned = False
            while roomNo < len(rooms):
                if checkConflict(rooms[roomNo], intervals[i]):
                    rooms[roomNo].append(intervals[i])
                    assigned = True
                    break
                roomNo += 1
            if not assigned:
                rooms.append([intervals[i]])
        return len(rooms)