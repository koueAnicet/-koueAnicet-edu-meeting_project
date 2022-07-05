from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'edu-meeting/index.html')


def meeting_detail(request):
    return render(request,' edu-meeting/meeting-details.html' )


def meetings(request):
    return render(request,' edu-meeting/meetings.html')