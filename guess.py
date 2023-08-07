import random

pool = []
for i in range(4):
    pool.append(random.randint(1, 10))
print(pool)

has = 0
success = 0

while True:
    # 字符串
    guess = input('Enter number with space:')

    # 退出
    if guess == 'q':
        break

    # 空格分割
    inputs = guess.split(' ')
    print(inputs)

    # 字符串转数字
    for k in range(len(inputs)):
        inputs[k] = int(inputs[k])

    print(inputs)

    # 比较
    for i in range(len(inputs)):
        if inputs[i] == pool[i]:
            success += 1
        elif inputs[i] in pool:
            has += 1

    print('has:{0}, success:{1}'.format(has, success))
