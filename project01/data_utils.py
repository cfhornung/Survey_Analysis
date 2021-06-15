
"""Utility functions for wrangling data."""

__author__ = "720053793"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Column Values."""
    col_val: list[str] = []
    for row in table:
        col_val.append(row[key]) 
    return col_val


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Columnar."""
    dict_table: dict[str, list[str]] = {}
    keys = table[0].keys()
    for i in keys:
        dict_table[i] = column_values(table, i)   
    return dict_table    


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Creating a head function."""
    head_dict: dict[str, list[str]] = {}
    keys = table.keys()
    for i in keys:
        col_val: list[str] = []
        row: int = 0
        for j in i:
            while row < n:
                col_val.append(table[i][row])
                head_dict[i] = col_val
                row += 1
    return head_dict


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Select Function."""
    select_dict: dict[str, list[str]] = {}
    for i in names:
        select_dict[i] = table[i]
    return select_dict


def count(values: list[str]) -> dict[str, int]:
    """Count."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1    
    return counts


def percentages(count: dict[int, int], list1: list[int]) -> list[int]:
    """Percentages."""
    i: int = 1
    percentages = []
    while i < 8:
        if i in count:
            number = int(round(count[i]/len(list1)*100, 0))
            percentages.append(number)
            i += 1
        else:
            number = 0
            percentages.append(number)
            i+=1
    return percentages


def perc(list: list[int]) -> dict[int, int]:
    """Percentages."""
    i: int = 0
    dict_perc: dict[int, int] = {}
    while i < 7:
            dict_perc[i+1] = list[i]
            i += 1
    return dict_perc


def useful(dictionary: dict[int, int]) -> dict[str, int]:
    """Useful."""
    low: list[int] = []
    moderate: list[int] = []
    high: list[int] = []
    i = 1
    while i < 8:
        if i < 4:
            value: int = dictionary[i]
            low.append(value)
            i += 1
        elif i < 6:
            value: int = dictionary[i]
            moderate.append(value)
            i += 1
        else:
            value: int = dictionary[i]
            high.append(value)
            i += 1
    low_sum: int = sum(low)
    moderate_sum: int = sum(moderate)
    high_sum: int = sum(high)
    useful_dict: dict[str, int] = {"low": low_sum, "moderate": moderate_sum, "high": high_sum}
    return useful_dict


def more_than(col: list[int]) -> list[bool]:
    """Masked Function."""
    result: list[bool] = []
    for item in col:
        result.append(item >= 50.0)
    return result


def pie(col: list[int]) -> float:
    """Useing this function to create a pie chart."""
    sums: int = sum(col)
    total: float = round(sums/7, 0)
    return total