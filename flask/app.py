from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

print(SQLAlchemy)

app = Flask(__name__) # references 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r>' % self.id
    
# creating an index route 
@app.route('/')
def index():
    # return "Hello world"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)