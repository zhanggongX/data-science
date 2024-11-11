"""
一开始有100个人，每个人都有100元
在每一轮都做如下的事情：
每个人都必须拿出1元钱给自己以外的其他人，给谁完全随机
如果某个人在这一轮的钱数为0，则不给其他人，但是可以接收
发送很多论后，这100人的财富分布均匀吗？

使用财富GiNi系数来表示是否均匀

gini 系数的计算公式
所有财富的差值的平均值总和/2*人数*社会财富总额
"""
import random


def calc_gini(money):
    total_money = 0
    calc_money = 0
    for i in range(len(money) - 1):
        total_money += money[i]
        for j in range(len(money) - 1):
            calc_money += abs(money[i] - money[j])

    return calc_money / (2 * len(money) * total_money)


def social_experiment(people: int, round: int) -> float:
    print(f"人数: {people}, 轮数: {round}")
    money = [100] * people

    for i in range(round):
        has_money = [False] * people
        for j in range(people):
            if money[j] > 0:
                has_money[j] = True

        for j in range(people):
            if has_money[j]:
                other = j
                while True:
                    other = random.randint(0, people - 1)
                    if other != j:
                        break
                money[j] -= 1
                money[other] += 1

    money = sorted(money)
    print(f"经过{round}轮后的财富分布：")
    for i in range(0, len(money), 10):
        print(money[i:i + 10])

    gini = calc_gini(money)
    print(f"现在的Gini系数为：{gini}")
    return 1.0


if __name__ == '__main__':
    social_experiment(100, 100000)
