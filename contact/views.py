from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import datetime

@csrf_exempt
def sendMail(request):	
	if request.method == 'POST' and request.is_ajax():
	
		message = request.POST['message']
		subject = str(request.POST['subject'])
		

		recipient_list = [settings.EMAIL_HOST_USER,]#get mail id from user
		email_from = settings.EMAIL_HOST_USER
		send_mail(subject, message, email_from, recipient_list )

		context={
			'result':'result',
		}
		return JsonResponse(context)

def successmail(request):
	return render(request, 'sent.html')
