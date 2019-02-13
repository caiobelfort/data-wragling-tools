import pandas as pd
from typing import List, Tuple, Dict


def merge_operator(lhs: pd.DataFrame,
                   rhs: pd.DataFrame,
                   keys: List[Tuple[str, str]] or Tuple[str, str],
                   how: str = 'inner',
                   keep_cols: List[str] = None,
                   **kwargs
                   ) -> pd.DataFrame:
    """
    Operator to merge two dataframe based on some keys.

    Parameters
    ----------
    lhs
        Left side dataframe
    rhs
        Right side dataframe
    keys
        Join on these keys
    how
        Options are ['inner', 'left', 'right]
    keep_cols
        Columns to keep on dataframe after merge
    **kwargs
        pandas merge arguments

    Returns
    -------
    pd.DataFrame
        Merged dataframe
    """

    # Check if keys exists in dataframes
    if isinstance(keys, list):
        lhs_keys, rhs_keys = zip(*keys)
        lhs_diffs = set(lhs_keys) - set(lhs.columns)
        rhs_diffs = set(rhs_keys) - set(rhs.columns)
        if len(lhs_diffs):
            raise KeyError(f"lhs doesn't have all keys passed. Missing keys: {list(lhs_diffs)}")
        if len(rhs_diffs):
            raise KeyError(f"rhs doesn't have all keys passed. Missing keys: {list(rhs_diffs)}")
    else:
        lhs_keys = keys[0]
        rhs_keys = keys[1]

        if lhs_keys not in lhs.columns:
            raise KeyError(f"lhs doesn't have passed key. Missing key {lhs_keys}")

        if rhs_keys not in rhs.columns:
            raise KeyError(f"lhs doesn't have passed key. Missing key {lhs_keys}")

    # Applies the merge between the dataframes
    merged_data = lhs.merge(rhs,
                            how=how,
                            left_on=lhs_keys,
                            right_on=rhs_keys,
                            **kwargs
                            )

    if keep_cols:
        return merged_data[keep_cols]
    return merged_data


def load_dataframe_from_file_operator(filename: str, format='csv', **kwargs) -> pd.DataFrame:
    """
    Loads dataframe from a local file using the method informed

    Parameters
    ----------

    filename
        The filename of data.
    format
        the format of data to read, options are ['csv', 'pickle', 'xlsx'].
    **kwargs
        Additional arguments for loader functions.

    Returns
    -------
    pd.DataFrame
       The dataframe loaded from the file
    """

    if format == 'csv':
        return pd.read_csv(filename, **kwargs)
    elif format == 'pickle':
        return pd.read_pickle(filename, **kwargs)
    elif format == 'xlsx':
        return pd.read_excel(filename, **kwargs)
    else:
        raise ValueError(f"format {format} isn't compatible.")


def write_dataframe_to_file_operator(data: pd.DataFrame, filename: str, format='csv', **kwargs):
    """
    Writes dataframe to a local file using method informed

    Parameters
    ----------
    filename
        The file to save the data
    format
        The format to save the data, options are ['csv', 'pickle', 'xlsx']
    kwargs
        Additional arguments for writer functions
    """

    if format == 'csv':
        data.to_csv(filename, **kwargs)
    elif format == 'pickle':
        data.to_pickle(filename, **kwargs)
    elif format == 'xlsx':
        data.to_excel(filename, **kwargs)
    else:
        raise ValueError(f"format {format} isn't compatible.")


def nan_imputer_operator(data: pd.DataFrame, col_mappers: dict) -> pd.DataFrame:
    """
    Input value to NaNs.

    Parameters
    ----------
    data: pd.DataFrame
    col_mappers: dict in format {col: value}

    Returns
    -------
    """

    cp_data = data.copy()

    for col in col_mappers.keys():
        cp_data[col] = cp_data.fillna(col_mappers[col])

    return cp_data
