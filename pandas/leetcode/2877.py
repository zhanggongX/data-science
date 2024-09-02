import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    cols = ['student_id', 'age']
    tps = {'student_id': 'Int32', 'age': 'Int32'}
    student = pd.DataFrame(student_data, columns=cols).astype(tps)
    return student


if __name__ == '__main__':
    student_data = [[1, 15],
                    [2, 11],
                    [3, 11],
                    [4, 20]]

    res = createDataframe(student_data)
    print(res)
