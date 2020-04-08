from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import create_entry_view, EntryListView, EntryDetailView, EntryDeleteView, EntryUpdateView

app_name = 'entry'
urlpatterns = [
    path('create/', create_entry_view, name='create-entry'),
    path('', EntryListView.as_view(), name='entry-list'),
    path('<int:id>/', EntryDetailView.as_view(), name='entry-detail'),
    path('<int:id>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    path('<int:id>/update/', EntryUpdateView.as_view(), name='entry-update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)