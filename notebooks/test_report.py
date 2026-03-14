from brain_core import CIPipelineValidator
from report_generator import ReportGenerator

validator = CIPipelineValidator()
reporter = ReportGenerator()

result = validator.validate_file_dict("notebooks/sample_dataset.csv")

reporter.generate(result)