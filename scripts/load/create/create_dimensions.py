from scripts.load.create.create_dim_date import create_dim_date
from scripts.load.create.create_dim_center import create_dim_center
from scripts.load.create.create_dim_geo import create_dim_geo
###############################################################

def create_dimensions():
    create_dim_date()
    create_dim_center()
    create_dim_geo()