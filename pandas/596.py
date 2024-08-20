
import pandas as pd


# select class from Courses group by class having count(student) >= 5;
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    df = df[df['student'] >=5]
    return df[['class']]


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
