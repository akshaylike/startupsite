from django.shortcuts import render_to_response
from startups.models import StartupDetails, Comment
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
  context = RequestContext(request)
  startups_list = StartupDetails.objects.all().order_by('-votes')
  context_dict = {'startups_list': startups_list}
  response = render_to_response('startups/index.html', context_dict, context)
  return response

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


def upvote(request):
  context = RequestContext(request)
  startup_id = request.GET['s_id']
  v = StartupDetails.objects.get(pk=int(startup_id))
  if startup_id in request.session:
    flag = int(request.session[startup_id])
    if flag == -1:
      v.votes = v.votes + 2
      v.save()
      request.session[startup_id] = 1
  else:
    v.votes = v.votes + 1
    v.save()
    request.session[startup_id] = 1
  return HttpResponse(v.votes)

def downvote(request):
  context = RequestContext(request)
  startup_id = request.GET['s_id']
  v = StartupDetails.objects.get(pk=int(startup_id))
  if startup_id in request.session:
    flag = int(request.session[startup_id])
    if flag == 1:
      v.votes = v.votes - 2
      v.save()
      request.session[startup_id] = -1
  else:
    v.votes = v.votes - 1
    v.save()
    request.session[startup_id] = -1
  return HttpResponse(v.votes)
