def letterCombinations(digits):
    Dict={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    no_of_digits=len(digits)
    result=[]
    i=0
    print(Dict.get(digits[i]))
    for i<no_of_digits:
        result=Combine(result,Dict.get(digits[i]))


def Combine(list1,str1):
    list2=[]
    if str1=="":
        return list1
    else:
        if list1!=[]:
            a=len(list1)
            i=0
            for i<a:
                list1=list1.append(list1[i]+str1[0])





letterCombinations("23")

