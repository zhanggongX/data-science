import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df['product_id']


if __name__ == '__main__':
    data = [[0, 'Y', 'N'],
            [1, 'Y', 'Y'],
            [2, 'N', 'Y'],
            [3, 'Y', 'Y'],
            [4, 'N', 'N']]
    world_pd = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable'])
    print(world_pd)
    res = find_products(world_pd)
    print(res)
