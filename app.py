from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

bundles = {
    '_scripts': Bundle(
        'scripts/vendor/angular.min.js',
        'scripts/vendor/bootstrap.min.js',
        'scripts/vendor/angular.route.min.js',
        output = 'bundles/scripts.js'
    ),
    '_styles': Bundle(
        'css/vendor/bootstrap.min.css',
        'css/site.css',
        output = 'bundles/styles.css'
    )
}
assets.register(bundles)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
