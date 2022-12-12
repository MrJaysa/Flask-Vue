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

@app.route('/images', methods=['POST'])
def imagess():
    form = ImgForm(form=request.form, files=request.files)
    if form.validate_on_submit():
        return 'saved'

    return f'not saved, {form.errors}'

    # image = request.files['file']
    # dbfile = Images()
    # dbfile.poster.put(image, filename=image.filename, content_type=image.content_type)
    # dbfile.save()

    return 'save'

@app.route('/img/<id>/', methods=['GET'])
def get_image(id):
    img = Images.objects.get_or_404(id=id)
    image = img.poster.read()
    content_type = img.poster.content_type
    filename = img.poster.filename

    return send_file(
        BytesIO(image), 
        download_name=filename, 
        mimetype=content_type
    ), 200


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(link(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)