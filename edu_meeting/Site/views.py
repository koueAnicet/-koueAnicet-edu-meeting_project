from django.shortcuts import render
from Site import models as models_site
from Meeting import models as models_meeting

# Create your views here.
def index(request):
    site = models_site.Siteweb.objects.first()
    service = models_site.Service.objects.all()
    banner = models_site.Banner.objects.first()
    categorie = models_meeting.CategoryMeeting.objects.all()
    meeting = models_meeting.Meetings.objects.all().filter(is_UPCOMING_meeting=True)
    return render(request,'edu-meeting/index.html', locals())

def home(request):

    return render(request, 'edu-meeting/index.html')


def meeting_detail(request):
    return render(request, 'edu-meeting/meeting-details.html' )


def meetings(request):
    return render(request, 'edu-meeting/meetings.html')