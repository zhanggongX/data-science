'''
select
id,
sum(case when month = 'Jan' then revenue end) Jan_Revenue,
sum(case when month = 'Feb' then revenue end) Feb_Revenue,
sum(case when month = 'Mar' then revenue end) Mar_Revenue,
sum(case when month = 'Apr' then revenue end) Apr_Revenue,
sum(case when month = 'May' then revenue end) May_Revenue,
sum(case when month = 'Jun' then revenue end) Jun_Revenue,
sum(case when month = 'Jul' then revenue end) Jul_Revenue,
sum(case when month = 'Aug' then revenue end) Aug_Revenue,
sum(case when month = 'Sep' then revenue end) Sep_Revenue,
sum(case when month = 'Oct' then revenue end) Oct_Revenue,
sum(case when month = 'Nov' then revenue end) Nov_Revenue,
sum(case when month = 'Dec' then revenue end) Dec_Revenue
from
Department
group by id;
'''
import numpy as np
import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # id 作为索引，列名为 month，值名为 revenue
    df = department.pivot(index='id', columns='month', values='revenue')
    df = df.reindex(columns=columns).rename(columns=lambda x: f'{x}_Revenue')
    df = df.reset_index()
    return df


if __name__ == '__main__':
    data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
    department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype(
        {'id': 'Int64', 'revenue': 'Int64', 'month': 'object'})

    print(reformat_table(department))
