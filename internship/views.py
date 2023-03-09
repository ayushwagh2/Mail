from django.shortcuts import render
from django.http import HttpResponse
from .models import Mails   

def mail_list_view(request):
    mails = Mails.objects.all()
    return render(request, 'mail_list.html', {'mails': mails})

def mail_detail_view(request, pk):
    mail = Mails.objects.get(pk=pk)
    mail.views += 1
    mail.save()
    return render(request, 'mail_detail.html', {'mail': mail})
