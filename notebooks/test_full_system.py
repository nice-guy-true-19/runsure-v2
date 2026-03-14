from smart_validator import SmartValidator
from report_generator import ReportGenerator

validator = SmartValidator()
reporter = ReportGenerator()

result = validator.validate("notebooks/sample_dataset.csv")

reporter.generate(result)