from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail

class Send(TemplateView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        description = request.POST["name"] + " " + request.POST["email"]+ " "+ request.POST["description"]
        mail_status = send_mail(
                request.POST["subject"],
                description,
                'tech-support@businessmarker.ru',
                ['tech-support@businessmarker.ru'],
                fail_silently=False,
                )
                
        return JsonResponse({'data': mail_status})