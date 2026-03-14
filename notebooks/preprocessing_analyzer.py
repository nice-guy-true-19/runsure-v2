import ast


class PreprocessingAnalyzer:
    def __init__(self):
        pass

    def analyze(self, filepath):
        with open(filepath, "r") as f:
            code = f.read()

        tree = ast.parse(code)

        found_functions = []
        call_order = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):
                    func_name = node.func.id

                elif isinstance(node.func, ast.Attribute):
                    func_name = node.func.attr

                else:
                    continue

                found_functions.append(func_name)
                call_order.append(func_name)

        warnings = []

        if "fit_transform" in call_order and "train_test_split" in call_order:
            if call_order.index("fit_transform") < call_order.index("train_test_split"):
                warnings.append("Potential Data Leakage: Scaling applied before train_test_split")

        return {
            "file": filepath,
            "parsed": True,
            "nodes": len(list(ast.walk(tree))),
            "functions_detected": list(set(found_functions)),
            "warnings": warnings
        }