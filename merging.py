import os
import pandas as pd


def merge_files(folder1_path, folder2_path, output_folder_path):
    # Define the paths to the folders containing the CSV files
    folder1_path = "./cg_rmsd_output"
    folder2_path = "./data/SCORES"
    output_folder_path = "./data/MERGED"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    # Function to read a CSV file into a DataFrame
    def read_csv_file(file_path):
        return pd.read_csv(file_path, index_col=None, header=0)

    # Get the list of CSV files in both folders
    files1 = [f for f in os.listdir(folder1_path) if f.endswith('.csv')]
    files2 = [f for f in os.listdir(folder2_path) if f.endswith('.csv')]

    # Find common filenames
    common_files = set(files1).intersection(files2)

    # Merge the DataFrames on the first column and save each merged file
    for filename in common_files:
        df1 = read_csv_file(os.path.join(folder1_path, filename))
        df2 = read_csv_file(os.path.join(folder2_path, filename))
        merged_df = pd.merge(df1, df2, on=df1.columns[0], how='inner')
        output_filename = os.path.join(output_folder_path, filename)
        merged_df.to_csv(output_filename, index=False)
        print(f"Merged CSV file '{filename}' has been saved to '{output_folder_path}'")

    print("Merging process completed.")
