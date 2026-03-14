import pandas as pd


class DatasetProfiler:

    def profile(self, filepath):

        # load dataset
        df = pd.read_csv(filepath)

        # basic statistics
        rows = len(df)
        columns = len(df.columns)

        # count numeric columns
        numeric_columns = df.select_dtypes(include=['number']).shape[1]

        # count categorical columns
        categorical_columns = df.select_dtypes(include=['object']).shape[1]

        # missing values
        missing_values = df.isnull().sum().sum()

        # missing ratio
        missing_ratio = missing_values / (rows * columns)

        # memory usage
        memory_usage_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)

        return {
            "rows": rows,
            "columns": columns,
            "numeric_columns": numeric_columns,
            "categorical_columns": categorical_columns,
            "missing_ratio": round(missing_ratio, 4),
            "memory_usage_mb": round(memory_usage_mb, 2)
        }