"""Reusable modeling helpers for the Airbnb project."""

from __future__ import annotations

import joblib
from sklearn.ensemble import RandomForestRegressor


def train_model(X, y):
	model = RandomForestRegressor()
	model.fit(X, y)
	return model


def save_model(model, path="../models/price_model.pkl"):
	joblib.dump(model, path)
	return path
