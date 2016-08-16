from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django import forms
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.posts.models import Post
from apps.categories.models import Category


class ListPostView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/posts/list.html'
    model = Post
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        return Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Post',
                'sidebar': ['post']
            }
        }
        context.update(info)
        return context


class PostForm(forms.ModelForm):
    """docstring for PostForm"""
    category = forms.ModelChoiceField(queryset=Category.objects.filter(type=1).order_by('-id'),
                                      widget=forms.Select(attrs={'class': 'form-control select2',
                                                                 'style': 'width: 100%;'}))

    class Meta:
        model = Post
        fields = ('name', 'slug', 'description',
                  'image', 'content', 'category')


class CreatePostView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/posts/create.html'
    model = Post
    initial = {
        'category': '1',
    }
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Post',
                'sidebar': ['post']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_post')


class UpdatePostView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/posts/update.html'
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Post',
                'sidebar': ['post']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_post')


class DeletePostView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Post

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_post')
