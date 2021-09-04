sumarized by me:
  не успел доделать, потому что залипал в барах, юзался, и просто вел себя непотребно.
  правда успел сделать основной функционал, а вот разбираться как там эту админку верстать было максимально лень.
  зачем она вообще нужна, если я могу запилить свою? очевидно потому что это противоречит философии джанги.
  вообще, знакомство с джангой получилось позитивным. если выбросить все свистелки, то возможно джанга даже
  в какой то мере юзабельна,
  типа прикольно, что есть тема с миграцией, но то что джанга неасинхронная - это конечно полная залупа,
  ни sse не поднять, ни вебсокет без танцев imo
  





> how to развернуть the server

    checkout requirements.txt

    celery uses rabbitmq as broker, u need to install erlang and rabbitmq server
    celery uses redis as backend, u need to install redis server
        u can omit making redis from sources if u use windows: https://stackoverflow.com/a/10525215/10562922

    django initialized according to https://docs.djangoproject.com/en/3.2/intro


    postgresql used as db engine


    do not forget to create db first, use " CREATE DATABASE alytics ; "


    checkout postgresql settings in alytics/alytics/settings.py -> DATABASES
    there is my local username/password you might want to change as well


    > u can make script to automate this u know? like hackers usually do...

        celery -A alytics worker --loglevel=INFO
            -- run celery

        ./redis-server
            -- run redis

        python manage.py runserver
            -- run server





> naming


    app name is "polls" as it is in https://docs.djangoproject.com/en/3.2/intro
    but routed as /


> admin

    user: kotya
    password 1



> random tips

    ./rabbitmqctl.bat list_queues
        -- list queues


    python manage.py makemigrations
        -- compile models


    python manage.py migrate
        -- apply models after compiling

