from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    for activitiy in Activity.objects.filter(pk=3):
        lista = activitiy.as_xml()

    context ={}
    
    #{'lista': lista,}

    return render(request, 'gantt/index.html',context)

def project(request):
    lista = "{\"data\":["
    for activitiy in Activity.objects.all():
        lista += activitiy.as_xml()
    lista += "], \"collections\": {\"links\":[{}]}"
    print lista
    test ="""{ "data":[{"id":"17","start_date":"2013-04-01 00:00:00","duration":"5","text":"Project #1","progress":"0.8","parent":"0","open":1},{"id":"2","start_date":"2013-04-01 00:00:00","duration":"6","text":"New task","progress":"0","parent":"17","open":1}], "collections": {"links":[{"id":"132","source":"17","target":"2","type":"0"}]}}"""
    return HttpResponse(test)


@csrf_exempt
def modify_project(request):
    query_dict = request.POST
    #print query_dict.items()
    if query_dict.__contains__('ids'):
        ids = query_dict.get("ids")
        print ids
        for id in ids.split(","):
            print "************************************" + id
            try:
                activity = Activity.objects.get(id=id)
                print "******************************FOUND ID"
            except ObjectDoesNotExist:
                activity = Activity(id=id)
                print "..............................NOT FOUND ID"
            d={}
            for key, value in query_dict.iteritems():
                if key.startswith(id):
                    #print "key :" + key.replace(id+"_", "") + " value: " + value
                    d[key.replace(id+"_", "")] = value
            d2=dict(
                id = d['id'],
                responsible_user = get_responsible_user_from_id(1),
                short_description = d['text'],
                long_description = d['text'],
                start_date = d['start_date'],
                end_date = d['start_date'],
                parent = get_parent_activity_from_id(d['parent']),
                activity_type = get_activity_type_from_id(2))
            print d2
            for key, value in d2.iteritems():
                print str(key) + " :: " + str(value)
                setattr(activity, key, value)

            if activity.save():
                test={"status":"ok"}
            else:
                test=""
    #{"type":"updated", "sid":15, "tid":15} or {"action":"error", ...}
    return HttpResponse(test)

def get_responsible_user_from_id(responsible_user_id):
    print "                              searching for user : " + str(responsible_user_id)
    responsible_user = get_object_or_404(User, pk=responsible_user_id)
    return responsible_user

def get_parent_activity_from_id(parent_activity_id):
    print "                              searching for activity : " + str(parent_activity_id)
    try:
        parent_activity = Activity.objects.get(pk=parent_activity_id)
    except ObjectDoesNotExist:
        parent_activity = None
    return parent_activity

def get_activity_type_from_id(activity_type_id):
    print "                              searching for activity_type : " + str(activity_type_id)
    activity_type = get_object_or_404(ActivityType, pk=activity_type_id)
    return activity_type
