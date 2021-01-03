from django.urls import path 
from . import views
# importing views from views..py 
from .views import home_view
  
urlpatterns = [ 
    path('blog/weight', home_view, name="blog-weight")
] 