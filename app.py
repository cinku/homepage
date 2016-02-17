from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

scripts = Bundle('scripts/vendor/angular.min.js', 'scripts/vendor/angular-route.min.js',
                 'scripts/vendor/jquery.min.js', 'scripts/vendor/bootstrap.min.js',
                 'scripts/app/app.js', 'scripts/app/directives/directives.js',
                 output='bundles/scripts.js')
styles = Bundle('css/vendor/bootstrap.min.css', 'css/site.css',
                output='bundles/styles.css')
assets.register('_scripts', scripts)
assets.register('_styles', styles)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
