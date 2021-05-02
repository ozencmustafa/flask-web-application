# Flask sinifi web sunucumuzu ayaga kaldirir.
from flask import Flask,render_template,flash,redirect,url_for,logging,request,session
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

# Kullanici giris decoratoru, session kontrolu saglar. ornegin login olarak acilabilen sayfalar bu decaratorler yardimi ile login degilse acilamaz.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session: # session icerisinde logged_in diye bir anahtar deger var mi, yok mu ?
            return f(*args, **kwargs)  # eger logged-in yapildi ise fonksiyonu normal bir sekilde cagirir.
        else:
            flash("This page can not be displayed unless you are logged-in","danger")   # burada danger bir categorydir.
            return redirect(url_for("login"))
    return decorated_function

# Kullanici Kayit Formu
class RegisterForm(Form):
    name = StringField("Name Surname",validators = [validators.Length(min = 4,max=25)])
    username = StringField("User Name",validators = [validators.Length(min = 4,max=25)])
    email = StringField("Email Adress",validators = [validators.Email(message ="Please type a valid email address")])
    password = PasswordField("Password:",validators=[
        validators.DataRequired(message = "Please type a password"),
        validators.EqualTo(fieldname = "confirm",message="Invalid Password")
    ])
    confirm = PasswordField("Verify your password")

class LoginForm(Form): # WT Form dan inherit ediyoruz.
    username =StringField("User Name")
    password = PasswordField("Password")
####1. once app adinda Flask sinifindan bir obje olusturduk
app = Flask(__name__)       # ozel bir degisken, terminalden calistirilirsa name degeri main oluyor.
app.secret_key = "myblog"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "myblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
####3 Request yapip HTML olarak response donuyoruz
@app.route("/")   #decoreter (request yapiyorus)
def index():
    return render_template("index.html")  # response donuyoruz

@app.route("/about")
def about():
    return render_template("about.html")

# Bu decerator dashbord fonksiyonu calismi kontrol ediyor, biz url/dashbord diye web browserda calistirinca dashbord a erisebiliyoruz ancak sadece login olunca erisilmesini istiyoruz.
# Diger bir degisle kullanici girisi yapilmamis ise bu fonksiyonu calistirmasin.
@app.route("/dashboard")     # bu sayfa sadece login oldugumzda gosterilecek
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():   # ans form.validate == True demek
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        query = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(query,(name,email,username,password))
        mysql.connection.commit()

        cursor.close()
        flash("Succesfuly Registered..","success")

        return redirect(url_for("login"))
    
    else:
        return render_template("register.html", form=form)

@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)   # request.form u LoginFormun icine gonderiyoruz
    if request.method == "POST":
        username = form.username.data # formdan girdigimiz username bilgisini aliyoruz.
        password_entered = form.password.data
        cursor = mysql.connection.cursor()
        query = "select * from users where username = %s"
        result = cursor.execute(query,(username,))
        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,real_password):  # True anlaminda
                flash("Your login is succesfull","success")

                session["logged_in"] = True     # logged in olduktan sonra session baslatiyoruz, session library import edilmisti.
                session["username"] = username  # session degiskenini bir sozluk olarak kullaniyoruz. ve anahtar degerlerini kendimiz belirliyoruz.


                return redirect(url_for("index"))   # index fonksiyonun ilisikli url adresine goder
            else:
                flash("Password is wrong","danger")
                return redirect(url_for("login")) 
        else:
            flash("User does not exist..","danger")
            return redirect(url_for("login"))     # login fonkiyonuna gider ve ilgili urle gider
            
    return render_template("login.html",form=form)

@app.route("/article/<string:id>")
def detail(id):
    return "Article Id:" + id

# Logout islemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

####2 Bilgisayarimda localhostu yani web sunususunu calistirmam gerekiyor
if __name__ == "__main__":  # terminalden mi calismis yoksa baska bir python code tan mi  cagrilmis 
    app.run(debug=True) # hatamisi gormek icin