class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            new_tuple = (temperatures[i], i)

            while stack and stack[-1][0] < new_tuple[0]:
                removed = stack.pop()
                result[removed[1]] = i - removed[1]
            
            stack.append(new_tuple)
        
        return result