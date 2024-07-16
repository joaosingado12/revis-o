from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, salvar, editar, update, excluir, novo

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('novo/', novo, name='novo')
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)