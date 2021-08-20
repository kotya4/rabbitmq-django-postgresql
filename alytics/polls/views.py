from django.shortcuts import render
from  django.http import HttpResponse
from .models import SavedFunction
from alytics.tasks import plot_func
import json



celery_results = []


def updatefuncs () :
    for f in SavedFunction.objects.all () :
        print ( f )
    r = { 'updatefuncs' : [ f.dictify () for f in SavedFunction.objects.all () ] }
    return HttpResponse ( json.dumps ( r ), content_type='application/json; charset=utf-8' )


def index ( request ) :
    global celery_results

    post = request.body
    if post :
        post = json.loads ( post.decode ( 'utf-8' ) )


        if 'newfunc' in post :
            post = post[ 'newfunc' ]
            o = SavedFunction.objects.create ( **post )
            # print ( o )
            # TIP: celery task arguments and return value must be serializable, default serializer tho is json parser
            celery_results += [ plot_func.delay ( o.id ) ]
            return updatefuncs ()


        if 'updatefuncs' in post :
            return updatefuncs ()



        return HttpResponse ( 'unknown post request' )


    context = {

    }
    return render ( request, 'polls/index.html', context )

