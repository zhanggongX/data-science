import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    a = products.loc[products['store1'].notna(), ['product_id', 'store1']]
    a['store'] = "store1"
    a.rename(columns={'store1': 'price'}, inplace=True)
    a = a[['product_id', 'store', 'price']]

    b = products.loc[products['store2'].notna(), ['product_id', 'store2']]
    b['store'] = "store2"
    b.rename(columns={'store2': 'price'}, inplace=True)
    b = b[['product_id', 'store', 'price']]

    c = products.loc[products['store3'].notna(), ['product_id', 'store3']]
    c['store'] = "store3"
    c.rename(columns={'store3': 'price'}, inplace=True)
    c = c[['product_id', 'store', 'price']]

    return pd.concat([a, b, c])


if __name__ == "__main__":
    products_array = {
        'product_id': [0, 1],
        'store1': [95, 70],
        'store2': [95, 70],
        'store3': [95, 70]
    }
    pd_products = pd.DataFrame(products_array)
    res = rearrange_products_table(pd_products)
    print(res)
