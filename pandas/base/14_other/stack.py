import pandas as pd
import numpy as np


def test_stack():
    tuples = list(
        zip(
            *[
                ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
                ["one", "two", "one", "two", "one", "two", "one", "two"],
            ]
        )
    )
    index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
    df = pd.DataFrame(np.arange(1, 17).reshape([8, 2]), index=index, columns=["A", "B"])
    df2 = df[:4]

    print(df2)
    df3 = df2.stack()
    print(df3)

    print(df3.unstack())
    print(df3.unstack('second'))


if __name__ == '__main__':
    test_stack()
