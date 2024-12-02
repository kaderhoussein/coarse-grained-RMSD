import os
import numpy as np
import pandas as pd
from merging import merge_files
from correlation_matrix import load_dataframes_from_folder, calculate_correlations, save_dataframe
from cg_rmsd import process_structures, process_single_structure
from heatmaps_plotting import generate_heatmaps

def test_cg_rmsd_single_structure():
    print("\nTesting Coarse-Grained RMSD Computation for Single Structure:")
    native_pdb = "./data/NATIVE/rp03.pdb"  # Replace with the actual folder path for native structures
    predicted_pdb = "./data/PREDS/rp03/3drna_rp03.pdb"  # Replace with the actual folder path for predicted structures
    atom_names = ['P', "C5'", "O5'", "C4'", "C3'", "C2'", "C1'", "O1'", "O3'"] # Replace by either a single atom or any combination among this list
    output_csv = "cg_rmsd.csv"
    process_single_structure(native_pdb, predicted_pdb, atom_names, output_csv)  # For a single structure

def test_cg_rmsd_multiple_structures():
    print("\nTesting Coarse-Grained RMSD Computation for Multiple Structures:")
    native_folder = "./data/NATIVE"  # Replace with the actual folder path for native structures
    preds_folder = "./data/PREDS"  # Replace with the actual folder path for predicted structures
    atom_names = ['P', "C5'", "O5'", "C4'", "C3'", "C2'", "C1'", "O1'", "O3'"]  # Replace by either a single atom or any combination of atoms among this list
    output_folder = "cg_rmsd_output"  # Replace with the actual output folder path
    process_structures(native_folder, preds_folder, atom_names, output_folder)  # For multiple structures

def test_csv_merging():
    print("\nTesting CSV Merging:")
    folder1_path = "./cg_rmsd_output"
    folder2_path = "./data/SCORES"
    output_folder_path = "./data/MERGED"
    merge_files(folder1_path, folder2_path, output_folder_path)

def test_correlation_calculations():
    print("\nTesting Correlation Calculations:")
    folder_path = "./data/MERGED"  # Update the path if needed
    output_path = "./corr_results"
    rna_data, rna_names = load_dataframes_from_folder(folder_path)
    pearson_results, spearman_results = calculate_correlations(rna_data, rna_names, output_path)
    print("Pearson Correlations:\n", pearson_results)
    print("Spearman Correlations:\n", spearman_results)
    save_dataframe(pearson_results, output_path, "pearson_results.csv")
    save_dataframe(spearman_results, output_path, "spearman_results.csv")

def test_heatmap_generation():
    print("\nTesting Heatmap Generation:")
    pearson_corr = "./corr_results/pearson_results.csv"
    spearman_corr = "./corr_results/spearman_results.csv"
    generate_heatmaps(pearson_corr, spearman_corr, "heatmap1.png", "heatmap2.png")

if __name__ == "__main__":
    # Call only the function you want to test
    # For example, to test Coarse-Grained RMSD for a single structure:
    test_cg_rmsd_single_structure()

    # To test Coarse-Grained RMSD for multiple structures:
    #test_cg_rmsd_multiple_structures()

    # To test CSV merging:
    # test_csv_merging()

    # To test correlation calculations:
    # test_correlation_calculations()

    # To test heatmap generation:
    # test_heatmap_generation()
