#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:

        result=""

        romanTable=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]

        for i in range(len(romanTable)-1,-1,-1):

            val=num//romanTable[i][1]
            num%=romanTable[i][1]
            result+=val*romanTable[i][0]
        
        return result





        
# @lc code=end

