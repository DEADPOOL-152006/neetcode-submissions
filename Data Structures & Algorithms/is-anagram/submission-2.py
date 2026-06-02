class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram=[]*len(s)
        flag_s={}
        flag_t={}
        if(len(s)!=len(t)):
            return False
        for ch in s:
            if(ch in flag_s):
                flag_s[ch]+=1
            else:
                flag_s[ch]=1
        for ch in t:
            if(ch in flag_t):
                flag_t[ch]+=1
            else:
                flag_t[ch]=1   

        if(flag_s==flag_t):
            return True
        else:
            return False    
        