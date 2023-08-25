import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(['class']).agg({'student': 'count'}).reset_index()
    df.sort_values(by='student', ascending=False, inplace=True)
    print(df)
    return df[df['student'] >= 5][['class']]


if __name__ == '__main__':
    data = [['A', 'Math'],
            ['B', 'English'],
            ['C', 'Math'],
            ['D', 'Biology'],
            ['E', 'Math'],
            ['F', 'Computer'],
            ['G', 'Math'],
            ['H', 'Math'],
            ['I', 'Math']]
    Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student': 'object', 'class': 'object'})

    res = find_classes(Courses)
    print(res)
