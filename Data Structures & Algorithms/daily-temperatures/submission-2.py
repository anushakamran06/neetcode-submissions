#defo need a empty list, iterate left to right

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []

        for i in range(len(temperatures)):
            total = 0
            for n in range(i,len(temperatures)):
                if temperatures[n] > temperatures[i]:
                    total += 1
            temp.append(total)


#i = 0, i= 1,2,3,4
#i = 1, i = 2,3,4


        