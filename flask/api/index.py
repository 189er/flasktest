from flask import Flask
from flask import request, render_template_string, render_template


app = Flask(__name__)

@app.route('/')
def home():
    template = '''
    {%% block body %%}
            <h3>%s</h3>
    {%% endblock %%}
    ''' % ( request.form.get('username') )
    return render_template_string(template)

@app.route('/about')
def about():
    return 'About'