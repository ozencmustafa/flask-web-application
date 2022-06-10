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






