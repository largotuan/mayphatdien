# users/urls.py


from django.urls import re_path,path
from .views import index,maycu,maychothue,maymoi,baotri,giohang,postgiohang,updategiohang,sanpham
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path(r"index/", index, name="index"),
    path(r"maycu/", maycu, name="maycu"),
    path(r"maychothue/", maychothue, name="maychothue"),
    path(r"maymoi/", maymoi, name="maymoi"),
    path(r"baotri/", baotri, name="baotri"),
    path(r"giohang/", giohang, name="giohang"),
    path(r"postgiohang/", postgiohang, name="postgiohang"),
    path(r"updategiohang/", updategiohang, name="updategiohang"),
    path(r"sanpham/<str:query>/", sanpham, name="sanpham"),
]