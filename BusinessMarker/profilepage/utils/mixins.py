from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
import os
import re

class Permissions(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        is_login_page = request.path == "/login_menu/"
        is_profile_page = request.path == "/profile/"
        is_ajax_page = request.path == "/profile/ajax/"
        is_user_authenticated = request.user.is_authenticated
        
        if is_user_authenticated:
            if not is_profile_page and not is_ajax_page:
                return HttpResponseRedirect('/profile/')
        if not is_user_authenticated and not is_login_page:
            return HttpResponseRedirect('/login_menu/')
        
        return super(Permissions, self).dispatch(request, *args, **kwargs)

    @property
    def _user_groups(self):

        return [g.lower() for g in self.request.user.groups.values_list('name', flat=True)]

    def get_context_data(self, **kwargs):
        context = super(Permissions, self).get_context_data(**kwargs)
        context['is_free'] = 'free' in self._user_groups
        context['is_basic'] = 'basic' in self._user_groups
        context['is_standart'] = 'standart' in self._user_groups
        context['is_premium'] = 'premium' in self._user_groups
        context['is_admin'] = 'admin' in self._user_groups

        return context

class News(TemplateView):
    def check_for_updates(self):
        try:
            git_log = os.popen("git log --oneline -n 10 --pretty=format:'%cs,%s'").readlines()
            # date, message = git_log[0].split(',')
            log_list = []
            for item in git_log:
                date, message = item.split(',')
                message = re.sub('[^A-Za-z0-9 ]+', '', message)
                date = re.sub('[^0-9-]+', '', date)
                log_list.append({"comment":message, "date":date})
                # Updates.objects.create(comment=message, date=date)

            return log_list

            # if not Updates.objects.filter(date=date).exists() or not Updates.objects.filter(comment=message).exists():
            #     Updates.objects.create(comment=message, date=date)

        except Exception as ex:
            print(ex)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updates = self.check_for_updates()
        # Updates.objects.all().delete()
        context['news'] = updates
        # Updates.objects.all()[:10]

        return context
