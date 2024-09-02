import pandas as pd

# select distinct employee_id, department_id from
# (
# select employee_id, department_id from Employee where primary_flag = 'Y'
# union all
# select employee_id, department_id from Employee group by employee_id having count(department_id) = 1
# ) t;
def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    pd1 = employee[employee['primary_flag'] == 'Y'][['employee_id', 'department_id']]
    pd2 = employee.groupby('employee_id').filter(lambda x : len(x) == 1)
    pd3 = pd.concat([pd1, pd2])[['employee_id', 'department_id']].drop_duplicates();
    return pd3


if __name__ == "__main__":
    data = [['1', '1', 'N'],
            ['2', '1', 'Y'],
            ['2', '2', 'N'],
            ['3', '3', 'N'],
            ['4', '2', 'N'],
            ['4', '3', 'Y'],
            ['4', '4', 'N']]
    employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype(
        {'employee_id': 'Int64', 'department_id': 'Int64', 'primary_flag': 'object'})

    res = find_primary_department(employee)
    print(res)
