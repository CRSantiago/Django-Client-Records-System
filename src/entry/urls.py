from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

from .views import create_entry_view, EntryListView, EntryDetailView, EntryDeleteView, EntryUpdateView

app_name = 'entry'
urlpatterns = [
    path('create/', login_required(create_entry_view), name='create-entry'),
    path('', login_required(EntryListView.as_view()), name='entry-list'),
    path('<int:id>/', login_required(EntryDetailView.as_view()), name='entry-detail'),
    path('<int:id>/delete/', login_required(EntryDeleteView.as_view()), name='entry-delete'),
    path('<int:id>/update/', login_required(EntryUpdateView.as_view()), name='entry-update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)