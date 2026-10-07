from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

inventory = pd.read_csv(DATA / "source_inventory.csv")
matrix = pd.read_csv(DATA / "preparedness_evidence_matrix.csv")
scorecard = pd.read_csv(DATA / "evidence_quality_scorecard.csv")

# Reproducible checks used for the publication package.
assert inventory["source_id"].is_unique
assert matrix["finding_id"].is_unique
assert set(matrix["source_id"]).issubset(set(inventory["source_id"]))
assert set(scorecard["source_id"]).issubset(set(inventory.loc[inventory["included"] == "Yes", "source_id"]))
assert matrix["domain"].nunique() == 7

print(f"Inventory sources: {len(inventory)}")
print(f"Matrix findings: {len(matrix)}")
print(f"Included sources scored: {len(scorecard)}")
print("Cleaning and validation checks passed.")
