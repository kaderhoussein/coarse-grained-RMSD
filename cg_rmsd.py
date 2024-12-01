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

    return rmsd / min_length

def process_single_structure(native_pdb, predicted_pdb, atom_names, output_csv):
    """
    Process a single native and predicted PDB file and compute CG-RMSD.
    """
    # Compute CG-RMSD
    cg_rmsd = compute_cg_rmsd(native_pdb, predicted_pdb, atom_names)

    # Prepare result
    result = [{
        'Native_PDB': os.path.basename(native_pdb),
        'Predicted_PDB': os.path.basename(predicted_pdb),
        'CG_RMSD': cg_rmsd
    }]

    # Save results to CSV
    df = pd.DataFrame(result)
    df.to_csv(output_csv, index=False)
    print(f"CG-RMSD result saved to {output_csv}")

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
            norm = "normalized_"
            pdb_name = ".pdb"

            results.append({
                '': norm + model_id + pdb_name,
                'CG_RMSD': cg_rmsd
            })

        # Save results to CSV
        output_csv = os.path.join(output_folder, f'{structure_id}.csv')
        df = pd.DataFrame(results)
        df.to_csv(output_csv, index=False)
        print(f"CG-RMSD results for {structure_id} saved to {output_csv}")

<<<<<<< HEAD:cg_rmsd.py
# Example usage for single structure
native_pdb = "/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/NATIVE/rp03.pdb"
predicted_pdb = "/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/PREDS/rp03/3drna_rp03.pdb"
atom_names = ['P', 'C5\'', 'O5\'', 'C4\'', 'C3\'', 'C2\'', 'C1\'', 'O1\'', 'O3\'']
output_csv = 'cg_rmsd_single_result.csv'

process_single_structure(native_pdb, predicted_pdb, atom_names, output_csv)

# Example usage for folders
native_folder = "/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/NATIVE"
preds_folder = "/home/kader/Documents/M2/Bioinformatics of RNA and non-coding world/project/Clement/coarse-grained-RMSD/data/PREDS"
=======
# Example usage
native_folder = "/home/jey/Bureau/m2/BIOinf_ARN/clement_B_project/coarse-grained-RMSD/data/NATIVE"
preds_folder = '/home/jey/Bureau/m2/BIOinf_ARN/clement_B_project/coarse-grained-RMSD/data/PREDS'
atom_names = ['P', 'C5\'', 'O5\'', 'C4\'','C3\'', 'C2\'', 'C1\'', 'O1\'', 'O3\'' ]
>>>>>>> 75e40fd0f933c36dbf91d99366188a2b6bea5f4e:cg_rmsd_v1.py
output_folder = 'cg_rmsd_results'

process_structures(native_folder, preds_folder, atom_names, output_folder)
