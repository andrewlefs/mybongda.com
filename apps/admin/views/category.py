from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
)
from apps.core.views import AdminRequiredMixin, SuperUserRequiredMixin, AdminBaseView
from apps.categories.models import Category


# Categories Management

class ListCategoryView(AdminBaseView, AdminRequiredMixin, ListView):
    """docstring for CategoryView"""
    model = Category
    template_name = 'admin/categories/list.html'

    def get_queryset(self):
        return Category.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Category List',
            'sidebar': ['category']
        }
        context['info'] = info
        return context


class CreateCategoryView(AdminBaseView, AdminRequiredMixin, CreateView):
    """docstring for CategoryCreateView"""
    model = Category
    fields = '__all__'
    template_name = 'admin/categories/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Create Category',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')


class UpdateCategoryView(AdminBaseView, AdminRequiredMixin, UpdateView):
    """docstring for CategoryUpdateView"""
    model = Category
    fields = '__all__'
    template_name = 'admin/categories/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Update Category',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')


class DeleteCategoryView(AdminBaseView, SuperUserRequiredMixin, DeleteView):
    """docstring for CategoryDeleteView"""
    model = Category

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_category')
