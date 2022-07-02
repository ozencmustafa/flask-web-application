This flask app can be run as a service with gunicorn but also you can run it also as a docker image.

## As a service:
```
ubuntu@ip-172-31-7-154:/etc/nginx/sites-enabled$ systemctl status flaskapp
� flaskapp.service - Gunicorn service
     Loaded: loaded (/etc/systemd/system/flaskapp.service; static; vendor preset: enabled)
     Active: active (running) since Sat 2022-07-02 20:30:26 UTC; 1h 39min ago
   Main PID: 463 (gunicorn3)
      Tasks: 4 (limit: 1145)
     Memory: 62.1M
     CGroup: /system.slice/flaskapp.service
             ├─463 /usr/bin/python3 /usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app
             ├─492 /usr/bin/python3 /usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app
             ├─493 /usr/bin/python3 /usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app
             └─495 /usr/bin/python3 /usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app

Jul 02 20:30:26 ip-172-31-7-154 systemd[1]: Started Gunicorn service.
Jul 02 20:30:27 ip-172-31-7-154 gunicorn3[463]: [2022-07-02 20:30:27 +0000] [463] [INFO] Starting gunicorn 20.0.4
Jul 02 20:30:27 ip-172-31-7-154 gunicorn3[463]: [2022-07-02 20:30:27 +0000] [463] [INFO] Listening at: unix:flaskapp.sock (463)
Jul 02 20:30:27 ip-172-31-7-154 gunicorn3[463]: [2022-07-02 20:30:27 +0000] [463] [INFO] Using worker: sync
Jul 02 20:30:27 ip-172-31-7-154 gunicorn3[492]: [2022-07-02 20:30:27 +0000] [492] [INFO] Booting worker with pid: 492
Jul 02 20:30:27 ip-172-31-7-154 gunicorn3[493]: [2022-07-02 20:30:27 +0000] [493] [INFO] Booting worker with pid: 493
Jul 02 20:30:27 ip-172-31-7-154 gunicorn3[495]: [2022-07-02 20:30:27 +0000] [495] [INFO] Booting worker with pid: 495
ubuntu@ip-172-31-7-154:/etc/nginx/sites-enabled$
```
## Docker Image
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

http:<realIP>:5000




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






