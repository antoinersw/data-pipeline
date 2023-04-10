from scripts.load.create.create_table import create_table


sql_statement = """
drop table if exists dim_center;
CREATE TABLE dim_center AS (
    select distinct gid 
    ,nom as nom_centre 
        from vaccination_centers
);

CREATE INDEX dim_center_index
ON dim_center (gid);

"""

def create_dim_center():
    create_table(sql_statement)