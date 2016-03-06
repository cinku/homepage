from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import *
from datetime import datetime
from flask_restful import Resource, Api, marshal_with, fields
import json

app = Flask(__name__)
assets = Environment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/sqlite/tmp/homepage.db'
db = SQLAlchemy(app)
api = Api(app)

scripts = Bundle('scripts/vendor/angular.min.js', 'scripts/vendor/angular-route.min.js',
                 'scripts/vendor/angular-animate.min.js',
                 'scripts/vendor/jquery.min.js', 'scripts/vendor/bootstrap.min.js',
                 'scripts/app/app.js', 'scripts/app/directives/directives.js',
                 'scripts/app/controllers/blog.js',
                 output='bundles/scripts.js')
styles = Bundle('css/vendor/bootstrap.min.css', 'css/site.css',
                output='bundles/styles.css')
assets.register('_scripts', scripts)
assets.register('_styles', styles)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tag = db.relationship('Tag', backref=db.backref('posts', lazy='dynamic'))
    
    def serialize():
        return {
            'title': fields.String,
            'content': fields.String,
            'pub_date': fields.DateTime(dt_format='iso8601')
        }

    def __init__(self, title, content, tag, pub_date=None):
        self.title = title
        self.content = content
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.tag = tag

    def __repr__(self):
        return '<Post %r>' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')
    
class Blog(Resource):
    @marshal_with(Post.serialize())
    def get(self, **kwargs):
        return Post.query.order_by(Post.pub_date.desc()).all()

api.add_resource(Blog, '/posts')

if __name__ == "__main__":
    app.run()
