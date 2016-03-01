from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from peewee import *
from sqlite3 import *

app = Flask(__name__)
assets = Environment(app)
db = sqlite('homepage.db')

scripts = Bundle('scripts/vendor/angular.min.js', 'scripts/vendor/angular-route.min.js',
                 'scripts/vendor/angular-animate.min.js',
                 'scripts/vendor/jquery.min.js', 'scripts/vendor/bootstrap.min.js',
                 'scripts/app/app.js', 'scripts/app/directives/directives.js',
                 output='bundles/scripts.js')
styles = Bundle('css/vendor/bootstrap.min.css', 'css/site.css',
                output='bundles/styles.css')
assets.register('_scripts', scripts)
assets.register('_styles', styles)

class Post(Model):
    title = CharField()
    url = CharField(unique=True)
    content = TextField()
    published = BooleanField(index=True)
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
