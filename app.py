from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Rohit Yadav\OneDrive\Desktop\flask\todo.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    dates=db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
        print("POST")
    
    alltodo = Todo.query.all()
    #return "<p>Hello, World!</p>"
    return render_template("index.html",alltodo=alltodo)
@app.route("/show")
def products():
    alltodo = Todo.query.all()
    print(alltodo)
    return "<p>this is the production page</p>"
@app.route("/update/<int:sno>")
@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()  # or use get_or_404
    if request.method == "POST":
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect("/")
    return render_template("update.html", todo=todo)
@app.route("/delete/<int:sno>")
def delete(sno):
    alltodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(alltodo)
    db.session.commit()
    print(alltodo)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True,port=8000)