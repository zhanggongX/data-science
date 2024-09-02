import pandas as pd


# select unique_id, name from Employees left join EmployeeUNI on Employees.id = EmployeeUNI.id
def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:

    queue = queue.sort_values('turn')
    queue['sum_weight'] = queue['weight'].cumsum()
    queue = queue[queue['sum_weight'] <= 1000]
    return queue.tail(1)[['person_name']]


if __name__ == '__main__':
    data = [[5, 'Alice', 250, 1],
            [4, 'Bob', 175, 5],
            [3, 'Alex', 350, 2],
            [6, 'John Cena', 400, 3],
            [1, 'Winston', 500, 6],
            [2, 'Marie', 200, 4]]

    queue = (pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype({'person_id': 'Int64', 'person_name': 'object', 'weight': 'Int64', 'turn': 'Int64'}))

    res = last_passenger(queue)

    print(res)
