
from config.constants import DATA_SOURCES_OUTDIR


appointments_by_centers = f"""
        CREATE TABLE appointments_by_centers (
    code_region TEXT,
    region TEXT,
    departement TEXT,
    id_centre TEXT,
    nom_centre TEXT,
    rang_vaccinal INTEGER,
    date_debut_semaine DATE,
    nb INTEGER,
    nb_rdv_cnam INTEGER,
    nb_rdv_rappel INTEGER
);


"""
vaccination_centers = f"""
   CREATE TABLE vaccination_centers (
    gid INTEGER,
    nom TEXT,
    arrete_pref_numero TEXT,
    xy_precis TEXT,
    id_adr INTEGER,
    adr_num TEXT,
    adr_voie TEXT,
    com_cp TEXT,
    com_insee TEXT,
    com_nom TEXT,
    lat_coor1 NUMERIC,
    long_coor1 NUMERIC,
    structure_siren TEXT,
    structure_type TEXT,
    structure_rais TEXT,
    structure_num TEXT,
    structure_voie TEXT,
    structure_cp TEXT,
    structure_insee TEXT,
    structure_com TEXT,
    _userid_creation TEXT,
    _userid_modification TEXT,
    _edit_datemaj TIMESTAMP,
    lieu_accessibilite TEXT,
    rdv_lundi TEXT,
    rdv_mardi TEXT,
    rdv_mercredi TEXT,
    rdv_jeudi TEXT,
    rdv_vendredi TEXT,
    rdv_samedi TEXT,
    rdv_dimanche TEXT,
    rdv TEXT,
    date_fermeture DATE,
    date_ouverture DATE,
    rdv_site_web TEXT,
    rdv_tel TEXT,
    rdv_tel2 TEXT,
    rdv_modalites TEXT,
    rdv_consultation_prevaccination TEXT,
    centre_svi_repondeur TEXT,
    centre_fermeture TEXT,
    reserve_professionels_sante BOOLEAN,
    centre_type TEXT
);

"""
stock = f"""
    CREATE TABLE stock (
    code_departement TEXT,
    departement TEXT,
    raison_sociale TEXT,
    libelle_pui TEXT,
    finess TEXT,
    type_de_vaccin TEXT,
    nb_ucd INTEGER,
    nb_doses INTEGER,
    date DATE
);

"""
vaccination_vs_appointments = f"""
    CREATE TABLE vaccination_vs_appointments (
    id_centre TEXT,
    date_debut_semaine TEXT,
    code_region TEXT,
    nom_region TEXT,
    code_departement TEXT,
    nom_departement TEXT,
    commune_insee TEXT,
    nom_centre TEXT,
    nombre_ucd TEXT,
    doses_allouees TEXT,
    rdv_pris TEXT
);

"""

all_tables_to_create = [appointments_by_centers, vaccination_centers,
              stock, vaccination_vs_appointments]
