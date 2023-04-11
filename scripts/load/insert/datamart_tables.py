aggregated_count_vax = """
DROP TABLE IF EXISTS temp_aggreg_count_vax;

create temporary table temp_aggreg_count_vax as (
    with base_table as (
        select vc.gid, vc.nom,vc.com_cp
            ,case
                when vc.rdv_site_web ~ 'doctolib' then 1
                else 0
            END as is_with_doctolib
        from vaccination_centers as vc
    ),
    aggreg_count_vax_bis as (
        select bt.gid, bt.nom as nom_centre, sum(abc.nb) as nb_of_appointments
            ,bt.is_with_doctolib,bt.com_cp as cp_commune
            from base_table as bt
                 left join appointments_by_centers as abc on Cast(bt.gid as varchar(120))= abc.id_centre
                    group by abc.id_centre,abc.nom_centre,bt.gid,bt.nom,bt.is_with_doctolib,abc.nb,bt.com_cp 
                        order by abc.nb desc
    )   
    select *
    from aggreg_count_vax_bis as vax 
);


 insert into aggreg_count_vax  (
    gid ,
    nom_centre ,
    nb_of_appointments ,
    is_with_doctolib 
    ,cp_commune 

)
select gid, nom_centre,nb_of_appointments,is_with_doctolib, cp_commune
from temp_aggreg_count_vax;

"""

overload_appointment_monitoring = """
drop table if EXISTS temp_overload_appointment_monitoring;

create temporary table if not exists temp_overload_appointment_monitoring as (
    with 
        grouped_table as ( 
                select da.mois,da.annee,da.week_num
                ,bt.id_centre,bt.departement
                , sum(bt.nb) as nb_rdv_pris,bt."date_debut_semaine"
            from appointments_by_centers as bt 
            left join dim_date as da on date(da.Jour) = date(bt.date_debut_semaine)
                group by da.mois,da.annee,da.week_num,bt.id_centre,bt.departement,bt.date_debut_semaine
            
)
 ,   vax_vs_appointments as (
        select vva."date_debut_semaine", vva.id_centre
            ,vva.code_departement, sum(CAST(vva.doses_allouees as INTEGER)) as doses_allouees, sum(CAST(vva.rdv_pris as INTEGER)) as rdv_planifies
           ,da.mois,da.annee,da.week_num
            from vaccination_vs_appointments as vva
            left join dim_date as da on date(da.Jour) = date(vva.date_debut_semaine)
            group by vva."date_debut_semaine", vva.id_centre, vva.code_departement, 
                       da.annee,da.mois,da.annee,da.week_num,vva.rdv_pris, vva.doses_allouees 

    )
    ,final_table as (
        select gt.mois, gt.annee, gt.week_num, gt.id_centre, gt.departement, gt.nb_rdv_pris,
       vax.doses_allouees, vax.rdv_planifies, concat(gt.mois,' ',gt.annee) as mois_anee,concat(gt.week_num, ' ',gt.annee) as semaine_annee 
        from grouped_table as gt
            left join vax_vs_appointments as vax  
            on date(vax."date_debut_semaine") = date(gt."date_debut_semaine")
            and vax.id_centre = gt.id_centre
            and vax.code_departement = gt.departement
    )

    select * from final_table
);

insert into overload_appointment_monitoring (
    mois, annee, week_num, id_centre, departement, nb_rdv_pris, doses_allouees, rdv_planifies, mois_anee, semaine_annee
)
SELECT * 
    from temp_overload_appointment_monitoring as s 
        order by s.rdv_planifies desc


"""


datamart_tables = [aggregated_count_vax,overload_appointment_monitoring]