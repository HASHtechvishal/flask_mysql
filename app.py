from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:8889/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(120), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'Item {self.name}'



@app.route('/')
def index():  # put application's code here
    fname = 'abc'
    fprice = 5000
    fcode = 'bdbdbdbdbdbdbdbdbd'
    fdesc = 'efefef ver ve vev ev e'
    entry = Item(name=fname, price=fprice, barcode=fcode, desc=fdesc)
    db.session.add(entry)
    db.session.commit()

    if 'yes == true':
        print('yes')
    return 'success'


if __name__ == '__main__':
    app.run(debug=True, port=8889)

