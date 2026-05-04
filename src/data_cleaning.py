"""Reusable data cleaning helpers for the Airbnb project."""

from __future__ import annotations

import pandas as pd


def clean_price(df: pd.DataFrame) -> pd.DataFrame:
	"""Convert the ``price`` column from currency text to numeric floats.

	The function removes dollar signs and commas, then casts the column to
	``float`` in place and returns the same DataFrame for chaining.
	"""
	df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
	return df
