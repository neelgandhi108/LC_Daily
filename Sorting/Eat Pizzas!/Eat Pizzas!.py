class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n , days = len(pizzas) , len(pizzas) // 4
        index = n -1
        total_wt = 0
        # For odd days: pick the heavist
        for i in range(1,days+1,2):
            total_wt += pizzas[index]
            index -= 1
        index -= 1
        # For even days:  pick 2 heavist
        for i in range(2,days+1,2):
            total_wt += pizzas[index]
            index -= 2
        return total_wt