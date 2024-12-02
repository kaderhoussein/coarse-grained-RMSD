# Coarse-grained RMSD

This repository contains a set of tools to analyze RNA structures by calculating Coarse-Grained RMSD (CG-RMSD), merging CSV files, calculating correlations, and generating heatmaps for visualizing structural data. The project evaluates predicted RNA structures against native structures and offers various utility functions.

## Features

- **Coarse-Grained RMSD Computation**: Compute Coarse-Grained RMSD between predicted and native RNA structures.
  - Supports both single structure and multiple structure computations.
  
- **CSV Merging**: Merge CSV files containing structural data, including CG-RMSD results and other metrics.

- **Correlation Calculations**: Compute Pearson and Spearman correlations.

- **Heatmap Generation**: Generate heatmaps to visualize Pearson and Spearman correlations.


## Installation

### Prerequisites

- Python 3.x
- Required Python libraries listed in `requirements.txt`

### Steps to Install

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/rna-structural-analysis.git
    cd rna-structural-analysis
    ```

2. Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Organize your input files into the appropriate directories:
   - Place native RNA structures in `./data/NATIVE/`.
   - Place predicted RNA structures in `./data/PREDS/`.
   - Place other CSV data (such as RMSD results) in `./data/SCORES/`.

## Usage

### Testing Functions

This project includes various functions for testing specific parts of the analysis. The following functions are available:

1. **Coarse-Grained RMSD for Single Structure**:

    ```python
    test_cg_rmsd_single_structure()
    ```

2. **Coarse-Grained RMSD for Multiple Structures**:

    ```python
    test_cg_rmsd_multiple_structures()
    ```

3. **CSV Merging**:

    ```python
    test_csv_merging()
    ```

4. **Correlation Calculations (Pearson and Spearman)**:

    ```python
    test_correlation_calculations()
    ```

5. **Heatmap Generation**:

    ```python
    test_heatmap_generation()
    ```

### Example Workflow

To run the full pipeline, you can call the following functions sequentially:

```python
if __name__ == "__main__":
    test_cg_rmsd_multiple_structures()       # Compute CG-RMSD for multiple structures
    test_csv_merging()                       # Merge RMSD results with other data
    test_correlation_calculations()          # Calculate correlations
    test_heatmap_generation()                # Generate heatmaps from correlation data


