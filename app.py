from flask import Flask, render_template, jsonify
from flask.ext.assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import *
from datetime import datetime
from flask_restful import Resource, Api
from marshmallow import Schema, fields, pprint

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

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    tags = db.relationship('Tag', secondary=tags, backref="posts")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'pub_date': self.pub_date,
            'tags': [i.name for i in self.tags]
        }

    def __init__(self, title, content, tags, pub_date=None):
        self.title = title
        self.content = content
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.tags = tags

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            # 'posts': [{'id': i.id, 'title': i.title} for i in self.posts]
        }

    def __init__(self, name):
        self.name = name
        
# class PostSchema(Schema):
#     id = fields.Integer()
#     title = fields.String()
#     content = fields.String()
#     pub_date = fields.DateTime()
#     tags = fields.Nested('TagSchema', exclude=('posts', ), many=True)
    
# class TagSchema(Schema):
#     id = fields.Integer()
#     name = fields.String()
#     posts = fields.Nested('PostSchema', exclude=('tags', ), many=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')
    
class Blog(Resource):
    def get(self):
        # return jsonify({'posts': [PostSchema().dump(i).data for i in Post.query.order_by(Post.pub_date.desc()).all()]}) 
        return jsonify({'posts': [i.serialize for i in Post.query.order_by(Post.pub_date.desc()).all()]})        

api.add_resource(Blog, '/posts')

if __name__ == "__main__":
    app.run(debug=True)
