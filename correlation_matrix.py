import pandas as pd
import os
from scipy.stats import pearsonr, spearmanr


# Function to load all DataFrames from a folder
def load_dataframes_from_folder(folder_path, file_extension=".csv"):
    """
    Load all files with the specified extension from a folder into DataFrames.
    
    :param folder_path: Path to the folder containing the files.
    :param file_extension: File extension to filter files (default is .csv).
    :return: List of DataFrames and their corresponding file names (without extension).
    """

    rna_data = []
    rna_names = []
        
    # List all files in the folder with the given extension
    for file_name in os.listdir(folder_path):
        if file_name.endswith(file_extension):
            # Full path to the file
            file_path = os.path.join(folder_path, file_name)
            
            # Load the file into a DataFrame
            df = pd.read_csv(file_path)
            rna_data.append(df)
            
            # Use the file name (without extension) as the RNA name
            rna_name = os.path.splitext(file_name)[0]
            rna_names.append(rna_name)
    
    return rna_data, rna_names


# Function to calculate correlations (from earlier code)
def calculate_correlations(rna_data, rna_names):
    """
    Calculate Pearson and Spearman correlations between CG_RMSD and other metrics for multiple RNAs.
    
    :param rna_data: List of DataFrames, each containing the data for a single RNA.
    :param rna_names: List of names corresponding to each RNA.
    :return: Two DataFrames containing Pearson and Spearman correlation coefficients.
    """
    # Initialize DataFrames to store the results
    pearson_results = pd.DataFrame(columns=["model_id"] + ["RMSD", "MCQ", "TM-score"])
    spearman_results = pd.DataFrame(columns=["model_id"] + ["RMSD", "MCQ", "TM-score"])
    
    # Loop through each RNA table
    for i, df in enumerate(rna_data):
        rna_name = rna_names[i]
        # Initialize a row for the current RNA
        pearson_row = {"model_id": f"CG_RMSD_{rna_name}"}
        spearman_row = {"model_id": f"CG_RMSD_{rna_name}"}
        
        # Calculate correlations for each metric
        for metric in ["RMSD", "MCQ", "TM-score"]:
            # Pearson correlation
            pearson_corr, _ = pearsonr(df["CG_RMSD"], df[metric])
            pearson_row[metric] = pearson_corr
            
            # Spearman correlation
            spearman_corr, _ = spearmanr(df["CG_RMSD"], df[metric])
            spearman_row[metric] = spearman_corr
        
        # Append the results to the DataFrames
        pearson_results = pd.concat([pearson_results, pd.DataFrame([pearson_row])], ignore_index=True)
        spearman_results = pd.concat([spearman_results, pd.DataFrame([spearman_row])], ignore_index=True)
    
    return pearson_results, spearman_results


# Function to save the 2 correlation dataFrames 
def save_dataframe(df, folder_path, filename):
    """
    Save a DataFrame to the specified folder with the given filename.
    
    :param df: The DataFrame to save.
    :param folder_path: Path to the folder where the file will be saved.
    :param filename: Name of the file (including .csv extension).
    """
    
    # Full path for the file
    file_path = os.path.join(folder_path, filename)
    
    # Save the DataFrame as a CSV file
    df.to_csv(file_path, index=False)
    print(f"DataFrame saved to {file_path}")


# Main code 
if __name__ == "__main__":
    # Path to the folder containing RNA files and in which will be saved correlation coefficients
    folder_path = "/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/SCORES_test"  # Change this to the actual folder path
    
    # Load DataFrames and names
    rna_data, rna_names = load_dataframes_from_folder(folder_path, file_extension=".csv")
    
    # Calculate correlations
    pearson_results, spearman_results = calculate_correlations(rna_data, rna_names)
    
    # Display the results
    print("Pearson Correlations:")
    print(pearson_results)
    print("\nSpearman Correlations:")
    print(spearman_results)

    # Save the correlation dataframe
    
    save_dataframe(pearson_results, folder_path, "pearson_results.csv")
    save_dataframe(spearman_results, folder_path, "spearman_results.csv")
    