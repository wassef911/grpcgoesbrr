import random


class MockModel:
    def predict(self, features):
        """Simulate model prediction.

        Args:
            features (list): A list of feature vectors, where each feature vector is a list of values.

        Returns:
            list: A list of predicted labels (TotalFraudDude or LooksLegit).
        """
        # Generate a random prediction for each feature vector
        # (okey to use random here since this is a mock model for fun!)
        return [random.choice([True, False]) for _ in features]

    def predict_proba(self, features):
        """Simulate model probability predictions.

        Args:
            features (list): A list of feature vectors.

        Returns:
            list: A list where each element is a list [probability of 0, probability of 1].
        """
        # Generate random probabilities for each prediction
        # (okey to use random here since this is a mock model for fun!)
        return [[random.random(), random.random()] for _ in features]
