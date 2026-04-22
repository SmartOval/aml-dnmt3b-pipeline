import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--outdir", required=True)
args = parser.parse_args()

df = pd.read_csv(args.input)

os.makedirs(args.outdir, exist_ok=True)

mean_expression = df["dnmt3b_expression"].mean()
mean_gwmb = df["gwmb"].mean()
correlation = df["dnmt3b_expression"].corr(df["gwmb"])

group_means = df.groupby("mrd_status")[["dnmt3b_expression", "gwmb"]].mean()

summary_path = os.path.join(args.outdir, "aml_summary.txt")
group_path = os.path.join(args.outdir, "mrd_group_means.csv")

with open(summary_path, "w") as f:
    f.write("DNMT3B AML Summary\n")
    f.write("------------------\n")
    f.write(f"Number of samples: {len(df)}\n")
    f.write(f"Mean DNMT3B expression: {mean_expression:.3f}\n")
    f.write(f"Mean GWMB: {mean_gwmb:.3f}\n")
    f.write(f"Correlation between DNMT3B expression and GWMB: {correlation:.3f}\n\n")
    f.write("Average values by MRD status:\n")
    f.write(group_means.to_string())
    f.write("\n")

group_means.to_csv(group_path)

print("Summary saved to:", summary_path)
print("Group means saved to:", group_path)