import os
import pandas as pd

def concat_csv_from_folders(base_directory, output_file):
    """
    Concatène tous les fichiers CSV dans un répertoire principal (y compris les sous-dossiers)
    en un seul fichier CSV, en gérant un séparateur personnalisé.

    Parameters:
        base_directory (str): Le chemin du répertoire principal.
        output_file (str): Le chemin du fichier de sortie.

    Returns:
        None
    """
    # Colonnes attendues
    expected_columns = ['article_url', 'article_canonical_url', 'article_slug', 'article_meta_title', 
                        'article_meta_desc', 'article_date_published', 'article_date_modified', 
                        'article_author', 'article_title', 'article_category', 'article_views', 
                        'article_reading_time', 'article_content', 'article_raw_content', 
                        'article_length', 'days_since_published', 'article_views_daily', 
                        'article_views_monthly', 'website', 'scraping_date']
    
    # Liste pour stocker les DataFrames
    all_dataframes = []

    # Parcours des dossiers et fichiers
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"Lecture du fichier : {file_path}")
                try:
                    # Lecture du fichier CSV avec le séparateur '|' et suppression des colonnes inutiles
                    df = pd.read_csv(file_path, sep='|', index_col=None)
                    
                    # Supprimer la colonne 'Unnamed: 0' si elle existe
                    if 'Unnamed: 0' in df.columns:
                        df = df.drop(columns=['Unnamed: 0'])
                    
                    # Filtrer pour ne garder que les colonnes attendues
                    df = df[[col for col in df.columns if col in expected_columns]]
                    
                    # Ajouter les colonnes manquantes avec des valeurs par défaut
                    for col in expected_columns:
                        if col not in df.columns:
                            df[col] = None
                    
                    # Réorganiser les colonnes dans l'ordre attendu
                    df = df[expected_columns]
                    
                    all_dataframes.append(df)
                except Exception as e:
                    print(f"Erreur lors de la lecture du fichier {file_path} : {e}")

    # Concaténation de tous les DataFrames
    if all_dataframes:
        concatenated_df = pd.concat(all_dataframes, ignore_index=True)
        
        # Enregistrement du fichier résultant
        concatenated_df.to_csv(output_file, index=False, sep='|')
        print(f"Fichiers concaténés avec succès dans : {output_file}")
    else:
        print("Aucun fichier CSV valide trouvé dans le répertoire spécifié.")

# Exemple d'utilisation
if __name__ == "__main__":
    base_directory = r"C:\Users\enzol\Desktop\Ecole\Cas_DSG.media"  # Remplacez par votre chemin
    output_file = r"C:\Users\enzol\Desktop\Ecole\Cas_DSG.media\concat_scrapping.csv"  # Remplacez par votre chemin
    concat_csv_from_folders(base_directory, output_file)
