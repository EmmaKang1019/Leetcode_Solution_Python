def lengthOfLongestSubstring(s: str) -> int:
    charDict = {}
    maxLen = 0
    left, right = 0,0
    if len(s) == 1:
        return 1
    while (right < len(s)):
        print('right : ', right)
        if s[right] in charDict:
#           right = 2, left = 0 dict : p w, s[2] : w
            print( 's[right]',s[right], 'charDict : ', charDict)
            left = max(left, charDict[s[right]]+1)
        length = right-left+1
        maxLen = max(maxLen,length)
        charDict[s[right]] = right
        right +=1
    return maxLen


print(lengthOfLongestSubstring('pwwkew'))