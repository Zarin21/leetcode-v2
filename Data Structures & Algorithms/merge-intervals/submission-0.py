class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda pair:pair[0])
        tmp = sorted_intervals[0]
        res = []
        for i in range(1, len(sorted_intervals)):
            if tmp[1] >= sorted_intervals[i][0]:
                tmp = [tmp[0], max(tmp[1], sorted_intervals[i][1])]
            else:
                res.append(tmp)
                tmp = sorted_intervals[i]
        res.append(tmp)
        return res