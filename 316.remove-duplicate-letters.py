#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters

# @lc code=start


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
            
        lastOccur={}
    
        for i,chr in enumerate(s):
            lastOccur[chr]=i
        # print(lastOccur)
        
        stack=[]
        checkAlpa=set()
        
        for i in range(len(s)):
            
            if s[i] not in checkAlpa:       
                while (stack and stack[-1] > s[i] and lastOccur[stack[-1]] > i):
                    checkAlpa.remove(stack.pop())
                stack.append(s[i])
                checkAlpa.add(s[i])
                
        return "".join(stack)
        
# @lc code=end

