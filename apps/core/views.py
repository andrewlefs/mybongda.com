from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.views.decorators.gzip import gzip_page


# Create your views here.
class AdminRequiredMixin(View):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *arg, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(request, *arg, **kwargs)


class SuperUserRequiredMixin(View):
    def dispatch(self, request, *arg, **kwargs):
        if not request.user.is_active or not request.user.is_superuser:
            raise PermissionDenied
        return super(SuperUserRequiredMixin, self).dispatch(request, *arg, **kwargs)


class AdminBaseView(View):
    @method_decorator(gzip_page)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminBaseView, self).dispatch(request, *args, **kwargs)


class BaseView(View):
    @method_decorator(gzip_page)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)
