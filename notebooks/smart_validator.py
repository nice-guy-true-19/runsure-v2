import os

from brain_core import CIPipelineValidator
from dataset_profiler import DatasetProfiler
from preprocessing_analyzer import PreprocessingAnalyzer


class SmartValidator:

    def __init__(self):
        self.pipeline_validator = CIPipelineValidator()
        self.dataset_profiler = DatasetProfiler()
        self.preprocessing_analyzer = PreprocessingAnalyzer()

    def validate(self, filepath):

        extension = os.path.splitext(filepath)[1]

        if extension == ".json":
            return self.pipeline_validator.validate_file_dict(filepath)

        elif extension == ".csv":

            profile = self.dataset_profiler.profile(filepath)

            return {
                "filepath": filepath,
                "risk_level": "LOW",
                "final_risk_score": 0,
                "warnings": [],
                "details": {"dataset_profile": profile}
            }

        elif extension == ".py":

            analysis = self.preprocessing_analyzer.analyze(filepath)

            return {
                "filepath": filepath,
                "risk_level": "MEDIUM" if analysis["warnings"] else "LOW",
                "final_risk_score": 50 if analysis["warnings"] else 0,
                "warnings": analysis["warnings"],
                "details": analysis
            }

        else:
            return {
                "filepath": filepath,
                "risk_level": "UNKNOWN",
                "final_risk_score": 0,
                "warnings": ["Unsupported file type"]
            }