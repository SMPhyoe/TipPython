# Created by Su Myat Phyoe at 9:30 pm 24/10/2023 using PyCharm

# Concrete implementation for a Linear Regression model
class LinearRegressionModel:
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
class RandomForestModel:
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


# Example usage:
model_type = "RandomForest"  # Change this to "LinearRegression" or another model type
if model_type == "LinearRegression":
    model = LinearRegressionModel()
elif model_type == "RandomForest":
    model = RandomForestModel()

# You can use the model without using any base classes
model.train("training_data")
prediction = model.predict("input_data")
print(f"Model Name: {model.model_name}")
