from create_table import create_table

sql_statement ="""
SELECT
  to_char(calendar_day, 'DD/MM/YYYY') AS jour,
  to_char(calendar_day, 'MM') AS mois,
  to_char(calendar_day, 'YYYY') AS annee,
  to_char(calendar_day, 'Day', 'NLS_DATE_LANGUAGE=''French''') AS jour_de_la_semaine,
  to_char(calendar_day, 'WW') AS numero_de_semaine,
  CASE 
    WHEN to_char(calendar_day, 'D') IN (1,7) THEN 0
    ELSE 1
  END AS est_jour_ouvre,
  to_char(calendar_day, 'D')::integer AS numero_jour_semaine
FROM (
  SELECT generate_series(
           date('2018-01-01'),
           date('2025-12-31'),
           '1 day'::interval
         ) AS calendar_day
) AS calendar
ORDER BY calendar_day;

"""

def create_dim_date():
    create_table(sql_statement)
