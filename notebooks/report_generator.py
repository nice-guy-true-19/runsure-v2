class ReportGenerator:

    def generate(self, result):

        print("\n================================")
        print("PIPELINE VALIDATION REPORT")
        print("================================")

        print("\nFILE:", result.get("filepath", "Unknown"))

        print("\nRISK LEVEL:", result.get("risk_level", "UNKNOWN"))
        print("FINAL SCORE:", result.get("final_risk_score", 0))

        print("\nWARNINGS")

        warnings = result.get("warnings", [])

        if warnings:
            for w in warnings:
                print("-", w)
        else:
            print("None")

        # NEW SECTION
        print("\nSUGGESTED ACTIONS")
        print("\nWHY THIS IS RISKY")

        if warnings:

            for w in warnings:

                if "missing value" in w:
                    print("- High missing data can bias models and reduce training accuracy.")

                elif "categorical columns" in w:
                    print("- Many categorical features increase dimensionality and model complexity.")

                elif "memory usage" in w:
                    print("- Large datasets may exceed system memory and crash training pipelines.")

                elif "Data Leakage" in w:
                    print("- Scaling before splitting exposes test data to training statistics.")

                else:
                    print("- This issue may affect model training reliability.")

            else:
                print("None")

        if warnings:

            for w in warnings:

                if "missing value" in w:
                    print("- Use SimpleImputer or fillna() to handle missing values")

                elif "categorical columns" in w:
                    print("- Apply encoding (OneHotEncoder or LabelEncoder)")

                elif "memory usage" in w:
                    print("- Use chunk loading or distributed tools like Dask")

                elif "Data Leakage" in w:
                    print("- Apply scaling AFTER train_test_split")

                else:
                    print("- Review preprocessing pipeline")

        else:
            print("None")

        print("\n================================\n")