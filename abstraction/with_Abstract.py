# Created by Su_Myat_Phyoe at 9:12 pm 24/10/2023 using PyCharm

from abc import ABC, abstractmethod


# Base class for prediction models
class PredictionModel(ABC):
    @abstractmethod
    def train(self, training_data):
        pass

    @abstractmethod
    def predict(self, input_data):
        pass

    @property
    @abstractmethod
    def model_name(self):
        pass


# Concrete implementation for a Linear Regression model
class LinearRegressionModel(PredictionModel):
    def train(self, training_data):
        # Replace with actual training logic
        print("Training Linear Regression model")

    def predict(self, input_data):
        # Replace with actual prediction logic
        print("Making predictions using Linear Regression model")
        return 42  # Replace with the actual prediction result

    @property
    def model_name(self):
        return "Linear Regression Model"


# Concrete implementation for a Random Forest model
class RandomForestModel(PredictionModel):
    def train(self, training_data):
        # Replace with actual training logic
        print("Training Random Forest model")

    def predict(self, input_data):
        # Replace with actual prediction logic
        print("Making predictions using Random Forest model")
        return 24  # Replace with the actual prediction result

    @property
    def model_name(self):
        return "Random Forest Model"


# Prediction Model Factory
class PredictionModelFactory:
    @staticmethod
    def create_model(model_type):
        if model_type == "LinearRegression":
            return LinearRegressionModel()
        elif model_type == "RandomForest":
            return RandomForestModel()
        # Add more model types as needed


# Example usage:
model_type = "RandomForest"  # Change this to "LinearRegression" or another model type
model = PredictionModelFactory.create_model(model_type)

# You can use the model interchangeably by adhering to the common PredictionModel base class
model.train("training_data")
prediction = model.predict("input_data")
print(f"Model Name: {model.model_name}")
