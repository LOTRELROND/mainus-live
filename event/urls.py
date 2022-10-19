from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name = "index"),
    path('detail/<slug>/', views.detail, name='detail'),
    path('addentry/', views.addEntry, name='addentry'),
    path('addauthor/', views.addAuthor, name = 'addauthor' ),
    path('delete/<slug>/', views.deletePost, name = 'deletepost' ),
    path('dashboard', views.dashboard, name = 'dashboard' ),
    path('edit/<slug>/', views.editEntry, name = 'edit' ),
    path('profile/<slug>',views.profile, name = 'profile'),
]