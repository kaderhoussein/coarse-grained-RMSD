import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Fonction pour charger les résultats de corrélation depuis un fichier CSV
def load_correlation_data(file_path):
    """
    Load correlation data from a CSV file.
    
    :param file_path: Path to the CSV file containing the correlation data.
    :return: DataFrame containing the correlation data.
    """
    return pd.read_csv(file_path)

# Fonction pour préparer les données pour la heatmap
def prepare_correlation_matrix(correlation_data):
    """
    Prepare the correlation data by setting 'model_id' as the index.
    
    :param correlation_data: DataFrame containing the correlation data.
    :return: Prepared DataFrame ready for heatmap plotting.
    """
    return correlation_data.set_index("model_id")

# Fonction pour créer et afficher la heatmap
def create_heatmap(correlation_matrix, file_name):
    """
    Create and display a heatmap of the correlation matrix.
    
    :param correlation_matrix: DataFrame containing the correlation matrix.
    :param file_name: Name of the file used for the title.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        fmt=".2f", 
        cmap="coolwarm", 
        linewidths=0.5,
        cbar_kws={'label': 'Correlation Coefficient'}
    )
    
    # Ajouter un titre et des labels
    plt.title(f"Correlation for {file_name}", fontsize=16)
    plt.xlabel("Metrics", fontsize=12)
    plt.ylabel("RNA", fontsize=12)
    
    # Afficher le graphique
    plt.tight_layout()
    plt.show()

# Fonction principale pour orchestrer le processus pour plusieurs fichiers
def main():
    folder_path = "/home/zozo/Bureau/Coarse_grain_RMSD/P_C1_O3_matrix/"  # Remplacez par le chemin de votre dossier
    files = ["pearson_results.csv", "spearman_results.csv"]  # Liste des fichiers à traiter
    
    # Traiter chaque fichier dans le dossier
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        correlation_data = load_correlation_data(file_path)
        correlation_matrix = prepare_correlation_matrix(correlation_data)
        create_heatmap(correlation_matrix, file_name)

if __name__ == "__main__":
    main()
