from django.shortcuts import render,redirect
from .models import studentdata
# Create your views here.
def studentpage(request):
    student=studentdata.objects.all()
    return render(request,'studentpage.html',{'student':student})
def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        studentdata(
            sname=request.POST.get('sname'),
            sage=request.POST.get('sage'),
            saddr=request.POST.get('saddr'),
            m1=request.POST.get('m1'),
            m2=request.POST.get('m2')
        ).save()
        return redirect(studentpage) 
def update_data(request,id):
    student=studentdata.objects.get(id=id)
    return render(request,'update_data.html',{'student':student}) 
def update_save_data(request,id):
    sr=studentdata.objects.get(id=id)
    sr.sname=request.POST.get('sname')
    sr.sage=request.POST.get('sage')
    sr.saddr=request.POST.get('saddr')
    sr.m1=request.POST.get('m1')
    sr.m2=request.POST.get('m2')
    sr.save()
    return redirect(studentpage)   
def delete_data(request,id):
    sd=studentdata.objects.get(id=id)
    sd.delete()
    return redirect(studentpage)
