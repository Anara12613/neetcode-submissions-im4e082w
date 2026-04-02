class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        begin = 0
        res = 0
        wind_state = defaultdict(int)

        for end in range(len(fruits)):
            wind_state[fruits[end]] += 1
            while len(wind_state) > 2:
                wind_state[fruits[begin]] -=1
                if wind_state[fruits[begin]] == 0:
                    del wind_state[fruits[begin]]
                begin += 1
            res = max(res, end - begin + 1)
        return res
                

        