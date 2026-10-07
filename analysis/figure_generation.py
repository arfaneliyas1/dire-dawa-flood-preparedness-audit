from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

matrix = pd.read_csv(DATA / "preparedness_evidence_matrix.csv")
scorecard = pd.read_csv(DATA / "evidence_quality_scorecard.csv")

# This script provides a minimal reproducible example for a domain-count figure.
# The publication figures were generated from the same verified matrix and scorecard.
domain_counts = matrix.groupby("domain")["source_id"].nunique().sort_values()
fig, ax = plt.subplots(figsize=(10, 5))
domain_counts.plot.barh(ax=ax, color="#2F6B7C")
ax.set_xlabel("Unique included sources")
ax.set_title("Evidence sources by preparedness domain")
fig.tight_layout()
fig.savefig(OUT / "domain_source_counts.png", dpi=180)
plt.close(fig)
print(f"Created {OUT / 'domain_source_counts.png'}")
