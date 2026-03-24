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


def main():
    pass


if __name__ == "__main__":
    main()
