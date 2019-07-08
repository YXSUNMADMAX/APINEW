from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/snippet', views.snippet_list),
    path('snippets/snippet/<int:pk>/', views.snippet_detail),
    path('snippets/author', views.author_list),
    path('snippets/author/<int:pk>/', views.author_detail),
]