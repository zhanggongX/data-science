import pandas as pd


# select t.*,
# if((t.x+t.y>t.z) and (t.x+t.z>t.y) and (t.y+t.z>t.x) = 1, 'Yes', 'No') triangle
# from Triangle t;

# select *,
# (case
# when (x + y <= z) then 'No'
# when (x + z <= y) then 'No'
# when (y + z <= x) then 'No'
# else 'Yes'
# end) as triangle
# from Triangle;
def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(lambda x: 'Yes' if (x['x'] + x['y'] > x['z']) and (x['x'] + x['z'] > x['y']) and (x['y'] + x['z'] > x['x']) else 'No', axis=1)
    return triangle[['x', 'y', 'z', 'triangle']]


if __name__ == '__main__':
    data = [[13, 15, 30], [10, 20, 15]]
    triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})

    res = triangle_judgement(triangle)
    print(res)
