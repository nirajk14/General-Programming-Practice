strs=["flower","flow","flight"]

def longestCommonPrefix(strs):
        a=min(len(strs[0]),len(strs[1]), len(strs[2]))
        k=[' ']*a
        i=0
        while i < a:
            if strs[0][i]==strs[1][i] and strs[1][i]==strs[2][i]:
                k[i]=strs[0][i]
            i=i+1
        if k==[' ']*a:
            return ""
        else:
            r= (''.join(k))
            m= r.split()
            return m[0]