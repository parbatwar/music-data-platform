import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")
# print(df.head())
# print(df.columns)
# print(df.dtypes)
# # print(df.isnull().sum())
# print(df["track_id"].duplicated().sum())

# duplicate_ids = df[df["track_id"].duplicated(keep=False)]
# print(duplicate_ids.head(10))

# duplicate_id = df["track_id"][df["track_id"].duplicated()].iloc[0]

# print("Duplicate track_id:", duplicate_id)
# print(df[df["track_id"] == duplicate_id])

# print("Exact duplicate rows:", df.duplicated().sum())

# duplicate_id = "0CDucx9lKxuCZplLXUz0iX"

# duplicate_rows = df[df["track_id"] == duplicate_id]

# print(duplicate_rows.T)

print("Rows:", len(df))
print("Columns:", len(df.columns))

df.info()
