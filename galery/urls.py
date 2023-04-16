from django.urls import path

from .views import GalleryView, DetailsView

urlpatterns = [
    path('', GalleryView.as_view()),
    path('<str:slug>/', DetailsView.as_view())
]
