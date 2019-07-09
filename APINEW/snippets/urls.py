from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippet/', views.SnippetList.as_view()),
    path('snippet/<int:pk>/', views.SnippetDetail.as_view()),
    path('author/', views.AuthorList.as_view()),
    path('author/<int:pk>/', views.AuthorDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)