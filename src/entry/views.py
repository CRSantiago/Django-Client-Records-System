from django.shortcuts import render, get_object_or_404,reverse
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import EntryForm
from .models import Entry

# Create your views here.
def create_entry_view(request):
    user = request.user
    form = EntryForm(request.POST or None)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        form = EntryForm()

    context = {
        'form': form
    }
    return render(request, 'entries/new_entry.html', context)

class EntryListView(ListView):
    template_name = 'entries/entry_list.html'
    queryset = Entry.objects.all()

class EntryDetailView(DetailView):
    template_name = 'entries/entry_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Entry, id=id_)

class EntryUpdateView(UpdateView):
    template_name = 'entries/new_entry.html'
    form_class = EntryForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Entry, id=id_)

class EntryDeleteView(DeleteView):
    template_name = 'entries/entry_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Entry, id=id_)

    def get_success_url(self):
        return reverse('entry:entry-list')

