from django.shortcuts import render

# Create your views here.
def experience(request):
    context= {'exp':'active'}
    return render(request, 'exper/experience.html',context)

  

