from django.shortcuts import render


def index ( request ) :
    context = {

    }
    return render ( request, 'polls/index.html', context )






# from django.http import StreamingHttpResponse
# def sse ( request ) :
#     def event_stream () :
#         while True :
#             print(123)
#             from time import sleep, time
#             sleep ( 3 )
#             yield f'posix { time () }'
#     return StreamingHttpResponse ( event_stream (), content_type='text/event-stream' )
