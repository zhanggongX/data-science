import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(['teacher_id']).agg(cnt=('subject_id', pd.Series.nunique)).reset_index()
    print(df)
    return df


if __name__ == '__main__':
    data = [[1, 2, 3],
            [1, 2, 4],
            [1, 3, 3],
            [2, 1, 1],
            [2, 2, 1],
            [2, 3, 1],
            [2, 4, 1]]
    Teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype(
        {'teacher_id': 'Int64', 'subject_id': 'Int64', 'dept_id': 'Int64'})

    res = count_unique_subjects(Teacher)
    print(res)
