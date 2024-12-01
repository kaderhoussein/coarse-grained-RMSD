import os
import numpy as np
import pandas as pd
from merging import merge_csv_files
from heatmap import generate_heatmap
from correlation_matrix import load_dataframes_from_folder, calculate_correlations
from cg_rmsd import process_structures

# Main testing script
if __name__ == "__main__":
    # Test Coarse-Grained RMSD Computation
    print("\nTesting Coarse-Grained RMSD Computation:")
    native_folder = "path_to_native_folder"  # Replace with the actual folder path for native structures
    preds_folder = "path_to_predictions_folder"  # Replace with the actual folder path for predicted structures
    atom_names = ['P', "C5'", "O5'", "C4'", "C3'", "C2'", "C1'", "O1'", "O3'"]  # Define atom names for CG representation
    output_folder = "path_to_cg_rmsd_output_folder"  # Replace with the actual output folder path
    process_structures(native_folder, preds_folder, atom_names, output_folder)

    # Test CSV merging
    print("\nTesting CSV Merging:")
    folder1_path = "path_to_folder1"  # Replace with the actual folder path
    folder2_path = "path_to_folder2"  # Replace with the actual folder path
    output_folder_path = "output_folder"  # Replace with the actual output folder path
    merge_csv_files(folder1_path, folder2_path, output_folder_path)

    # Test heatmap generation
    print("\nTesting Heatmap Generation:")
    heatmap_file_path = "path_to_heatmap_csv"  # Replace with the actual CSV file path
    generate_heatmap(heatmap_file_path)

    # Test correlation calculations
    print("\nTesting Correlation Calculations:")
    folder_path = "path_to_correlation_data_folder"  # Replace with the actual folder path
    rna_data, rna_names = load_dataframes_from_folder(folder_path)
    pearson_results, spearman_results = calculate_correlations(rna_data, rna_names)
    print("Pearson Correlations:\n", pearson_results)
    print("Spearman Correlations:\n", spearman_results)
