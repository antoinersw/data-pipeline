from create_table import create_table


sql_statement = """
    select distinct gid,nom 
        from vaccination_centers
"""

def create_dim_center():
    create_table(sql_statement)