class Solution:
    def decodeString(self, s: str) -> str:
        str_stack=[]
        num_stack=[]
        curr_str=""
        curr_num=0
        for i in s:
            if(i.isdigit()):
                curr_num=curr_num * 10 + int(i)
            elif(i.isalpha()):
                curr_str+=i

                
            elif(i=='['):
                num_stack.append(curr_num)  
                str_stack.append(curr_str)
                curr_num=0
                curr_str=""
            elif(i==']'):
                temp = curr_str
                curr_str=str_stack.pop()
                num= num_stack.pop()
                curr_str += temp * num
            
        return curr_str