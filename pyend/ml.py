from pyend.mock import MockModel
from abc import ABC
import logging
from pydantic import BaseModel
from typing import Any

logger = logging.getLogger(__name__)


class BasePrediction(BaseModel):
    pass


class FraudPrediction(BasePrediction):
    transaction_id: int
    predicted_label: bool
    fraud_probability: float


class SomeModel(ABC):
    def __init__(self, pickle_path: str) -> None:
        self.model = MockModel()  # joblib.load(pickle_path)

    def predict(self, *args, **kwargs) -> BasePrediction:
        raise NotImplementedError


class HighlySophisticatedModel(SomeModel):
    def __init__(self, pickle_path: str) -> None:
        super().__init__(pickle_path)

    def transform_to_feature(
        self,
        transaction_id: int,
        amount: float,
        time: str,
        age_of_account: str,
        number_of_transactions: int,
    ) -> list[Any]:
        # imagine this is a complex transformation with some science behind it.
        return [[transaction_id, amount, time, age_of_account, number_of_transactions]]

    def predict(
        self,
        transaction_id: int,
        amount: float,
        time: str,
        age_of_account: str,
        number_of_transactions: int,
    ) -> FraudPrediction:
        features = self.transform_to_feature(
            transaction_id, amount, time, age_of_account, number_of_transactions
        )
        predicted_label = self.model.predict(features)[0]
        fraud_probability = self.model.predict_proba(features)[0][0]
        return FraudPrediction(
            transaction_id=transaction_id,
            predicted_label=predicted_label,
            fraud_probability=fraud_probability,
        )
