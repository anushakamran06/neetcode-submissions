#brute force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []

        for i in range(len(temperatures)):
            total = 0
            for n in range(i+1,len(temperatures)):
                if temperatures[n] > temperatures[i]:
                    total = n - i
                    break
            temp.append(total)
        return temp
 
#VERY IMPORTANT: know when you are resetting total. incorrect solution:

#for i in range(len(temperatures)): 
#    for n in range(i+1, len(temperatures)):
#        if temperatures[i] > temperatures[n]:
#           total += 1
#        temp.append(total)
#return temp, yo


        