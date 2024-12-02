import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_heatmaps(csv_file1, csv_file2, output_file1=None, output_file2=None):
    """
    Generate two independent heatmaps from two CSV files containing correlation data.

    Parameters:
    - csv_file1: Path to the first CSV file.
    - csv_file2: Path to the second CSV file.
    - output_file1: Optional path to save the first heatmap as an image file.
    - output_file2: Optional path to save the second heatmap as an image file.
    """
    # Load the CSV files into pandas DataFrames
    df1 = pd.read_csv(csv_file1, index_col=0)
    df2 = pd.read_csv(csv_file2, index_col=0)

    # Generate the first heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df1, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Heatmap 1")
    if output_file1:
        plt.savefig(output_file1, dpi=300, bbox_inches="tight")
        print(f"Heatmap 1 saved to {output_file1}")
    else:
        plt.show()

    # Generate the second heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df2, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Heatmap 2")
    if output_file2:
        plt.savefig(output_file2, dpi=300, bbox_inches="tight")
        print(f"Heatmap 2 saved to {output_file2}")
    else:
        plt.show()

