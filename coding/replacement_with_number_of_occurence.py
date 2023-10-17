class Solution():
    def frequencySort(self,s):
        dict1 = {}
        for i in s:
            j = ord(i)
            if(j in dict1):
                dict1[j] +=1
            else:
                dict1[j] = 1
        sorted_dict = sorted(dict1.items(),key=lambda x:x[1],reverse=True)
        s =''
        dict1 = {}
        for i in range(len(sorted_dict)):
            s += chr(sorted_dict[i][0])*sorted_dict[i][1]
        return s
s = 'Edre'
obj = Solution()
print(obj.frequencySort(s))