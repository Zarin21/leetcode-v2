class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_back = cost[1]
        two_back = cost[0]

        for i in range(2, len(cost)):
            tmp = one_back
            one_back = min(one_back, two_back) + cost[i]
            two_back = tmp

        return min(one_back, two_back)