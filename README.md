### Platform

Website run on EC2 instance. \
Ubuntu 22.04 TLS \
Type: t2.micro \
Web url: http://3.123.16.242/  \
GitHub: https://github.com/ozencmustafa/flask-web-application.git 

At the moment gunicorn runs in the background but wil be run as a service

```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install flask
sudo apt-get install nginx
sudo apt-get install gunicorn3

git clone https://github.com/ozencmustafa/flask-web-application.git 
```

### Configure nginx
```
cd /etc/nginx/sites_enabled
sudo vi flaskapp 
sudo systemctl daemon-reload
sudo service nginx restart
```

### Run gunicorn3
```
cd ~/flask_web_apllication
gunicorn3 app:app --daemon
```

Image is also dockerized.
### Docker Image
You can pull the image as:
```
docker pull ozenc499/my_devops_site:latest
```

### How to dockerize
To dockerize and automatize your deployment you have to create a Dockerfile.
Assume these commands are needed to deploy your application on an ubuntu server.

You can create your docker file as below.
```
#~/devops_site$# cat Dockerfile
FROM ubuntu

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y pip pip
RUN pip install flask

RUN git clone https://github.com/ozencmustafa/flask-web-application.git
RUN cp -r flask-web-application /opt/

ENTRYPOINT FLASK_APP=/opt/flask-web-application/app.py flask run --host=0.0.0.0
```

Then we run  build command to create the docker image.
```
sudo docker build .
```

As it is already builted, I run the command again with -t tag to give a name.  It will not rebuilt it as it is cached.
```
sudo docker build . -t my_devops_site
```

You can check your images
```
# sudo docker images
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
my_devops_site   latest    943ef50c0c55   18 minutes ago   498MB
<none>           <none>    11c1d42b19a3   20 minutes ago   465MB
ubuntu           latest    27941809078c   3 weeks ago      77.8MB
```

You can run the image as below so that you can access it with the real IP of the Docker host.
```
sudo docker run -p 5000:5000 my_devops_site
```

### Notes to myself
#### Render html template
---
Bu projede html sayfasini render ettik. Render edilecek html sayfasi template directory \
altinda durur. render_template library kullandik ve homepage icin fonksiyon html \
sayfasini return etti. 

---
#### Static file
Static file orneginde, css file kullandik. html sayfasini render ettigimiz zaman css file ne olacak ?\
Cevap basit: static dosyalar static directory altinda duracaklar.

index.html page icerisinde css file link verildi ve styles.css file icerisinde style eklendi.

#### Use https://html5up.net/
You can use ready-to use templates from html5up.net and you can move index.html and
images and all other static files according to our static and template
directories and modify paths of the static files in the index.html.


```

Sonuc: html file kullanildi ve css ile style edildi. 

Chrome web sayfalarinin cache' ini tutar. Biz ise surekli degisilik yaptigimiz icin yaptigimiz 
degisikligin hemen uygulandigini nasil check ederiz?
Cevap: cevap aslinda ilginc, hard reset denen bir sey ve refresh circle basarken 
shifte basili tutarak yapiliyor. 


```
---
### Herhangi bir template nasil editlenir
```
chrome developer tool'tan( sag click inspect) console tabina gelip "document.body.contentEditable=true"
javascript codu calistirarak index.html sayfasini editable yapariz ve kendi istegimize gore editleriz.
Sonra istemedigin yerleri secip backspace ile sileblirsin. Ben section seklinde silmeyi dogru buluyorum.
Sonra degisiklikleri kaydetemeyecegimiz icin web sayfasini ctrl save ile save as yapip, ondex.html ile yer degistirmek.





```






