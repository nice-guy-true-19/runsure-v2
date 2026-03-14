import warnings
warnings.filterwarnings("ignore")

from brain_core import CIPipelineValidator

validator = CIPipelineValidator()

result = validator.validate_file_dict("notebooks/sample_dataset.csv")

print("\nFILE:", result["filepath"])
print("RISK LEVEL:", result["risk_level"])
print("FINAL SCORE:", result["final_risk_score"])

print("\nDATASET PROFILE")

profile = result["details"].get("dataset_profile", {})

for key, value in profile.items():
    print(f"{key}: {value}")

print("\nWARNINGS")

if result["warnings"]:
    for w in result["warnings"]:
        print("-", w)
else:
    print("None")

print("\nSUGGESTED ACTIONS")

if result["warnings"]:
    for w in result["warnings"]:
        if "missing value" in w:
            print("- Use SimpleImputer or fillna() to handle missing values")

        elif "categorical columns" in w:
            print("- Apply encoding (OneHotEncoder or LabelEncoder)")

        elif "memory usage" in w:
            print("- Use chunk loading (pandas chunksize) or Dask")

        else:
            print("- Review preprocessing pipeline")
else:
    print("None")