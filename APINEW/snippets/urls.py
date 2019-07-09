from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippet/', views.snippet_list),
    path('snippet/<int:pk>/', views.snippet_detail),
    path('author/', views.author_list),
    path('author/<int:pk>/', views.author_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)