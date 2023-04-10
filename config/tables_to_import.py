
from config.constants import DATA_SOURCES_OUTDIR


appointments_by_centers = f"""
        COPY appointments_by_centers(code_region, region, departement, id_centre, nom_centre, rang_vaccinal, date_debut_semaine, nb, nb_rdv_cnam, nb_rdv_rappel) 
            FROM '{DATA_SOURCES_OUTDIR}/appointments_by_centers.csv' 
                DELIMITER ',' 
                CSV HEADER;
"""
vaccination_centers = f"""
   COPY vaccination_centers(gid,nom,arrete_pref_numero,xy_precis,id_adr,adr_num,adr_voie,com_cp,com_insee,com_nom,lat_coor1,long_coor1,structure_siren,structure_type,structure_rais,structure_num,structure_voie,structure_cp,structure_insee,structure_com,_userid_creation,_userid_modification,_edit_datemaj,lieu_accessibilite,rdv_lundi,rdv_mardi,rdv_mercredi,rdv_jeudi,rdv_vendredi,rdv_samedi,rdv_dimanche,rdv,date_fermeture,date_ouverture,rdv_site_web,rdv_tel,rdv_tel2,rdv_modalites,rdv_consultation_prevaccination,centre_svi_repondeur,centre_fermeture,reserve_professionels_sante,centre_type)
    FROM '{DATA_SOURCES_OUTDIR}/vaccination_centers.csv'
        DELIMITER ','
        CSV HEADER ;
"""
stock = f"""
    COPY stock(code_departement, departement, raison_sociale, libelle_pui, finess, type_de_vaccin, nb_ucd, nb_doses, date)
        FROM '{DATA_SOURCES_OUTDIR}/stock.csv'
            DELIMITER ','
            CSV HEADER;
"""
vaccination_vs_appointments = f"""
    COPY vaccination_vs_appointments(id_centre, date_debut_semaine, code_region, nom_region, code_departement, nom_departement, commune_insee, nom_centre, nombre_ucd, doses_allouees, rdv_pris) 
        FROM '{DATA_SOURCES_OUTDIR}/vaccination_vs_appointments.csv' 
            DELIMITER ',' 
            CSV HEADER;
"""
geo_etendue = f"""
COPY geo_etendue(code_commune_INSEE, nom_commune_postal, code_postal, libelle_acheminement, ligne_5, latitude, longitude, code_commune, article, nom_commune, nom_commune_complet, code_departement, nom_departement, code_region, nom_region)
FROM '{DATA_SOURCES_OUTDIR}/geo_etendue.csv'
DELIMITER ','
CSV HEADER;

"""

all_tables = [appointments_by_centers, vaccination_centers,
              stock, vaccination_vs_appointments, geo_etendue]
