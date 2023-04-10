
from config.constants import DATA_SOURCES_OUTDIR


appointments_by_centers = f"""
drop table if exists appointments_by_centers;
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
CREATE INDEX appointments_by_centers_index
ON appointments_by_centers (id_centre,date_debut_semaine,departement);

"""
vaccination_centers = f"""
drop table if exists vaccination_centers;
   CREATE TABLE vaccination_centers (
    gid INTEGER,
    nom TEXT,
    arrete_pref_numero TEXT,
    xy_precis TEXT,
    id_adr TEXT,
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
CREATE INDEX vaccination_centers_index
ON vaccination_centers (gid, com_cp,date_fermeture,date_ouverture);
"""
stock = f"""
drop table if exists stock;
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
CREATE INDEX stock_index
ON stock(date,code_departement);
"""
vaccination_vs_appointments = f"""
drop table if exists vaccination_vs_appointments;
    CREATE TABLE vaccination_vs_appointments (
    id_centre TEXT,
    date_debut_semaine DATE,
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
CREATE INDEX vaccination_vs_appointments_index
ON vaccination_vs_appointments(id_centre,code_departement,date_debut_semaine);
"""


geo_etendue = """
drop table if exists geo_etendue;
    CREATE TABLE geo_etendue (
  code_commune_INSEE TEXT,
  nom_commune_postal TEXT,
  code_postal TEXT,
  libelle_acheminement TEXT,
  ligne_5 TEXT,
  latitude FLOAT,
  longitude FLOAT,
  code_commune TEXT,
  article TEXT,
  nom_commune TEXT,
  nom_commune_complet TEXT,
  code_departement TEXT,
  nom_departement TEXT,
  code_region TEXT,
  nom_region TEXT
);

CREATE INDEX geo_etendue_index
ON geo_etendue(code_postal);

"""



all_tables_to_create = [appointments_by_centers, vaccination_centers,
              stock, vaccination_vs_appointments,geo_etendue]
