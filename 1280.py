import pandas as pd


# select t.*, count(e.subject_name) attended_exams
# from (select s1.student_id, s1.student_name, s2.subject_name from Students s1, Subjects s2) t
# left join Examinations e on t.student_id = e.student_id and t.subject_name = e.subject_name
# group by t.student_id, t.subject_name
# order by t.student_id, t.subject_name;
def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(students.assign(key=1), subjects.assign(key=1), on='key').drop('key', axis=1)
    df_exam = (Examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
               .astype({'attended_exams': 'Int64'}))
    df_res = pd.merge(df, df_exam, on=['student_id', 'subject_name'], how='left')
    df_res.fillna({"attended_exams": 0}, inplace=True)
    df_res.sort_values(by=['student_id', 'subject_name'], inplace=True)
    print(df_res)
    return df_res[['student_id', 'student_name', 'subject_name', 'attended_exams']]


if __name__ == '__main__':
    data = [[1, 'Alice'],
            [2, 'Bob'],
            [13, 'John'],
            [6, 'Alex']]
    Students = (pd.DataFrame(data, columns=['student_id', 'student_name'])
                .astype({'student_id': 'Int64', 'student_name': 'object'}))

    data = [['Math'],
            ['Physics'],
            ['Programming']]
    Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name': 'object'})

    data = [[1, 'Math'],
            [1, 'Physics'],
            [1, 'Programming'],
            [2, 'Programming'],
            [1, 'Physics'],
            [1, 'Math'],
            [13, 'Math'],
            [13, 'Programming'],
            [13, 'Physics'],
            [2, 'Math'],
            [1, 'Math']]
    Examinations = (pd.DataFrame(data, columns=['student_id', 'subject_name'])
                    .astype({'student_id': 'Int64', 'subject_name': 'object'}))

    res = students_and_examinations(Students, Subjects, Examinations)
    # print(res)
