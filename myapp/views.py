from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one':one, 'project':'myapp'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_myapp_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

import tw2.core
import myapp.widgets
@view_config(route_name='movie', renderer='templates/widget.pt')
def view_widget(request):
    widget = myapp.widgets.MovieForm.req()
    widget.fetch_data(request)
    tw2.core.register_controller(widget, 'movie_submit')
    return {'widget': widget}


@view_config(route_name='list', renderer='templates/widget.pt')
def view_list(request):
    widget = myapp.widgets.MovieList.req()
    widget.fetch_data(request)
    return {'widget': widget}


@view_config(route_name='grid', renderer='templates/widget.pt')
def view_grid(request):
    widget = myapp.widgets.GridWidget.req()
    tw2.core.register_controller(widget, 'db_jqgrid')
    return {'widget': widget}
