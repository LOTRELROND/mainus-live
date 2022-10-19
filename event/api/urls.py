from django.urls import path
from event.api import views as api_views

urlpatterns = [
    path('post/',api_views.PostListCreateAPIView.as_view(),name="post-list"),
    path('post/<int:pk>/',api_views.PostDetailAPIView.as_view(), name="post-edit"),
    path('author/',api_views.AuthorListCreateAPIView.as_view(),name="author-list"),
    path('author/<int:pk>/',api_views.AuthorDetailAPIView.as_view(), name="author-edit"),
    path('category/',api_views.CategoryListCreateAPIView.as_view(),name="category-list"),
    path('category/<int:pk>/',api_views.CategoryDetailAPIView().as_view(),name="category-edit"),
    path('reply/',api_views.ReplyListCreateAPIView.as_view(),name="reply-list"),
    path('reply/<int:pk>/',api_views.ReplyDetailAPIView.as_view(),name="reply-edit"),
]
