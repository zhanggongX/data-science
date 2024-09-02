import pandas as pd


# Write your MySQL query statement below
# select distinct id,
# case
# when p_id is null then 'Root'
# when son_id is null then 'Leaf'
# else 'Inner'
# end as Type
# from (select t1.id, t1.p_id, t2.id as son_id from tree t1 left join  tree t2 on t1.id = t2.p_id) t;

def calc_type(tree_copy, row):
    if pd.isnull(row['p_id']):
        return 'Root'
    elif row['id'] in tree_copy['p_id'].unique():
        return 'Inner'
    else:
        return 'Leaf'


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree_copy = tree.copy()
    tree_copy['Type'] = tree_copy.apply(lambda row : calc_type(tree_copy, row), axis=1)

    df = tree_copy[['id', 'Type']].sort_values('id')
    return df

if __name__ == '__main__':
    data = [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]]
    tree = pd.DataFrame(data, columns=['id', 'p_id']).astype({'id': 'Int64', 'p_id': 'Int64'})

    res = tree_node(tree)
    print(res)
