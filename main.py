from io import StringIO

import httpx
import pandas as pd
import polars as pl

SCHEMA = pl.Schema(
    [
        ("integers", pl.Int64),
        ("floats", pl.Float64),
        ("list_integers", pl.List(pl.Int64)),
        ("list_floats", pl.List(pl.Float64)),
        ("list_strings", pl.List(pl.Utf8)),
    ]
)


URL = "https://raw.githubusercontent.com/tbm-novonesis/json-2-parquet/refs/heads/main/example.json"


def main():
    print("- " * 15, "Polars", " -" * 15)
    response = httpx.get(URL)
    df = pl.read_json(StringIO(response.text), schema=SCHEMA)
    print(df)

    print("- " * 15, "Pandas", " -" * 15)
    df = pd.read_json(URL, orient="records")
    print(df)


if __name__ == "__main__":
    main()
