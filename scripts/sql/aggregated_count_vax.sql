DROP TABLE IF EXISTS temp_aggreg_count_vax;

create temporary table temp_aggreg_count_vax as (
    with base_table as (
        select vc.gid, vc.nom,
            case
                when vc.rdv_site_web ~ 'doctolib' then 1
                else 0
            END as is_with_doctolib
        from vaccination_centers as vc
    )
    , aggreg_count_vax as ( 
        select abc.id_centre as gid
            ,abc.nom_centre, sum(nb) as nb_of_appointments
            ,bt.is_with_doctolib
            from appointments_by_centers as abc
                left join base_table as bt on Cast(bt.gid as varchar(120))= abc.id_centre
                    group by abc.id_centre,abc.nom_centre,bt.is_with_doctolib,abc.nb
                        order by abc.nb desc
    )
    select *
    from aggreg_count_vax
);

--  create table aggreg_count_vax  (
--     gid TEXT,
--     nom_centre TEXT,
--     nb_of_appointments INTEGER,
--     is_with_doctolib INTEGER

-- );

 
INSERT INTO aggreg_count_vax(
    gid, nom_centre,nb_of_appointments,is_with_doctolib
)
select *
from temp_aggreg_count_vax;

select * from aggreg_count_vax