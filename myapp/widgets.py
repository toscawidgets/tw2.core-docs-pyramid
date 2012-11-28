import tw2.core
import tw2.forms
import tw2.sqla
import tw2.jqplugins.jqgrid
import myapp.models


class MovieForm(tw2.sqla.DbFormPage):
    title = 'Movie'
    redirect = '/list'
    entity = myapp.models.Movie

    resources = [tw2.core.CSSLink(link='static/myapp.css')]

    class child(tw2.forms.TableForm):
        action = '/tw2_controllers/movie_submit'
        id = tw2.forms.HiddenField()
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genres = tw2.sqla.DbCheckBoxList(entity=myapp.models.Genre)

        class cast(tw2.forms.GridLayout):
            extra_reps = 5
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()


class MovieList(tw2.sqla.DbListPage):
    entity = myapp.models.Movie
    title = 'Movies'
    newlink = tw2.forms.LinkField(link='/movie', text='New', value=1)

    class child(tw2.forms.GridLayout):
        title = tw2.forms.LabelField()
        id = tw2.forms.LinkField(link='/movie?id=$', text='Edit', label=None)

class GridWidget(tw2.jqplugins.jqgrid.SQLAjqGridWidget):
    id = 'grid_widget'
    entity = myapp.models.Movie
    excluded_columns = ['id']
    prmFilter = {'stringResult': True, 'searchOnEnter': False}
    pager_options = { "search" : True, "refresh" : True, "add" : False, }
    options = {
        'caption': 'A grid!',
        'url': '/tw2_controllers/db_jqgrid/',
        'rowNum':15,
        'rowList':[15,30,50],
        'viewrecords':True,
        'imgpath': 'scripts/jqGrid/themes/green/images',
        'width': 900,
        'height': 'auto',
    }
