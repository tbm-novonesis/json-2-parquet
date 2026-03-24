from pathlib import Path

import polars as pl


class Test:
    SCHEMA = pl.Schema(
        [
            ("integers", pl.Int64),
            ("floats", pl.Float64),
            ("list_integers", pl.List(pl.Int64)),
            ("list_floats", pl.List(pl.Float64)),
            ("list_strings", pl.List(pl.Utf8)),
        ]
    )

    DF = pl.DataFrame(
        {
            "integers": [1, 2, 3, 4, 5],
            "floats": [1.0, 2.0, 3.0, 4.0, 5.0],
            "list_integers": [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
            "list_floats": [
                [1.0, 2.0],
                [3.0, 4.0],
                [5.0, 6.0],
                [7.0, 8.0],
                [9.0, 10.0],
            ],
            "list_strings": [
                ["a", "b"],
                ["c", "d"],
                ["e", "f"],
                ["g", "h"],
                ["i", "j"],
            ],
        }
    )

    def test_write(self):
        actual = self.DF.write_json()
        expected = (Path(__file__).parent / "testdata.json").read_text().strip()
        assert actual == expected

    def test_read(self):
        actual = pl.read_json(
            Path(__file__).parent / "testdata.json", schema=self.SCHEMA
        )
        expected = self.DF
        assert actual.equals(expected)
