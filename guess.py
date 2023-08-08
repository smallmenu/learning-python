import random

pool = []
flag = []
for i in range(4):
    if i > 0:
        while True:
            x = random.randint(1, 10)
            if x not in pool:
                pool.append(x)
                break
    else:
        pool.append(random.randint(1, 10))

print(pool)

while True:
    has = 0
    success = 0

    # 字符串
    guess = input('Enter number with space:')

    # 空格分割
    inputs = guess.split(' ')
    print(inputs)

    # 字符串转数字
    for k in range(len(inputs)):
        inputs[k] = int(inputs[k])

    print(inputs)

    # 比较
    for i in range(len(pool)):
        if inputs[i] == pool[i]:
            success += 1
        elif inputs[i] in pool:
            has += 1

    if success == 4:
        break

    print('has:{0}, success:{1}'.format(has, success))

print('Correct')
