from apis.version1.routes import route_charts
from apis.version1.routes import route_data
from apis.version1.routes import route_help
from apis.version1.routes import route_home
from apis.version1.routes import route_inverters
from apis.version1.routes import route_settings

routes_list = [
    route_home.router,
    route_settings.router,
    route_data.router,
    route_help.router,
    route_charts.router,
    route_inverters.router,
]
