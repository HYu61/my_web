from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.all_projects, name='projects_index'),
    path('<cate_name>/', views.get_project_by_cate, name='projects_by_cate'),
    path('detail/<int:project_id>/', views.project_detail, name='project_detail'),

]