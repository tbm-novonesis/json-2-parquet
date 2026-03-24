# `JSON` to Parquet

Read data from a URL into Pandas and Polars dataframes.

## Parquet

Offered by both dataframe libraries:

- [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html)
- [`polars.DataFrame.write_parquet`](https://docs.pola.rs/api/python/dev/reference/api/polars.DataFrame.write_parquet.html)

## Use

```sh
uv sync
uv run python main.py
```

## CI/CD

```sh
task ci
```
