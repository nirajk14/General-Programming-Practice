class Solution(object):
    def lengthOfLongestSubstring(self, s):
        q = deque()
        items = {}
        maxLen = 0
        
        for c in s:
            if c in items:
                poppedItem = None
                while poppedItem != c:
                    poppedItem = q.popleft()
                    if poppedItem in items:
                        items.pop(poppedItem)
            q.append(c)
            items[c] = c
                
            maxLen = max(maxLen, len(q))
        
        return maxLen