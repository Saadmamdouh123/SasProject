import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#1
df = pd.read_csv("C:/Users/Saad/Desktop/sas/DataSet.csv")
# print(df.head())

#2
# print("Dimensions du dataset :", df.shape)

#3
print("\nColonnes disponibles dans le dataset :")
# print(df.columns.tolist())

#4
colonnes_utiles = ['SEQN', 'SMQ020', 'RIAGENDR', 'RIDAGEYR', 'DMDEDUC2', 'BMXWT', 'BMXHT', 'BMXBMI']
df_subset = df[colonnes_utiles]
# print(df_subset)

#5 
# print(df_subset.info())

#6
df_subset.columns = ['seqn', 'smoking', 'gender', 'age', 'education', 'weight', 'height', 'bmi']
# print(df_subset)

#7
nombre_doublons = df_subset.duplicated().sum()
# print("Nombre de doublons dans le dataset :", nombre_doublons)

#8
Sup_doublons = df_subset.drop_duplicates()
# print(Sup_doublons)

#9
delete_seqn = df_subset.drop(columns=['seqn'])
# print(delete_seqn.columns.to_list())

#10
find_Nan = df_subset.columns[df_subset.isna().any()].to_list()
# print(find_Nan)

#11

educ_mean = df_subset.fillna(df_subset['education'].mean())
# print(educ_mean)

#12

educ_med = df_subset.copy()
educ_med[['education', 'height', 'bmi']] = educ_med[['education', 'height', 'bmi']].fillna(educ_med[['education', 'height', 'bmi']].median())
# print(educ_med)

#13


# Boucle sur chaque colonne pour détecter les outliers
# Liste des colonnes numériques à analyser
# Copier le DataFrame pour ne pas modifier l'original
df_clean = df_subset.copy()
print(f"Nombre de lignes avant suppression des outliers : {df_clean.shape[0]}")

# Colonnes numériques sur lesquelles appliquer la détection
numeric_cols_for_outliers = ['age', 'weight', 'height', 'bmi']

# Créer un ensemble pour stocker les index des lignes à supprimer
indices_to_drop = set()

# Boucle pour identifier les index des outliers pour chaque colonne
for col in numeric_cols_for_outliers:
    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identifier les index des outliers pour la colonne actuelle
    outlier_indices = df_clean[(df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)].index
    
    # Ajouter ces index à notre ensemble (set) pour éviter les doublons
    indices_to_drop.update(outlier_indices)
    
    print(f"👉 {col} : {len(outlier_indices)} valeurs aberrantes détectées.")

# Supprimer toutes les lignes identifiées en une seule fois
df_clean = df_clean.drop(index=list(indices_to_drop))

print("\n" + "="*50)
print(f"Nombre total de lignes uniques contenant des outliers : {len(indices_to_drop)}")
print(f"Nombre de lignes après suppression des outliers : {df_clean.shape[0]}")
print("="*50 + "\n")

# Afficher un aperçu du DataFrame nettoyé
print("Aperçu du jeu de données nettoyé :")
print(df_clean.head())

#16

df_clean = df_clean.dropna()

# Visualiser les relations entre variables
sns.pairplot(df_clean)
plt.show()







