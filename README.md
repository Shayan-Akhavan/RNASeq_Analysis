# RNA-Seq Analysis Tool 🧬

[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](requirements.txt)

A Python-based tool for exploratory analysis of RNA sequencing (RNA-Seq) data. This tool provides visualizations and statistical analysis of gene expression patterns.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Data Format](#data-format)
- [Technical Details](#technical-details)


## ✨ Features

- Distribution visualization of expression levels
- Identification and visualization of highly variable genes
- Principal Component Analysis (PCA) for sample clustering
- Basic statistical summaries

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rnaseq-analysis.git
cd rnaseq-analysis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📖 Usage

1. Place your RNA-Seq data file (in RPKM format) in the project directory
2. Run the analysis:
```bash
python RNASeq.py
```

### Example
```python
python RNASeq.py --input GSE71585_RefSeq_RPKM.csv.gz --output results/
```

## 📊 Output

The script generates three visualizations:

### 1. Expression Distribution Plot
![Image](https://github.com/user-attachments/assets/281ba1fd-6862-460b-9914-6952a5841d05)
- Histogram showing distribution of gene expression levels
- Log scale for better visualization of range





### 2. Variable Genes Heatmap
![Image](https://github.com/user-attachments/assets/cd55b07f-3c58-4655-9df3-d2560bbbd7d2)
- Visualizes top 50 most variable genes
- Helps identify expression patterns



### 3. PCA Plot
![Image](https://github.com/user-attachments/assets/78167ec5-84c6-4d4c-9986-fd4f62d753e1)
- Shows first two principal components
- Useful for identifying sample clusters

## 📑 Data Format

Input file requirements:
- Gzipped CSV format (.csv.gz)
- RPKM normalized expression values
- Structure:
  ```
  gene_id,sample1,sample2,sample3,...
  GENE1,0.5,1.2,0.8,...
  GENE2,2.1,1.8,1.9,...
  ```

## 🔧 Technical Details

The analysis pipeline includes:
1. Data loading and preprocessing
2. Conversion to numeric format
3. Summary statistics generation
4. Visualization creation
5. PCA analysis

## ⚠️ Dependencies

- pandas >= 1.3.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- scikit-learn >= 0.24.0

