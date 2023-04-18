from django.shortcuts import render
# Create your views here.
def pc_status(request, pc_id):
    pc = PC.objects.get(id=pc_id)
    context = {'pc': pc}
    return render(request, 'pc_status.html', context)
