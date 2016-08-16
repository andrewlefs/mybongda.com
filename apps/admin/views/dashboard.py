from django.contrib.admin.forms import (AdminAuthenticationForm, PasswordChangeForm)
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    FormView, TemplateView
)
from django.http import (HttpResponseRedirect)
from django.core.urlresolvers import (reverse_lazy)
from apps.core.views import (AdminRequiredMixin, AdminBaseView, SuperUserRequiredMixin)


# Create your views here.

class LoginView(FormView):
    template_name = 'admin/login.html'
    form_class = AdminAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Login',
            }
        }
        context.update(info)
        return context

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)


class DashboardView(AdminBaseView, AdminRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'

    @method_decorator(cache_page(15 * 60))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Dashboard',
                'sidebar': ['dashboard']
            }
        }
        context.update(info)
        return context


class ChangePasswordView(AdminBaseView, SuperUserRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'admin/profile.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'title': 'Change Password',
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')
