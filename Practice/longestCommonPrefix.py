strs=["flower","flow","flight"]
strs2=["flow","flower"]

def longestCommonPrefix(strs):
        a=len(min(strs,key=len))
        b=len(strs)
        if b==1:
            return strs[0]
        k=[' ']*a
        
        j=0
        while j < a:
            i=0
            while i < b-1:
                if strs[i][j]==strs[i+1][j]:
                    i=i+1
                    if i==b-1:
                        k[j]=strs[i][j]
                    continue
                else:
                    j=a
                    break
            j=j+1
        if k==[' ']*a:
            return ""
        else:
            r= (''.join(k))
            m= r.split()
            return m[0]
print(longestCommonPrefix(strs2))