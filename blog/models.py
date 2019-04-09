from django.db import models #başka yerlerden bir şeyleri projemize dahil eder import ve from
from django.utils import timezone


class Post(models.Model): #bu satır modelimizi tanımlıyor (bir nesne).class bir nesen tanımlamızı belirten anahtar kelime.Post ise modelimin adı.models.Model = Post'un bir Django Modeli olduğunu belirtir.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #başka bir modele referans tanımlar.
    title = models.CharField(max_length=200) #belirli bir uzunluktaki metinleri tanımlamak için kullanılır.
    text = models.TextField(null=True) #bu da uzun metinleri tanımlar.
    created_date = models.DateField(default = timezone.now,null=True) #models.DateTimeField = bu da gün ve saati tanımlamada kullanılır.
    published_date = models.DateField(blank=True, null=True)


    def publish(self): #publish metodu. def bunun bir fonksiyon/method olduğunu söylüyor. publish ise methodumuzun ismi.
        self.published_date = timezone.now()
        self.save()


    def __str__(self): # döndürme işlemi yapar
        return self.title   