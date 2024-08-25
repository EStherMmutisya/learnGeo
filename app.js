from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self)
        return f'<Data {self.id}>'

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        data = Data.query.all()
        return jsonify([item.json() for item in data])
    elif request.method == 'POST':
        data = Data(name=request.json['name'])
        db.session.add(data)
        db.session.commit()
        return jsonify(data.json())

@app.route('/api/data/<int:id>', methods=['PUT', 'DELETE'])
def data_update_delete(id):
    data = Data.query.get_or_404(id)
    if request.method == 'PUT':
        data.name = request.json['name']
        db.session.commit()
        return jsonify(data.json())
    elif request.method == 'DELETE':
        db.session.delete(data)
        db.session.commit()
        return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)