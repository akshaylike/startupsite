from django.shortcuts import render_to_response
from startups.models import StartupDetails, Comment
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect


def vote(request):
    startup_id = request.GET['startup_id']
    startup = StartupDetails.objects.get(id=startup_id)
    vote = int(request.GET['vote'])
    if startup_id in request.session:
        startup.votes -= request.session[startup_id]
        startup.votes += vote
        startup.save()
        request.session[startup_id] = vote
    return HttpResponse(startup.votes)


def index(request):
  context = RequestContext(request)
  startups_list = StartupDetails.objects.all().order_by('-votes')
  for startup in startups_list:
    if startup.id in request.session:
      startup.current_user_vote = request.session[startup.id]
    else:
      request.session[startup.id] = 0
      startup.current_user_vote = request.session[startup.id]

  return render_to_response('startups/index.html', {'startups_list': startups_list}, context)


def add_comment(request):
  context = RequestContext(request)
  startup_id = None
  if request.method == 'POST':
    name = request.POST['name']
    comment = request.POST['comment']
    startup_id = request.POST['startupid']
    if startup_id:
      s = StartupDetails.objects.get(pk=int(startup_id))
      c = Comment(name=name,text=comment,startup=s)
      c.save()
  return HttpResponseRedirect("/startups/")
