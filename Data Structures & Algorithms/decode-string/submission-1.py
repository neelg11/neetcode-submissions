class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        key_stack = []
        curr = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num*10 + int(c)
            elif c == '[':
                key_stack.append(curr)
                num_stack.append(curr_num)
                curr = ""
                curr_num = 0
            elif c == ']':
                num = num_stack.pop()
                prev = key_stack.pop()
                curr = prev + curr*num
            else:
                curr += c

        return curr





