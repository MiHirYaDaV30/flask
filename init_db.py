from app import app, db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")