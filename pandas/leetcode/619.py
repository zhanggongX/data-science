import pandas as pd


# select max(num) num
# from
# (select num, count(1) countval from MyNumbers group by num) t1
# where countval = 1;
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    se = my_numbers.drop_duplicates(keep=False).max()
    print(se)
    print("-------")
    df = se.to_frame()
    print(df)
    print("--------")
    return df.T

if __name__ == '__main__':
    data = [[8], [8], [3], [3], [1], [4], [5], [6]]
    my_numbers = pd.DataFrame(data, columns=['num']).astype({'num': 'Int64'})

    res = biggest_single_number(my_numbers)
    print(res)
