#defo need a empty list, iterate left to right

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.temp = []
        total = 0

        for i in range(len(temperatures)):
            for n in range(i,len(temperatures)):
                if temperatures[i] > temperatures[n]:
                    total += 1
            self.temp.append(total)


#i = 0, i= 1,2,3,4
#i = 1, i = 2,3,4


        