from stack import Stack

def fun(str):
    stack = Stack()
    left = '(<{['
    right = ')>}]'
    dic = {')': '(', '>': '<', '}': '{', ']': '['}
    for i in str:
        if i in left:
            stack.push(i)
        elif i in right:
            if dic[i] == stack.peek():
                stack.pop()
            else:
                return False
        else:
            continue
    if stack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        str = input('Please input string:')
        print(fun(str))