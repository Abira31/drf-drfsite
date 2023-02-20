from django.urls import path
from women import views
urlpatterns = [
    path('womens/',views.WomenAPIView.as_view()),
]