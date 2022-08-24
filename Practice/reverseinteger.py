class Solution(object):
    def checksign(self,x):
        if abs(x)==x:
            posi=True
        else:
            posi=False
        return posi
    def reverse(self, x):
        if x<=-pow(2,31) or x>=pow(2,31)-1:
            return 0
        init=self.checksign(x)
        x=abs(x)
        i=0
        num=0
        while x!=0:
            rem=x%10
            num=num*10+rem
            i=i+1
            x=x/10
        if init==False:
            num=-num
        if num<=-pow(2,31) or num>=pow(2,31)-1:
            return 0
        else:
            return num