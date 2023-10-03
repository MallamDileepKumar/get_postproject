from django.shortcuts import render

# Create your views here.
def getinput(request):
    return render(request,'input.html')
def postinput(request):
    return render(request,'output.html')
def post(request):
    if request.method == 'GET':
        x = int(request.GET['t1'])
        y = int(request.GET['t2'])
        z = x+y
        return render(request,'index.html',{'z':z})
    else:
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        z = x + y
        return render(request, 'index.html', {'z': z})








