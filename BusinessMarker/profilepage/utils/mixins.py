from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class Permissions(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login_menu/')

        return super(Permissions, self).dispatch(request, *args, **kwargs)

    @property
    def _user_groups(self):

        return [g.lower() for g in self.request.user.groups.values_list('name', flat=True)]

    def get_context_data(self, **kwargs):
        context = super(Permissions, self).get_context_data(**kwargs)
        context['is_free'] = 'free' in self._user_groups
        context['is_premium'] = 'premium' in self._user_groups
        context['is_admin'] = 'admin' in self._user_groups

        return context