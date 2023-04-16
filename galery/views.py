from django.views.generic import ListView, DetailView

from .models import Category, Photo

class GalleryView(ListView):
    template_name = 'gallery.html'
    model = Photo
    context_object_name = "photos"

    extra_context = {
        "categories": Category.objects.all(),
    }

    def get_queryset(self):
        category_name = self.request.GET.get("category")

        if category_name:
            photos = Photo.objects.filter(category__title=category_name)
        else:
            photos = Photo.objects.all()

        return photos

class DetailsView(DetailView):
    model = Photo
    template_name = 'detail.html'
    context_object_name = "photo"