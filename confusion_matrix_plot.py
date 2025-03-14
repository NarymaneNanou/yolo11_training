import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Exemple de données de prédictions et de vraies étiquettes (vous devez les remplacer par vos données)
y_true = [0, 1, 2, 2, 0, 1, 1, 0, 2, 1]  # Vraies étiquettes
y_pred = [0, 1, 2, 2, 0, 1, 0, 0, 2, 1]  # Prédictions du modèle

# Calcul de la matrice de confusion
cm = confusion_matrix(y_true, y_pred)

# Normalisation de la matrice de confusion
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

# Affichage de la matrice de confusion avec seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', xticklabels=True, yticklabels=True)

# Ajout des labels et du titre
plt.title('Matrice de confusion normalisée')
plt.xlabel('Prédictions')
plt.ylabel('Vraies étiquettes')

# Sauvegarde dans un fichier PNG
plt.savefig('train/confusion_matrix_normalized.png')

# Affichage de la matrice
plt.show()
