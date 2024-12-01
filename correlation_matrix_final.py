import pandas as pd
import os
from scipy.stats import pearsonr, spearmanr

# Function to load all DataFrames from a folder
def load_dataframes_from_folder(folder_path, file_extension=".csv"):
    rna_data = []
    rna_names = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(file_extension):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            rna_data.append(df)
            rna_name = os.path.splitext(file_name)[0]
            rna_names.append(rna_name)
    return rna_data, rna_names

# Function to calculate correlations
def calculate_correlations(rna_data, rna_names, output_path):
    pearson_results = pd.DataFrame(columns=["model_id"] + ["RMSD", "MCQ", "TM-score"])
    spearman_results = pd.DataFrame(columns=["model_id"] + ["RMSD", "MCQ", "TM-score"])
    
    for i, df in enumerate(rna_data):
        rna_name = rna_names[i]
        pearson_row = {"model_id": f"CG_RMSD_{rna_name}"}
        spearman_row = {"model_id": f"CG_RMSD_{rna_name}"}
        
        # Ensure to drop rows with NaN in any column before calculating correlations
        df_cleaned = df.dropna(subset=["CG_RMSD", "RMSD", "MCQ", "TM-score"])
        df_cleaned.to_csv(f"{output_path}/cleaned_file_{rna_name}.csv", index=False)
        
        for metric in ["RMSD", "MCQ", "TM-score"]:
            if not df_cleaned.empty:
                # Pearson correlation, handling NaN values automatically
                pearson_corr, _ = pearsonr(df_cleaned["CG_RMSD"], df_cleaned[metric])
                pearson_row[metric] = pearson_corr
                
                # Spearman correlation, handling NaN values automatically
                spearman_corr, _ = spearmanr(df_cleaned["CG_RMSD"], df_cleaned[metric])
                spearman_row[metric] = spearman_corr
        
        pearson_results = pd.concat([pearson_results, pd.DataFrame([pearson_row])], ignore_index=True)
        spearman_results = pd.concat([spearman_results, pd.DataFrame([spearman_row])], ignore_index=True)
    
    return pearson_results, spearman_results

# Function to save results
def save_dataframe(df, folder_path, filename):
    file_path = os.path.join(folder_path, filename)
    df.to_csv(file_path, index=False)
    print(f"DataFrame saved to {file_path}")

# Main code 
if __name__ == "__main__":
    folder_path = "/home/jey/Bureau/m2/BIOinf_ARN/clement_B_project/coarse-grained-RMSD/merged/"  # Path to your folder
    output_path = "/home/jey/Bureau/m2/BIOinf_ARN/clement_B_project/coarse-grained-RMSD/corr_results"

    rna_data, rna_names = load_dataframes_from_folder(folder_path, file_extension=".csv")
    pearson_results, spearman_results = calculate_correlations(rna_data, rna_names, output_path)

    print("Pearson Correlations:")
    print(pearson_results)
    print("\nSpearman Correlations:")
    print(spearman_results)

    # Save results
    save_dataframe(pearson_results, output_path, "pearson_results.csv")
    save_dataframe(spearman_results, output_path, "spearman_results.csv")
