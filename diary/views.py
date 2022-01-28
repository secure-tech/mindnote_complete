from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse
from .models import Page
from .forms import PageForm
# Create your views here.

def index(request):
    return render(request,'diary/index.html')

class PostListView(ListView):
    model = Page
    template_name = 'dairy/page_list.html'
    ordering = ['-dt_created']
    paginate_by = 8
    page_kwarg = 'page'

class PageDetailView(DetailView):
    model = Page
    template_name = 'diary/page_detail.html'
    pk_url_kwarg = 'page_id'

def info(request):
    return render(request,'diary/info.html')

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self) -> str:
        return reverse('page-detail', kwargs={'page_id':self.object.id})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self) -> str:
        return reverse('page-detail',kwargs={'page_id':self.object.id})


class PageDeleteView(DeleteView):
    model = Page
    template_name = 'diary/page_confirm_delete.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self) -> str:
        return reverse('page-list')