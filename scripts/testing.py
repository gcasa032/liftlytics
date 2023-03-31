import pandas
import pyarrow.parquet
import clean_openpwl
import ingest_openpwl
from datetime import datetime
import re

def print_schema():

    schema = pyarrow.parquet.read_schema(out_path, memory_map=True)
    aws_schema = []

    for r in schema:
        aws_schema.append({
        "Name": r.name,
        "Type": r.type,
        "Comment": ""
        })

    print(aws_schema)

csv_path = ""
out_path = ""

df2 = pandas.read_parquet(out_path)

df_age = df2[df2['Age'] > 80]
bw_constraint = df2[df2['BodyweightKg'] > 230][['Name', 'BodyweightKg', 'Date', 'Federation', 'Equipment', 'Division', 'TotalKg']].sort_values(by="BodyweightKg", ascending=False)
total_constraint = df2[['Name', 'BodyweightKg', 'Date', 'Federation', 'Equipment', 'Division', 'TotalKg']].sort_values(by="TotalKg", ascending=False)


df_dupes = clean_openpwl.dupe_constraint(df2)


print(df_dupes.head(30))
