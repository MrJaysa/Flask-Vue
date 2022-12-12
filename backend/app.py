from flask import Flask, send_from_directory, jsonify
from flask_sqalalchemy import Sqlalchemy
from flask_marshmallow        import Marshmallow
from os.path import join as link

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db':'testdb',
    'host':'localhost',
    'port':27017
}

app.config['SERVER_NAME'] = 'jaysa:5000'

db = Sqlalchemy()
db.init_app(app)

ma = Marshmallow
ma.init_app(app)

class Images(db.Model):
    __name__     = 'images'

    id           = db.Column(db.Integer,     primary_key=True)
    title        = db.Column(db.String(255), nullable=True)
    url          = db.Column(db.String(255), nullable=True)
    thumbnailUrl = db.Column(db.String(255), nullable=True)

    def create(self, name, img):
        self.title = title
        self.url   = url
        self.thumbnailUrl = thumbnailUrl
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Images_schema(ma.Schema):
    class Meta:
        Model  = Images
        fields = ("title", "url", "thumbnailUrl")

@app.before_first_request



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(link(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)