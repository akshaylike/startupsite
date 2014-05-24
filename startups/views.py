from django.shortcuts import render_to_response
from startups.models import StartupDetails
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.sessions.models import Session;

previously_voted = 0
def index(request):
  context = RequestContext(request)
  startups_list = StartupDetails.objects.all().order_by('-votes')
  context_dict = {'startups_list': startups_list}
  response = render_to_response('startups/index.html', context_dict, context)
  return response

def upvote(request):
  context = RequestContext(request)
  startup_id = None
  if request.method == 'GET':
    startup_id = request.GET['s_id']
  votes = 0
  if startup_id:
    startup = StartupDetails.objects.get(id=int(startup_id))
    if startup:
        votes = startup.votes + 1
        startup.votes = votes
        startup.save()
  return HttpResponse(votes)

def downvote(request):
  context = RequestContext(request)
  previously_voted = 0
  startup_id = None
  if request.method == 'GET':
    startup_id = request.GET['s_id']
  votes = 0
  if startup_id:
    startup = StartupDetails.objects.get(id=int(startup_id))
    if startup:
      votes = max(0, startup.votes - 1)
      startup.votes = votes
      startup.save()
  return HttpResponse(votes)
