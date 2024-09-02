from typing import List

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]

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
    res = getDataframeSize(res)

    print(res)