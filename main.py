from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.pipeline.batch_prediction import start_batch_prediction
from sensor.exception import SensorException

file_path = "/config/workspace/aps_failure_training_set1.csv"

print(__name__)
if __name__ == "__main__":
     try:
          Start_training_pipeline()
          output_file = start_batch_prediction(input_file_path= file_path)
          print(output_file)
     except Exception as e:
          print(e)