# Mini Pediatric AML Epigenetics Pipeline


## Overview

This project implements a bioinformatics pipeline inspired by research related to my practicum research: pediatric acute myeloid leukemia (AML) research. The pipeline focuses on summarizing relationships between DNMT3B gene expression, genome-wide methylation burden (GWMB), and minimal residual disease (MRD) status.

The workflow processes a small toy dataset, cleans the data and generates summaries including averages and correlations. it is craeted to be reproducible and runnable using Docker and Nextflow.

## Getting Started

### Setup

Ensure that the following tools are installed:
- Docker 
- Nextflow

Clone the repository and navigate into the project folder:
```
git clone https://github.com/SmartOval/aml-dnmt3b-pipeline
cd aml-dnmt3b-pipeline
```
Finally, build the Docker container:
```
docker build -t aml-dnmt3b:latest .
```
### Usage

Run the pipeline using the provided toy dataset:
```
nextflow run main.nf -profile docker
```
This terminal command starts the full workflow inside the Docker contianer

### Output

After running the pipline, results will be created in the results/ directory:

* results/cleaned/aml_toy_data.cleaned.csv
    Cleaned version of the inputted dataset.
* results/summary/aml_summary.txt
    Text summary including:
    * Number of samples
    * Mean DNMT3B expression
    * Mean GWMB
    * Correlation between DNMT3B expression and GWMB
    * Group-wise averages by their respective MRD statuses.
* results/summary/mrd_group_means.csv
    * Table of average DNMT3B expression and GWMB group by MRD status.

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Nobel Makonnen 
