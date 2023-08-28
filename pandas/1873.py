import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda e: e['salary'] if e['employee_id'] % 2 and not e['name'].startswith('M') else 0,
        axis=1
    )
    # return employees
    df = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    return df


if __name__ == "__main__":
    data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
    Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
        {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})

    res_pd = calculate_special_bonus(Employees)
    print(res_pd)
