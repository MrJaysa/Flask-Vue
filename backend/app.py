from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy         import SQLAlchemy
from flask_marshmallow        import Marshmallow
from os.path import join as link
from requests import get

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./tmp/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

class Images(db.Model):
    __name__     = 'images'

    id           = db.Column(db.Integer,     primary_key=True)
    title        = db.Column(db.String(255), nullable=True)
    url          = db.Column(db.String(255), nullable=True)
    thumbnailUrl = db.Column(db.String(255), nullable=True)

    def create(self, title, url, thumbnailUrl):
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
def before_first_request():
    with app.app_context():
        db.create_all()

    if not Images.query.first():
        req = get('https://jsonplaceholder.typicode.com/photos')
        response = req.json()
        for data in response:
            img = Images()
            img.create(
                thumbnailUrl =data['thumbnailUrl'],
                title = data['title'],
                url = data['url'],
            )
            img.save()

@app.route('/api/get-data')
def present_data():
    schema = Images_schema(many=True)
    data = Images.query.paginate(page=request.args.get('page', 1, type=int), per_page=10, error_out=False)
    
    return jsonify(
        status   = 200,
        data     = schema.dump(data.items),
        has_next = data.has_next,
        page     = data.page,
        total_page = data.total//10
    ), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(link(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# https://vuejs.org/tutorial/#step-7
# https://vuejs.org/examples/#fetching-data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)