from xml.etree.ElementInclude import include

import pandas as pd


# Write your MySQL query statement below
# select name from SalesPerson where sales_id not in
# (select s.sales_id from SalesPerson s
# left join  Orders o on s.sales_id = o.sales_id
# left join Company c on o.com_id = c.com_id where c.name = 'RED');

# select s.name from
# SalesPerson s
# left join orders o on s.sales_id = o.sales_id
# left join Company c on o.com_id = c.com_id
# group by s.name having sum(case c.name when 'RED' then 1 else 0 end) = 0;

def count_company(x) -> int:
    ans = 0
    for i in range(len(x)):
        s = x.iloc[i]['name_y']
        if s == 'RED':
            ans += 1
    return ans

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # return sales_person[~sales_person.sales_id.isin(orders[orders.com_id.isin(company[company.name == 'RED'].com_id)].sales_id)]
    # 合并数据
    df = sales_person.merge(orders, left_on='sales_id', right_on='sales_id', how='left').merge(company, left_on='com_id', right_on='com_id', how='left')
    df = df.groupby(['name_x']).apply(count_company, include_groups=False)
    df = df.reset_index()
    df.rename(columns={'name_x':'name', 0: 'redCount'}, inplace=True)
    return df[df['redCount'] == 0][['name']]



if __name__ == '__main__':
    data = [[1, 'John', 100000, 6, '4/1/2006'],
            [2, 'Amy', 12000, 5, '5/1/2010'],
            [3, 'Mark', 65000, 12, '12/25/2008'],
            [4, 'Pam', 25000, 25, '1/1/2005'],
            [5, 'Alex', 5000, 10, '2/3/2007']]
    SalesPerson = (pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date'])
                   .astype({'sales_id': 'Int64', 'name': 'object', 'salary': 'Int64', 'commission_rate': 'Int64',
                            'hire_date': 'datetime64[ns]'}))
    data = [[1, 'RED', 'Boston'],
            [2, 'ORANGE', 'New York'],
            [3, 'YELLOW', 'Boston'],
            [4, 'GREEN', 'Austin']]
    Company = (pd.DataFrame(data, columns=['com_id', 'name', 'city'])
               .astype({'com_id': 'Int64', 'name': 'object', 'city': 'object'}))

    data = [[1, '1/1/2014', 3, 4, 10000],
            [2, '2/1/2014', 4, 5, 5000],
            [3, '3/1/2014', 1, 1, 50000],
            [4, '4/1/2014', 1, 4, 25000]]
    Orders = (pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount'])
              .astype({'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'com_id': 'Int64', 'sales_id': 'Int64',
                       'amount': 'Int64'}))

    res = sales_person(SalesPerson, Company, Orders)
    print(res)
