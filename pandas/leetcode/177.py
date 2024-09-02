import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if len(df) < N:
        return pd.DataFrame({'getNthHighestSalary(2)': [None]})
    return df.sort_values("salary", ascending=False).head(N).tail(1)


if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'Int64', 'salary': 'Int64'})

    res = nth_highest_salary(Employee, 2)
    print(res)
