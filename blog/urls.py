from django.urls import path
from .views import all_blogs_view, detail_view

app_name = "blog"

urlpatterns = [
    path('', all_blogs_view, name = 'all_blogs'),
    path('<int:id>/', detail_view, name = 'detail')
]
