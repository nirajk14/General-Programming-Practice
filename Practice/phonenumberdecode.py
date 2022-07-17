def letterCombinations(digits):
    Dict={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    no_of_digits=len(digits)
    result=['']
    i=0
    print(Dict.get(digits[i]))
    while i<no_of_digits:
        result=Combine2(result,Dict.get(digits[i]))
        i+=1
    return result


def Combine(list1,str1):
    list2=[]
    if str1=="":
        return list1
    else:
        str1=str1[1:]
        return Combine(list1,str1)

def Combine2(list1,str2):
    list2=[]
    i=0
    while i<len(list1):
        j=0
        while j<len(str2):
            list2.append(list1[i]+str2[j])
            j+=1
        i+=1
    return list2

        





#print(Combine2([''],"def"))
print(letterCombinations("4355"))

