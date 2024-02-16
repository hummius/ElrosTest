from django.urls import path
from .views import *

app_name = 'AutoApp'
urlpatterns = [
    path('countries/', CountryListView.as_view()),
    path('countries/<int:pk>/', CountryView.as_view()),
    path('countries/get_data/', export_country),
    path('manufacturer/', ManufacturerListView.as_view()),
    path('manufacturer/<int:pk>/', ManufacturerView.as_view()),
    path('manufacturer/get_data/', export_auto),
    path('automobiles/', AutomobilesListView.as_view()),
    path('automobiles/<int:pk>/', AutomobileView.as_view()),
    path('automobiles/get_data/', export_auto),
    path('commentaries/', CommentListView.as_view()),
    path('commentaries/<int:pk>/', CommentView.as_view()),
    path('commentaries/get_data/', export_auto),
    ]
