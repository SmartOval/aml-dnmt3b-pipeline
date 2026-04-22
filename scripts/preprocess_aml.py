import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input", required = True)
parser.add_argument("--output", required = True)
args = parser.parse_args()

df = pd.read_csv(args.input)

needed = ["sample_id", "dnmt3b_expression", "gwmb", "mrd_status"]

for col in needed:
	if col not in df.columns:
		print(f"Missing Column: {col}")
		exit(1)

df = df[needed]

df["dnmt3b_expression"] = pd.to_numeric(df["dnmt3b_expression"], errors = "coerce")
df["gwmb"] = pd.to_numeric(df["gwmb"], errors = "coerce")
df["mrd_status"] = df["mrd_status"].str.lower()

df = df.dropna()

outdir = os.path.dirname(args.output)

if outdir != "":
    os.makedirs(outdir, exist_ok=True)

df.to_csv(args.output, index=False)
print("Clean File saved to:", args.output)
