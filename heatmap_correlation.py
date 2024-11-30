import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les résultats de corrélation depuis un fichier CSV
file_path = "/home/zozo/Bureau/Coarse_grain_RMSD/P_C1_O3_SCORES_merged_nan/pearson_results.csv"  # Remplacez par le chemin vers votre fichier
correlation_data = pd.read_csv(file_path)

# Réorganiser les données pour une heatmap
# On exclut la colonne "RNA" pour travailler sur les valeurs de corrélation
correlation_matrix = correlation_data.set_index("model_id")

# Créer une heatmap
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
plt.title("Correlation Between CG_RMSD and Other Metrics", fontsize=16)
plt.xlabel("Metrics", fontsize=12)
plt.ylabel("RNA", fontsize=12)

# Afficher le graphique
plt.tight_layout()
plt.show()
