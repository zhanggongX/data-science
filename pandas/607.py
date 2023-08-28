import pandas as pd


# Write your MySQL query statement below
# select name from SalesPerson where sales_id not in
# (select s.sales_id from SalesPerson s
# left join  Orders o on s.sales_id = o.sales_id
# left join Company c on o.com_id = c.com_id where c.name = 'RED');
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(company, on='com_id', how='left')
    red_sales_df = df[df['name'] == 'RED']['sales_id']
    print(red_sales_df)

    df = sales_person[~sales_person['sales_id'].isin(red_sales_df)][['name']]
    print(df)
    return df


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
