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

repo_dir = "../data/opl-repo"
out_dir = "../data/download-out"

ingest_openpwl.download_openpwl_data(out_dir, repo_dir)
