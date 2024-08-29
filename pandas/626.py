import pandas as pd

'''
select 
(case 
when s2.id % 2 = 0 then s1.id+1
when s2.id % 2 = 1 then s1.id-1
when s2.id is null and s1.id % 2 = 0 then s1.id-1
else s1.id
end) as id,
s1.student
from Seat s1 left join Seat s2 on s1.id+1 = s2.id order by id;
'''


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # 创建一个新的列，用于存储交换后的学生姓名
    seat['exchange_student'] = seat['student']

    # 当id是奇数时，检查下一行是否存在，并且下一行的学生姓名与当前行的学生姓名交换
    seat.loc[(seat['id'] % 2 == 1) & (seat['id'] < seat['id'].max()), 'exchange_student'] = seat['student'].shift(-1)
    # 当id是偶数时，将当前行的学生姓名与前一行的学生姓名交换
    seat.loc[seat['id'] % 2 == 0, 'exchange_student'] = seat['student'].shift(1)

    # 输出交换后的座位表
    return seat.rename(columns={'student': 'old_student', 'exchange_student': 'student'})[['id', 'student']]


if __name__ == '__main__':
    data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames'], [6, 'Julia']]
    seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id': 'Int64', 'student': 'object'})

    res = exchange_seats(seat)
    print(res)

    data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
    seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id': 'Int64', 'student': 'object'})

    res = exchange_seats(seat)
    print(res)
