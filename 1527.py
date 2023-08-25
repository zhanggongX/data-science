import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = []

    def check(t):
        a = t.split()
        for j in a:
            if j.startswith('DIAB1'):
                return True
        return False

    for i in range(len(patients)):
        t = patients.iloc[i, 2]
        print(t)

        if check(t):
            mask.append(True)
        else:
            mask.append(False)
    return patients[mask]


if __name__ == '__main__':
    data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'],
            [5, 'Alain', 'DIAB201']]
    Patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
        {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})

    res = find_patients(Patients)
    print(res)
