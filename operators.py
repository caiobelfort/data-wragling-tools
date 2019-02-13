import pandas as pd
from typing import List, Tuple


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
    lhs: Left side dataframe
    rhs: Right side dataframe
    keys: Join on these keys
    how: Options are ['inner', 'left', 'right]
    keep_cols: Columns to keep on dataframe after merge
    **kwargs: pandas merge arguments

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

