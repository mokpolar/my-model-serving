import os
from typing import List, Optional, Tuple
import logging

import joblib
from sklearn.pipeline import Pipeline

from app.data import PredictionInput, PredictionOutput



class NewsgroupModel:
    model: Optional[Pipeline]
    target: Optional[List[str]]


    def load_model(self):
        model_file = os.path.join(os.path.dirname(__file__), "sklearn_model/newsgroups_model.joblib")
        loaded_model: Tuple[Pipeline, List[str]] = joblib.load(model_file)
        model, target = loaded_model


        self.model = model
        self.target = target

    async def predict(self, input: PredictionInput) -> PredictionOutput:
        if not self.model or not self.target:
            raise RuntimeError("Model is not loaded")

        logging.info("hi")

        prediction = self.model.predict([input.text])
        category = self.target[prediction[0]]
        return PredictionOutput(category=category)

        
