from django.urls import path
from django.conf.urls import url, re_path
from . import views

# urlpatterns = [
#     path('image_codes/(?P<image_code_id>[\w-]+)', views.ImageCodeView.as_view())
# ]

urlpatterns = [
    re_path(r'^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view())
]