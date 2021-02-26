from django.urls import path, include
from .views import *

urlpatterns = [
    path('brand/', BrandView.as_view()),
    path('create_brand', CreateBrand.as_view()),
    path('crete_auto_lost/', AutoLostCreate.as_view()),
    path('view_auto_lost/', AutoLostView.as_view()),
    path('view_model', ModelView.as_view()),
]