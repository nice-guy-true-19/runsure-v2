from preprocessing_analyzer import PreprocessingAnalyzer

analyzer = PreprocessingAnalyzer()

result = analyzer.analyze("notebooks/sample_preprocess.py")

print("\nFILE:", result["file"])
print("PARSED:", result["parsed"])
print("TOTAL AST NODES:", result["nodes"])
print("FUNCTIONS:", result["functions_detected"])
print("WARNINGS:", result["warnings"])