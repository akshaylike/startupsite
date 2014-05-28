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

def upvote(request):
  context = RequestContext(request)
  startup_id = request.GET['s_id']
  vflag = 'Uvoted' + str(startup_id)
  if vflag in request.session:
    v = StartupDetails.objects.get(id=int(startup_id))
    if vflag[:1] == 'D':
      v.votes += 1
      v.save()
      return HttpResponse(v.votes)
    else:
      return HttpResponse(v.votes)
  else:
    if request.method == 'GET':
      votes = 0
      if startup_id:
        startup = StartupDetails.objects.get(id=int(startup_id))
        if startup:
          votes = startup.votes + 1
          startup.votes = votes
          startup.save()
          request.session[vflag] = True
          return HttpResponse(votes)


def downvote(request):
  context = RequestContext(request)
  startup_id = request.GET['s_id']
  vflag = 'Dvoted' + str(startup_id)
  if vflag in request.session:
    v = StartupDetails.objects.get(id=int(startup_id))
    print vflag
    if vflag[:1] == 'U':
      v.votes -= 1
      v.save()
      return HttpResponse(v.votes)
    else:
      return HttpResponse(v.votes)
  else:
    if request.method == 'GET':
      votes = 0
      if startup_id:
        startup = StartupDetails.objects.get(id=int(startup_id))
        if startup:
          votes = max(0, startup.votes - 1)
          startup.votes = votes
          startup.save()
          request.session[vflag] = True
          return HttpResponse(votes)


def add_comment(request):
  context = RequestContext(request)
  startup_id = None
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    comment = request.POST['comment']
    startup_id = request.POST['startupid']
    if startup_id:
      s = StartupDetails.objects.get(pk=int(startup_id))
      c = Comment(name=name,email=email,text=comment,startup=s)
      c.save(commit=True)
  return HttpResponse(c)
