############ MERGING CORRELATION RESULTS ##################################
import pandas as pd

# Example: Load your three CSV files
# Replace these paths with the actual paths to your files
df1 = pd.read_csv("/home/zozo/Bureau/Coarse_grain_RMSD/P-C1-O3/corr_results/spearman_results.csv")  # Combination 1
df2 = pd.read_csv("/home/zozo/Bureau/Coarse_grain_RMSD/C1/corr_results/spearman_results.csv")  # Combination 2
df3 = pd.read_csv("/home/zozo/Bureau/Coarse_grain_RMSD/C1-03/corr_results/spearman_results.csv")  # Combination 3
df4 = pd.read_csv("/home/zozo/Bureau/Coarse_grain_RMSD/All_atoms/corr_results/spearman_results.csv")  # Combination 3

# Add a new column to indicate the atom combination for each DataFrame
df1["Atom_Combination"] = "P, C1', O3'"
df2["Atom_Combination"] = "C1'"
df3["Atom_Combination"] = "C1', O3'"
df4["Atom_Combination"] = "All_atoms"

# Combine the three DataFrames into one
combined_df = pd.concat([df4, df1, df3, df2], axis=0)

# Optional: Reset the index for a clean DataFrame
combined_df.reset_index(drop=True, inplace=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("/home/zozo/Bureau/Coarse_grain_RMSD/combined_results_spearman.csv", index=False)

# Print the first few rows of the combined DataFrame to verify
print(combined_df.head())

################## BOX PLOT #########################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
file_path = "/home/zozo/Bureau/Coarse_grain_RMSD/combined_results_spearman.csv"  # Replace with your actual file path
correlation_data = pd.read_csv(file_path)

# Reshape the data from wide to long format
correlation_data_long = correlation_data.melt(
    id_vars=["model_id", "Atom_Combination"],  # Columns to keep as is
    value_vars=["RMSD", "MCQ", "TM-score"],   # Columns to unpivot
    var_name="Metric",                        # Name for the new column for metrics
    value_name="Correlation"                  # Name for the new column for correlations
)

# Verify the reshaped data
print(correlation_data_long.head())

# Create box plots for each metric, grouped by Atom_Combination
g = sns.catplot(
    data=correlation_data_long,
    x="Atom_Combination",
    y="Correlation",
    col="Metric",  # Separate plot for each metric
    kind="box",
    palette="coolwarm",
    height=5,
    aspect=1.5
)

# Customize the layout
g.set_titles("{col_name}")  # Title for each subplot
g.set_axis_labels("Atom Combination", "Correlation")  # Shared axis labels
g.set_xticklabels(rotation=45, ha="right")  # Rotate x-axis labels
plt.subplots_adjust(top=0.85)  # Add space for a global title
g.fig.suptitle("Spearman Correlation Distributions by Atom Combination and Metric", fontsize=16)

# Show the plot
plt.show()
