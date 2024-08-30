import pandas as pd


# update Salary set sex = if(sex = 'm', 'f', 'm');
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].apply(lambda x: 'f' if x == 'm' else 'm')
    return salary

if __name__ == '__main__':
    data = [[1, 'A', 'm', 2500], [2, 'B', 'f', 1500], [3, 'C', 'm', 5500], [4, 'D', 'f', 500]]
    salary = pd.DataFrame(data, columns=['id', 'name', 'sex', 'salary']).astype(
        {'id': 'Int64', 'name': 'object', 'sex': 'object', 'salary': 'Int64'})

    res = swap_salary(salary)
    print(res)