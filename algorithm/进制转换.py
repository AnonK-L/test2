def fun(num, jz):
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while num > 0:
        result.append(characters[num % jz])
        num = int(num / jz)
    result.reverse()                    # 注:reverse()方法无返回值
    return (''.join(result))
while True:
    n = int(input('请输入数字:'))
    a = int(input('请输入进制:'))
    print(fun(n, a))