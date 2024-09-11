import pandas as pd


# select p.project_id, round(avg(e.experience_years), 2) as average_years
# from Project p
# left join Employee e on p.employee_id = e.employee_id
# group by p.project_id;
def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project, employee, on='employee_id', how='left')
    df = df[['project_id', 'experience_years']].groupby('project_id', as_index=False).agg(average_years=('experience_years', 'mean')).round(2)
    return df


if __name__ == '__main__':
    data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
    project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype(
        {'project_id': 'Int64', 'employee_id': 'Int64'})
    data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
    employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})

    res = project_employees_i(project, employee)
    print(res)
