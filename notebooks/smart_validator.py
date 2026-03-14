import os

from preprocessing_analyzer import PreprocessingAnalyzer
from dataset_profiler import DatasetProfiler
from brain_core import CIPipelineValidator


class SmartValidator:

    def __init__(self):
        self.dataset_profiler = DatasetProfiler()
        self.preprocessing_analyzer = PreprocessingAnalyzer()
        self.pipeline_validator = CIPipelineValidator()

    def validate(self, filepath):

        extension = os.path.splitext(filepath)[1]

        if extension == ".json":
            return self.pipeline_validator.validate(filepath)

        elif extension == ".csv":
            return self.dataset_profiler.profile(filepath)

        elif extension == ".py":
            return self.preprocessing_analyzer.analyze(filepath)

        else:
            return {"error": "Unsupported file type"}