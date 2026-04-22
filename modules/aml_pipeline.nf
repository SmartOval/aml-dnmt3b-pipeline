process PREPROCESS_AML {
    publishDir "results/cleaned", mode: "copy"

    input:
    path input_csv

    output:
    path "aml_toy_data.cleaned.csv"

    script:
    """
    python /app/scripts/preprocess_aml.py \
      --input $input_csv \
      --output aml_toy_data.cleaned.csv
    """
}

process SUMMARIZE_AML {
    publishDir "results/summary", mode: "copy"

    input:
    path cleaned_csv

    output:
    path "aml_summary.txt"
    path "mrd_group_means.csv"

    script:
    """
    python /app/scripts/summarize_aml.py \
      --input $cleaned_csv \
      --outdir .
    """
}