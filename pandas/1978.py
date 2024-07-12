import pandas as pd


# select e1.employee_id from
# Employees e1
# left join Employees e2 on
# e1.manager_id = e2.employee_id
# where e1.salary < 30000
# and e2.employee_id is null
# and e1.manager_id is not null
# order by e1.employee_id;

# def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.loc[(employees['salary']<30000) & (~employees['manager_id'].isnull()) & (~employees['manager_id'].isin(employees['employee_id'])) , ['employee_id']].sort_values(by='employee_id')

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = (employees['salary'] < 30000) & (~employees['manager_id'].isnull()) & (~employees['manager_id'].isin(employees['employee_id']))
    print(df)
    df = employees.loc[df, ['employee_id']].sort_values(by='employee_id')
    return df


if __name__ == "__main__":
    data = [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241],
            [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'manager_id', 'salary']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'manager_id': 'Int64', 'salary': 'Int64'})

    res = find_employees(employees)
    print(res)
