import pandas as pd


# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby('email')['id'].transform('min')
    removed_person = person[person['id'] != min_id]
    person.drop(removed_person.index, inplace=True)
    # return


if __name__ == '__main__':
    data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
    Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'int64', 'email': 'object'})

    delete_duplicate_emails(Person)
