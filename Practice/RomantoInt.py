def romanToInt(s):
        #I=1 L=50 V=5 M=1000 X=100 D=500 C=100
        Int=0
        i=0
        while i<len(s):
            if s[i]=='M':
                Int+=1000
            elif s[i]=='C':
                if i+1>=len(s):
                    Int+=100
                else:
                    if s[i+1]=='D':
                        
                        Int+=400
                        i=i+2
                        continue
                    elif s[i+1]=='M':
                        Int+=900
                        i=i+2
                        continue
                    else:
                        Int+=100
            elif s[i]=='X':
                if i+1>=len(s):
                    Int+=10
                else:
                    if s[i+1]=='L':
                        Int+=40
                        i=i+2
                        continue
                    elif s[i+1]=='C':
                        Int+=90
                        i=i+2
                        continue
                    else:
                        Int+=10
            elif s[i]=='I':
                if i+1>=len(s):
                    Int+=1
                else:
                    if s[i+1]=='V':
                        Int+=4
                        i=i+2
                        continue
                    elif s[i+1]=='X':
                        Int+=9
                        i=i+2
                        continue
                    else:
                        Int+=1
            elif s[i]=='V':
                Int+=5
            elif s[i]=='L':
                Int+=50
            elif s[i]=='D':
                Int+=500
            i=i+1
        return Int


print(romanToInt("III"))
print(romanToInt("MCMXCVIII"))