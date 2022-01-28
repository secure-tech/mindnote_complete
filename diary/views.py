from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    CreateView,ListView,DetailView,UpdateView,DeleteView,TemplateView,RedirectView
)
from django.urls import reverse
from .models import Page
from .forms import PageForm
# Create your views here.

class IndexRedirect(RedirectView):
    pattern_name = 'page-list'

class PostListView(ListView):
    model = Page
    # ListView에서는 model명_list.html이 default
    ordering = ['-dt_created']
    paginate_by = 8
    # page_kwarg도 'page'가 default

class PageDetailView(DetailView):
    model = Page
    # DetailView에서는 model명_list.html이 default
    # pk_url_kwarg도 pk가 기본값이기 때문에, urls.py에서 pk로 설정하면 적어주지 않아도 됨.

class InfoTemplateView(TemplateView):
    template_name = 'diary/info.html'

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    #form_class로 form을 부르면 기본값이 model명_form.html임.

    def get_success_url(self) -> str:
        return reverse('page-detail', kwargs={'pk':self.object.id})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    #위 CreateView랑 같은 이유
    # pk_url_kwarg도 pk가 기본값이기 때문에, urls.py에서 pk로 설정하면 적어주지 않아도 됨.

    def get_success_url(self) -> str:
        return reverse('page-detail',kwargs={'pk':self.object.id})


class PageDeleteView(DeleteView):
    model = Page
    # DeleteView에서는 model명_confirm_delete.html이 default
    # pk_url_kwarg도 pk가 기본값이기 때문에, urls.py에서 pk로 설정하면 적어주지 않아도 됨.

    def get_success_url(self) -> str:
        return reverse('page-list')