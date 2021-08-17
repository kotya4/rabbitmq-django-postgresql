from django.shortcuts import render
from .models import SavedFunction
from alytics.tasks import count_functions
import json
from django.contrib import messages




# def index_parse_post_request ( post ) :
#     post = json.loads ( post.decode ( 'utf-8' ) )
#     if 'newfunc' in post :
#         post = post[ 'newfunc' ]
#         SavedFunction.objects.create ( **post )
#         print ( '>>> SavedFunction created <<<' )
#         result = count_functions.delay ()
#         print ( '>>> celery <<<', result )
#         print ( 'where is result?' )
#         print ( result.get ( timeout=1 ) )
#     elif 'needupdate' in post :
#         pass


# TODO: this must be in admin side lol


def index ( request ) :
    # if request.body : return index_parse_post_request ( request.body )

    post = request.body
    if post :
        post = json.loads ( post.decode ( 'utf-8' ) )
        if 'newfunc' in post :
            post = post[ 'newfunc' ]
            SavedFunction.objects.create ( **post )
            print ( '>>> SavedFunction created <<<' )
            result = count_functions.delay ()
            print ( '>>> celery <<<', result )
            print ( 'where is result?' )
            r = result.get ( timeout=1 )
            print ( r )
            messages.success ( request, 'Form submission successful' )
        else :
            messages.success ( request, 'fuck you' )


    context = {

    }
    return render ( request, 'polls/index.html', context )

