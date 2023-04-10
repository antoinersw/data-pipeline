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
            ,bt.is_with_doctolib,bt.com_cp
            from base_table as bt
                 left join appointments_by_centers as abc on Cast(bt.gid as varchar(120))= abc.id_centre
                    group by abc.id_centre,abc.nom_centre,bt.gid,bt.nom,bt.is_with_doctolib,abc.nb,bt.com_cp
                        order by abc.nb desc
    )   
    -- , aggreg_count_vax as ( 
    --     select abc.id_centre as gid
    --         ,abc.nom_centre, sum(nb) as nb_of_appointments
    --         ,bt.is_with_doctolib,bt.com_cp
    --         from appointments_by_centers as abc
    --             left join base_table as bt on Cast(bt.gid as varchar(120))= abc.id_centre
    --                 group by abc.id_centre,abc.nom_centre,bt.is_with_doctolib,abc.nb,com_cp
    --                     order by abc.nb desc
    -- )
    select *
    from aggreg_count_vax_bis as vax 
);

drop table if exists aggreg_count_vax;
 create table aggreg_count_vax  (
    gid TEXT,
    nom_centre TEXT,
    nb_of_appointments INTEGER,
    is_with_doctolib INTEGER
    ,cp_commune TEXT

);
-- SELECT * from temp_aggreg_count_vax;

truncate table aggreg_count_vax;
INSERT INTO aggreg_count_vax(
    gid, nom_centre,nb_of_appointments,is_with_doctolib,cp_commune
)
select *
from temp_aggreg_count_vax;

 