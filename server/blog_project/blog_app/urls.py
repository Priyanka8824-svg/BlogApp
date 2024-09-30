from django.urls import path
from .views import *

urlpatterns = [
    path('blog/create/', BlogCreateAPI.as_view() ),
    path('blog/list/', BlogListAPI.as_view() ),
    path('blog/update/<pk>/', BlogUpdateAPI.as_view() ),
    path('blog/delete/<pk>/', BlogDeleteAPI.as_view() ),
    path('blog/retrieve/<pk>/', BlogRetrieveAPI.as_view() )
]