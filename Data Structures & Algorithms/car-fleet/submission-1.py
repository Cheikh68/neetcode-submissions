class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted(range(len(position)), key=lambda i: position[i], reverse=True)
        stack = []

        for index in sorted_pos:
            if not stack:
                stack.append([index])
            else:
                fleet_index = stack[-1][0]
                arrival_time = (target - position[index]) / speed[index]
                fleet_time = (target - position[fleet_index]) / speed[fleet_index]
                
                if arrival_time <= fleet_time:
                    stack[-1].append(index)
                else:
                    stack.append([index])
        
        return len(stack)