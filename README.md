# Projet de Scraping pour WordPress

## Description

Ce projet contient trois scripts conçus pour extraire des données d'articles à partir de sites WordPress. Les scripts fonctionnent uniquement sur des sites utilisant WordPress et génèrent un fichier CSV contenant diverses informations détaillées sur les articles publiés.

### Fichiers inclus
1. **scraping_for_the_rex_child.ipynb**
2. **scraping_for_newsparpes_child.ipynb**
3. **scraping_for_gloria.ipynb**

### Fonctionnalités principales
- Extraction de métadonnées des articles : URL, titre, description, auteur, catégories, et plus.
- Analyse des statistiques des articles : nombre de vues, temps de lecture estimé, etc.
- Génération d'un fichier CSV structuré avec les colonnes suivantes :
  - `article_url`
  - `article_canonical_url`
  - `article_slug`
  - `article_meta_title`
  - `article_meta_desc`
  - `article_date_published`
  - `article_date_modified`
  - `article_author`
  - `article_title`
  - `article_category`
  - `article_views`
  - `article_reading_time`
  - `article_content`
  - `article_raw_content`
  - `article_length`
  - `days_since_published`
  - `article_views_daily`
  - `article_views_monthly`
  - `website`
  - `scraping_date`

---

## Prérequis

- Python 3.x
- Jupyter Notebook
- Bibliothèques Python nécessaires (listées dans chaque fichier `.ipynb`)

---

## Utilisation

### Étape 1 : Identifier le thème WordPress
Avant d'utiliser un des scripts, identifiez le **thème WordPress** utilisé par le site cible. Cette information détermine quel script doit être exécuté.

### Étape 2 : Modifier les variables
Dans le script sélectionné, adaptez les variables suivantes en fonction de votre cible :
```
website = 's-finance'  # Remplacez par le nom du site
abbr = 'sfi'          # Remplacez par l'abréviation du site
tld = '.fr'           # Remplacez par le domaine de premier niveau du site
```

### Étape 3 : Exécuter le script
Lancez le fichier `.ipynb` correspondant dans Jupyter Notebook. Une fois l'exécution terminée, un fichier CSV contenant les données extraites sera généré.

### Étape 4 : Concaténer les fichiers CSV

Une fois tous les fichiers CSV générés, lancez le script `concat.py` pour les concaténer en un seul fichier CSV global. Cela créera un fichier résumant toutes les données extraites dans un format unique et uniforme.

---

## Limitations

- Les scripts fonctionnent uniquement avec des sites utilisant WordPress.
- Le thème WordPress doit être connu pour choisir le bon script.
- Les scripts peuvent nécessiter des ajustements si la structure HTML du site diffère.

---

## Auteur

**Enzo Léon**
