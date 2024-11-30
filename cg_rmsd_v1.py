import os
import numpy as np
import pandas as pd
from Bio.PDB import PDBParser
from utils import compute_rssd, plot_points

def extract_coarse_grained_coordinates(structure, atom_names):
    """
    Extract the coordinates of the chosen atoms for the coarse-grained representation.
    """
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    if atom.get_id() in atom_names:
                        coords.append(atom.get_coord())
    coords = np.array(coords)
    print(f"Extracted {len(coords)} atoms for coarse-grained representation.")
    return coords

def compute_cg_rmsd(native_pdb, predicted_pdb, atom_names):
    """
    Compute the Coarse-grained RMSD between native and predicted structures.
    """
    # Parse PDB files
    parser = PDBParser(QUIET=True)
    native_structure = parser.get_structure('native', native_pdb)
    predicted_structure = parser.get_structure('predicted', predicted_pdb)

    # Extract coordinates of the chosen atoms
    native_coords = extract_coarse_grained_coordinates(native_structure, atom_names)
    predicted_coords = extract_coarse_grained_coordinates(predicted_structure, atom_names)

    # Ensure the same number of atoms are used for alignment
    min_length = min(len(native_coords), len(predicted_coords))
    native_coords = native_coords[:min_length]
    predicted_coords = predicted_coords[:min_length]

    # Compute CG-RMSD using the utils function
    rotation, rmsd = compute_rssd(native_coords, predicted_coords)

    # Optionally, plot the points to visualize the alignment
    #plot_points(native_coords, predicted_coords, rotation)

    return rmsd/min_length

def process_structures(native_folder, preds_folder, atom_names, output_folder):
    """
    Process all structures and compute CG-RMSD for each model.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of native structures
    native_files = [f for f in os.listdir(native_folder) if f.endswith('.pdb')]

    for native_file in native_files:
        structure_id = native_file.split('.')[0]
        native_pdb = os.path.join(native_folder, native_file)

        # Get list of predicted structures for the current native structure
        pred_folder = os.path.join(preds_folder, structure_id)
        if not os.path.exists(pred_folder):
            continue

        pred_files = [f for f in os.listdir(pred_folder) if f.endswith('.pdb')]

        results = []
        for pred_file in pred_files:
            model_id = pred_file.split('.')[0]
            predicted_pdb = os.path.join(pred_folder, pred_file)

            # Compute CG-RMSD
            cg_rmsd = compute_cg_rmsd(native_pdb, predicted_pdb, atom_names)

            # Store result
            results.append({
                'model_id': model_id,
                'cg_rmsd': cg_rmsd
            })

        # Save results to CSV
        output_csv = os.path.join(output_folder, f'{structure_id}_cg_rmsd_results.csv')
        df = pd.DataFrame(results)
        df.to_csv(output_csv, index=False)
        print(f"CG-RMSD results for {structure_id} saved to {output_csv}")

# Example usage
native_folder = "/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/NATIVE"
preds_folder = '/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/PREDS'
atom_names = ['P', 'C5\'', 'O5\'']
output_folder = 'cg_rmsd_results'

process_structures(native_folder, preds_folder, atom_names, output_folder)
