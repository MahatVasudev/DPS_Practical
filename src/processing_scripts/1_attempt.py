import matplotlib.pyplot as plt
import polars as pl


def show_info(data: pl.DataFrame):
    data.show(5)

    print("------ Column Glimpse --------")
    data.glimpse()

    print("------ Column Description --------")
    data.describe().show(None)

    data.null_count().show(None)

    duplicates = data.is_duplicated()

    print("Duplicates present in the dataset: ", duplicates.sum())

    print("Sample Duplicates")

    data.filter(duplicates).show(3)


def remove_duplicates(data: pl.DataFrame): ...


def correct_dtypes(data: pl.DataFrame, analysis=False):

    if analysis:
        data.filter(~pl.col("StockCode").str.contains(r"^\d+$")).show()


if __name__ == "__main__":
    with pl.Config(tbl_cols=-1, tbl_width_chars=-1):
        data = pl.read_excel("data/online_retail_II.xlsx")
        data.with_columns(pl.col('s').dt.date

        show_info(data)

        # correct_dtypes(data, analysis=True) # is not valid
