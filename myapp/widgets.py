import tw2.core
import tw2.forms


class MovieForm(tw2.forms.FormPage):
    title = 'Movie'
    resources = [tw2.core.CSSLink(link='static/myapp.css')]

    class child(tw2.forms.TableForm):
        id = tw2.forms.HiddenField()
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genres = tw2.forms.CheckBoxList(options=[
            'Action', 'Comedy', 'Romance', 'Sci-fi'])

        class cast(tw2.forms.GridLayout):
            extra_reps = 5
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()
