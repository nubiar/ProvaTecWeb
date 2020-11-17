from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:henrique123@localhost/agenda'
db = SQLAlchemy(app)

class agenda(db.Model):
    __tablename__ = 'contato'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class placar(db.Model):
    __tablename__ = 'resultado'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nometime1 = db.Column(db.String(50))
    placartime1 = db.Column(db.String(5))
    nometime2 = db.Column(db.String(50))
    placartime2 = db.Column(db.String(5))
    def __init__(self, nometime1, placartime1,nometime2,placartime2):
        self.nometime1 = nometime1
        self.placartime1 = placartime1
        self.nometime2 = nometime2
        self.placartime2 = placartime2


class time(db.Model):
    __tablename__ = 'times'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nometime = db.Column(db.String(50))
    historia = db.Column(db.String(50000))
    tecnico = db.Column(db.String(50))
    armador = db.Column(db.String(50))
    ala = db.Column(db.String(50))
    pivo = db.Column(db.String(50))
    def __init__(self,nometime,historia,tecnico,armador,ala,pivo):
        self.nometime = nometime
        self.historia = historia
        self.tecnico = tecnico
        self.armador = armador
        self.ala = ala
        self.pivo = pivo
    
class loginvip(db.Model):
    __tablename__ = 'loginvips'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(50))
    senha = db.Column(db.String(20))
    def __init__(self,email,senha):
        self.email = email
        self.senha = senha

db.create_all()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrosms")
def cadastrosms():
    return render_template("cadastrosms.html")

@app.route("/cadastrartime")
def cadastrartime():
    return render_template("cadastrartime.html")

@app.route("/cadastroplacar")
def cadastroplacar():
    return render_template("cadastroplacar.html")

@app.route("/cadastrovip")
def cadastrovip():
    return render_template("cadastrovip.html")

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/equipes")
def equipes():
    return render_template("equipes.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        telefone = (request.form.get("telefone"))
        if nome:
            f = agenda(nome,telefone)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/cadastrartimes",methods=['GET', 'POST'])
def cadastrotimes():
    if request.method =="POST":
        nometime = (request.form.get("nometime"))
        historia = (request.form.get("historia"))
        tecnico = (request.form.get("tecnico"))
        armador = (request.form.get("armador"))
        ala = (request.form.get("ala"))
        pivo = (request.form.get("pivo"))
        if nometime:
            f = time(nometime,historia,tecnico,armador,ala,pivo)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/cadastroplacar",methods=['GET', 'POST'])
def cadastrarplacar():
    if request.method =="POST":
        nometime1 = (request.form.get("nometime1"))
        placartime1 = (request.form.get("placartime1"))
        nometime2 = (request.form.get("nometime2"))
        placartime2 = (request.form.get("placartime2"))
        if nometime1:
            f = placar(nometime1, placartime1,nometime2,placartime2)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/cadastrovip",methods=['GET', 'POST'])
def cadastrarvip():
    if request.method =="POST":
        email = (request.form.get("email"))
        senha = (request.form.get("senha"))
        if email:
            f = loginvip(email, senha)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

if __name__ == "__main__":
    app.run(debug=True)

