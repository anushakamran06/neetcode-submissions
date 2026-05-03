#MONOTONIC STACK
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair of [temp,index]

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
               j = stack.pop()
               res[j] = i-j
            stack.append(i)
        return res
       
                

            
