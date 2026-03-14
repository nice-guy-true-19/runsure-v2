from dataset_profiler import DatasetProfiler

profiler = DatasetProfiler()

result = profiler.profile("notebooks/sample_dataset.csv")

print(result)