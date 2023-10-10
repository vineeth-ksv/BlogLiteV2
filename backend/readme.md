# Local Setup
- Clone the project
- Run `setup.sh`

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development

# Folder Structure

- `db_directory` has the sqlite DB. It can be anywhere on the machine. Adjust the path in ``application/config.py`. Repo ships with one required for testing.
- `application` is where our application code is
- `.gitignore` - ignore file
- `setup.sh` set up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `static` - default `static` files folder. It serves at '/static' path. More about it is [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/static/).
- `static/bootstrap` We have already added the bootstrap files so it can be used
- `static/style.css` Custom CSS. You can edit it. Its empty currently
- `templates` - Default flask templates folder


```
backend
¦   .gitignore
¦   BlogLite_V2 Documentation.pdf
¦   Bloglite_V2.yaml
¦   celerybeat-schedule
¦   dump.rdb
¦   local_beat.sh
¦   local_run.sh
¦   local_setup.sh
¦   local_workers.sh
¦   main.py
¦   readme.md
¦   requirements.txt
¦   
+---.env
¦   ¦   pyvenv.cfg
¦   ¦   
¦   +---Include
¦   ¦   +---site
¦   ¦       +---python3.8
¦   ¦           +---greenlet
¦   ¦                   greenlet.h
¦   ¦                   
¦   +---Lib
¦   ¦   +---site-packages
¦   ¦       ¦   brotli.py
¦   ¦       ¦   distutils-precedence.pth
¦   ¦       ¦   flask_bcrypt.py
¦   ¦       ¦   flask_principal.py
¦   ¦       ¦   pkgutil_resolve_name.py
¦   ¦       ¦   pvectorc.cp38-win_amd64.pyd
¦   ¦       ¦   six.py
¦   ¦       ¦   _brotli.cp38-win_amd64.pyd
¦   ¦       ¦   _cffi_backend.cp38-win_amd64.pyd
¦   ¦       ¦   _pyrsistent_version.py
¦   ¦       ¦   
¦   ¦       +---amqp
¦   ¦       ¦   ¦   abstract_channel.py
¦   ¦       ¦   ¦   basic_message.py
¦   ¦       ¦   ¦   channel.py
¦   ¦       ¦   ¦   connection.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   method_framing.py
¦   ¦       ¦   ¦   platform.py
¦   ¦       ¦   ¦   protocol.py
¦   ¦       ¦   ¦   sasl.py
¦   ¦       ¦   ¦   serialization.py
¦   ¦       ¦   ¦   spec.py
¦   ¦       ¦   ¦   transport.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           abstract_channel.cpython-38.pyc
¦   ¦       ¦           basic_message.cpython-38.pyc
¦   ¦       ¦           channel.cpython-38.pyc
¦   ¦       ¦           connection.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           method_framing.cpython-38.pyc
¦   ¦       ¦           platform.cpython-38.pyc
¦   ¦       ¦           protocol.cpython-38.pyc
¦   ¦       ¦           sasl.cpython-38.pyc
¦   ¦       ¦           serialization.cpython-38.pyc
¦   ¦       ¦           spec.cpython-38.pyc
¦   ¦       ¦           transport.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---amqp-5.1.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---aniso8601
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   date.py
¦   ¦       ¦   ¦   decimalfraction.py
¦   ¦       ¦   ¦   duration.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   interval.py
¦   ¦       ¦   ¦   resolution.py
¦   ¦       ¦   ¦   time.py
¦   ¦       ¦   ¦   timezone.py
¦   ¦       ¦   ¦   utcoffset.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---builders
¦   ¦       ¦   ¦   ¦   python.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_init.py
¦   ¦       ¦   ¦   ¦   ¦   test_python.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_init.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_python.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           python.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   test_compat.py
¦   ¦       ¦   ¦   ¦   test_date.py
¦   ¦       ¦   ¦   ¦   test_decimalfraction.py
¦   ¦       ¦   ¦   ¦   test_duration.py
¦   ¦       ¦   ¦   ¦   test_init.py
¦   ¦       ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   test_time.py
¦   ¦       ¦   ¦   ¦   test_timezone.py
¦   ¦       ¦   ¦   ¦   test_utcoffset.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦           test_compat.cpython-38.pyc
¦   ¦       ¦   ¦           test_date.cpython-38.pyc
¦   ¦       ¦   ¦           test_decimalfraction.cpython-38.pyc
¦   ¦       ¦   ¦           test_duration.cpython-38.pyc
¦   ¦       ¦   ¦           test_init.cpython-38.pyc
¦   ¦       ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦           test_time.cpython-38.pyc
¦   ¦       ¦   ¦           test_timezone.cpython-38.pyc
¦   ¦       ¦   ¦           test_utcoffset.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           date.cpython-38.pyc
¦   ¦       ¦           decimalfraction.cpython-38.pyc
¦   ¦       ¦           duration.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           interval.cpython-38.pyc
¦   ¦       ¦           resolution.cpython-38.pyc
¦   ¦       ¦           time.cpython-38.pyc
¦   ¦       ¦           timezone.cpython-38.pyc
¦   ¦       ¦           utcoffset.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---aniso8601-9.0.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---async_timeout
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---async_timeout-4.0.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---attr
¦   ¦       ¦   ¦   converters.py
¦   ¦       ¦   ¦   converters.pyi
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   exceptions.pyi
¦   ¦       ¦   ¦   filters.py
¦   ¦       ¦   ¦   filters.pyi
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   setters.py
¦   ¦       ¦   ¦   setters.pyi
¦   ¦       ¦   ¦   validators.py
¦   ¦       ¦   ¦   validators.pyi
¦   ¦       ¦   ¦   _cmp.py
¦   ¦       ¦   ¦   _cmp.pyi
¦   ¦       ¦   ¦   _compat.py
¦   ¦       ¦   ¦   _config.py
¦   ¦       ¦   ¦   _funcs.py
¦   ¦       ¦   ¦   _make.py
¦   ¦       ¦   ¦   _next_gen.py
¦   ¦       ¦   ¦   _typing_compat.pyi
¦   ¦       ¦   ¦   _version_info.py
¦   ¦       ¦   ¦   _version_info.pyi
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           converters.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           filters.cpython-38.pyc
¦   ¦       ¦           setters.cpython-38.pyc
¦   ¦       ¦           validators.cpython-38.pyc
¦   ¦       ¦           _cmp.cpython-38.pyc
¦   ¦       ¦           _compat.cpython-38.pyc
¦   ¦       ¦           _config.cpython-38.pyc
¦   ¦       ¦           _funcs.cpython-38.pyc
¦   ¦       ¦           _make.cpython-38.pyc
¦   ¦       ¦           _next_gen.cpython-38.pyc
¦   ¦       ¦           _version_info.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---attrs
¦   ¦       ¦   ¦   converters.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   filters.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   setters.py
¦   ¦       ¦   ¦   validators.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           converters.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           filters.cpython-38.pyc
¦   ¦       ¦           setters.cpython-38.pyc
¦   ¦       ¦           validators.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---attrs-23.1.0.dist-info
¦   ¦       ¦   ¦   INSTALLER
¦   ¦       ¦   ¦   METADATA
¦   ¦       ¦   ¦   RECORD
¦   ¦       ¦   ¦   WHEEL
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---licenses
¦   ¦       ¦           LICENSE
¦   ¦       ¦           
¦   ¦       +---bcrypt
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   _bcrypt.pyd
¦   ¦       ¦   ¦   _bcrypt.pyi
¦   ¦       ¦   ¦   __about__.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __about__.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---bcrypt-4.0.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---billiard
¦   ¦       ¦   ¦   common.py
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   connection.py
¦   ¦       ¦   ¦   context.py
¦   ¦       ¦   ¦   einfo.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   five.py
¦   ¦       ¦   ¦   forkserver.py
¦   ¦       ¦   ¦   heap.py
¦   ¦       ¦   ¦   managers.py
¦   ¦       ¦   ¦   pool.py
¦   ¦       ¦   ¦   popen_fork.py
¦   ¦       ¦   ¦   popen_forkserver.py
¦   ¦       ¦   ¦   popen_spawn_posix.py
¦   ¦       ¦   ¦   popen_spawn_win32.py
¦   ¦       ¦   ¦   process.py
¦   ¦       ¦   ¦   queues.py
¦   ¦       ¦   ¦   reduction.py
¦   ¦       ¦   ¦   resource_sharer.py
¦   ¦       ¦   ¦   semaphore_tracker.py
¦   ¦       ¦   ¦   sharedctypes.py
¦   ¦       ¦   ¦   spawn.py
¦   ¦       ¦   ¦   synchronize.py
¦   ¦       ¦   ¦   util.py
¦   ¦       ¦   ¦   _ext.py
¦   ¦       ¦   ¦   _win.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---dummy
¦   ¦       ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           common.cpython-38.pyc
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           connection.cpython-38.pyc
¦   ¦       ¦           context.cpython-38.pyc
¦   ¦       ¦           einfo.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           five.cpython-38.pyc
¦   ¦       ¦           forkserver.cpython-38.pyc
¦   ¦       ¦           heap.cpython-38.pyc
¦   ¦       ¦           managers.cpython-38.pyc
¦   ¦       ¦           pool.cpython-38.pyc
¦   ¦       ¦           popen_fork.cpython-38.pyc
¦   ¦       ¦           popen_forkserver.cpython-38.pyc
¦   ¦       ¦           popen_spawn_posix.cpython-38.pyc
¦   ¦       ¦           popen_spawn_win32.cpython-38.pyc
¦   ¦       ¦           process.cpython-38.pyc
¦   ¦       ¦           queues.cpython-38.pyc
¦   ¦       ¦           reduction.cpython-38.pyc
¦   ¦       ¦           resource_sharer.cpython-38.pyc
¦   ¦       ¦           semaphore_tracker.cpython-38.pyc
¦   ¦       ¦           sharedctypes.cpython-38.pyc
¦   ¦       ¦           spawn.cpython-38.pyc
¦   ¦       ¦           synchronize.cpython-38.pyc
¦   ¦       ¦           util.cpython-38.pyc
¦   ¦       ¦           _ext.cpython-38.pyc
¦   ¦       ¦           _win.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---billiard-3.6.4.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---blinker
¦   ¦       ¦   ¦   base.py
¦   ¦       ¦   ¦   _saferef.py
¦   ¦       ¦   ¦   _utilities.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           base.cpython-38.pyc
¦   ¦       ¦           _saferef.cpython-38.pyc
¦   ¦       ¦           _utilities.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---blinker-1.5.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---Brotli-1.0.9.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---cachelib
¦   ¦       ¦   ¦   base.py
¦   ¦       ¦   ¦   file.py
¦   ¦       ¦   ¦   memcached.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   redis.py
¦   ¦       ¦   ¦   serializers.py
¦   ¦       ¦   ¦   simple.py
¦   ¦       ¦   ¦   uwsgi.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           base.cpython-38.pyc
¦   ¦       ¦           file.cpython-38.pyc
¦   ¦       ¦           memcached.cpython-38.pyc
¦   ¦       ¦           redis.cpython-38.pyc
¦   ¦       ¦           serializers.cpython-38.pyc
¦   ¦       ¦           simple.cpython-38.pyc
¦   ¦       ¦           uwsgi.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---cachelib-0.9.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---cachetools
¦   ¦       ¦   ¦   func.py
¦   ¦       ¦   ¦   keys.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           func.cpython-38.pyc
¦   ¦       ¦           keys.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---cachetools-5.3.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---celery
¦   ¦       ¦   ¦   beat.py
¦   ¦       ¦   ¦   bootsteps.py
¦   ¦       ¦   ¦   canvas.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   local.py
¦   ¦       ¦   ¦   platforms.py
¦   ¦       ¦   ¦   result.py
¦   ¦       ¦   ¦   schedules.py
¦   ¦       ¦   ¦   signals.py
¦   ¦       ¦   ¦   states.py
¦   ¦       ¦   ¦   _state.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---app
¦   ¦       ¦   ¦   ¦   amqp.py
¦   ¦       ¦   ¦   ¦   annotations.py
¦   ¦       ¦   ¦   ¦   autoretry.py
¦   ¦       ¦   ¦   ¦   backends.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   builtins.py
¦   ¦       ¦   ¦   ¦   control.py
¦   ¦       ¦   ¦   ¦   defaults.py
¦   ¦       ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   log.py
¦   ¦       ¦   ¦   ¦   registry.py
¦   ¦       ¦   ¦   ¦   routes.py
¦   ¦       ¦   ¦   ¦   task.py
¦   ¦       ¦   ¦   ¦   trace.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           amqp.cpython-38.pyc
¦   ¦       ¦   ¦           annotations.cpython-38.pyc
¦   ¦       ¦   ¦           autoretry.cpython-38.pyc
¦   ¦       ¦   ¦           backends.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           builtins.cpython-38.pyc
¦   ¦       ¦   ¦           control.cpython-38.pyc
¦   ¦       ¦   ¦           defaults.cpython-38.pyc
¦   ¦       ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦           log.cpython-38.pyc
¦   ¦       ¦   ¦           registry.cpython-38.pyc
¦   ¦       ¦   ¦           routes.cpython-38.pyc
¦   ¦       ¦   ¦           task.cpython-38.pyc
¦   ¦       ¦   ¦           trace.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---apps
¦   ¦       ¦   ¦   ¦   beat.py
¦   ¦       ¦   ¦   ¦   multi.py
¦   ¦       ¦   ¦   ¦   worker.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           beat.cpython-38.pyc
¦   ¦       ¦   ¦           multi.cpython-38.pyc
¦   ¦       ¦   ¦           worker.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---backends
¦   ¦       ¦   ¦   ¦   arangodb.py
¦   ¦       ¦   ¦   ¦   asynchronous.py
¦   ¦       ¦   ¦   ¦   azureblockblob.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   cache.py
¦   ¦       ¦   ¦   ¦   cassandra.py
¦   ¦       ¦   ¦   ¦   consul.py
¦   ¦       ¦   ¦   ¦   cosmosdbsql.py
¦   ¦       ¦   ¦   ¦   couchbase.py
¦   ¦       ¦   ¦   ¦   couchdb.py
¦   ¦       ¦   ¦   ¦   dynamodb.py
¦   ¦       ¦   ¦   ¦   elasticsearch.py
¦   ¦       ¦   ¦   ¦   filesystem.py
¦   ¦       ¦   ¦   ¦   mongodb.py
¦   ¦       ¦   ¦   ¦   redis.py
¦   ¦       ¦   ¦   ¦   rpc.py
¦   ¦       ¦   ¦   ¦   s3.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---database
¦   ¦       ¦   ¦   ¦   ¦   models.py
¦   ¦       ¦   ¦   ¦   ¦   session.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           models.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           session.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           arangodb.cpython-38.pyc
¦   ¦       ¦   ¦           asynchronous.cpython-38.pyc
¦   ¦       ¦   ¦           azureblockblob.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           cache.cpython-38.pyc
¦   ¦       ¦   ¦           cassandra.cpython-38.pyc
¦   ¦       ¦   ¦           consul.cpython-38.pyc
¦   ¦       ¦   ¦           cosmosdbsql.cpython-38.pyc
¦   ¦       ¦   ¦           couchbase.cpython-38.pyc
¦   ¦       ¦   ¦           couchdb.cpython-38.pyc
¦   ¦       ¦   ¦           dynamodb.cpython-38.pyc
¦   ¦       ¦   ¦           elasticsearch.cpython-38.pyc
¦   ¦       ¦   ¦           filesystem.cpython-38.pyc
¦   ¦       ¦   ¦           mongodb.cpython-38.pyc
¦   ¦       ¦   ¦           redis.cpython-38.pyc
¦   ¦       ¦   ¦           rpc.cpython-38.pyc
¦   ¦       ¦   ¦           s3.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---bin
¦   ¦       ¦   ¦   ¦   amqp.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   beat.py
¦   ¦       ¦   ¦   ¦   call.py
¦   ¦       ¦   ¦   ¦   celery.py
¦   ¦       ¦   ¦   ¦   control.py
¦   ¦       ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   graph.py
¦   ¦       ¦   ¦   ¦   list.py
¦   ¦       ¦   ¦   ¦   logtool.py
¦   ¦       ¦   ¦   ¦   migrate.py
¦   ¦       ¦   ¦   ¦   multi.py
¦   ¦       ¦   ¦   ¦   purge.py
¦   ¦       ¦   ¦   ¦   result.py
¦   ¦       ¦   ¦   ¦   shell.py
¦   ¦       ¦   ¦   ¦   upgrade.py
¦   ¦       ¦   ¦   ¦   worker.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           amqp.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           beat.cpython-38.pyc
¦   ¦       ¦   ¦           call.cpython-38.pyc
¦   ¦       ¦   ¦           celery.cpython-38.pyc
¦   ¦       ¦   ¦           control.cpython-38.pyc
¦   ¦       ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦           graph.cpython-38.pyc
¦   ¦       ¦   ¦           list.cpython-38.pyc
¦   ¦       ¦   ¦           logtool.cpython-38.pyc
¦   ¦       ¦   ¦           migrate.cpython-38.pyc
¦   ¦       ¦   ¦           multi.cpython-38.pyc
¦   ¦       ¦   ¦           purge.cpython-38.pyc
¦   ¦       ¦   ¦           result.cpython-38.pyc
¦   ¦       ¦   ¦           shell.cpython-38.pyc
¦   ¦       ¦   ¦           upgrade.cpython-38.pyc
¦   ¦       ¦   ¦           worker.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---concurrency
¦   ¦       ¦   ¦   ¦   asynpool.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   eventlet.py
¦   ¦       ¦   ¦   ¦   gevent.py
¦   ¦       ¦   ¦   ¦   prefork.py
¦   ¦       ¦   ¦   ¦   solo.py
¦   ¦       ¦   ¦   ¦   thread.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           asynpool.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           eventlet.cpython-38.pyc
¦   ¦       ¦   ¦           gevent.cpython-38.pyc
¦   ¦       ¦   ¦           prefork.cpython-38.pyc
¦   ¦       ¦   ¦           solo.cpython-38.pyc
¦   ¦       ¦   ¦           thread.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---contrib
¦   ¦       ¦   ¦   ¦   abortable.py
¦   ¦       ¦   ¦   ¦   migrate.py
¦   ¦       ¦   ¦   ¦   pytest.py
¦   ¦       ¦   ¦   ¦   rdb.py
¦   ¦       ¦   ¦   ¦   sphinx.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---testing
¦   ¦       ¦   ¦   ¦   ¦   app.py
¦   ¦       ¦   ¦   ¦   ¦   manager.py
¦   ¦       ¦   ¦   ¦   ¦   mocks.py
¦   ¦       ¦   ¦   ¦   ¦   tasks.py
¦   ¦       ¦   ¦   ¦   ¦   worker.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           app.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           manager.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mocks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tasks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           worker.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           abortable.cpython-38.pyc
¦   ¦       ¦   ¦           migrate.cpython-38.pyc
¦   ¦       ¦   ¦           pytest.cpython-38.pyc
¦   ¦       ¦   ¦           rdb.cpython-38.pyc
¦   ¦       ¦   ¦           sphinx.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---events
¦   ¦       ¦   ¦   ¦   cursesmon.py
¦   ¦       ¦   ¦   ¦   dispatcher.py
¦   ¦       ¦   ¦   ¦   dumper.py
¦   ¦       ¦   ¦   ¦   event.py
¦   ¦       ¦   ¦   ¦   receiver.py
¦   ¦       ¦   ¦   ¦   snapshot.py
¦   ¦       ¦   ¦   ¦   state.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           cursesmon.cpython-38.pyc
¦   ¦       ¦   ¦           dispatcher.cpython-38.pyc
¦   ¦       ¦   ¦           dumper.cpython-38.pyc
¦   ¦       ¦   ¦           event.cpython-38.pyc
¦   ¦       ¦   ¦           receiver.cpython-38.pyc
¦   ¦       ¦   ¦           snapshot.cpython-38.pyc
¦   ¦       ¦   ¦           state.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---fixups
¦   ¦       ¦   ¦   ¦   django.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           django.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---loaders
¦   ¦       ¦   ¦   ¦   app.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   default.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           app.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           default.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---security
¦   ¦       ¦   ¦   ¦   certificate.py
¦   ¦       ¦   ¦   ¦   key.py
¦   ¦       ¦   ¦   ¦   serialization.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           certificate.cpython-38.pyc
¦   ¦       ¦   ¦           key.cpython-38.pyc
¦   ¦       ¦   ¦           serialization.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---utils
¦   ¦       ¦   ¦   ¦   abstract.py
¦   ¦       ¦   ¦   ¦   collections.py
¦   ¦       ¦   ¦   ¦   debug.py
¦   ¦       ¦   ¦   ¦   deprecated.py
¦   ¦       ¦   ¦   ¦   functional.py
¦   ¦       ¦   ¦   ¦   graph.py
¦   ¦       ¦   ¦   ¦   imports.py
¦   ¦       ¦   ¦   ¦   iso8601.py
¦   ¦       ¦   ¦   ¦   log.py
¦   ¦       ¦   ¦   ¦   nodenames.py
¦   ¦       ¦   ¦   ¦   objects.py
¦   ¦       ¦   ¦   ¦   saferepr.py
¦   ¦       ¦   ¦   ¦   serialization.py
¦   ¦       ¦   ¦   ¦   sysinfo.py
¦   ¦       ¦   ¦   ¦   term.py
¦   ¦       ¦   ¦   ¦   text.py
¦   ¦       ¦   ¦   ¦   threads.py
¦   ¦       ¦   ¦   ¦   time.py
¦   ¦       ¦   ¦   ¦   timer2.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---dispatch
¦   ¦       ¦   ¦   ¦   ¦   signal.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           signal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---static
¦   ¦       ¦   ¦   ¦   ¦   celery_128.png
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           abstract.cpython-38.pyc
¦   ¦       ¦   ¦           collections.cpython-38.pyc
¦   ¦       ¦   ¦           debug.cpython-38.pyc
¦   ¦       ¦   ¦           deprecated.cpython-38.pyc
¦   ¦       ¦   ¦           functional.cpython-38.pyc
¦   ¦       ¦   ¦           graph.cpython-38.pyc
¦   ¦       ¦   ¦           imports.cpython-38.pyc
¦   ¦       ¦   ¦           iso8601.cpython-38.pyc
¦   ¦       ¦   ¦           log.cpython-38.pyc
¦   ¦       ¦   ¦           nodenames.cpython-38.pyc
¦   ¦       ¦   ¦           objects.cpython-38.pyc
¦   ¦       ¦   ¦           saferepr.cpython-38.pyc
¦   ¦       ¦   ¦           serialization.cpython-38.pyc
¦   ¦       ¦   ¦           sysinfo.cpython-38.pyc
¦   ¦       ¦   ¦           term.cpython-38.pyc
¦   ¦       ¦   ¦           text.cpython-38.pyc
¦   ¦       ¦   ¦           threads.cpython-38.pyc
¦   ¦       ¦   ¦           time.cpython-38.pyc
¦   ¦       ¦   ¦           timer2.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---worker
¦   ¦       ¦   ¦   ¦   autoscale.py
¦   ¦       ¦   ¦   ¦   components.py
¦   ¦       ¦   ¦   ¦   control.py
¦   ¦       ¦   ¦   ¦   heartbeat.py
¦   ¦       ¦   ¦   ¦   loops.py
¦   ¦       ¦   ¦   ¦   pidbox.py
¦   ¦       ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   state.py
¦   ¦       ¦   ¦   ¦   strategy.py
¦   ¦       ¦   ¦   ¦   worker.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---consumer
¦   ¦       ¦   ¦   ¦   ¦   agent.py
¦   ¦       ¦   ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   ¦   consumer.py
¦   ¦       ¦   ¦   ¦   ¦   control.py
¦   ¦       ¦   ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   ¦   gossip.py
¦   ¦       ¦   ¦   ¦   ¦   heart.py
¦   ¦       ¦   ¦   ¦   ¦   mingle.py
¦   ¦       ¦   ¦   ¦   ¦   tasks.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           agent.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           consumer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           control.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           gossip.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           heart.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mingle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tasks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           autoscale.cpython-38.pyc
¦   ¦       ¦   ¦           components.cpython-38.pyc
¦   ¦       ¦   ¦           control.cpython-38.pyc
¦   ¦       ¦   ¦           heartbeat.cpython-38.pyc
¦   ¦       ¦   ¦           loops.cpython-38.pyc
¦   ¦       ¦   ¦           pidbox.cpython-38.pyc
¦   ¦       ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦           state.cpython-38.pyc
¦   ¦       ¦   ¦           strategy.cpython-38.pyc
¦   ¦       ¦   ¦           worker.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           beat.cpython-38.pyc
¦   ¦       ¦           bootsteps.cpython-38.pyc
¦   ¦       ¦           canvas.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           local.cpython-38.pyc
¦   ¦       ¦           platforms.cpython-38.pyc
¦   ¦       ¦           result.cpython-38.pyc
¦   ¦       ¦           schedules.cpython-38.pyc
¦   ¦       ¦           signals.cpython-38.pyc
¦   ¦       ¦           states.cpython-38.pyc
¦   ¦       ¦           _state.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---celery-5.2.7.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---certifi
¦   ¦       ¦   ¦   cacert.pem
¦   ¦       ¦   ¦   core.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           core.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---certifi-2022.12.7.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---cffi
¦   ¦       ¦   ¦   api.py
¦   ¦       ¦   ¦   backend_ctypes.py
¦   ¦       ¦   ¦   cffi_opcode.py
¦   ¦       ¦   ¦   commontypes.py
¦   ¦       ¦   ¦   cparser.py
¦   ¦       ¦   ¦   error.py
¦   ¦       ¦   ¦   ffiplatform.py
¦   ¦       ¦   ¦   lock.py
¦   ¦       ¦   ¦   model.py
¦   ¦       ¦   ¦   parse_c_type.h
¦   ¦       ¦   ¦   pkgconfig.py
¦   ¦       ¦   ¦   recompiler.py
¦   ¦       ¦   ¦   setuptools_ext.py
¦   ¦       ¦   ¦   vengine_cpy.py
¦   ¦       ¦   ¦   vengine_gen.py
¦   ¦       ¦   ¦   verifier.py
¦   ¦       ¦   ¦   _cffi_errors.h
¦   ¦       ¦   ¦   _cffi_include.h
¦   ¦       ¦   ¦   _embedding.h
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           api.cpython-38.pyc
¦   ¦       ¦           backend_ctypes.cpython-38.pyc
¦   ¦       ¦           cffi_opcode.cpython-38.pyc
¦   ¦       ¦           commontypes.cpython-38.pyc
¦   ¦       ¦           cparser.cpython-38.pyc
¦   ¦       ¦           error.cpython-38.pyc
¦   ¦       ¦           ffiplatform.cpython-38.pyc
¦   ¦       ¦           lock.cpython-38.pyc
¦   ¦       ¦           model.cpython-38.pyc
¦   ¦       ¦           pkgconfig.cpython-38.pyc
¦   ¦       ¦           recompiler.cpython-38.pyc
¦   ¦       ¦           setuptools_ext.cpython-38.pyc
¦   ¦       ¦           vengine_cpy.cpython-38.pyc
¦   ¦       ¦           vengine_gen.cpython-38.pyc
¦   ¦       ¦           verifier.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---cffi-1.15.1.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---charset_normalizer
¦   ¦       ¦   ¦   api.py
¦   ¦       ¦   ¦   cd.py
¦   ¦       ¦   ¦   constant.py
¦   ¦       ¦   ¦   legacy.py
¦   ¦       ¦   ¦   md.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   md.py
¦   ¦       ¦   ¦   md__mypyc.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   models.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   version.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---assets
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---cli
¦   ¦       ¦   ¦   ¦   normalizer.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           normalizer.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           api.cpython-38.pyc
¦   ¦       ¦           cd.cpython-38.pyc
¦   ¦       ¦           constant.cpython-38.pyc
¦   ¦       ¦           legacy.cpython-38.pyc
¦   ¦       ¦           md.cpython-38.pyc
¦   ¦       ¦           models.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---charset_normalizer-3.1.0.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---click
¦   ¦       ¦   ¦   core.py
¦   ¦       ¦   ¦   decorators.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   formatting.py
¦   ¦       ¦   ¦   globals.py
¦   ¦       ¦   ¦   parser.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   shell_completion.py
¦   ¦       ¦   ¦   termui.py
¦   ¦       ¦   ¦   testing.py
¦   ¦       ¦   ¦   types.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   _compat.py
¦   ¦       ¦   ¦   _termui_impl.py
¦   ¦       ¦   ¦   _textwrap.py
¦   ¦       ¦   ¦   _winconsole.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           core.cpython-38.pyc
¦   ¦       ¦           decorators.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           formatting.cpython-38.pyc
¦   ¦       ¦           globals.cpython-38.pyc
¦   ¦       ¦           parser.cpython-38.pyc
¦   ¦       ¦           shell_completion.cpython-38.pyc
¦   ¦       ¦           termui.cpython-38.pyc
¦   ¦       ¦           testing.cpython-38.pyc
¦   ¦       ¦           types.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           _compat.cpython-38.pyc
¦   ¦       ¦           _termui_impl.cpython-38.pyc
¦   ¦       ¦           _textwrap.cpython-38.pyc
¦   ¦       ¦           _winconsole.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---click-8.1.3.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---click_didyoumean
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---click_didyoumean-0.3.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---click_plugins
¦   ¦       ¦   ¦   core.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           core.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---click_plugins-1.1.1.dist-info
¦   ¦       ¦       AUTHORS.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---click_repl
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---click_repl-0.2.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---colorama
¦   ¦       ¦   ¦   ansi.py
¦   ¦       ¦   ¦   ansitowin32.py
¦   ¦       ¦   ¦   initialise.py
¦   ¦       ¦   ¦   win32.py
¦   ¦       ¦   ¦   winterm.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   ansitowin32_test.py
¦   ¦       ¦   ¦   ¦   ansi_test.py
¦   ¦       ¦   ¦   ¦   initialise_test.py
¦   ¦       ¦   ¦   ¦   isatty_test.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   winterm_test.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           ansitowin32_test.cpython-38.pyc
¦   ¦       ¦   ¦           ansi_test.cpython-38.pyc
¦   ¦       ¦   ¦           initialise_test.cpython-38.pyc
¦   ¦       ¦   ¦           isatty_test.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           winterm_test.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           ansi.cpython-38.pyc
¦   ¦       ¦           ansitowin32.cpython-38.pyc
¦   ¦       ¦           initialise.cpython-38.pyc
¦   ¦       ¦           win32.cpython-38.pyc
¦   ¦       ¦           winterm.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---colorama-0.4.6.dist-info
¦   ¦       ¦   ¦   INSTALLER
¦   ¦       ¦   ¦   METADATA
¦   ¦       ¦   ¦   RECORD
¦   ¦       ¦   ¦   REQUESTED
¦   ¦       ¦   ¦   WHEEL
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---licenses
¦   ¦       ¦           LICENSE.txt
¦   ¦       ¦           
¦   ¦       +---cssselect
¦   ¦       ¦   ¦   parser.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   xpath.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           parser.cpython-38.pyc
¦   ¦       ¦           xpath.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---cssselect-1.2.0.dist-info
¦   ¦       ¦       AUTHORS
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---cssselect2
¦   ¦       ¦   ¦   compiler.py
¦   ¦       ¦   ¦   parser.py
¦   ¦       ¦   ¦   tree.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           compiler.cpython-38.pyc
¦   ¦       ¦           parser.cpython-38.pyc
¦   ¦       ¦           tree.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---cssselect2-0.7.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---cssutils
¦   ¦       ¦   ¦   codec.py
¦   ¦       ¦   ¦   css2productions.py
¦   ¦       ¦   ¦   cssproductions.py
¦   ¦       ¦   ¦   errorhandler.py
¦   ¦       ¦   ¦   helper.py
¦   ¦       ¦   ¦   parse.py
¦   ¦       ¦   ¦   prodparser.py
¦   ¦       ¦   ¦   profiles.py
¦   ¦       ¦   ¦   sac.py
¦   ¦       ¦   ¦   script.py
¦   ¦       ¦   ¦   serialize.py
¦   ¦       ¦   ¦   settings.py
¦   ¦       ¦   ¦   tokenize2.py
¦   ¦       ¦   ¦   util.py
¦   ¦       ¦   ¦   _fetch.py
¦   ¦       ¦   ¦   _fetchgae.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---css
¦   ¦       ¦   ¦   ¦   colors.py
¦   ¦       ¦   ¦   ¦   csscharsetrule.py
¦   ¦       ¦   ¦   ¦   csscomment.py
¦   ¦       ¦   ¦   ¦   cssfontfacerule.py
¦   ¦       ¦   ¦   ¦   cssimportrule.py
¦   ¦       ¦   ¦   ¦   cssmediarule.py
¦   ¦       ¦   ¦   ¦   cssnamespacerule.py
¦   ¦       ¦   ¦   ¦   csspagerule.py
¦   ¦       ¦   ¦   ¦   cssproperties.py
¦   ¦       ¦   ¦   ¦   cssrule.py
¦   ¦       ¦   ¦   ¦   cssrulelist.py
¦   ¦       ¦   ¦   ¦   cssstyledeclaration.py
¦   ¦       ¦   ¦   ¦   cssstylerule.py
¦   ¦       ¦   ¦   ¦   cssstylesheet.py
¦   ¦       ¦   ¦   ¦   cssunknownrule.py
¦   ¦       ¦   ¦   ¦   cssvalue.py
¦   ¦       ¦   ¦   ¦   cssvariablesdeclaration.py
¦   ¦       ¦   ¦   ¦   cssvariablesrule.py
¦   ¦       ¦   ¦   ¦   marginrule.py
¦   ¦       ¦   ¦   ¦   property.py
¦   ¦       ¦   ¦   ¦   selector.py
¦   ¦       ¦   ¦   ¦   selectorlist.py
¦   ¦       ¦   ¦   ¦   value.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           colors.cpython-38.pyc
¦   ¦       ¦   ¦           csscharsetrule.cpython-38.pyc
¦   ¦       ¦   ¦           csscomment.cpython-38.pyc
¦   ¦       ¦   ¦           cssfontfacerule.cpython-38.pyc
¦   ¦       ¦   ¦           cssimportrule.cpython-38.pyc
¦   ¦       ¦   ¦           cssmediarule.cpython-38.pyc
¦   ¦       ¦   ¦           cssnamespacerule.cpython-38.pyc
¦   ¦       ¦   ¦           csspagerule.cpython-38.pyc
¦   ¦       ¦   ¦           cssproperties.cpython-38.pyc
¦   ¦       ¦   ¦           cssrule.cpython-38.pyc
¦   ¦       ¦   ¦           cssrulelist.cpython-38.pyc
¦   ¦       ¦   ¦           cssstyledeclaration.cpython-38.pyc
¦   ¦       ¦   ¦           cssstylerule.cpython-38.pyc
¦   ¦       ¦   ¦           cssstylesheet.cpython-38.pyc
¦   ¦       ¦   ¦           cssunknownrule.cpython-38.pyc
¦   ¦       ¦   ¦           cssvalue.cpython-38.pyc
¦   ¦       ¦   ¦           cssvariablesdeclaration.cpython-38.pyc
¦   ¦       ¦   ¦           cssvariablesrule.cpython-38.pyc
¦   ¦       ¦   ¦           marginrule.cpython-38.pyc
¦   ¦       ¦   ¦           property.cpython-38.pyc
¦   ¦       ¦   ¦           selector.cpython-38.pyc
¦   ¦       ¦   ¦           selectorlist.cpython-38.pyc
¦   ¦       ¦   ¦           value.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---scripts
¦   ¦       ¦   ¦   ¦   csscapture.py
¦   ¦       ¦   ¦   ¦   csscombine.py
¦   ¦       ¦   ¦   ¦   cssparse.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           csscapture.cpython-38.pyc
¦   ¦       ¦   ¦           csscombine.cpython-38.pyc
¦   ¦       ¦   ¦           cssparse.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---stylesheets
¦   ¦       ¦   ¦   ¦   medialist.py
¦   ¦       ¦   ¦   ¦   mediaquery.py
¦   ¦       ¦   ¦   ¦   stylesheet.py
¦   ¦       ¦   ¦   ¦   stylesheetlist.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           medialist.cpython-38.pyc
¦   ¦       ¦   ¦           mediaquery.cpython-38.pyc
¦   ¦       ¦   ¦           stylesheet.cpython-38.pyc
¦   ¦       ¦   ¦           stylesheetlist.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   basetest.py
¦   ¦       ¦   ¦   ¦   test_codec.py
¦   ¦       ¦   ¦   ¦   test_csscharsetrule.py
¦   ¦       ¦   ¦   ¦   test_csscomment.py
¦   ¦       ¦   ¦   ¦   test_cssfontfacerule.py
¦   ¦       ¦   ¦   ¦   test_cssimportrule.py
¦   ¦       ¦   ¦   ¦   test_cssmediarule.py
¦   ¦       ¦   ¦   ¦   test_cssnamespacerule.py
¦   ¦       ¦   ¦   ¦   test_csspagerule.py
¦   ¦       ¦   ¦   ¦   test_cssproperties.py
¦   ¦       ¦   ¦   ¦   test_cssrule.py
¦   ¦       ¦   ¦   ¦   test_cssrulelist.py
¦   ¦       ¦   ¦   ¦   test_cssstyledeclaration.py
¦   ¦       ¦   ¦   ¦   test_cssstylerule.py
¦   ¦       ¦   ¦   ¦   test_cssstylesheet.py
¦   ¦       ¦   ¦   ¦   test_cssunknownrule.py
¦   ¦       ¦   ¦   ¦   test_cssutils.py
¦   ¦       ¦   ¦   ¦   test_cssutilsimport.py
¦   ¦       ¦   ¦   ¦   test_cssvalue.py
¦   ¦       ¦   ¦   ¦   test_cssvariablesdeclaration.py
¦   ¦       ¦   ¦   ¦   test_cssvariablesrule.py
¦   ¦       ¦   ¦   ¦   test_domimplementation.py
¦   ¦       ¦   ¦   ¦   test_errorhandler.py
¦   ¦       ¦   ¦   ¦   test_helper.py
¦   ¦       ¦   ¦   ¦   test_marginrule.py
¦   ¦       ¦   ¦   ¦   test_medialist.py
¦   ¦       ¦   ¦   ¦   test_mediaquery.py
¦   ¦       ¦   ¦   ¦   test_parse.py
¦   ¦       ¦   ¦   ¦   test_prodparser.py
¦   ¦       ¦   ¦   ¦   test_profiles.py
¦   ¦       ¦   ¦   ¦   test_properties.py
¦   ¦       ¦   ¦   ¦   test_property.py
¦   ¦       ¦   ¦   ¦   test_scripts_csscombine.py
¦   ¦       ¦   ¦   ¦   test_selector.py
¦   ¦       ¦   ¦   ¦   test_selectorlist.py
¦   ¦       ¦   ¦   ¦   test_serialize.py
¦   ¦       ¦   ¦   ¦   test_settings.py
¦   ¦       ¦   ¦   ¦   test_stylesheet.py
¦   ¦       ¦   ¦   ¦   test_tokenize2.py
¦   ¦       ¦   ¦   ¦   test_util.py
¦   ¦       ¦   ¦   ¦   test_value.py
¦   ¦       ¦   ¦   ¦   test_x.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---sheets
¦   ¦       ¦   ¦   ¦   ¦   096.css
¦   ¦       ¦   ¦   ¦   ¦   097.css
¦   ¦       ¦   ¦   ¦   ¦   1.css
¦   ¦       ¦   ¦   ¦   ¦   1ascii.css
¦   ¦       ¦   ¦   ¦   ¦   1import.css
¦   ¦       ¦   ¦   ¦   ¦   1inherit-ascii.css
¦   ¦       ¦   ¦   ¦   ¦   1inherit-iso.css
¦   ¦       ¦   ¦   ¦   ¦   1inherit-utf8.css
¦   ¦       ¦   ¦   ¦   ¦   1utf.css
¦   ¦       ¦   ¦   ¦   ¦   2inherit-iso.css
¦   ¦       ¦   ¦   ¦   ¦   2resolve.css
¦   ¦       ¦   ¦   ¦   ¦   acid2.css
¦   ¦       ¦   ¦   ¦   ¦   all.css
¦   ¦       ¦   ¦   ¦   ¦   atrule.css
¦   ¦       ¦   ¦   ¦   ¦   bad.css
¦   ¦       ¦   ¦   ¦   ¦   basic.css
¦   ¦       ¦   ¦   ¦   ¦   bundle.css
¦   ¦       ¦   ¦   ¦   ¦   cases.css
¦   ¦       ¦   ¦   ¦   ¦   csscombine-1.css
¦   ¦       ¦   ¦   ¦   ¦   csscombine-2.css
¦   ¦       ¦   ¦   ¦   ¦   csscombine-proxy.css
¦   ¦       ¦   ¦   ¦   ¦   cthedot_default.css
¦   ¦       ¦   ¦   ¦   ¦   default_html4.css
¦   ¦       ¦   ¦   ¦   ¦   hacks.css
¦   ¦       ¦   ¦   ¦   ¦   html.css
¦   ¦       ¦   ¦   ¦   ¦   html20.css
¦   ¦       ¦   ¦   ¦   ¦   html40.css
¦   ¦       ¦   ¦   ¦   ¦   import.css
¦   ¦       ¦   ¦   ¦   ¦   import3.css
¦   ¦       ¦   ¦   ¦   ¦   ll.css
¦   ¦       ¦   ¦   ¦   ¦   ll2.css
¦   ¦       ¦   ¦   ¦   ¦   multiple-values.css
¦   ¦       ¦   ¦   ¦   ¦   page_test.css
¦   ¦       ¦   ¦   ¦   ¦   sample_5.css
¦   ¦       ¦   ¦   ¦   ¦   sample_7.css
¦   ¦       ¦   ¦   ¦   ¦   simple.css
¦   ¦       ¦   ¦   ¦   ¦   single-color.css
¦   ¦       ¦   ¦   ¦   ¦   slashcode.css
¦   ¦       ¦   ¦   ¦   ¦   t-HACKS.css
¦   ¦       ¦   ¦   ¦   ¦   test-unicode.css
¦   ¦       ¦   ¦   ¦   ¦   test.css
¦   ¦       ¦   ¦   ¦   ¦   tigris.css
¦   ¦       ¦   ¦   ¦   ¦   tigris2.css
¦   ¦       ¦   ¦   ¦   ¦   u_simple.css
¦   ¦       ¦   ¦   ¦   ¦   vars.css
¦   ¦       ¦   ¦   ¦   ¦   varsimport.css
¦   ¦       ¦   ¦   ¦   ¦   v_simple.css
¦   ¦       ¦   ¦   ¦   ¦   xhtml2.css
¦   ¦       ¦   ¦   ¦   ¦   xhtml22.css
¦   ¦       ¦   ¦   ¦   ¦   yuck.css
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---images
¦   ¦       ¦   ¦   ¦   ¦       example.gif
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---import
¦   ¦       ¦   ¦   ¦   ¦   ¦   import-impossible.css
¦   ¦       ¦   ¦   ¦   ¦   ¦   import2.css
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---images2
¦   ¦       ¦   ¦   ¦   ¦           example2.gif
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---var
¦   ¦       ¦   ¦   ¦           start.css
¦   ¦       ¦   ¦   ¦           use.css
¦   ¦       ¦   ¦   ¦           vars.css
¦   ¦       ¦   ¦   ¦           vars2.css
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---test_encutils
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           basetest.cpython-38.pyc
¦   ¦       ¦   ¦           test_codec.cpython-38.pyc
¦   ¦       ¦   ¦           test_csscharsetrule.cpython-38.pyc
¦   ¦       ¦   ¦           test_csscomment.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssfontfacerule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssimportrule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssmediarule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssnamespacerule.cpython-38.pyc
¦   ¦       ¦   ¦           test_csspagerule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssproperties.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssrule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssrulelist.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssstyledeclaration.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssstylerule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssstylesheet.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssunknownrule.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssutils.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssutilsimport.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssvalue.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssvariablesdeclaration.cpython-38.pyc
¦   ¦       ¦   ¦           test_cssvariablesrule.cpython-38.pyc
¦   ¦       ¦   ¦           test_domimplementation.cpython-38.pyc
¦   ¦       ¦   ¦           test_errorhandler.cpython-38.pyc
¦   ¦       ¦   ¦           test_helper.cpython-38.pyc
¦   ¦       ¦   ¦           test_marginrule.cpython-38.pyc
¦   ¦       ¦   ¦           test_medialist.cpython-38.pyc
¦   ¦       ¦   ¦           test_mediaquery.cpython-38.pyc
¦   ¦       ¦   ¦           test_parse.cpython-38.pyc
¦   ¦       ¦   ¦           test_prodparser.cpython-38.pyc
¦   ¦       ¦   ¦           test_profiles.cpython-38.pyc
¦   ¦       ¦   ¦           test_properties.cpython-38.pyc
¦   ¦       ¦   ¦           test_property.cpython-38.pyc
¦   ¦       ¦   ¦           test_scripts_csscombine.cpython-38.pyc
¦   ¦       ¦   ¦           test_selector.cpython-38.pyc
¦   ¦       ¦   ¦           test_selectorlist.cpython-38.pyc
¦   ¦       ¦   ¦           test_serialize.cpython-38.pyc
¦   ¦       ¦   ¦           test_settings.cpython-38.pyc
¦   ¦       ¦   ¦           test_stylesheet.cpython-38.pyc
¦   ¦       ¦   ¦           test_tokenize2.cpython-38.pyc
¦   ¦       ¦   ¦           test_util.cpython-38.pyc
¦   ¦       ¦   ¦           test_value.cpython-38.pyc
¦   ¦       ¦   ¦           test_x.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           codec.cpython-38.pyc
¦   ¦       ¦           css2productions.cpython-38.pyc
¦   ¦       ¦           cssproductions.cpython-38.pyc
¦   ¦       ¦           errorhandler.cpython-38.pyc
¦   ¦       ¦           helper.cpython-38.pyc
¦   ¦       ¦           parse.cpython-38.pyc
¦   ¦       ¦           prodparser.cpython-38.pyc
¦   ¦       ¦           profiles.cpython-38.pyc
¦   ¦       ¦           sac.cpython-38.pyc
¦   ¦       ¦           script.cpython-38.pyc
¦   ¦       ¦           serialize.cpython-38.pyc
¦   ¦       ¦           settings.cpython-38.pyc
¦   ¦       ¦           tokenize2.cpython-38.pyc
¦   ¦       ¦           util.cpython-38.pyc
¦   ¦       ¦           _fetch.cpython-38.pyc
¦   ¦       ¦           _fetchgae.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---cssutils-2.6.0.dist-info
¦   ¦       ¦       COPYING
¦   ¦       ¦       COPYING.LESSER
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---dateutil
¦   ¦       ¦   ¦   easter.py
¦   ¦       ¦   ¦   relativedelta.py
¦   ¦       ¦   ¦   rrule.py
¦   ¦       ¦   ¦   tzwin.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   _common.py
¦   ¦       ¦   ¦   _version.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---parser
¦   ¦       ¦   ¦   ¦   isoparser.py
¦   ¦       ¦   ¦   ¦   _parser.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           isoparser.cpython-38.pyc
¦   ¦       ¦   ¦           _parser.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tz
¦   ¦       ¦   ¦   ¦   tz.py
¦   ¦       ¦   ¦   ¦   win.py
¦   ¦       ¦   ¦   ¦   _common.py
¦   ¦       ¦   ¦   ¦   _factories.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           tz.cpython-38.pyc
¦   ¦       ¦   ¦           win.cpython-38.pyc
¦   ¦       ¦   ¦           _common.cpython-38.pyc
¦   ¦       ¦   ¦           _factories.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---zoneinfo
¦   ¦       ¦   ¦   ¦   dateutil-zoneinfo.tar.gz
¦   ¦       ¦   ¦   ¦   rebuild.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           rebuild.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           easter.cpython-38.pyc
¦   ¦       ¦           relativedelta.cpython-38.pyc
¦   ¦       ¦           rrule.cpython-38.pyc
¦   ¦       ¦           tzwin.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           _common.cpython-38.pyc
¦   ¦       ¦           _version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---dns
¦   ¦       ¦   ¦   asyncbackend.py
¦   ¦       ¦   ¦   asyncquery.py
¦   ¦       ¦   ¦   asyncresolver.py
¦   ¦       ¦   ¦   dnssec.py
¦   ¦       ¦   ¦   dnssectypes.py
¦   ¦       ¦   ¦   e164.py
¦   ¦       ¦   ¦   edns.py
¦   ¦       ¦   ¦   entropy.py
¦   ¦       ¦   ¦   enum.py
¦   ¦       ¦   ¦   exception.py
¦   ¦       ¦   ¦   flags.py
¦   ¦       ¦   ¦   grange.py
¦   ¦       ¦   ¦   immutable.py
¦   ¦       ¦   ¦   inet.py
¦   ¦       ¦   ¦   ipv4.py
¦   ¦       ¦   ¦   ipv6.py
¦   ¦       ¦   ¦   message.py
¦   ¦       ¦   ¦   name.py
¦   ¦       ¦   ¦   namedict.py
¦   ¦       ¦   ¦   node.py
¦   ¦       ¦   ¦   opcode.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   query.py
¦   ¦       ¦   ¦   rcode.py
¦   ¦       ¦   ¦   rdata.py
¦   ¦       ¦   ¦   rdataclass.py
¦   ¦       ¦   ¦   rdataset.py
¦   ¦       ¦   ¦   rdatatype.py
¦   ¦       ¦   ¦   renderer.py
¦   ¦       ¦   ¦   resolver.py
¦   ¦       ¦   ¦   reversename.py
¦   ¦       ¦   ¦   rrset.py
¦   ¦       ¦   ¦   serial.py
¦   ¦       ¦   ¦   set.py
¦   ¦       ¦   ¦   tokenizer.py
¦   ¦       ¦   ¦   transaction.py
¦   ¦       ¦   ¦   tsig.py
¦   ¦       ¦   ¦   tsigkeyring.py
¦   ¦       ¦   ¦   ttl.py
¦   ¦       ¦   ¦   update.py
¦   ¦       ¦   ¦   version.py
¦   ¦       ¦   ¦   versioned.py
¦   ¦       ¦   ¦   win32util.py
¦   ¦       ¦   ¦   wire.py
¦   ¦       ¦   ¦   xfr.py
¦   ¦       ¦   ¦   zone.py
¦   ¦       ¦   ¦   zonefile.py
¦   ¦       ¦   ¦   zonetypes.py
¦   ¦       ¦   ¦   _asyncbackend.py
¦   ¦       ¦   ¦   _asyncio_backend.py
¦   ¦       ¦   ¦   _curio_backend.py
¦   ¦       ¦   ¦   _immutable_ctx.py
¦   ¦       ¦   ¦   _trio_backend.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---quic
¦   ¦       ¦   ¦   ¦   _asyncio.py
¦   ¦       ¦   ¦   ¦   _common.py
¦   ¦       ¦   ¦   ¦   _sync.py
¦   ¦       ¦   ¦   ¦   _trio.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           _asyncio.cpython-38.pyc
¦   ¦       ¦   ¦           _common.cpython-38.pyc
¦   ¦       ¦   ¦           _sync.cpython-38.pyc
¦   ¦       ¦   ¦           _trio.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---rdtypes
¦   ¦       ¦   ¦   ¦   dnskeybase.py
¦   ¦       ¦   ¦   ¦   dsbase.py
¦   ¦       ¦   ¦   ¦   euibase.py
¦   ¦       ¦   ¦   ¦   mxbase.py
¦   ¦       ¦   ¦   ¦   nsbase.py
¦   ¦       ¦   ¦   ¦   svcbbase.py
¦   ¦       ¦   ¦   ¦   tlsabase.py
¦   ¦       ¦   ¦   ¦   txtbase.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---ANY
¦   ¦       ¦   ¦   ¦   ¦   AFSDB.py
¦   ¦       ¦   ¦   ¦   ¦   AMTRELAY.py
¦   ¦       ¦   ¦   ¦   ¦   AVC.py
¦   ¦       ¦   ¦   ¦   ¦   CAA.py
¦   ¦       ¦   ¦   ¦   ¦   CDNSKEY.py
¦   ¦       ¦   ¦   ¦   ¦   CDS.py
¦   ¦       ¦   ¦   ¦   ¦   CERT.py
¦   ¦       ¦   ¦   ¦   ¦   CNAME.py
¦   ¦       ¦   ¦   ¦   ¦   CSYNC.py
¦   ¦       ¦   ¦   ¦   ¦   DLV.py
¦   ¦       ¦   ¦   ¦   ¦   DNAME.py
¦   ¦       ¦   ¦   ¦   ¦   DNSKEY.py
¦   ¦       ¦   ¦   ¦   ¦   DS.py
¦   ¦       ¦   ¦   ¦   ¦   EUI48.py
¦   ¦       ¦   ¦   ¦   ¦   EUI64.py
¦   ¦       ¦   ¦   ¦   ¦   GPOS.py
¦   ¦       ¦   ¦   ¦   ¦   HINFO.py
¦   ¦       ¦   ¦   ¦   ¦   HIP.py
¦   ¦       ¦   ¦   ¦   ¦   ISDN.py
¦   ¦       ¦   ¦   ¦   ¦   L32.py
¦   ¦       ¦   ¦   ¦   ¦   L64.py
¦   ¦       ¦   ¦   ¦   ¦   LOC.py
¦   ¦       ¦   ¦   ¦   ¦   LP.py
¦   ¦       ¦   ¦   ¦   ¦   MX.py
¦   ¦       ¦   ¦   ¦   ¦   NID.py
¦   ¦       ¦   ¦   ¦   ¦   NINFO.py
¦   ¦       ¦   ¦   ¦   ¦   NS.py
¦   ¦       ¦   ¦   ¦   ¦   NSEC.py
¦   ¦       ¦   ¦   ¦   ¦   NSEC3.py
¦   ¦       ¦   ¦   ¦   ¦   NSEC3PARAM.py
¦   ¦       ¦   ¦   ¦   ¦   OPENPGPKEY.py
¦   ¦       ¦   ¦   ¦   ¦   OPT.py
¦   ¦       ¦   ¦   ¦   ¦   PTR.py
¦   ¦       ¦   ¦   ¦   ¦   RP.py
¦   ¦       ¦   ¦   ¦   ¦   RRSIG.py
¦   ¦       ¦   ¦   ¦   ¦   RT.py
¦   ¦       ¦   ¦   ¦   ¦   SMIMEA.py
¦   ¦       ¦   ¦   ¦   ¦   SOA.py
¦   ¦       ¦   ¦   ¦   ¦   SPF.py
¦   ¦       ¦   ¦   ¦   ¦   SSHFP.py
¦   ¦       ¦   ¦   ¦   ¦   TKEY.py
¦   ¦       ¦   ¦   ¦   ¦   TLSA.py
¦   ¦       ¦   ¦   ¦   ¦   TSIG.py
¦   ¦       ¦   ¦   ¦   ¦   TXT.py
¦   ¦       ¦   ¦   ¦   ¦   URI.py
¦   ¦       ¦   ¦   ¦   ¦   X25.py
¦   ¦       ¦   ¦   ¦   ¦   ZONEMD.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           AFSDB.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           AMTRELAY.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           AVC.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           CAA.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           CDNSKEY.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           CDS.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           CERT.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           CNAME.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           CSYNC.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           DLV.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           DNAME.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           DNSKEY.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           DS.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           EUI48.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           EUI64.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           GPOS.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           HINFO.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           HIP.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ISDN.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           L32.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           L64.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           LOC.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           LP.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           MX.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NID.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NINFO.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NS.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NSEC.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NSEC3.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NSEC3PARAM.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           OPENPGPKEY.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           OPT.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           PTR.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           RP.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           RRSIG.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           RT.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           SMIMEA.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           SOA.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           SPF.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           SSHFP.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           TKEY.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           TLSA.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           TSIG.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           TXT.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           URI.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           X25.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ZONEMD.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---CH
¦   ¦       ¦   ¦   ¦   ¦   A.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           A.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---IN
¦   ¦       ¦   ¦   ¦   ¦   A.py
¦   ¦       ¦   ¦   ¦   ¦   AAAA.py
¦   ¦       ¦   ¦   ¦   ¦   APL.py
¦   ¦       ¦   ¦   ¦   ¦   DHCID.py
¦   ¦       ¦   ¦   ¦   ¦   HTTPS.py
¦   ¦       ¦   ¦   ¦   ¦   IPSECKEY.py
¦   ¦       ¦   ¦   ¦   ¦   KX.py
¦   ¦       ¦   ¦   ¦   ¦   NAPTR.py
¦   ¦       ¦   ¦   ¦   ¦   NSAP.py
¦   ¦       ¦   ¦   ¦   ¦   NSAP_PTR.py
¦   ¦       ¦   ¦   ¦   ¦   PX.py
¦   ¦       ¦   ¦   ¦   ¦   SRV.py
¦   ¦       ¦   ¦   ¦   ¦   SVCB.py
¦   ¦       ¦   ¦   ¦   ¦   WKS.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           A.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           AAAA.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           APL.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           DHCID.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           HTTPS.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           IPSECKEY.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           KX.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NAPTR.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NSAP.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           NSAP_PTR.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           PX.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           SRV.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           SVCB.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           WKS.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           dnskeybase.cpython-38.pyc
¦   ¦       ¦   ¦           dsbase.cpython-38.pyc
¦   ¦       ¦   ¦           euibase.cpython-38.pyc
¦   ¦       ¦   ¦           mxbase.cpython-38.pyc
¦   ¦       ¦   ¦           nsbase.cpython-38.pyc
¦   ¦       ¦   ¦           svcbbase.cpython-38.pyc
¦   ¦       ¦   ¦           tlsabase.cpython-38.pyc
¦   ¦       ¦   ¦           txtbase.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           asyncbackend.cpython-38.pyc
¦   ¦       ¦           asyncquery.cpython-38.pyc
¦   ¦       ¦           asyncresolver.cpython-38.pyc
¦   ¦       ¦           dnssec.cpython-38.pyc
¦   ¦       ¦           dnssectypes.cpython-38.pyc
¦   ¦       ¦           e164.cpython-38.pyc
¦   ¦       ¦           edns.cpython-38.pyc
¦   ¦       ¦           entropy.cpython-38.pyc
¦   ¦       ¦           enum.cpython-38.pyc
¦   ¦       ¦           exception.cpython-38.pyc
¦   ¦       ¦           flags.cpython-38.pyc
¦   ¦       ¦           grange.cpython-38.pyc
¦   ¦       ¦           immutable.cpython-38.pyc
¦   ¦       ¦           inet.cpython-38.pyc
¦   ¦       ¦           ipv4.cpython-38.pyc
¦   ¦       ¦           ipv6.cpython-38.pyc
¦   ¦       ¦           message.cpython-38.pyc
¦   ¦       ¦           name.cpython-38.pyc
¦   ¦       ¦           namedict.cpython-38.pyc
¦   ¦       ¦           node.cpython-38.pyc
¦   ¦       ¦           opcode.cpython-38.pyc
¦   ¦       ¦           query.cpython-38.pyc
¦   ¦       ¦           rcode.cpython-38.pyc
¦   ¦       ¦           rdata.cpython-38.pyc
¦   ¦       ¦           rdataclass.cpython-38.pyc
¦   ¦       ¦           rdataset.cpython-38.pyc
¦   ¦       ¦           rdatatype.cpython-38.pyc
¦   ¦       ¦           renderer.cpython-38.pyc
¦   ¦       ¦           resolver.cpython-38.pyc
¦   ¦       ¦           reversename.cpython-38.pyc
¦   ¦       ¦           rrset.cpython-38.pyc
¦   ¦       ¦           serial.cpython-38.pyc
¦   ¦       ¦           set.cpython-38.pyc
¦   ¦       ¦           tokenizer.cpython-38.pyc
¦   ¦       ¦           transaction.cpython-38.pyc
¦   ¦       ¦           tsig.cpython-38.pyc
¦   ¦       ¦           tsigkeyring.cpython-38.pyc
¦   ¦       ¦           ttl.cpython-38.pyc
¦   ¦       ¦           update.cpython-38.pyc
¦   ¦       ¦           version.cpython-38.pyc
¦   ¦       ¦           versioned.cpython-38.pyc
¦   ¦       ¦           win32util.cpython-38.pyc
¦   ¦       ¦           wire.cpython-38.pyc
¦   ¦       ¦           xfr.cpython-38.pyc
¦   ¦       ¦           zone.cpython-38.pyc
¦   ¦       ¦           zonefile.cpython-38.pyc
¦   ¦       ¦           zonetypes.cpython-38.pyc
¦   ¦       ¦           _asyncbackend.cpython-38.pyc
¦   ¦       ¦           _asyncio_backend.cpython-38.pyc
¦   ¦       ¦           _curio_backend.cpython-38.pyc
¦   ¦       ¦           _immutable_ctx.cpython-38.pyc
¦   ¦       ¦           _trio_backend.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---dnspython-2.3.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---email_validator
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---email_validator-1.3.1.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---encutils
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---flask
¦   ¦       ¦   ¦   app.py
¦   ¦       ¦   ¦   blueprints.py
¦   ¦       ¦   ¦   cli.py
¦   ¦       ¦   ¦   config.py
¦   ¦       ¦   ¦   ctx.py
¦   ¦       ¦   ¦   debughelpers.py
¦   ¦       ¦   ¦   globals.py
¦   ¦       ¦   ¦   helpers.py
¦   ¦       ¦   ¦   logging.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   scaffold.py
¦   ¦       ¦   ¦   sessions.py
¦   ¦       ¦   ¦   signals.py
¦   ¦       ¦   ¦   templating.py
¦   ¦       ¦   ¦   testing.py
¦   ¦       ¦   ¦   typing.py
¦   ¦       ¦   ¦   views.py
¦   ¦       ¦   ¦   wrappers.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---json
¦   ¦       ¦   ¦   ¦   provider.py
¦   ¦       ¦   ¦   ¦   tag.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           provider.cpython-38.pyc
¦   ¦       ¦   ¦           tag.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           app.cpython-38.pyc
¦   ¦       ¦           blueprints.cpython-38.pyc
¦   ¦       ¦           cli.cpython-38.pyc
¦   ¦       ¦           config.cpython-38.pyc
¦   ¦       ¦           ctx.cpython-38.pyc
¦   ¦       ¦           debughelpers.cpython-38.pyc
¦   ¦       ¦           globals.cpython-38.pyc
¦   ¦       ¦           helpers.cpython-38.pyc
¦   ¦       ¦           logging.cpython-38.pyc
¦   ¦       ¦           scaffold.cpython-38.pyc
¦   ¦       ¦           sessions.cpython-38.pyc
¦   ¦       ¦           signals.cpython-38.pyc
¦   ¦       ¦           templating.cpython-38.pyc
¦   ¦       ¦           testing.cpython-38.pyc
¦   ¦       ¦           typing.cpython-38.pyc
¦   ¦       ¦           views.cpython-38.pyc
¦   ¦       ¦           wrappers.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask-2.2.2.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---Flask_Bcrypt-1.0.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_caching
¦   ¦       ¦   ¦   jinja2ext.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---backends
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   filesystemcache.py
¦   ¦       ¦   ¦   ¦   memcache.py
¦   ¦       ¦   ¦   ¦   nullcache.py
¦   ¦       ¦   ¦   ¦   rediscache.py
¦   ¦       ¦   ¦   ¦   simplecache.py
¦   ¦       ¦   ¦   ¦   uwsgicache.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           filesystemcache.cpython-38.pyc
¦   ¦       ¦   ¦           memcache.cpython-38.pyc
¦   ¦       ¦   ¦           nullcache.cpython-38.pyc
¦   ¦       ¦   ¦           rediscache.cpython-38.pyc
¦   ¦       ¦   ¦           simplecache.cpython-38.pyc
¦   ¦       ¦   ¦           uwsgicache.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---contrib
¦   ¦       ¦   ¦   ¦   googlecloudstoragecache.py
¦   ¦       ¦   ¦   ¦   uwsgicache.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           googlecloudstoragecache.cpython-38.pyc
¦   ¦       ¦   ¦           uwsgicache.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           jinja2ext.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_Caching-2.0.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_cors
¦   ¦       ¦   ¦   core.py
¦   ¦       ¦   ¦   decorator.py
¦   ¦       ¦   ¦   extension.py
¦   ¦       ¦   ¦   version.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           core.cpython-38.pyc
¦   ¦       ¦           decorator.cpython-38.pyc
¦   ¦       ¦           extension.cpython-38.pyc
¦   ¦       ¦           version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_Cors-3.0.10.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_login
¦   ¦       ¦   ¦   config.py
¦   ¦       ¦   ¦   login_manager.py
¦   ¦       ¦   ¦   mixins.py
¦   ¦       ¦   ¦   signals.py
¦   ¦       ¦   ¦   test_client.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   __about__.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           config.cpython-38.pyc
¦   ¦       ¦           login_manager.cpython-38.pyc
¦   ¦       ¦           mixins.cpython-38.pyc
¦   ¦       ¦           signals.cpython-38.pyc
¦   ¦       ¦           test_client.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           __about__.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_Login-0.6.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---Flask_Principal-0.4.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_restful
¦   ¦       ¦   ¦   fields.py
¦   ¦       ¦   ¦   inputs.py
¦   ¦       ¦   ¦   reqparse.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __version__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---representations
¦   ¦       ¦   ¦   ¦   json.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           json.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---utils
¦   ¦       ¦   ¦   ¦   cors.py
¦   ¦       ¦   ¦   ¦   crypto.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           cors.cpython-38.pyc
¦   ¦       ¦   ¦           crypto.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           fields.cpython-38.pyc
¦   ¦       ¦           inputs.cpython-38.pyc
¦   ¦       ¦           reqparse.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __version__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_RESTful-0.3.9.dist-info
¦   ¦       ¦       AUTHORS.md
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_restplus
¦   ¦       ¦   ¦   api.py
¦   ¦       ¦   ¦   apidoc.py
¦   ¦       ¦   ¦   cors.py
¦   ¦       ¦   ¦   errors.py
¦   ¦       ¦   ¦   fields.py
¦   ¦       ¦   ¦   inputs.py
¦   ¦       ¦   ¦   marshalling.py
¦   ¦       ¦   ¦   mask.py
¦   ¦       ¦   ¦   model.py
¦   ¦       ¦   ¦   namespace.py
¦   ¦       ¦   ¦   postman.py
¦   ¦       ¦   ¦   representations.py
¦   ¦       ¦   ¦   reqparse.py
¦   ¦       ¦   ¦   resource.py
¦   ¦       ¦   ¦   specs.py
¦   ¦       ¦   ¦   swagger.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   _http.py
¦   ¦       ¦   ¦   __about__.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---schemas
¦   ¦       ¦   ¦   ¦   oas-2.0.json
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---static
¦   ¦       ¦   ¦   ¦   droid-sans.css
¦   ¦       ¦   ¦   ¦   favicon-16x16.png
¦   ¦       ¦   ¦   ¦   favicon-32x32.png
¦   ¦       ¦   ¦   ¦   oauth2-redirect.html
¦   ¦       ¦   ¦   ¦   swagger-ui-bundle.js
¦   ¦       ¦   ¦   ¦   swagger-ui-bundle.js.map
¦   ¦       ¦   ¦   ¦   swagger-ui-standalone-preset.js
¦   ¦       ¦   ¦   ¦   swagger-ui-standalone-preset.js.map
¦   ¦       ¦   ¦   ¦   swagger-ui.css
¦   ¦       ¦   ¦   ¦   swagger-ui.css.map
¦   ¦       ¦   ¦   ¦   swagger-ui.js
¦   ¦       ¦   ¦   ¦   swagger-ui.js.map
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---files
¦   ¦       ¦   ¦           .npmignore
¦   ¦       ¦   ¦           droid-sans-latin-400.woff
¦   ¦       ¦   ¦           droid-sans-latin-400.woff2
¦   ¦       ¦   ¦           droid-sans-latin-700.woff
¦   ¦       ¦   ¦           droid-sans-latin-700.woff2
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---templates
¦   ¦       ¦   ¦       swagger-ui-css.html
¦   ¦       ¦   ¦       swagger-ui-libs.html
¦   ¦       ¦   ¦       swagger-ui.html
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           api.cpython-38.pyc
¦   ¦       ¦           apidoc.cpython-38.pyc
¦   ¦       ¦           cors.cpython-38.pyc
¦   ¦       ¦           errors.cpython-38.pyc
¦   ¦       ¦           fields.cpython-38.pyc
¦   ¦       ¦           inputs.cpython-38.pyc
¦   ¦       ¦           marshalling.cpython-38.pyc
¦   ¦       ¦           mask.cpython-38.pyc
¦   ¦       ¦           model.cpython-38.pyc
¦   ¦       ¦           namespace.cpython-38.pyc
¦   ¦       ¦           postman.cpython-38.pyc
¦   ¦       ¦           representations.cpython-38.pyc
¦   ¦       ¦           reqparse.cpython-38.pyc
¦   ¦       ¦           resource.cpython-38.pyc
¦   ¦       ¦           specs.cpython-38.pyc
¦   ¦       ¦           swagger.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           _http.cpython-38.pyc
¦   ¦       ¦           __about__.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---flask_restplus-0.13.0.dist-info
¦   ¦       ¦       DESCRIPTION.rst
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       METADATA
¦   ¦       ¦       metadata.json
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_security
¦   ¦       ¦   ¦   babel.py
¦   ¦       ¦   ¦   changeable.py
¦   ¦       ¦   ¦   cli.py
¦   ¦       ¦   ¦   confirmable.py
¦   ¦       ¦   ¦   core.py
¦   ¦       ¦   ¦   datastore.py
¦   ¦       ¦   ¦   decorators.py
¦   ¦       ¦   ¦   forms.py
¦   ¦       ¦   ¦   json.py
¦   ¦       ¦   ¦   mail_util.py
¦   ¦       ¦   ¦   oauth_glue.py
¦   ¦       ¦   ¦   passwordless.py
¦   ¦       ¦   ¦   password_util.py
¦   ¦       ¦   ¦   phone_util.py
¦   ¦       ¦   ¦   proxies.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   quart_compat.py
¦   ¦       ¦   ¦   recoverable.py
¦   ¦       ¦   ¦   recovery_codes.py
¦   ¦       ¦   ¦   registerable.py
¦   ¦       ¦   ¦   signals.py
¦   ¦       ¦   ¦   tf_plugin.py
¦   ¦       ¦   ¦   totp.py
¦   ¦       ¦   ¦   twofactor.py
¦   ¦       ¦   ¦   unified_signin.py
¦   ¦       ¦   ¦   username_util.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   views.py
¦   ¦       ¦   ¦   webauthn.py
¦   ¦       ¦   ¦   webauthn_util.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---models
¦   ¦       ¦   ¦   ¦   fsqla.py
¦   ¦       ¦   ¦   ¦   fsqla_v2.py
¦   ¦       ¦   ¦   ¦   fsqla_v3.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           fsqla.cpython-38.pyc
¦   ¦       ¦   ¦           fsqla_v2.cpython-38.pyc
¦   ¦       ¦   ¦           fsqla_v3.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---static
¦   ¦       ¦   ¦   +---js
¦   ¦       ¦   ¦           base64.js
¦   ¦       ¦   ¦           webauthn.js
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---templates
¦   ¦       ¦   ¦   +---security
¦   ¦       ¦   ¦       ¦   base.html
¦   ¦       ¦   ¦       ¦   change_password.html
¦   ¦       ¦   ¦       ¦   forgot_password.html
¦   ¦       ¦   ¦       ¦   login_user.html
¦   ¦       ¦   ¦       ¦   mf_recovery.html
¦   ¦       ¦   ¦       ¦   mf_recovery_codes.html
¦   ¦       ¦   ¦       ¦   register_user.html
¦   ¦       ¦   ¦       ¦   reset_password.html
¦   ¦       ¦   ¦       ¦   send_confirmation.html
¦   ¦       ¦   ¦       ¦   send_login.html
¦   ¦       ¦   ¦       ¦   two_factor_select.html
¦   ¦       ¦   ¦       ¦   two_factor_setup.html
¦   ¦       ¦   ¦       ¦   two_factor_verify_code.html
¦   ¦       ¦   ¦       ¦   us_setup.html
¦   ¦       ¦   ¦       ¦   us_signin.html
¦   ¦       ¦   ¦       ¦   us_verify.html
¦   ¦       ¦   ¦       ¦   verify.html
¦   ¦       ¦   ¦       ¦   wan_register.html
¦   ¦       ¦   ¦       ¦   wan_signin.html
¦   ¦       ¦   ¦       ¦   wan_verify.html
¦   ¦       ¦   ¦       ¦   _macros.html
¦   ¦       ¦   ¦       ¦   _menu.html
¦   ¦       ¦   ¦       ¦   _messages.html
¦   ¦       ¦   ¦       ¦   
¦   ¦       ¦   ¦       +---email
¦   ¦       ¦   ¦               change_notice.html
¦   ¦       ¦   ¦               change_notice.txt
¦   ¦       ¦   ¦               confirmation_instructions.html
¦   ¦       ¦   ¦               confirmation_instructions.txt
¦   ¦       ¦   ¦               login_instructions.html
¦   ¦       ¦   ¦               login_instructions.txt
¦   ¦       ¦   ¦               reset_instructions.html
¦   ¦       ¦   ¦               reset_instructions.txt
¦   ¦       ¦   ¦               reset_notice.html
¦   ¦       ¦   ¦               reset_notice.txt
¦   ¦       ¦   ¦               two_factor_instructions.html
¦   ¦       ¦   ¦               two_factor_instructions.txt
¦   ¦       ¦   ¦               two_factor_rescue.html
¦   ¦       ¦   ¦               two_factor_rescue.txt
¦   ¦       ¦   ¦               us_instructions.html
¦   ¦       ¦   ¦               us_instructions.txt
¦   ¦       ¦   ¦               welcome.html
¦   ¦       ¦   ¦               welcome.txt
¦   ¦       ¦   ¦               welcome_existing.html
¦   ¦       ¦   ¦               welcome_existing.txt
¦   ¦       ¦   ¦               welcome_existing_username.html
¦   ¦       ¦   ¦               welcome_existing_username.txt
¦   ¦       ¦   ¦               
¦   ¦       ¦   +---translations
¦   ¦       ¦   ¦   ¦   flask_security.pot
¦   ¦       ¦   ¦   ¦   pwl.txt
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---af_ZA
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ca_ES
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---da_DK
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---de_DE
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---es_ES
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---eu_ES
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---fr_FR
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---hu_HU
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---hy_AM
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---is_IS
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ja_JP
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---nl_NL
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pl_PL
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pt_BR
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pt_PT
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ru_RU
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tr_TR
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           flask_security.mo
¦   ¦       ¦   ¦   ¦           flask_security.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---zh_Hans_CN
¦   ¦       ¦   ¦       +---LC_MESSAGES
¦   ¦       ¦   ¦               flask_security.mo
¦   ¦       ¦   ¦               flask_security.po
¦   ¦       ¦   ¦               
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           babel.cpython-38.pyc
¦   ¦       ¦           changeable.cpython-38.pyc
¦   ¦       ¦           cli.cpython-38.pyc
¦   ¦       ¦           confirmable.cpython-38.pyc
¦   ¦       ¦           core.cpython-38.pyc
¦   ¦       ¦           datastore.cpython-38.pyc
¦   ¦       ¦           decorators.cpython-38.pyc
¦   ¦       ¦           forms.cpython-38.pyc
¦   ¦       ¦           json.cpython-38.pyc
¦   ¦       ¦           mail_util.cpython-38.pyc
¦   ¦       ¦           oauth_glue.cpython-38.pyc
¦   ¦       ¦           passwordless.cpython-38.pyc
¦   ¦       ¦           password_util.cpython-38.pyc
¦   ¦       ¦           phone_util.cpython-38.pyc
¦   ¦       ¦           proxies.cpython-38.pyc
¦   ¦       ¦           quart_compat.cpython-38.pyc
¦   ¦       ¦           recoverable.cpython-38.pyc
¦   ¦       ¦           recovery_codes.cpython-38.pyc
¦   ¦       ¦           registerable.cpython-38.pyc
¦   ¦       ¦           signals.cpython-38.pyc
¦   ¦       ¦           tf_plugin.cpython-38.pyc
¦   ¦       ¦           totp.cpython-38.pyc
¦   ¦       ¦           twofactor.cpython-38.pyc
¦   ¦       ¦           unified_signin.cpython-38.pyc
¦   ¦       ¦           username_util.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           views.cpython-38.pyc
¦   ¦       ¦           webauthn.cpython-38.pyc
¦   ¦       ¦           webauthn_util.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_Security_Too-5.1.2.dist-info
¦   ¦       ¦       AUTHORS
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---flask_sqlalchemy
¦   ¦       ¦   ¦   cli.py
¦   ¦       ¦   ¦   extension.py
¦   ¦       ¦   ¦   model.py
¦   ¦       ¦   ¦   pagination.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   query.py
¦   ¦       ¦   ¦   record_queries.py
¦   ¦       ¦   ¦   session.py
¦   ¦       ¦   ¦   track_modifications.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           cli.cpython-38.pyc
¦   ¦       ¦           extension.cpython-38.pyc
¦   ¦       ¦           model.cpython-38.pyc
¦   ¦       ¦           pagination.cpython-38.pyc
¦   ¦       ¦           query.cpython-38.pyc
¦   ¦       ¦           record_queries.cpython-38.pyc
¦   ¦       ¦           session.cpython-38.pyc
¦   ¦       ¦           track_modifications.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_SQLAlchemy-3.0.2.dist-info
¦   ¦       ¦   ¦   INSTALLER
¦   ¦       ¦   ¦   METADATA
¦   ¦       ¦   ¦   RECORD
¦   ¦       ¦   ¦   REQUESTED
¦   ¦       ¦   ¦   WHEEL
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---license_files
¦   ¦       ¦           LICENSE.rst
¦   ¦       ¦           
¦   ¦       +---flask_wtf
¦   ¦       ¦   ¦   csrf.py
¦   ¦       ¦   ¦   file.py
¦   ¦       ¦   ¦   form.py
¦   ¦       ¦   ¦   i18n.py
¦   ¦       ¦   ¦   _compat.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---recaptcha
¦   ¦       ¦   ¦   ¦   fields.py
¦   ¦       ¦   ¦   ¦   validators.py
¦   ¦       ¦   ¦   ¦   widgets.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           fields.cpython-38.pyc
¦   ¦       ¦   ¦           validators.cpython-38.pyc
¦   ¦       ¦   ¦           widgets.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           csrf.cpython-38.pyc
¦   ¦       ¦           file.cpython-38.pyc
¦   ¦       ¦           form.cpython-38.pyc
¦   ¦       ¦           i18n.cpython-38.pyc
¦   ¦       ¦           _compat.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Flask_WTF-1.1.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---fontTools
¦   ¦       ¦   ¦   afmLib.py
¦   ¦       ¦   ¦   agl.py
¦   ¦       ¦   ¦   fontBuilder.py
¦   ¦       ¦   ¦   help.py
¦   ¦       ¦   ¦   tfmLib.py
¦   ¦       ¦   ¦   ttx.py
¦   ¦       ¦   ¦   unicode.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---cffLib
¦   ¦       ¦   ¦   ¦   specializer.py
¦   ¦       ¦   ¦   ¦   width.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           specializer.cpython-38.pyc
¦   ¦       ¦   ¦           width.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---colorLib
¦   ¦       ¦   ¦   ¦   builder.py
¦   ¦       ¦   ¦   ¦   errors.py
¦   ¦       ¦   ¦   ¦   geometry.py
¦   ¦       ¦   ¦   ¦   table_builder.py
¦   ¦       ¦   ¦   ¦   unbuilder.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           builder.cpython-38.pyc
¦   ¦       ¦   ¦           errors.cpython-38.pyc
¦   ¦       ¦   ¦           geometry.cpython-38.pyc
¦   ¦       ¦   ¦           table_builder.cpython-38.pyc
¦   ¦       ¦   ¦           unbuilder.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---config
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---cu2qu
¦   ¦       ¦   ¦   ¦   benchmark.py
¦   ¦       ¦   ¦   ¦   cli.py
¦   ¦       ¦   ¦   ¦   cu2qu.py
¦   ¦       ¦   ¦   ¦   errors.py
¦   ¦       ¦   ¦   ¦   ufo.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           benchmark.cpython-38.pyc
¦   ¦       ¦   ¦           cli.cpython-38.pyc
¦   ¦       ¦   ¦           cu2qu.cpython-38.pyc
¦   ¦       ¦   ¦           errors.cpython-38.pyc
¦   ¦       ¦   ¦           ufo.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---designspaceLib
¦   ¦       ¦   ¦   ¦   split.py
¦   ¦       ¦   ¦   ¦   statNames.py
¦   ¦       ¦   ¦   ¦   types.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           split.cpython-38.pyc
¦   ¦       ¦   ¦           statNames.cpython-38.pyc
¦   ¦       ¦   ¦           types.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---encodings
¦   ¦       ¦   ¦   ¦   codecs.py
¦   ¦       ¦   ¦   ¦   MacRoman.py
¦   ¦       ¦   ¦   ¦   StandardEncoding.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           codecs.cpython-38.pyc
¦   ¦       ¦   ¦           MacRoman.cpython-38.pyc
¦   ¦       ¦   ¦           StandardEncoding.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---feaLib
¦   ¦       ¦   ¦   ¦   ast.py
¦   ¦       ¦   ¦   ¦   builder.py
¦   ¦       ¦   ¦   ¦   error.py
¦   ¦       ¦   ¦   ¦   lexer.py
¦   ¦       ¦   ¦   ¦   location.py
¦   ¦       ¦   ¦   ¦   lookupDebugInfo.py
¦   ¦       ¦   ¦   ¦   parser.py
¦   ¦       ¦   ¦   ¦   variableScalar.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           ast.cpython-38.pyc
¦   ¦       ¦   ¦           builder.cpython-38.pyc
¦   ¦       ¦   ¦           error.cpython-38.pyc
¦   ¦       ¦   ¦           lexer.cpython-38.pyc
¦   ¦       ¦   ¦           location.cpython-38.pyc
¦   ¦       ¦   ¦           lookupDebugInfo.cpython-38.pyc
¦   ¦       ¦   ¦           parser.cpython-38.pyc
¦   ¦       ¦   ¦           variableScalar.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---merge
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   cmap.py
¦   ¦       ¦   ¦   ¦   layout.py
¦   ¦       ¦   ¦   ¦   options.py
¦   ¦       ¦   ¦   ¦   tables.py
¦   ¦       ¦   ¦   ¦   unicode.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           cmap.cpython-38.pyc
¦   ¦       ¦   ¦           layout.cpython-38.pyc
¦   ¦       ¦   ¦           options.cpython-38.pyc
¦   ¦       ¦   ¦           tables.cpython-38.pyc
¦   ¦       ¦   ¦           unicode.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---misc
¦   ¦       ¦   ¦   ¦   arrayTools.py
¦   ¦       ¦   ¦   ¦   bezierTools.py
¦   ¦       ¦   ¦   ¦   classifyTools.py
¦   ¦       ¦   ¦   ¦   cliTools.py
¦   ¦       ¦   ¦   ¦   configTools.py
¦   ¦       ¦   ¦   ¦   cython.py
¦   ¦       ¦   ¦   ¦   dictTools.py
¦   ¦       ¦   ¦   ¦   eexec.py
¦   ¦       ¦   ¦   ¦   encodingTools.py
¦   ¦       ¦   ¦   ¦   etree.py
¦   ¦       ¦   ¦   ¦   filenames.py
¦   ¦       ¦   ¦   ¦   fixedTools.py
¦   ¦       ¦   ¦   ¦   intTools.py
¦   ¦       ¦   ¦   ¦   loggingTools.py
¦   ¦       ¦   ¦   ¦   macCreatorType.py
¦   ¦       ¦   ¦   ¦   macRes.py
¦   ¦       ¦   ¦   ¦   psCharStrings.py
¦   ¦       ¦   ¦   ¦   psLib.py
¦   ¦       ¦   ¦   ¦   psOperators.py
¦   ¦       ¦   ¦   ¦   py23.py
¦   ¦       ¦   ¦   ¦   roundTools.py
¦   ¦       ¦   ¦   ¦   sstruct.py
¦   ¦       ¦   ¦   ¦   symfont.py
¦   ¦       ¦   ¦   ¦   testTools.py
¦   ¦       ¦   ¦   ¦   textTools.py
¦   ¦       ¦   ¦   ¦   timeTools.py
¦   ¦       ¦   ¦   ¦   transform.py
¦   ¦       ¦   ¦   ¦   treeTools.py
¦   ¦       ¦   ¦   ¦   vector.py
¦   ¦       ¦   ¦   ¦   visitor.py
¦   ¦       ¦   ¦   ¦   xmlReader.py
¦   ¦       ¦   ¦   ¦   xmlWriter.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---plistlib
¦   ¦       ¦   ¦   ¦   ¦   py.typed
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           arrayTools.cpython-38.pyc
¦   ¦       ¦   ¦           bezierTools.cpython-38.pyc
¦   ¦       ¦   ¦           classifyTools.cpython-38.pyc
¦   ¦       ¦   ¦           cliTools.cpython-38.pyc
¦   ¦       ¦   ¦           configTools.cpython-38.pyc
¦   ¦       ¦   ¦           cython.cpython-38.pyc
¦   ¦       ¦   ¦           dictTools.cpython-38.pyc
¦   ¦       ¦   ¦           eexec.cpython-38.pyc
¦   ¦       ¦   ¦           encodingTools.cpython-38.pyc
¦   ¦       ¦   ¦           etree.cpython-38.pyc
¦   ¦       ¦   ¦           filenames.cpython-38.pyc
¦   ¦       ¦   ¦           fixedTools.cpython-38.pyc
¦   ¦       ¦   ¦           intTools.cpython-38.pyc
¦   ¦       ¦   ¦           loggingTools.cpython-38.pyc
¦   ¦       ¦   ¦           macCreatorType.cpython-38.pyc
¦   ¦       ¦   ¦           macRes.cpython-38.pyc
¦   ¦       ¦   ¦           psCharStrings.cpython-38.pyc
¦   ¦       ¦   ¦           psLib.cpython-38.pyc
¦   ¦       ¦   ¦           psOperators.cpython-38.pyc
¦   ¦       ¦   ¦           py23.cpython-38.pyc
¦   ¦       ¦   ¦           roundTools.cpython-38.pyc
¦   ¦       ¦   ¦           sstruct.cpython-38.pyc
¦   ¦       ¦   ¦           symfont.cpython-38.pyc
¦   ¦       ¦   ¦           testTools.cpython-38.pyc
¦   ¦       ¦   ¦           textTools.cpython-38.pyc
¦   ¦       ¦   ¦           timeTools.cpython-38.pyc
¦   ¦       ¦   ¦           transform.cpython-38.pyc
¦   ¦       ¦   ¦           treeTools.cpython-38.pyc
¦   ¦       ¦   ¦           vector.cpython-38.pyc
¦   ¦       ¦   ¦           visitor.cpython-38.pyc
¦   ¦       ¦   ¦           xmlReader.cpython-38.pyc
¦   ¦       ¦   ¦           xmlWriter.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---mtiLib
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---otlLib
¦   ¦       ¦   ¦   ¦   builder.py
¦   ¦       ¦   ¦   ¦   error.py
¦   ¦       ¦   ¦   ¦   maxContextCalc.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---optimize
¦   ¦       ¦   ¦   ¦   ¦   gpos.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           gpos.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           builder.cpython-38.pyc
¦   ¦       ¦   ¦           error.cpython-38.pyc
¦   ¦       ¦   ¦           maxContextCalc.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---pens
¦   ¦       ¦   ¦   ¦   areaPen.py
¦   ¦       ¦   ¦   ¦   basePen.py
¦   ¦       ¦   ¦   ¦   boundsPen.py
¦   ¦       ¦   ¦   ¦   cairoPen.py
¦   ¦       ¦   ¦   ¦   cocoaPen.py
¦   ¦       ¦   ¦   ¦   cu2quPen.py
¦   ¦       ¦   ¦   ¦   filterPen.py
¦   ¦       ¦   ¦   ¦   freetypePen.py
¦   ¦       ¦   ¦   ¦   hashPointPen.py
¦   ¦       ¦   ¦   ¦   momentsPen.py
¦   ¦       ¦   ¦   ¦   perimeterPen.py
¦   ¦       ¦   ¦   ¦   pointInsidePen.py
¦   ¦       ¦   ¦   ¦   pointPen.py
¦   ¦       ¦   ¦   ¦   qtPen.py
¦   ¦       ¦   ¦   ¦   qu2cuPen.py
¦   ¦       ¦   ¦   ¦   quartzPen.py
¦   ¦       ¦   ¦   ¦   recordingPen.py
¦   ¦       ¦   ¦   ¦   reportLabPen.py
¦   ¦       ¦   ¦   ¦   reverseContourPen.py
¦   ¦       ¦   ¦   ¦   roundingPen.py
¦   ¦       ¦   ¦   ¦   statisticsPen.py
¦   ¦       ¦   ¦   ¦   svgPathPen.py
¦   ¦       ¦   ¦   ¦   t2CharStringPen.py
¦   ¦       ¦   ¦   ¦   teePen.py
¦   ¦       ¦   ¦   ¦   transformPen.py
¦   ¦       ¦   ¦   ¦   ttGlyphPen.py
¦   ¦       ¦   ¦   ¦   wxPen.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           areaPen.cpython-38.pyc
¦   ¦       ¦   ¦           basePen.cpython-38.pyc
¦   ¦       ¦   ¦           boundsPen.cpython-38.pyc
¦   ¦       ¦   ¦           cairoPen.cpython-38.pyc
¦   ¦       ¦   ¦           cocoaPen.cpython-38.pyc
¦   ¦       ¦   ¦           cu2quPen.cpython-38.pyc
¦   ¦       ¦   ¦           filterPen.cpython-38.pyc
¦   ¦       ¦   ¦           freetypePen.cpython-38.pyc
¦   ¦       ¦   ¦           hashPointPen.cpython-38.pyc
¦   ¦       ¦   ¦           momentsPen.cpython-38.pyc
¦   ¦       ¦   ¦           perimeterPen.cpython-38.pyc
¦   ¦       ¦   ¦           pointInsidePen.cpython-38.pyc
¦   ¦       ¦   ¦           pointPen.cpython-38.pyc
¦   ¦       ¦   ¦           qtPen.cpython-38.pyc
¦   ¦       ¦   ¦           qu2cuPen.cpython-38.pyc
¦   ¦       ¦   ¦           quartzPen.cpython-38.pyc
¦   ¦       ¦   ¦           recordingPen.cpython-38.pyc
¦   ¦       ¦   ¦           reportLabPen.cpython-38.pyc
¦   ¦       ¦   ¦           reverseContourPen.cpython-38.pyc
¦   ¦       ¦   ¦           roundingPen.cpython-38.pyc
¦   ¦       ¦   ¦           statisticsPen.cpython-38.pyc
¦   ¦       ¦   ¦           svgPathPen.cpython-38.pyc
¦   ¦       ¦   ¦           t2CharStringPen.cpython-38.pyc
¦   ¦       ¦   ¦           teePen.cpython-38.pyc
¦   ¦       ¦   ¦           transformPen.cpython-38.pyc
¦   ¦       ¦   ¦           ttGlyphPen.cpython-38.pyc
¦   ¦       ¦   ¦           wxPen.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---qu2cu
¦   ¦       ¦   ¦   ¦   benchmark.py
¦   ¦       ¦   ¦   ¦   cli.py
¦   ¦       ¦   ¦   ¦   qu2cu.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           benchmark.cpython-38.pyc
¦   ¦       ¦   ¦           cli.cpython-38.pyc
¦   ¦       ¦   ¦           qu2cu.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---subset
¦   ¦       ¦   ¦   ¦   cff.py
¦   ¦       ¦   ¦   ¦   svg.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           cff.cpython-38.pyc
¦   ¦       ¦   ¦           svg.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---svgLib
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---path
¦   ¦       ¦   ¦   ¦   ¦   arc.py
¦   ¦       ¦   ¦   ¦   ¦   parser.py
¦   ¦       ¦   ¦   ¦   ¦   shapes.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           arc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           shapes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---t1Lib
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---ttLib
¦   ¦       ¦   ¦   ¦   macUtils.py
¦   ¦       ¦   ¦   ¦   removeOverlaps.py
¦   ¦       ¦   ¦   ¦   scaleUpem.py
¦   ¦       ¦   ¦   ¦   sfnt.py
¦   ¦       ¦   ¦   ¦   standardGlyphOrder.py
¦   ¦       ¦   ¦   ¦   ttCollection.py
¦   ¦       ¦   ¦   ¦   ttFont.py
¦   ¦       ¦   ¦   ¦   ttGlyphSet.py
¦   ¦       ¦   ¦   ¦   ttVisitor.py
¦   ¦       ¦   ¦   ¦   woff2.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tables
¦   ¦       ¦   ¦   ¦   ¦   asciiTable.py
¦   ¦       ¦   ¦   ¦   ¦   BitmapGlyphMetrics.py
¦   ¦       ¦   ¦   ¦   ¦   B_A_S_E_.py
¦   ¦       ¦   ¦   ¦   ¦   C_B_D_T_.py
¦   ¦       ¦   ¦   ¦   ¦   C_B_L_C_.py
¦   ¦       ¦   ¦   ¦   ¦   C_F_F_.py
¦   ¦       ¦   ¦   ¦   ¦   C_F_F__2.py
¦   ¦       ¦   ¦   ¦   ¦   C_O_L_R_.py
¦   ¦       ¦   ¦   ¦   ¦   C_P_A_L_.py
¦   ¦       ¦   ¦   ¦   ¦   DefaultTable.py
¦   ¦       ¦   ¦   ¦   ¦   D_S_I_G_.py
¦   ¦       ¦   ¦   ¦   ¦   D__e_b_g.py
¦   ¦       ¦   ¦   ¦   ¦   E_B_D_T_.py
¦   ¦       ¦   ¦   ¦   ¦   E_B_L_C_.py
¦   ¦       ¦   ¦   ¦   ¦   F_F_T_M_.py
¦   ¦       ¦   ¦   ¦   ¦   F__e_a_t.py
¦   ¦       ¦   ¦   ¦   ¦   grUtils.py
¦   ¦       ¦   ¦   ¦   ¦   G_D_E_F_.py
¦   ¦       ¦   ¦   ¦   ¦   G_M_A_P_.py
¦   ¦       ¦   ¦   ¦   ¦   G_P_K_G_.py
¦   ¦       ¦   ¦   ¦   ¦   G_P_O_S_.py
¦   ¦       ¦   ¦   ¦   ¦   G_S_U_B_.py
¦   ¦       ¦   ¦   ¦   ¦   G__l_a_t.py
¦   ¦       ¦   ¦   ¦   ¦   G__l_o_c.py
¦   ¦       ¦   ¦   ¦   ¦   H_V_A_R_.py
¦   ¦       ¦   ¦   ¦   ¦   J_S_T_F_.py
¦   ¦       ¦   ¦   ¦   ¦   L_T_S_H_.py
¦   ¦       ¦   ¦   ¦   ¦   M_A_T_H_.py
¦   ¦       ¦   ¦   ¦   ¦   M_E_T_A_.py
¦   ¦       ¦   ¦   ¦   ¦   M_V_A_R_.py
¦   ¦       ¦   ¦   ¦   ¦   otBase.py
¦   ¦       ¦   ¦   ¦   ¦   otConverters.py
¦   ¦       ¦   ¦   ¦   ¦   otData.py
¦   ¦       ¦   ¦   ¦   ¦   otTables.py
¦   ¦       ¦   ¦   ¦   ¦   otTraverse.py
¦   ¦       ¦   ¦   ¦   ¦   O_S_2f_2.py
¦   ¦       ¦   ¦   ¦   ¦   sbixGlyph.py
¦   ¦       ¦   ¦   ¦   ¦   sbixStrike.py
¦   ¦       ¦   ¦   ¦   ¦   S_I_N_G_.py
¦   ¦       ¦   ¦   ¦   ¦   S_T_A_T_.py
¦   ¦       ¦   ¦   ¦   ¦   S_V_G_.py
¦   ¦       ¦   ¦   ¦   ¦   S__i_l_f.py
¦   ¦       ¦   ¦   ¦   ¦   S__i_l_l.py
¦   ¦       ¦   ¦   ¦   ¦   table_API_readme.txt
¦   ¦       ¦   ¦   ¦   ¦   ttProgram.py
¦   ¦       ¦   ¦   ¦   ¦   TupleVariation.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_B_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_C_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_D_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_J_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_P_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_S_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I_V_.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I__0.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I__1.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I__2.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I__3.py
¦   ¦       ¦   ¦   ¦   ¦   T_S_I__5.py
¦   ¦       ¦   ¦   ¦   ¦   T_T_F_A_.py
¦   ¦       ¦   ¦   ¦   ¦   V_D_M_X_.py
¦   ¦       ¦   ¦   ¦   ¦   V_O_R_G_.py
¦   ¦       ¦   ¦   ¦   ¦   V_V_A_R_.py
¦   ¦       ¦   ¦   ¦   ¦   _a_n_k_r.py
¦   ¦       ¦   ¦   ¦   ¦   _a_v_a_r.py
¦   ¦       ¦   ¦   ¦   ¦   _b_s_l_n.py
¦   ¦       ¦   ¦   ¦   ¦   _c_i_d_g.py
¦   ¦       ¦   ¦   ¦   ¦   _c_m_a_p.py
¦   ¦       ¦   ¦   ¦   ¦   _c_v_a_r.py
¦   ¦       ¦   ¦   ¦   ¦   _c_v_t.py
¦   ¦       ¦   ¦   ¦   ¦   _f_e_a_t.py
¦   ¦       ¦   ¦   ¦   ¦   _f_p_g_m.py
¦   ¦       ¦   ¦   ¦   ¦   _f_v_a_r.py
¦   ¦       ¦   ¦   ¦   ¦   _g_a_s_p.py
¦   ¦       ¦   ¦   ¦   ¦   _g_c_i_d.py
¦   ¦       ¦   ¦   ¦   ¦   _g_l_y_f.py
¦   ¦       ¦   ¦   ¦   ¦   _g_v_a_r.py
¦   ¦       ¦   ¦   ¦   ¦   _h_d_m_x.py
¦   ¦       ¦   ¦   ¦   ¦   _h_e_a_d.py
¦   ¦       ¦   ¦   ¦   ¦   _h_h_e_a.py
¦   ¦       ¦   ¦   ¦   ¦   _h_m_t_x.py
¦   ¦       ¦   ¦   ¦   ¦   _k_e_r_n.py
¦   ¦       ¦   ¦   ¦   ¦   _l_c_a_r.py
¦   ¦       ¦   ¦   ¦   ¦   _l_o_c_a.py
¦   ¦       ¦   ¦   ¦   ¦   _l_t_a_g.py
¦   ¦       ¦   ¦   ¦   ¦   _m_a_x_p.py
¦   ¦       ¦   ¦   ¦   ¦   _m_e_t_a.py
¦   ¦       ¦   ¦   ¦   ¦   _m_o_r_t.py
¦   ¦       ¦   ¦   ¦   ¦   _m_o_r_x.py
¦   ¦       ¦   ¦   ¦   ¦   _n_a_m_e.py
¦   ¦       ¦   ¦   ¦   ¦   _o_p_b_d.py
¦   ¦       ¦   ¦   ¦   ¦   _p_o_s_t.py
¦   ¦       ¦   ¦   ¦   ¦   _p_r_e_p.py
¦   ¦       ¦   ¦   ¦   ¦   _p_r_o_p.py
¦   ¦       ¦   ¦   ¦   ¦   _s_b_i_x.py
¦   ¦       ¦   ¦   ¦   ¦   _t_r_a_k.py
¦   ¦       ¦   ¦   ¦   ¦   _v_h_e_a.py
¦   ¦       ¦   ¦   ¦   ¦   _v_m_t_x.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           asciiTable.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           BitmapGlyphMetrics.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           B_A_S_E_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           C_B_D_T_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           C_B_L_C_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           C_F_F_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           C_F_F__2.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           C_O_L_R_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           C_P_A_L_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           DefaultTable.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           D_S_I_G_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           D__e_b_g.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           E_B_D_T_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           E_B_L_C_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           F_F_T_M_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           F__e_a_t.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           grUtils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G_D_E_F_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G_M_A_P_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G_P_K_G_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G_P_O_S_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G_S_U_B_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G__l_a_t.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           G__l_o_c.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           H_V_A_R_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           J_S_T_F_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           L_T_S_H_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           M_A_T_H_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           M_E_T_A_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           M_V_A_R_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           otBase.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           otConverters.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           otData.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           otTables.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           otTraverse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           O_S_2f_2.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sbixGlyph.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sbixStrike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           S_I_N_G_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           S_T_A_T_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           S_V_G_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           S__i_l_f.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           S__i_l_l.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ttProgram.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           TupleVariation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_B_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_C_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_D_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_J_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_P_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_S_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I_V_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I__0.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I__1.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I__2.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I__3.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_S_I__5.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           T_T_F_A_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           V_D_M_X_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           V_O_R_G_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           V_V_A_R_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _a_n_k_r.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _a_v_a_r.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _b_s_l_n.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _c_i_d_g.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _c_m_a_p.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _c_v_a_r.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _c_v_t.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _f_e_a_t.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _f_p_g_m.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _f_v_a_r.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _g_a_s_p.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _g_c_i_d.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _g_l_y_f.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _g_v_a_r.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _h_d_m_x.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _h_e_a_d.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _h_h_e_a.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _h_m_t_x.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _k_e_r_n.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _l_c_a_r.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _l_o_c_a.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _l_t_a_g.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _m_a_x_p.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _m_e_t_a.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _m_o_r_t.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _m_o_r_x.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _n_a_m_e.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _o_p_b_d.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _p_o_s_t.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _p_r_e_p.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _p_r_o_p.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _s_b_i_x.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _t_r_a_k.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _v_h_e_a.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _v_m_t_x.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           macUtils.cpython-38.pyc
¦   ¦       ¦   ¦           removeOverlaps.cpython-38.pyc
¦   ¦       ¦   ¦           scaleUpem.cpython-38.pyc
¦   ¦       ¦   ¦           sfnt.cpython-38.pyc
¦   ¦       ¦   ¦           standardGlyphOrder.cpython-38.pyc
¦   ¦       ¦   ¦           ttCollection.cpython-38.pyc
¦   ¦       ¦   ¦           ttFont.cpython-38.pyc
¦   ¦       ¦   ¦           ttGlyphSet.cpython-38.pyc
¦   ¦       ¦   ¦           ttVisitor.cpython-38.pyc
¦   ¦       ¦   ¦           woff2.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---ufoLib
¦   ¦       ¦   ¦   ¦   converters.py
¦   ¦       ¦   ¦   ¦   errors.py
¦   ¦       ¦   ¦   ¦   etree.py
¦   ¦       ¦   ¦   ¦   filenames.py
¦   ¦       ¦   ¦   ¦   glifLib.py
¦   ¦       ¦   ¦   ¦   kerning.py
¦   ¦       ¦   ¦   ¦   plistlib.py
¦   ¦       ¦   ¦   ¦   pointPen.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   validators.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           converters.cpython-38.pyc
¦   ¦       ¦   ¦           errors.cpython-38.pyc
¦   ¦       ¦   ¦           etree.cpython-38.pyc
¦   ¦       ¦   ¦           filenames.cpython-38.pyc
¦   ¦       ¦   ¦           glifLib.cpython-38.pyc
¦   ¦       ¦   ¦           kerning.cpython-38.pyc
¦   ¦       ¦   ¦           plistlib.cpython-38.pyc
¦   ¦       ¦   ¦           pointPen.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           validators.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---unicodedata
¦   ¦       ¦   ¦   ¦   Blocks.py
¦   ¦       ¦   ¦   ¦   OTTags.py
¦   ¦       ¦   ¦   ¦   ScriptExtensions.py
¦   ¦       ¦   ¦   ¦   Scripts.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           Blocks.cpython-38.pyc
¦   ¦       ¦   ¦           OTTags.cpython-38.pyc
¦   ¦       ¦   ¦           ScriptExtensions.cpython-38.pyc
¦   ¦       ¦   ¦           Scripts.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---varLib
¦   ¦       ¦   ¦   ¦   builder.py
¦   ¦       ¦   ¦   ¦   cff.py
¦   ¦       ¦   ¦   ¦   errors.py
¦   ¦       ¦   ¦   ¦   featureVars.py
¦   ¦       ¦   ¦   ¦   interpolatable.py
¦   ¦       ¦   ¦   ¦   interpolate_layout.py
¦   ¦       ¦   ¦   ¦   iup.py
¦   ¦       ¦   ¦   ¦   merger.py
¦   ¦       ¦   ¦   ¦   models.py
¦   ¦       ¦   ¦   ¦   mutator.py
¦   ¦       ¦   ¦   ¦   mvar.py
¦   ¦       ¦   ¦   ¦   plot.py
¦   ¦       ¦   ¦   ¦   stat.py
¦   ¦       ¦   ¦   ¦   varStore.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---instancer
¦   ¦       ¦   ¦   ¦   ¦   featureVars.py
¦   ¦       ¦   ¦   ¦   ¦   names.py
¦   ¦       ¦   ¦   ¦   ¦   solver.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           featureVars.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           names.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           solver.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           builder.cpython-38.pyc
¦   ¦       ¦   ¦           cff.cpython-38.pyc
¦   ¦       ¦   ¦           errors.cpython-38.pyc
¦   ¦       ¦   ¦           featureVars.cpython-38.pyc
¦   ¦       ¦   ¦           interpolatable.cpython-38.pyc
¦   ¦       ¦   ¦           interpolate_layout.cpython-38.pyc
¦   ¦       ¦   ¦           iup.cpython-38.pyc
¦   ¦       ¦   ¦           merger.cpython-38.pyc
¦   ¦       ¦   ¦           models.cpython-38.pyc
¦   ¦       ¦   ¦           mutator.cpython-38.pyc
¦   ¦       ¦   ¦           mvar.cpython-38.pyc
¦   ¦       ¦   ¦           plot.cpython-38.pyc
¦   ¦       ¦   ¦           stat.cpython-38.pyc
¦   ¦       ¦   ¦           varStore.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---voltLib
¦   ¦       ¦   ¦   ¦   ast.py
¦   ¦       ¦   ¦   ¦   error.py
¦   ¦       ¦   ¦   ¦   lexer.py
¦   ¦       ¦   ¦   ¦   parser.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           ast.cpython-38.pyc
¦   ¦       ¦   ¦           error.cpython-38.pyc
¦   ¦       ¦   ¦           lexer.cpython-38.pyc
¦   ¦       ¦   ¦           parser.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           afmLib.cpython-38.pyc
¦   ¦       ¦           agl.cpython-38.pyc
¦   ¦       ¦           fontBuilder.cpython-38.pyc
¦   ¦       ¦           help.cpython-38.pyc
¦   ¦       ¦           tfmLib.cpython-38.pyc
¦   ¦       ¦           ttx.cpython-38.pyc
¦   ¦       ¦           unicode.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---fonttools-4.39.3.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---greenlet
¦   ¦       ¦   ¦   greenlet.cpp
¦   ¦       ¦   ¦   greenlet.h
¦   ¦       ¦   ¦   greenlet_allocator.hpp
¦   ¦       ¦   ¦   greenlet_compiler_compat.hpp
¦   ¦       ¦   ¦   greenlet_cpython_compat.hpp
¦   ¦       ¦   ¦   greenlet_exceptions.hpp
¦   ¦       ¦   ¦   greenlet_greenlet.hpp
¦   ¦       ¦   ¦   greenlet_internal.hpp
¦   ¦       ¦   ¦   greenlet_refs.hpp
¦   ¦       ¦   ¦   greenlet_slp_switch.hpp
¦   ¦       ¦   ¦   greenlet_thread_state.hpp
¦   ¦       ¦   ¦   greenlet_thread_state_dict_cleanup.hpp
¦   ¦       ¦   ¦   greenlet_thread_support.hpp
¦   ¦       ¦   ¦   slp_platformselect.h
¦   ¦       ¦   ¦   _greenlet.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---platform
¦   ¦       ¦   ¦   ¦   setup_switch_x64_masm.cmd
¦   ¦       ¦   ¦   ¦   switch_aarch64_gcc.h
¦   ¦       ¦   ¦   ¦   switch_alpha_unix.h
¦   ¦       ¦   ¦   ¦   switch_amd64_unix.h
¦   ¦       ¦   ¦   ¦   switch_arm32_gcc.h
¦   ¦       ¦   ¦   ¦   switch_arm32_ios.h
¦   ¦       ¦   ¦   ¦   switch_arm64_masm.asm
¦   ¦       ¦   ¦   ¦   switch_arm64_masm.obj
¦   ¦       ¦   ¦   ¦   switch_arm64_msvc.h
¦   ¦       ¦   ¦   ¦   switch_csky_gcc.h
¦   ¦       ¦   ¦   ¦   switch_m68k_gcc.h
¦   ¦       ¦   ¦   ¦   switch_mips_unix.h
¦   ¦       ¦   ¦   ¦   switch_ppc64_aix.h
¦   ¦       ¦   ¦   ¦   switch_ppc64_linux.h
¦   ¦       ¦   ¦   ¦   switch_ppc_aix.h
¦   ¦       ¦   ¦   ¦   switch_ppc_linux.h
¦   ¦       ¦   ¦   ¦   switch_ppc_macosx.h
¦   ¦       ¦   ¦   ¦   switch_ppc_unix.h
¦   ¦       ¦   ¦   ¦   switch_riscv_unix.h
¦   ¦       ¦   ¦   ¦   switch_s390_unix.h
¦   ¦       ¦   ¦   ¦   switch_sparc_sun_gcc.h
¦   ¦       ¦   ¦   ¦   switch_x32_unix.h
¦   ¦       ¦   ¦   ¦   switch_x64_masm.asm
¦   ¦       ¦   ¦   ¦   switch_x64_masm.obj
¦   ¦       ¦   ¦   ¦   switch_x64_msvc.h
¦   ¦       ¦   ¦   ¦   switch_x86_msvc.h
¦   ¦       ¦   ¦   ¦   switch_x86_unix.h
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   leakcheck.py
¦   ¦       ¦   ¦   ¦   test_contextvars.py
¦   ¦       ¦   ¦   ¦   test_cpp.py
¦   ¦       ¦   ¦   ¦   test_extension_interface.py
¦   ¦       ¦   ¦   ¦   test_gc.py
¦   ¦       ¦   ¦   ¦   test_generator.py
¦   ¦       ¦   ¦   ¦   test_generator_nested.py
¦   ¦       ¦   ¦   ¦   test_greenlet.py
¦   ¦       ¦   ¦   ¦   test_greenlet_trash.py
¦   ¦       ¦   ¦   ¦   test_leaks.py
¦   ¦       ¦   ¦   ¦   test_stack_saved.py
¦   ¦       ¦   ¦   ¦   test_throw.py
¦   ¦       ¦   ¦   ¦   test_tracing.py
¦   ¦       ¦   ¦   ¦   test_version.py
¦   ¦       ¦   ¦   ¦   test_weakref.py
¦   ¦       ¦   ¦   ¦   _test_extension.c
¦   ¦       ¦   ¦   ¦   _test_extension.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _test_extension_cpp.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _test_extension_cpp.cpp
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           leakcheck.cpython-38.pyc
¦   ¦       ¦   ¦           test_contextvars.cpython-38.pyc
¦   ¦       ¦   ¦           test_cpp.cpython-38.pyc
¦   ¦       ¦   ¦           test_extension_interface.cpython-38.pyc
¦   ¦       ¦   ¦           test_gc.cpython-38.pyc
¦   ¦       ¦   ¦           test_generator.cpython-38.pyc
¦   ¦       ¦   ¦           test_generator_nested.cpython-38.pyc
¦   ¦       ¦   ¦           test_greenlet.cpython-38.pyc
¦   ¦       ¦   ¦           test_greenlet_trash.cpython-38.pyc
¦   ¦       ¦   ¦           test_leaks.cpython-38.pyc
¦   ¦       ¦   ¦           test_stack_saved.cpython-38.pyc
¦   ¦       ¦   ¦           test_throw.cpython-38.pyc
¦   ¦       ¦   ¦           test_tracing.cpython-38.pyc
¦   ¦       ¦   ¦           test_version.cpython-38.pyc
¦   ¦       ¦   ¦           test_weakref.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---greenlet-2.0.1.dist-info
¦   ¦       ¦       AUTHORS
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       LICENSE.PSF
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---html5lib
¦   ¦       ¦   ¦   constants.py
¦   ¦       ¦   ¦   html5parser.py
¦   ¦       ¦   ¦   serializer.py
¦   ¦       ¦   ¦   _ihatexml.py
¦   ¦       ¦   ¦   _inputstream.py
¦   ¦       ¦   ¦   _tokenizer.py
¦   ¦       ¦   ¦   _utils.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---filters
¦   ¦       ¦   ¦   ¦   alphabeticalattributes.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   inject_meta_charset.py
¦   ¦       ¦   ¦   ¦   lint.py
¦   ¦       ¦   ¦   ¦   optionaltags.py
¦   ¦       ¦   ¦   ¦   sanitizer.py
¦   ¦       ¦   ¦   ¦   whitespace.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           alphabeticalattributes.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           inject_meta_charset.cpython-38.pyc
¦   ¦       ¦   ¦           lint.cpython-38.pyc
¦   ¦       ¦   ¦           optionaltags.cpython-38.pyc
¦   ¦       ¦   ¦           sanitizer.cpython-38.pyc
¦   ¦       ¦   ¦           whitespace.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---treeadapters
¦   ¦       ¦   ¦   ¦   genshi.py
¦   ¦       ¦   ¦   ¦   sax.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           genshi.cpython-38.pyc
¦   ¦       ¦   ¦           sax.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---treebuilders
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   dom.py
¦   ¦       ¦   ¦   ¦   etree.py
¦   ¦       ¦   ¦   ¦   etree_lxml.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           dom.cpython-38.pyc
¦   ¦       ¦   ¦           etree.cpython-38.pyc
¦   ¦       ¦   ¦           etree_lxml.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---treewalkers
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   dom.py
¦   ¦       ¦   ¦   ¦   etree.py
¦   ¦       ¦   ¦   ¦   etree_lxml.py
¦   ¦       ¦   ¦   ¦   genshi.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           dom.cpython-38.pyc
¦   ¦       ¦   ¦           etree.cpython-38.pyc
¦   ¦       ¦   ¦           etree_lxml.cpython-38.pyc
¦   ¦       ¦   ¦           genshi.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_trie
¦   ¦       ¦   ¦   ¦   py.py
¦   ¦       ¦   ¦   ¦   _base.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           py.cpython-38.pyc
¦   ¦       ¦   ¦           _base.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           constants.cpython-38.pyc
¦   ¦       ¦           html5parser.cpython-38.pyc
¦   ¦       ¦           serializer.cpython-38.pyc
¦   ¦       ¦           _ihatexml.cpython-38.pyc
¦   ¦       ¦           _inputstream.cpython-38.pyc
¦   ¦       ¦           _tokenizer.cpython-38.pyc
¦   ¦       ¦           _utils.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---html5lib-1.1.dist-info
¦   ¦       ¦       AUTHORS.rst
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---idna
¦   ¦       ¦   ¦   codec.py
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   core.py
¦   ¦       ¦   ¦   idnadata.py
¦   ¦       ¦   ¦   intranges.py
¦   ¦       ¦   ¦   package_data.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   uts46data.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           codec.cpython-38.pyc
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           core.cpython-38.pyc
¦   ¦       ¦           idnadata.cpython-38.pyc
¦   ¦       ¦           intranges.cpython-38.pyc
¦   ¦       ¦           package_data.cpython-38.pyc
¦   ¦       ¦           uts46data.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---idna-3.4.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.md
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---imageio
¦   ¦       ¦   ¦   freeze.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   testing.py
¦   ¦       ¦   ¦   typing.py
¦   ¦       ¦   ¦   v2.py
¦   ¦       ¦   ¦   v2.pyi
¦   ¦       ¦   ¦   v3.py
¦   ¦       ¦   ¦   v3.pyi
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---config
¦   ¦       ¦   ¦   ¦   extensions.py
¦   ¦       ¦   ¦   ¦   extensions.pyi
¦   ¦       ¦   ¦   ¦   plugins.py
¦   ¦       ¦   ¦   ¦   plugins.pyi
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           extensions.cpython-38.pyc
¦   ¦       ¦   ¦           plugins.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---core
¦   ¦       ¦   ¦   ¦   fetching.py
¦   ¦       ¦   ¦   ¦   findlib.py
¦   ¦       ¦   ¦   ¦   format.py
¦   ¦       ¦   ¦   ¦   format.pyi
¦   ¦       ¦   ¦   ¦   imopen.py
¦   ¦       ¦   ¦   ¦   imopen.pyi
¦   ¦       ¦   ¦   ¦   legacy_plugin_wrapper.py
¦   ¦       ¦   ¦   ¦   legacy_plugin_wrapper.pyi
¦   ¦       ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   request.pyi
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   v3_plugin_api.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           fetching.cpython-38.pyc
¦   ¦       ¦   ¦           findlib.cpython-38.pyc
¦   ¦       ¦   ¦           format.cpython-38.pyc
¦   ¦       ¦   ¦           imopen.cpython-38.pyc
¦   ¦       ¦   ¦           legacy_plugin_wrapper.cpython-38.pyc
¦   ¦       ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           v3_plugin_api.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---plugins
¦   ¦       ¦   ¦   ¦   bsdf.py
¦   ¦       ¦   ¦   ¦   dicom.py
¦   ¦       ¦   ¦   ¦   example.py
¦   ¦       ¦   ¦   ¦   feisem.py
¦   ¦       ¦   ¦   ¦   ffmpeg.py
¦   ¦       ¦   ¦   ¦   fits.py
¦   ¦       ¦   ¦   ¦   freeimage.py
¦   ¦       ¦   ¦   ¦   freeimagemulti.py
¦   ¦       ¦   ¦   ¦   gdal.py
¦   ¦       ¦   ¦   ¦   grab.py
¦   ¦       ¦   ¦   ¦   lytro.py
¦   ¦       ¦   ¦   ¦   npz.py
¦   ¦       ¦   ¦   ¦   opencv.py
¦   ¦       ¦   ¦   ¦   pillow.py
¦   ¦       ¦   ¦   ¦   pillowmulti.py
¦   ¦       ¦   ¦   ¦   pillow_info.py
¦   ¦       ¦   ¦   ¦   pillow_legacy.py
¦   ¦       ¦   ¦   ¦   pyav.py
¦   ¦       ¦   ¦   ¦   simpleitk.py
¦   ¦       ¦   ¦   ¦   spe.py
¦   ¦       ¦   ¦   ¦   swf.py
¦   ¦       ¦   ¦   ¦   tifffile.py
¦   ¦       ¦   ¦   ¦   tifffile_v3.py
¦   ¦       ¦   ¦   ¦   _bsdf.py
¦   ¦       ¦   ¦   ¦   _dicom.py
¦   ¦       ¦   ¦   ¦   _freeimage.py
¦   ¦       ¦   ¦   ¦   _swf.py
¦   ¦       ¦   ¦   ¦   _tifffile.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           bsdf.cpython-38.pyc
¦   ¦       ¦   ¦           dicom.cpython-38.pyc
¦   ¦       ¦   ¦           example.cpython-38.pyc
¦   ¦       ¦   ¦           feisem.cpython-38.pyc
¦   ¦       ¦   ¦           ffmpeg.cpython-38.pyc
¦   ¦       ¦   ¦           fits.cpython-38.pyc
¦   ¦       ¦   ¦           freeimage.cpython-38.pyc
¦   ¦       ¦   ¦           freeimagemulti.cpython-38.pyc
¦   ¦       ¦   ¦           gdal.cpython-38.pyc
¦   ¦       ¦   ¦           grab.cpython-38.pyc
¦   ¦       ¦   ¦           lytro.cpython-38.pyc
¦   ¦       ¦   ¦           npz.cpython-38.pyc
¦   ¦       ¦   ¦           opencv.cpython-38.pyc
¦   ¦       ¦   ¦           pillow.cpython-38.pyc
¦   ¦       ¦   ¦           pillowmulti.cpython-38.pyc
¦   ¦       ¦   ¦           pillow_info.cpython-38.pyc
¦   ¦       ¦   ¦           pillow_legacy.cpython-38.pyc
¦   ¦       ¦   ¦           pyav.cpython-38.pyc
¦   ¦       ¦   ¦           simpleitk.cpython-38.pyc
¦   ¦       ¦   ¦           spe.cpython-38.pyc
¦   ¦       ¦   ¦           swf.cpython-38.pyc
¦   ¦       ¦   ¦           tifffile.cpython-38.pyc
¦   ¦       ¦   ¦           tifffile_v3.cpython-38.pyc
¦   ¦       ¦   ¦           _bsdf.cpython-38.pyc
¦   ¦       ¦   ¦           _dicom.cpython-38.pyc
¦   ¦       ¦   ¦           _freeimage.cpython-38.pyc
¦   ¦       ¦   ¦           _swf.cpython-38.pyc
¦   ¦       ¦   ¦           _tifffile.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---resources
¦   ¦       ¦   ¦   ¦   shipped_resources_go_here
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---images
¦   ¦       ¦   ¦           astronaut.png
¦   ¦       ¦   ¦           chelsea.png
¦   ¦       ¦   ¦           chelsea.zip
¦   ¦       ¦   ¦           cockatoo.mp4
¦   ¦       ¦   ¦           newtonscradle.gif
¦   ¦       ¦   ¦           realshort.mp4
¦   ¦       ¦   ¦           stent.npz
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           freeze.cpython-38.pyc
¦   ¦       ¦           testing.cpython-38.pyc
¦   ¦       ¦           typing.cpython-38.pyc
¦   ¦       ¦           v2.cpython-38.pyc
¦   ¦       ¦           v3.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---imageio-2.24.0.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---importlib_metadata
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   _adapters.py
¦   ¦       ¦   ¦   _collections.py
¦   ¦       ¦   ¦   _compat.py
¦   ¦       ¦   ¦   _functools.py
¦   ¦       ¦   ¦   _itertools.py
¦   ¦       ¦   ¦   _meta.py
¦   ¦       ¦   ¦   _py39compat.py
¦   ¦       ¦   ¦   _text.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           _adapters.cpython-38.pyc
¦   ¦       ¦           _collections.cpython-38.pyc
¦   ¦       ¦           _compat.cpython-38.pyc
¦   ¦       ¦           _functools.cpython-38.pyc
¦   ¦       ¦           _itertools.cpython-38.pyc
¦   ¦       ¦           _meta.cpython-38.pyc
¦   ¦       ¦           _py39compat.cpython-38.pyc
¦   ¦       ¦           _text.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---importlib_metadata-5.1.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---importlib_resources
¦   ¦       ¦   ¦   abc.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   readers.py
¦   ¦       ¦   ¦   simple.py
¦   ¦       ¦   ¦   _adapters.py
¦   ¦       ¦   ¦   _common.py
¦   ¦       ¦   ¦   _compat.py
¦   ¦       ¦   ¦   _itertools.py
¦   ¦       ¦   ¦   _legacy.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   test_compatibilty_files.py
¦   ¦       ¦   ¦   ¦   test_contents.py
¦   ¦       ¦   ¦   ¦   test_custom.py
¦   ¦       ¦   ¦   ¦   test_files.py
¦   ¦       ¦   ¦   ¦   test_open.py
¦   ¦       ¦   ¦   ¦   test_path.py
¦   ¦       ¦   ¦   ¦   test_read.py
¦   ¦       ¦   ¦   ¦   test_reader.py
¦   ¦       ¦   ¦   ¦   test_resource.py
¦   ¦       ¦   ¦   ¦   update-zips.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   _compat.py
¦   ¦       ¦   ¦   ¦   _path.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---data01
¦   ¦       ¦   ¦   ¦   ¦   binary.file
¦   ¦       ¦   ¦   ¦   ¦   utf-16.file
¦   ¦       ¦   ¦   ¦   ¦   utf-8.file
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---subdirectory
¦   ¦       ¦   ¦   ¦   ¦   ¦   binary.file
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---data02
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---one
¦   ¦       ¦   ¦   ¦   ¦   ¦   resource1.txt
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---subdirectory
¦   ¦       ¦   ¦   ¦   ¦   +---subsubdir
¦   ¦       ¦   ¦   ¦   ¦           resource.txt
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---two
¦   ¦       ¦   ¦   ¦   ¦   ¦   resource2.txt
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---namespacedata01
¦   ¦       ¦   ¦   ¦       binary.file
¦   ¦       ¦   ¦   ¦       utf-16.file
¦   ¦       ¦   ¦   ¦       utf-8.file
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---zipdata01
¦   ¦       ¦   ¦   ¦   ¦   ziptestdata.zip
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---zipdata02
¦   ¦       ¦   ¦   ¦   ¦   ziptestdata.zip
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           test_compatibilty_files.cpython-38.pyc
¦   ¦       ¦   ¦           test_contents.cpython-38.pyc
¦   ¦       ¦   ¦           test_custom.cpython-38.pyc
¦   ¦       ¦   ¦           test_files.cpython-38.pyc
¦   ¦       ¦   ¦           test_open.cpython-38.pyc
¦   ¦       ¦   ¦           test_path.cpython-38.pyc
¦   ¦       ¦   ¦           test_read.cpython-38.pyc
¦   ¦       ¦   ¦           test_reader.cpython-38.pyc
¦   ¦       ¦   ¦           test_resource.cpython-38.pyc
¦   ¦       ¦   ¦           update-zips.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           _compat.cpython-38.pyc
¦   ¦       ¦   ¦           _path.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           abc.cpython-38.pyc
¦   ¦       ¦           readers.cpython-38.pyc
¦   ¦       ¦           simple.cpython-38.pyc
¦   ¦       ¦           _adapters.cpython-38.pyc
¦   ¦       ¦           _common.cpython-38.pyc
¦   ¦       ¦           _compat.cpython-38.pyc
¦   ¦       ¦           _itertools.cpython-38.pyc
¦   ¦       ¦           _legacy.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---importlib_resources-5.12.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---itsdangerous
¦   ¦       ¦   ¦   encoding.py
¦   ¦       ¦   ¦   exc.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   serializer.py
¦   ¦       ¦   ¦   signer.py
¦   ¦       ¦   ¦   timed.py
¦   ¦       ¦   ¦   url_safe.py
¦   ¦       ¦   ¦   _json.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           encoding.cpython-38.pyc
¦   ¦       ¦           exc.cpython-38.pyc
¦   ¦       ¦           serializer.cpython-38.pyc
¦   ¦       ¦           signer.cpython-38.pyc
¦   ¦       ¦           timed.cpython-38.pyc
¦   ¦       ¦           url_safe.cpython-38.pyc
¦   ¦       ¦           _json.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---itsdangerous-2.1.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---jinja2
¦   ¦       ¦   ¦   async_utils.py
¦   ¦       ¦   ¦   bccache.py
¦   ¦       ¦   ¦   compiler.py
¦   ¦       ¦   ¦   constants.py
¦   ¦       ¦   ¦   debug.py
¦   ¦       ¦   ¦   defaults.py
¦   ¦       ¦   ¦   environment.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ext.py
¦   ¦       ¦   ¦   filters.py
¦   ¦       ¦   ¦   idtracking.py
¦   ¦       ¦   ¦   lexer.py
¦   ¦       ¦   ¦   loaders.py
¦   ¦       ¦   ¦   meta.py
¦   ¦       ¦   ¦   nativetypes.py
¦   ¦       ¦   ¦   nodes.py
¦   ¦       ¦   ¦   optimizer.py
¦   ¦       ¦   ¦   parser.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   runtime.py
¦   ¦       ¦   ¦   sandbox.py
¦   ¦       ¦   ¦   tests.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   visitor.py
¦   ¦       ¦   ¦   _identifier.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           async_utils.cpython-38.pyc
¦   ¦       ¦           bccache.cpython-38.pyc
¦   ¦       ¦           compiler.cpython-38.pyc
¦   ¦       ¦           constants.cpython-38.pyc
¦   ¦       ¦           debug.cpython-38.pyc
¦   ¦       ¦           defaults.cpython-38.pyc
¦   ¦       ¦           environment.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           ext.cpython-38.pyc
¦   ¦       ¦           filters.cpython-38.pyc
¦   ¦       ¦           idtracking.cpython-38.pyc
¦   ¦       ¦           lexer.cpython-38.pyc
¦   ¦       ¦           loaders.cpython-38.pyc
¦   ¦       ¦           meta.cpython-38.pyc
¦   ¦       ¦           nativetypes.cpython-38.pyc
¦   ¦       ¦           nodes.cpython-38.pyc
¦   ¦       ¦           optimizer.cpython-38.pyc
¦   ¦       ¦           parser.cpython-38.pyc
¦   ¦       ¦           runtime.cpython-38.pyc
¦   ¦       ¦           sandbox.cpython-38.pyc
¦   ¦       ¦           tests.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           visitor.cpython-38.pyc
¦   ¦       ¦           _identifier.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Jinja2-3.1.2.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---jsonschema
¦   ¦       ¦   ¦   cli.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   protocols.py
¦   ¦       ¦   ¦   validators.py
¦   ¦       ¦   ¦   _format.py
¦   ¦       ¦   ¦   _legacy_validators.py
¦   ¦       ¦   ¦   _types.py
¦   ¦       ¦   ¦   _utils.py
¦   ¦       ¦   ¦   _validators.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---benchmarks
¦   ¦       ¦   ¦   ¦   issue232.py
¦   ¦       ¦   ¦   ¦   json_schema_test_suite.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---issue232
¦   ¦       ¦   ¦   ¦       issue.json
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           issue232.cpython-38.pyc
¦   ¦       ¦   ¦           json_schema_test_suite.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---schemas
¦   ¦       ¦   ¦   ¦   draft2019-09.json
¦   ¦       ¦   ¦   ¦   draft2020-12.json
¦   ¦       ¦   ¦   ¦   draft3.json
¦   ¦       ¦   ¦   ¦   draft4.json
¦   ¦       ¦   ¦   ¦   draft6.json
¦   ¦       ¦   ¦   ¦   draft7.json
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---vocabularies
¦   ¦       ¦   ¦       +---draft2019-09
¦   ¦       ¦   ¦       ¦       applicator
¦   ¦       ¦   ¦       ¦       content
¦   ¦       ¦   ¦       ¦       core
¦   ¦       ¦   ¦       ¦       meta-data
¦   ¦       ¦   ¦       ¦       validation
¦   ¦       ¦   ¦       ¦       
¦   ¦       ¦   ¦       +---draft2020-12
¦   ¦       ¦   ¦               applicator
¦   ¦       ¦   ¦               content
¦   ¦       ¦   ¦               core
¦   ¦       ¦   ¦               format
¦   ¦       ¦   ¦               format-annotation
¦   ¦       ¦   ¦               format-assertion
¦   ¦       ¦   ¦               meta-data
¦   ¦       ¦   ¦               unevaluated
¦   ¦       ¦   ¦               validation
¦   ¦       ¦   ¦               
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   fuzz_validate.py
¦   ¦       ¦   ¦   ¦   test_cli.py
¦   ¦       ¦   ¦   ¦   test_deprecations.py
¦   ¦       ¦   ¦   ¦   test_exceptions.py
¦   ¦       ¦   ¦   ¦   test_format.py
¦   ¦       ¦   ¦   ¦   test_jsonschema_test_suite.py
¦   ¦       ¦   ¦   ¦   test_types.py
¦   ¦       ¦   ¦   ¦   test_utils.py
¦   ¦       ¦   ¦   ¦   test_validators.py
¦   ¦       ¦   ¦   ¦   _helpers.py
¦   ¦       ¦   ¦   ¦   _suite.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           fuzz_validate.cpython-38.pyc
¦   ¦       ¦   ¦           test_cli.cpython-38.pyc
¦   ¦       ¦   ¦           test_deprecations.cpython-38.pyc
¦   ¦       ¦   ¦           test_exceptions.cpython-38.pyc
¦   ¦       ¦   ¦           test_format.cpython-38.pyc
¦   ¦       ¦   ¦           test_jsonschema_test_suite.cpython-38.pyc
¦   ¦       ¦   ¦           test_types.cpython-38.pyc
¦   ¦       ¦   ¦           test_utils.cpython-38.pyc
¦   ¦       ¦   ¦           test_validators.cpython-38.pyc
¦   ¦       ¦   ¦           _helpers.cpython-38.pyc
¦   ¦       ¦   ¦           _suite.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           cli.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           protocols.cpython-38.pyc
¦   ¦       ¦           validators.cpython-38.pyc
¦   ¦       ¦           _format.cpython-38.pyc
¦   ¦       ¦           _legacy_validators.cpython-38.pyc
¦   ¦       ¦           _types.cpython-38.pyc
¦   ¦       ¦           _utils.cpython-38.pyc
¦   ¦       ¦           _validators.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---jsonschema-4.17.3.dist-info
¦   ¦       ¦   ¦   entry_points.txt
¦   ¦       ¦   ¦   INSTALLER
¦   ¦       ¦   ¦   METADATA
¦   ¦       ¦   ¦   RECORD
¦   ¦       ¦   ¦   WHEEL
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---licenses
¦   ¦       ¦           COPYING
¦   ¦       ¦           
¦   ¦       +---kombu
¦   ¦       ¦   ¦   abstract.py
¦   ¦       ¦   ¦   clocks.py
¦   ¦       ¦   ¦   common.py
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   compression.py
¦   ¦       ¦   ¦   connection.py
¦   ¦       ¦   ¦   entity.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   log.py
¦   ¦       ¦   ¦   matcher.py
¦   ¦       ¦   ¦   message.py
¦   ¦       ¦   ¦   messaging.py
¦   ¦       ¦   ¦   mixins.py
¦   ¦       ¦   ¦   pidbox.py
¦   ¦       ¦   ¦   pools.py
¦   ¦       ¦   ¦   resource.py
¦   ¦       ¦   ¦   serialization.py
¦   ¦       ¦   ¦   simple.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---asynchronous
¦   ¦       ¦   ¦   ¦   debug.py
¦   ¦       ¦   ¦   ¦   hub.py
¦   ¦       ¦   ¦   ¦   semaphore.py
¦   ¦       ¦   ¦   ¦   timer.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---aws
¦   ¦       ¦   ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   ¦   ext.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---sqs
¦   ¦       ¦   ¦   ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ext.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   message.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   queue.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           message.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           queue.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---http
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   curl.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           curl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           debug.cpython-38.pyc
¦   ¦       ¦   ¦           hub.cpython-38.pyc
¦   ¦       ¦   ¦           semaphore.cpython-38.pyc
¦   ¦       ¦   ¦           timer.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---transport
¦   ¦       ¦   ¦   ¦   azureservicebus.py
¦   ¦       ¦   ¦   ¦   azurestoragequeues.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   consul.py
¦   ¦       ¦   ¦   ¦   etcd.py
¦   ¦       ¦   ¦   ¦   filesystem.py
¦   ¦       ¦   ¦   ¦   librabbitmq.py
¦   ¦       ¦   ¦   ¦   memory.py
¦   ¦       ¦   ¦   ¦   mongodb.py
¦   ¦       ¦   ¦   ¦   pyamqp.py
¦   ¦       ¦   ¦   ¦   pyro.py
¦   ¦       ¦   ¦   ¦   qpid.py
¦   ¦       ¦   ¦   ¦   redis.py
¦   ¦       ¦   ¦   ¦   SLMQ.py
¦   ¦       ¦   ¦   ¦   SQS.py
¦   ¦       ¦   ¦   ¦   zookeeper.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---sqlalchemy
¦   ¦       ¦   ¦   ¦   ¦   models.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           models.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---virtual
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   exchange.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           exchange.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           azureservicebus.cpython-38.pyc
¦   ¦       ¦   ¦           azurestoragequeues.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           consul.cpython-38.pyc
¦   ¦       ¦   ¦           etcd.cpython-38.pyc
¦   ¦       ¦   ¦           filesystem.cpython-38.pyc
¦   ¦       ¦   ¦           librabbitmq.cpython-38.pyc
¦   ¦       ¦   ¦           memory.cpython-38.pyc
¦   ¦       ¦   ¦           mongodb.cpython-38.pyc
¦   ¦       ¦   ¦           pyamqp.cpython-38.pyc
¦   ¦       ¦   ¦           pyro.cpython-38.pyc
¦   ¦       ¦   ¦           qpid.cpython-38.pyc
¦   ¦       ¦   ¦           redis.cpython-38.pyc
¦   ¦       ¦   ¦           SLMQ.cpython-38.pyc
¦   ¦       ¦   ¦           SQS.cpython-38.pyc
¦   ¦       ¦   ¦           zookeeper.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---utils
¦   ¦       ¦   ¦   ¦   amq_manager.py
¦   ¦       ¦   ¦   ¦   collections.py
¦   ¦       ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   debug.py
¦   ¦       ¦   ¦   ¦   div.py
¦   ¦       ¦   ¦   ¦   encoding.py
¦   ¦       ¦   ¦   ¦   eventio.py
¦   ¦       ¦   ¦   ¦   functional.py
¦   ¦       ¦   ¦   ¦   imports.py
¦   ¦       ¦   ¦   ¦   json.py
¦   ¦       ¦   ¦   ¦   limits.py
¦   ¦       ¦   ¦   ¦   objects.py
¦   ¦       ¦   ¦   ¦   scheduling.py
¦   ¦       ¦   ¦   ¦   text.py
¦   ¦       ¦   ¦   ¦   time.py
¦   ¦       ¦   ¦   ¦   url.py
¦   ¦       ¦   ¦   ¦   uuid.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           amq_manager.cpython-38.pyc
¦   ¦       ¦   ¦           collections.cpython-38.pyc
¦   ¦       ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦           debug.cpython-38.pyc
¦   ¦       ¦   ¦           div.cpython-38.pyc
¦   ¦       ¦   ¦           encoding.cpython-38.pyc
¦   ¦       ¦   ¦           eventio.cpython-38.pyc
¦   ¦       ¦   ¦           functional.cpython-38.pyc
¦   ¦       ¦   ¦           imports.cpython-38.pyc
¦   ¦       ¦   ¦           json.cpython-38.pyc
¦   ¦       ¦   ¦           limits.cpython-38.pyc
¦   ¦       ¦   ¦           objects.cpython-38.pyc
¦   ¦       ¦   ¦           scheduling.cpython-38.pyc
¦   ¦       ¦   ¦           text.cpython-38.pyc
¦   ¦       ¦   ¦           time.cpython-38.pyc
¦   ¦       ¦   ¦           url.cpython-38.pyc
¦   ¦       ¦   ¦           uuid.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           abstract.cpython-38.pyc
¦   ¦       ¦           clocks.cpython-38.pyc
¦   ¦       ¦           common.cpython-38.pyc
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           compression.cpython-38.pyc
¦   ¦       ¦           connection.cpython-38.pyc
¦   ¦       ¦           entity.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           log.cpython-38.pyc
¦   ¦       ¦           matcher.cpython-38.pyc
¦   ¦       ¦           message.cpython-38.pyc
¦   ¦       ¦           messaging.cpython-38.pyc
¦   ¦       ¦           mixins.cpython-38.pyc
¦   ¦       ¦           pidbox.cpython-38.pyc
¦   ¦       ¦           pools.cpython-38.pyc
¦   ¦       ¦           resource.cpython-38.pyc
¦   ¦       ¦           serialization.cpython-38.pyc
¦   ¦       ¦           simple.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---kombu-5.2.4.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---lxml
¦   ¦       ¦   ¦   apihelpers.pxi
¦   ¦       ¦   ¦   builder.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   builder.py
¦   ¦       ¦   ¦   classlookup.pxi
¦   ¦       ¦   ¦   cleanup.pxi
¦   ¦       ¦   ¦   cssselect.py
¦   ¦       ¦   ¦   debug.pxi
¦   ¦       ¦   ¦   docloader.pxi
¦   ¦       ¦   ¦   doctestcompare.py
¦   ¦       ¦   ¦   dtd.pxi
¦   ¦       ¦   ¦   ElementInclude.py
¦   ¦       ¦   ¦   etree.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   etree.h
¦   ¦       ¦   ¦   etree.pyx
¦   ¦       ¦   ¦   etree_api.h
¦   ¦       ¦   ¦   extensions.pxi
¦   ¦       ¦   ¦   iterparse.pxi
¦   ¦       ¦   ¦   lxml.etree.h
¦   ¦       ¦   ¦   lxml.etree_api.h
¦   ¦       ¦   ¦   nsclasses.pxi
¦   ¦       ¦   ¦   objectify.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   objectify.pyx
¦   ¦       ¦   ¦   objectpath.pxi
¦   ¦       ¦   ¦   parser.pxi
¦   ¦       ¦   ¦   parsertarget.pxi
¦   ¦       ¦   ¦   proxy.pxi
¦   ¦       ¦   ¦   public-api.pxi
¦   ¦       ¦   ¦   pyclasslookup.py
¦   ¦       ¦   ¦   readonlytree.pxi
¦   ¦       ¦   ¦   relaxng.pxi
¦   ¦       ¦   ¦   sax.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   sax.py
¦   ¦       ¦   ¦   saxparser.pxi
¦   ¦       ¦   ¦   schematron.pxi
¦   ¦       ¦   ¦   serializer.pxi
¦   ¦       ¦   ¦   usedoctest.py
¦   ¦       ¦   ¦   xinclude.pxi
¦   ¦       ¦   ¦   xmlerror.pxi
¦   ¦       ¦   ¦   xmlid.pxi
¦   ¦       ¦   ¦   xmlschema.pxi
¦   ¦       ¦   ¦   xpath.pxi
¦   ¦       ¦   ¦   xslt.pxi
¦   ¦       ¦   ¦   xsltext.pxi
¦   ¦       ¦   ¦   _elementpath.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _elementpath.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---html
¦   ¦       ¦   ¦   ¦   builder.py
¦   ¦       ¦   ¦   ¦   clean.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   clean.py
¦   ¦       ¦   ¦   ¦   defs.py
¦   ¦       ¦   ¦   ¦   diff.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   diff.py
¦   ¦       ¦   ¦   ¦   ElementSoup.py
¦   ¦       ¦   ¦   ¦   formfill.py
¦   ¦       ¦   ¦   ¦   html5parser.py
¦   ¦       ¦   ¦   ¦   soupparser.py
¦   ¦       ¦   ¦   ¦   usedoctest.py
¦   ¦       ¦   ¦   ¦   _diffcommand.py
¦   ¦       ¦   ¦   ¦   _html5builder.py
¦   ¦       ¦   ¦   ¦   _setmixin.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           builder.cpython-38.pyc
¦   ¦       ¦   ¦           clean.cpython-38.pyc
¦   ¦       ¦   ¦           defs.cpython-38.pyc
¦   ¦       ¦   ¦           diff.cpython-38.pyc
¦   ¦       ¦   ¦           ElementSoup.cpython-38.pyc
¦   ¦       ¦   ¦           formfill.cpython-38.pyc
¦   ¦       ¦   ¦           html5parser.cpython-38.pyc
¦   ¦       ¦   ¦           soupparser.cpython-38.pyc
¦   ¦       ¦   ¦           usedoctest.cpython-38.pyc
¦   ¦       ¦   ¦           _diffcommand.cpython-38.pyc
¦   ¦       ¦   ¦           _html5builder.cpython-38.pyc
¦   ¦       ¦   ¦           _setmixin.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---includes
¦   ¦       ¦   ¦   ¦   c14n.pxd
¦   ¦       ¦   ¦   ¦   config.pxd
¦   ¦       ¦   ¦   ¦   dtdvalid.pxd
¦   ¦       ¦   ¦   ¦   etreepublic.pxd
¦   ¦       ¦   ¦   ¦   etree_defs.h
¦   ¦       ¦   ¦   ¦   htmlparser.pxd
¦   ¦       ¦   ¦   ¦   lxml-version.h
¦   ¦       ¦   ¦   ¦   relaxng.pxd
¦   ¦       ¦   ¦   ¦   schematron.pxd
¦   ¦       ¦   ¦   ¦   tree.pxd
¦   ¦       ¦   ¦   ¦   uri.pxd
¦   ¦       ¦   ¦   ¦   xinclude.pxd
¦   ¦       ¦   ¦   ¦   xmlerror.pxd
¦   ¦       ¦   ¦   ¦   xmlparser.pxd
¦   ¦       ¦   ¦   ¦   xmlschema.pxd
¦   ¦       ¦   ¦   ¦   xpath.pxd
¦   ¦       ¦   ¦   ¦   xslt.pxd
¦   ¦       ¦   ¦   ¦   __init__.pxd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---extlibs
¦   ¦       ¦   ¦   ¦   ¦   zconf.h
¦   ¦       ¦   ¦   ¦   ¦   zlib.h
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---libexslt
¦   ¦       ¦   ¦   ¦   ¦   exslt.h
¦   ¦       ¦   ¦   ¦   ¦   exsltconfig.h
¦   ¦       ¦   ¦   ¦   ¦   exsltexports.h
¦   ¦       ¦   ¦   ¦   ¦   libexslt.h
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---libxml
¦   ¦       ¦   ¦   ¦   ¦   c14n.h
¦   ¦       ¦   ¦   ¦   ¦   catalog.h
¦   ¦       ¦   ¦   ¦   ¦   chvalid.h
¦   ¦       ¦   ¦   ¦   ¦   debugXML.h
¦   ¦       ¦   ¦   ¦   ¦   dict.h
¦   ¦       ¦   ¦   ¦   ¦   DOCBparser.h
¦   ¦       ¦   ¦   ¦   ¦   encoding.h
¦   ¦       ¦   ¦   ¦   ¦   entities.h
¦   ¦       ¦   ¦   ¦   ¦   globals.h
¦   ¦       ¦   ¦   ¦   ¦   hash.h
¦   ¦       ¦   ¦   ¦   ¦   HTMLparser.h
¦   ¦       ¦   ¦   ¦   ¦   HTMLtree.h
¦   ¦       ¦   ¦   ¦   ¦   list.h
¦   ¦       ¦   ¦   ¦   ¦   nanoftp.h
¦   ¦       ¦   ¦   ¦   ¦   nanohttp.h
¦   ¦       ¦   ¦   ¦   ¦   parser.h
¦   ¦       ¦   ¦   ¦   ¦   parserInternals.h
¦   ¦       ¦   ¦   ¦   ¦   pattern.h
¦   ¦       ¦   ¦   ¦   ¦   relaxng.h
¦   ¦       ¦   ¦   ¦   ¦   SAX.h
¦   ¦       ¦   ¦   ¦   ¦   SAX2.h
¦   ¦       ¦   ¦   ¦   ¦   schemasInternals.h
¦   ¦       ¦   ¦   ¦   ¦   schematron.h
¦   ¦       ¦   ¦   ¦   ¦   threads.h
¦   ¦       ¦   ¦   ¦   ¦   tree.h
¦   ¦       ¦   ¦   ¦   ¦   uri.h
¦   ¦       ¦   ¦   ¦   ¦   valid.h
¦   ¦       ¦   ¦   ¦   ¦   xinclude.h
¦   ¦       ¦   ¦   ¦   ¦   xlink.h
¦   ¦       ¦   ¦   ¦   ¦   xmlautomata.h
¦   ¦       ¦   ¦   ¦   ¦   xmlerror.h
¦   ¦       ¦   ¦   ¦   ¦   xmlexports.h
¦   ¦       ¦   ¦   ¦   ¦   xmlIO.h
¦   ¦       ¦   ¦   ¦   ¦   xmlmemory.h
¦   ¦       ¦   ¦   ¦   ¦   xmlmodule.h
¦   ¦       ¦   ¦   ¦   ¦   xmlreader.h
¦   ¦       ¦   ¦   ¦   ¦   xmlregexp.h
¦   ¦       ¦   ¦   ¦   ¦   xmlsave.h
¦   ¦       ¦   ¦   ¦   ¦   xmlschemas.h
¦   ¦       ¦   ¦   ¦   ¦   xmlschemastypes.h
¦   ¦       ¦   ¦   ¦   ¦   xmlstring.h
¦   ¦       ¦   ¦   ¦   ¦   xmlunicode.h
¦   ¦       ¦   ¦   ¦   ¦   xmlversion.h
¦   ¦       ¦   ¦   ¦   ¦   xmlwriter.h
¦   ¦       ¦   ¦   ¦   ¦   xpath.h
¦   ¦       ¦   ¦   ¦   ¦   xpathInternals.h
¦   ¦       ¦   ¦   ¦   ¦   xpointer.h
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---libxslt
¦   ¦       ¦   ¦   ¦   ¦   attributes.h
¦   ¦       ¦   ¦   ¦   ¦   documents.h
¦   ¦       ¦   ¦   ¦   ¦   extensions.h
¦   ¦       ¦   ¦   ¦   ¦   extra.h
¦   ¦       ¦   ¦   ¦   ¦   functions.h
¦   ¦       ¦   ¦   ¦   ¦   imports.h
¦   ¦       ¦   ¦   ¦   ¦   keys.h
¦   ¦       ¦   ¦   ¦   ¦   libxslt.h
¦   ¦       ¦   ¦   ¦   ¦   namespaces.h
¦   ¦       ¦   ¦   ¦   ¦   numbersInternals.h
¦   ¦       ¦   ¦   ¦   ¦   preproc.h
¦   ¦       ¦   ¦   ¦   ¦   security.h
¦   ¦       ¦   ¦   ¦   ¦   templates.h
¦   ¦       ¦   ¦   ¦   ¦   transform.h
¦   ¦       ¦   ¦   ¦   ¦   trio.h
¦   ¦       ¦   ¦   ¦   ¦   triodef.h
¦   ¦       ¦   ¦   ¦   ¦   variables.h
¦   ¦       ¦   ¦   ¦   ¦   win32config.h
¦   ¦       ¦   ¦   ¦   ¦   xslt.h
¦   ¦       ¦   ¦   ¦   ¦   xsltconfig.h
¦   ¦       ¦   ¦   ¦   ¦   xsltexports.h
¦   ¦       ¦   ¦   ¦   ¦   xsltInternals.h
¦   ¦       ¦   ¦   ¦   ¦   xsltlocale.h
¦   ¦       ¦   ¦   ¦   ¦   xsltutils.h
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---isoschematron
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---resources
¦   ¦       ¦   ¦   ¦   +---rng
¦   ¦       ¦   ¦   ¦   ¦       iso-schematron.rng
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---xsl
¦   ¦       ¦   ¦   ¦       ¦   RNG2Schtrn.xsl
¦   ¦       ¦   ¦   ¦       ¦   XSD2Schtrn.xsl
¦   ¦       ¦   ¦   ¦       ¦   
¦   ¦       ¦   ¦   ¦       +---iso-schematron-xslt1
¦   ¦       ¦   ¦   ¦               iso_abstract_expand.xsl
¦   ¦       ¦   ¦   ¦               iso_dsdl_include.xsl
¦   ¦       ¦   ¦   ¦               iso_schematron_message.xsl
¦   ¦       ¦   ¦   ¦               iso_schematron_skeleton_for_xslt1.xsl
¦   ¦       ¦   ¦   ¦               iso_svrl_for_xslt1.xsl
¦   ¦       ¦   ¦   ¦               readme.txt
¦   ¦       ¦   ¦   ¦               
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           builder.cpython-38.pyc
¦   ¦       ¦           cssselect.cpython-38.pyc
¦   ¦       ¦           doctestcompare.cpython-38.pyc
¦   ¦       ¦           ElementInclude.cpython-38.pyc
¦   ¦       ¦           pyclasslookup.cpython-38.pyc
¦   ¦       ¦           sax.cpython-38.pyc
¦   ¦       ¦           usedoctest.cpython-38.pyc
¦   ¦       ¦           _elementpath.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---lxml-4.9.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       LICENSES.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---markupsafe
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   _native.py
¦   ¦       ¦   ¦   _speedups.c
¦   ¦       ¦   ¦   _speedups.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _speedups.pyi
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           _native.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---MarkupSafe-2.1.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---numpy
¦   ¦       ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ctypeslib.py
¦   ¦       ¦   ¦   ctypeslib.pyi
¦   ¦       ¦   ¦   dual.py
¦   ¦       ¦   ¦   LICENSE.txt
¦   ¦       ¦   ¦   matlib.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   setup.py
¦   ¦       ¦   ¦   version.py
¦   ¦       ¦   ¦   _distributor_init.py
¦   ¦       ¦   ¦   _globals.py
¦   ¦       ¦   ¦   _pytesttester.py
¦   ¦       ¦   ¦   _pytesttester.pyi
¦   ¦       ¦   ¦   _version.py
¦   ¦       ¦   ¦   __config__.py
¦   ¦       ¦   ¦   __init__.cython-30.pxd
¦   ¦       ¦   ¦   __init__.pxd
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---.libs
¦   ¦       ¦   ¦       libopenblas64__v0.3.21-gcc_10_3_0.dll
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---array_api
¦   ¦       ¦   ¦   ¦   linalg.py
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _array_object.py
¦   ¦       ¦   ¦   ¦   _constants.py
¦   ¦       ¦   ¦   ¦   _creation_functions.py
¦   ¦       ¦   ¦   ¦   _data_type_functions.py
¦   ¦       ¦   ¦   ¦   _dtypes.py
¦   ¦       ¦   ¦   ¦   _elementwise_functions.py
¦   ¦       ¦   ¦   ¦   _manipulation_functions.py
¦   ¦       ¦   ¦   ¦   _searching_functions.py
¦   ¦       ¦   ¦   ¦   _set_functions.py
¦   ¦       ¦   ¦   ¦   _sorting_functions.py
¦   ¦       ¦   ¦   ¦   _statistical_functions.py
¦   ¦       ¦   ¦   ¦   _typing.py
¦   ¦       ¦   ¦   ¦   _utility_functions.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_array_object.py
¦   ¦       ¦   ¦   ¦   ¦   test_creation_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_data_type_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_elementwise_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_set_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_sorting_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_validation.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_array_object.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_creation_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_data_type_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_elementwise_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_set_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_sorting_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           linalg.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           _array_object.cpython-38.pyc
¦   ¦       ¦   ¦           _constants.cpython-38.pyc
¦   ¦       ¦   ¦           _creation_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _data_type_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _dtypes.cpython-38.pyc
¦   ¦       ¦   ¦           _elementwise_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _manipulation_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _searching_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _set_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _sorting_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _statistical_functions.cpython-38.pyc
¦   ¦       ¦   ¦           _typing.cpython-38.pyc
¦   ¦       ¦   ¦           _utility_functions.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---compat
¦   ¦       ¦   ¦   ¦   py3k.py
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _inspect.py
¦   ¦       ¦   ¦   ¦   _pep440.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_compat.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           py3k.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           _inspect.cpython-38.pyc
¦   ¦       ¦   ¦           _pep440.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---core
¦   ¦       ¦   ¦   ¦   arrayprint.py
¦   ¦       ¦   ¦   ¦   arrayprint.pyi
¦   ¦       ¦   ¦   ¦   cversions.py
¦   ¦       ¦   ¦   ¦   defchararray.py
¦   ¦       ¦   ¦   ¦   defchararray.pyi
¦   ¦       ¦   ¦   ¦   einsumfunc.py
¦   ¦       ¦   ¦   ¦   einsumfunc.pyi
¦   ¦       ¦   ¦   ¦   fromnumeric.py
¦   ¦       ¦   ¦   ¦   fromnumeric.pyi
¦   ¦       ¦   ¦   ¦   function_base.py
¦   ¦       ¦   ¦   ¦   function_base.pyi
¦   ¦       ¦   ¦   ¦   generate_numpy_api.py
¦   ¦       ¦   ¦   ¦   getlimits.py
¦   ¦       ¦   ¦   ¦   getlimits.pyi
¦   ¦       ¦   ¦   ¦   memmap.py
¦   ¦       ¦   ¦   ¦   memmap.pyi
¦   ¦       ¦   ¦   ¦   multiarray.py
¦   ¦       ¦   ¦   ¦   multiarray.pyi
¦   ¦       ¦   ¦   ¦   numeric.py
¦   ¦       ¦   ¦   ¦   numeric.pyi
¦   ¦       ¦   ¦   ¦   numerictypes.py
¦   ¦       ¦   ¦   ¦   numerictypes.pyi
¦   ¦       ¦   ¦   ¦   overrides.py
¦   ¦       ¦   ¦   ¦   records.py
¦   ¦       ¦   ¦   ¦   records.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   setup_common.py
¦   ¦       ¦   ¦   ¦   shape_base.py
¦   ¦       ¦   ¦   ¦   shape_base.pyi
¦   ¦       ¦   ¦   ¦   umath.py
¦   ¦       ¦   ¦   ¦   umath_tests.py
¦   ¦       ¦   ¦   ¦   _add_newdocs.py
¦   ¦       ¦   ¦   ¦   _add_newdocs_scalars.py
¦   ¦       ¦   ¦   ¦   _asarray.py
¦   ¦       ¦   ¦   ¦   _asarray.pyi
¦   ¦       ¦   ¦   ¦   _dtype.py
¦   ¦       ¦   ¦   ¦   _dtype_ctypes.py
¦   ¦       ¦   ¦   ¦   _exceptions.py
¦   ¦       ¦   ¦   ¦   _internal.py
¦   ¦       ¦   ¦   ¦   _internal.pyi
¦   ¦       ¦   ¦   ¦   _machar.py
¦   ¦       ¦   ¦   ¦   _methods.py
¦   ¦       ¦   ¦   ¦   _multiarray_tests.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _multiarray_umath.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _operand_flag_tests.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _rational_tests.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _simd.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _string_helpers.py
¦   ¦       ¦   ¦   ¦   _struct_ufunc_tests.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _type_aliases.py
¦   ¦       ¦   ¦   ¦   _type_aliases.pyi
¦   ¦       ¦   ¦   ¦   _ufunc_config.py
¦   ¦       ¦   ¦   ¦   _ufunc_config.pyi
¦   ¦       ¦   ¦   ¦   _umath_tests.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---include
¦   ¦       ¦   ¦   ¦   +---numpy
¦   ¦       ¦   ¦   ¦       ¦   .doxyfile
¦   ¦       ¦   ¦   ¦       ¦   arrayobject.h
¦   ¦       ¦   ¦   ¦       ¦   arrayscalars.h
¦   ¦       ¦   ¦   ¦       ¦   experimental_dtype_api.h
¦   ¦       ¦   ¦   ¦       ¦   halffloat.h
¦   ¦       ¦   ¦   ¦       ¦   multiarray_api.txt
¦   ¦       ¦   ¦   ¦       ¦   ndarrayobject.h
¦   ¦       ¦   ¦   ¦       ¦   ndarraytypes.h
¦   ¦       ¦   ¦   ¦       ¦   noprefix.h
¦   ¦       ¦   ¦   ¦       ¦   npy_1_7_deprecated_api.h
¦   ¦       ¦   ¦   ¦       ¦   npy_3kcompat.h
¦   ¦       ¦   ¦   ¦       ¦   npy_common.h
¦   ¦       ¦   ¦   ¦       ¦   npy_cpu.h
¦   ¦       ¦   ¦   ¦       ¦   npy_endian.h
¦   ¦       ¦   ¦   ¦       ¦   npy_interrupt.h
¦   ¦       ¦   ¦   ¦       ¦   npy_math.h
¦   ¦       ¦   ¦   ¦       ¦   npy_no_deprecated_api.h
¦   ¦       ¦   ¦   ¦       ¦   npy_os.h
¦   ¦       ¦   ¦   ¦       ¦   numpyconfig.h
¦   ¦       ¦   ¦   ¦       ¦   oldnumeric.h
¦   ¦       ¦   ¦   ¦       ¦   old_defines.h
¦   ¦       ¦   ¦   ¦       ¦   ufuncobject.h
¦   ¦       ¦   ¦   ¦       ¦   ufunc_api.txt
¦   ¦       ¦   ¦   ¦       ¦   utils.h
¦   ¦       ¦   ¦   ¦       ¦   _neighborhood_iterator_imp.h
¦   ¦       ¦   ¦   ¦       ¦   _numpyconfig.h
¦   ¦       ¦   ¦   ¦       ¦   __multiarray_api.h
¦   ¦       ¦   ¦   ¦       ¦   __ufunc_api.h
¦   ¦       ¦   ¦   ¦       ¦   
¦   ¦       ¦   ¦   ¦       +---libdivide
¦   ¦       ¦   ¦   ¦       ¦       libdivide.h
¦   ¦       ¦   ¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦   ¦   ¦       ¦       
¦   ¦       ¦   ¦   ¦       +---random
¦   ¦       ¦   ¦   ¦               bitgen.h
¦   ¦       ¦   ¦   ¦               distributions.h
¦   ¦       ¦   ¦   ¦               
¦   ¦       ¦   ¦   +---lib
¦   ¦       ¦   ¦   ¦   ¦   npymath.lib
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---npy-pkg-config
¦   ¦       ¦   ¦   ¦           mlib.ini
¦   ¦       ¦   ¦   ¦           npymath.ini
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_abc.py
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_argparse.py
¦   ¦       ¦   ¦   ¦   ¦   test_arraymethod.py
¦   ¦       ¦   ¦   ¦   ¦   test_arrayprint.py
¦   ¦       ¦   ¦   ¦   ¦   test_array_coercion.py
¦   ¦       ¦   ¦   ¦   ¦   test_array_interface.py
¦   ¦       ¦   ¦   ¦   ¦   test_casting_floatingpoint_errors.py
¦   ¦       ¦   ¦   ¦   ¦   test_casting_unittests.py
¦   ¦       ¦   ¦   ¦   ¦   test_conversion_utils.py
¦   ¦       ¦   ¦   ¦   ¦   test_cpu_dispatcher.py
¦   ¦       ¦   ¦   ¦   ¦   test_cpu_features.py
¦   ¦       ¦   ¦   ¦   ¦   test_custom_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   test_cython.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   test_defchararray.py
¦   ¦       ¦   ¦   ¦   ¦   test_deprecations.py
¦   ¦       ¦   ¦   ¦   ¦   test_dlpack.py
¦   ¦       ¦   ¦   ¦   ¦   test_dtype.py
¦   ¦       ¦   ¦   ¦   ¦   test_einsum.py
¦   ¦       ¦   ¦   ¦   ¦   test_errstate.py
¦   ¦       ¦   ¦   ¦   ¦   test_extint128.py
¦   ¦       ¦   ¦   ¦   ¦   test_function_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_getlimits.py
¦   ¦       ¦   ¦   ¦   ¦   test_half.py
¦   ¦       ¦   ¦   ¦   ¦   test_hashtable.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexerrors.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   test_item_selection.py
¦   ¦       ¦   ¦   ¦   ¦   test_limited_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_longdouble.py
¦   ¦       ¦   ¦   ¦   ¦   test_machar.py
¦   ¦       ¦   ¦   ¦   ¦   test_memmap.py
¦   ¦       ¦   ¦   ¦   ¦   test_mem_overlap.py
¦   ¦       ¦   ¦   ¦   ¦   test_mem_policy.py
¦   ¦       ¦   ¦   ¦   ¦   test_multiarray.py
¦   ¦       ¦   ¦   ¦   ¦   test_nditer.py
¦   ¦       ¦   ¦   ¦   ¦   test_nep50_promotions.py
¦   ¦       ¦   ¦   ¦   ¦   test_numeric.py
¦   ¦       ¦   ¦   ¦   ¦   test_numerictypes.py
¦   ¦       ¦   ¦   ¦   ¦   test_overrides.py
¦   ¦       ¦   ¦   ¦   ¦   test_print.py
¦   ¦       ¦   ¦   ¦   ¦   test_protocols.py
¦   ¦       ¦   ¦   ¦   ¦   test_records.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalarbuffer.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalarinherit.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalarmath.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalarprint.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalar_ctors.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalar_methods.py
¦   ¦       ¦   ¦   ¦   ¦   test_shape_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_simd.py
¦   ¦       ¦   ¦   ¦   ¦   test_simd_module.py
¦   ¦       ¦   ¦   ¦   ¦   test_strings.py
¦   ¦       ¦   ¦   ¦   ¦   test_ufunc.py
¦   ¦       ¦   ¦   ¦   ¦   test_umath.py
¦   ¦       ¦   ¦   ¦   ¦   test_umath_accuracy.py
¦   ¦       ¦   ¦   ¦   ¦   test_umath_complex.py
¦   ¦       ¦   ¦   ¦   ¦   test_unicode.py
¦   ¦       ¦   ¦   ¦   ¦   test__exceptions.py
¦   ¦       ¦   ¦   ¦   ¦   _locales.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---data
¦   ¦       ¦   ¦   ¦   ¦       astype_copy.pkl
¦   ¦       ¦   ¦   ¦   ¦       generate_umath_validation_data.cpp
¦   ¦       ¦   ¦   ¦   ¦       recarray_from_file.fits
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arccos.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arccosh.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arcsin.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arcsinh.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arctan.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-arctanh.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-cbrt.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-cos.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-cosh.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-exp.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-exp2.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-expm1.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log10.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log1p.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-log2.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-README.txt
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-sin.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-sinh.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-tan.csv
¦   ¦       ¦   ¦   ¦   ¦       umath-validation-set-tanh.csv
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---examples
¦   ¦       ¦   ¦   ¦   ¦   +---cython
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   checks.pyx
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---limited_api
¦   ¦       ¦   ¦   ¦   ¦       ¦   limited_api.c
¦   ¦       ¦   ¦   ¦   ¦       ¦   setup.py
¦   ¦       ¦   ¦   ¦   ¦       ¦   
¦   ¦       ¦   ¦   ¦   ¦       +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦               setup.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦               
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_abc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_argparse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arraymethod.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arrayprint.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_array_coercion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_array_interface.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_casting_floatingpoint_errors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_casting_unittests.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_conversion_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cpu_dispatcher.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cpu_features.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_custom_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cython.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_defchararray.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_deprecations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_dlpack.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_einsum.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_errstate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_extint128.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_function_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_getlimits.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_half.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_hashtable.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexerrors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_item_selection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_limited_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_longdouble.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_machar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_memmap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_mem_overlap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_mem_policy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_multiarray.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_nditer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_nep50_promotions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numerictypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_overrides.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_print.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_protocols.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_records.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalarbuffer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalarinherit.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalarmath.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalarprint.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalar_ctors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalar_methods.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_shape_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_simd.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_simd_module.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_strings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ufunc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_umath.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_umath_accuracy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_umath_complex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_unicode.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test__exceptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _locales.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           arrayprint.cpython-38.pyc
¦   ¦       ¦   ¦           cversions.cpython-38.pyc
¦   ¦       ¦   ¦           defchararray.cpython-38.pyc
¦   ¦       ¦   ¦           einsumfunc.cpython-38.pyc
¦   ¦       ¦   ¦           fromnumeric.cpython-38.pyc
¦   ¦       ¦   ¦           function_base.cpython-38.pyc
¦   ¦       ¦   ¦           generate_numpy_api.cpython-38.pyc
¦   ¦       ¦   ¦           getlimits.cpython-38.pyc
¦   ¦       ¦   ¦           memmap.cpython-38.pyc
¦   ¦       ¦   ¦           multiarray.cpython-38.pyc
¦   ¦       ¦   ¦           numeric.cpython-38.pyc
¦   ¦       ¦   ¦           numerictypes.cpython-38.pyc
¦   ¦       ¦   ¦           overrides.cpython-38.pyc
¦   ¦       ¦   ¦           records.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           setup_common.cpython-38.pyc
¦   ¦       ¦   ¦           shape_base.cpython-38.pyc
¦   ¦       ¦   ¦           umath.cpython-38.pyc
¦   ¦       ¦   ¦           umath_tests.cpython-38.pyc
¦   ¦       ¦   ¦           _add_newdocs.cpython-38.pyc
¦   ¦       ¦   ¦           _add_newdocs_scalars.cpython-38.pyc
¦   ¦       ¦   ¦           _asarray.cpython-38.pyc
¦   ¦       ¦   ¦           _dtype.cpython-38.pyc
¦   ¦       ¦   ¦           _dtype_ctypes.cpython-38.pyc
¦   ¦       ¦   ¦           _exceptions.cpython-38.pyc
¦   ¦       ¦   ¦           _internal.cpython-38.pyc
¦   ¦       ¦   ¦           _machar.cpython-38.pyc
¦   ¦       ¦   ¦           _methods.cpython-38.pyc
¦   ¦       ¦   ¦           _string_helpers.cpython-38.pyc
¦   ¦       ¦   ¦           _type_aliases.cpython-38.pyc
¦   ¦       ¦   ¦           _ufunc_config.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---distutils
¦   ¦       ¦   ¦   ¦   armccompiler.py
¦   ¦       ¦   ¦   ¦   ccompiler.py
¦   ¦       ¦   ¦   ¦   ccompiler_opt.py
¦   ¦       ¦   ¦   ¦   conv_template.py
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   cpuinfo.py
¦   ¦       ¦   ¦   ¦   exec_command.py
¦   ¦       ¦   ¦   ¦   extension.py
¦   ¦       ¦   ¦   ¦   from_template.py
¦   ¦       ¦   ¦   ¦   intelccompiler.py
¦   ¦       ¦   ¦   ¦   lib2def.py
¦   ¦       ¦   ¦   ¦   line_endings.py
¦   ¦       ¦   ¦   ¦   log.py
¦   ¦       ¦   ¦   ¦   mingw32ccompiler.py
¦   ¦       ¦   ¦   ¦   misc_util.py
¦   ¦       ¦   ¦   ¦   msvc9compiler.py
¦   ¦       ¦   ¦   ¦   msvccompiler.py
¦   ¦       ¦   ¦   ¦   npy_pkg_config.py
¦   ¦       ¦   ¦   ¦   numpy_distribution.py
¦   ¦       ¦   ¦   ¦   pathccompiler.py
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   system_info.py
¦   ¦       ¦   ¦   ¦   unixccompiler.py
¦   ¦       ¦   ¦   ¦   _shell_utils.py
¦   ¦       ¦   ¦   ¦   __config__.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---checks
¦   ¦       ¦   ¦   ¦       cpu_asimd.c
¦   ¦       ¦   ¦   ¦       cpu_asimddp.c
¦   ¦       ¦   ¦   ¦       cpu_asimdfhm.c
¦   ¦       ¦   ¦   ¦       cpu_asimdhp.c
¦   ¦       ¦   ¦   ¦       cpu_avx.c
¦   ¦       ¦   ¦   ¦       cpu_avx2.c
¦   ¦       ¦   ¦   ¦       cpu_avx512cd.c
¦   ¦       ¦   ¦   ¦       cpu_avx512f.c
¦   ¦       ¦   ¦   ¦       cpu_avx512_clx.c
¦   ¦       ¦   ¦   ¦       cpu_avx512_cnl.c
¦   ¦       ¦   ¦   ¦       cpu_avx512_icl.c
¦   ¦       ¦   ¦   ¦       cpu_avx512_knl.c
¦   ¦       ¦   ¦   ¦       cpu_avx512_knm.c
¦   ¦       ¦   ¦   ¦       cpu_avx512_skx.c
¦   ¦       ¦   ¦   ¦       cpu_f16c.c
¦   ¦       ¦   ¦   ¦       cpu_fma3.c
¦   ¦       ¦   ¦   ¦       cpu_fma4.c
¦   ¦       ¦   ¦   ¦       cpu_neon.c
¦   ¦       ¦   ¦   ¦       cpu_neon_fp16.c
¦   ¦       ¦   ¦   ¦       cpu_neon_vfpv4.c
¦   ¦       ¦   ¦   ¦       cpu_popcnt.c
¦   ¦       ¦   ¦   ¦       cpu_sse.c
¦   ¦       ¦   ¦   ¦       cpu_sse2.c
¦   ¦       ¦   ¦   ¦       cpu_sse3.c
¦   ¦       ¦   ¦   ¦       cpu_sse41.c
¦   ¦       ¦   ¦   ¦       cpu_sse42.c
¦   ¦       ¦   ¦   ¦       cpu_ssse3.c
¦   ¦       ¦   ¦   ¦       cpu_vsx.c
¦   ¦       ¦   ¦   ¦       cpu_vsx2.c
¦   ¦       ¦   ¦   ¦       cpu_vsx3.c
¦   ¦       ¦   ¦   ¦       cpu_vsx4.c
¦   ¦       ¦   ¦   ¦       cpu_vx.c
¦   ¦       ¦   ¦   ¦       cpu_vxe.c
¦   ¦       ¦   ¦   ¦       cpu_vxe2.c
¦   ¦       ¦   ¦   ¦       cpu_xop.c
¦   ¦       ¦   ¦   ¦       extra_avx512bw_mask.c
¦   ¦       ¦   ¦   ¦       extra_avx512dq_mask.c
¦   ¦       ¦   ¦   ¦       extra_avx512f_reduce.c
¦   ¦       ¦   ¦   ¦       extra_vsx4_mma.c
¦   ¦       ¦   ¦   ¦       extra_vsx_asm.c
¦   ¦       ¦   ¦   ¦       test_flags.c
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---command
¦   ¦       ¦   ¦   ¦   ¦   autodist.py
¦   ¦       ¦   ¦   ¦   ¦   bdist_rpm.py
¦   ¦       ¦   ¦   ¦   ¦   build.py
¦   ¦       ¦   ¦   ¦   ¦   build_clib.py
¦   ¦       ¦   ¦   ¦   ¦   build_ext.py
¦   ¦       ¦   ¦   ¦   ¦   build_py.py
¦   ¦       ¦   ¦   ¦   ¦   build_scripts.py
¦   ¦       ¦   ¦   ¦   ¦   build_src.py
¦   ¦       ¦   ¦   ¦   ¦   config.py
¦   ¦       ¦   ¦   ¦   ¦   config_compiler.py
¦   ¦       ¦   ¦   ¦   ¦   develop.py
¦   ¦       ¦   ¦   ¦   ¦   egg_info.py
¦   ¦       ¦   ¦   ¦   ¦   install.py
¦   ¦       ¦   ¦   ¦   ¦   install_clib.py
¦   ¦       ¦   ¦   ¦   ¦   install_data.py
¦   ¦       ¦   ¦   ¦   ¦   install_headers.py
¦   ¦       ¦   ¦   ¦   ¦   sdist.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           autodist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           bdist_rpm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_clib.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_py.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_scripts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_src.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           config.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           config_compiler.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           develop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           egg_info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_clib.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_headers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sdist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---fcompiler
¦   ¦       ¦   ¦   ¦   ¦   absoft.py
¦   ¦       ¦   ¦   ¦   ¦   arm.py
¦   ¦       ¦   ¦   ¦   ¦   compaq.py
¦   ¦       ¦   ¦   ¦   ¦   environment.py
¦   ¦       ¦   ¦   ¦   ¦   fujitsu.py
¦   ¦       ¦   ¦   ¦   ¦   g95.py
¦   ¦       ¦   ¦   ¦   ¦   gnu.py
¦   ¦       ¦   ¦   ¦   ¦   hpux.py
¦   ¦       ¦   ¦   ¦   ¦   ibm.py
¦   ¦       ¦   ¦   ¦   ¦   intel.py
¦   ¦       ¦   ¦   ¦   ¦   lahey.py
¦   ¦       ¦   ¦   ¦   ¦   mips.py
¦   ¦       ¦   ¦   ¦   ¦   nag.py
¦   ¦       ¦   ¦   ¦   ¦   none.py
¦   ¦       ¦   ¦   ¦   ¦   nv.py
¦   ¦       ¦   ¦   ¦   ¦   pathf95.py
¦   ¦       ¦   ¦   ¦   ¦   pg.py
¦   ¦       ¦   ¦   ¦   ¦   sun.py
¦   ¦       ¦   ¦   ¦   ¦   vast.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           absoft.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           arm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compaq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           environment.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           fujitsu.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           g95.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           gnu.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hpux.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ibm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           intel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           lahey.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mips.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           nag.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           none.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           nv.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pathf95.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pg.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sun.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           vast.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---mingw
¦   ¦       ¦   ¦   ¦       gfortran_vs2003_hack.c
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_build_ext.py
¦   ¦       ¦   ¦   ¦   ¦   test_ccompiler_opt.py
¦   ¦       ¦   ¦   ¦   ¦   test_ccompiler_opt_conf.py
¦   ¦       ¦   ¦   ¦   ¦   test_exec_command.py
¦   ¦       ¦   ¦   ¦   ¦   test_fcompiler.py
¦   ¦       ¦   ¦   ¦   ¦   test_fcompiler_gnu.py
¦   ¦       ¦   ¦   ¦   ¦   test_fcompiler_intel.py
¦   ¦       ¦   ¦   ¦   ¦   test_fcompiler_nagfor.py
¦   ¦       ¦   ¦   ¦   ¦   test_from_template.py
¦   ¦       ¦   ¦   ¦   ¦   test_log.py
¦   ¦       ¦   ¦   ¦   ¦   test_mingw32ccompiler.py
¦   ¦       ¦   ¦   ¦   ¦   test_misc_util.py
¦   ¦       ¦   ¦   ¦   ¦   test_npy_pkg_config.py
¦   ¦       ¦   ¦   ¦   ¦   test_shell_utils.py
¦   ¦       ¦   ¦   ¦   ¦   test_system_info.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_build_ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ccompiler_opt.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ccompiler_opt_conf.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_exec_command.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fcompiler.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fcompiler_gnu.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fcompiler_intel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fcompiler_nagfor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_from_template.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_log.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_mingw32ccompiler.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_misc_util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_npy_pkg_config.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_shell_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_system_info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           armccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           ccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           ccompiler_opt.cpython-38.pyc
¦   ¦       ¦   ¦           conv_template.cpython-38.pyc
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           cpuinfo.cpython-38.pyc
¦   ¦       ¦   ¦           exec_command.cpython-38.pyc
¦   ¦       ¦   ¦           extension.cpython-38.pyc
¦   ¦       ¦   ¦           from_template.cpython-38.pyc
¦   ¦       ¦   ¦           intelccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           lib2def.cpython-38.pyc
¦   ¦       ¦   ¦           line_endings.cpython-38.pyc
¦   ¦       ¦   ¦           log.cpython-38.pyc
¦   ¦       ¦   ¦           mingw32ccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           misc_util.cpython-38.pyc
¦   ¦       ¦   ¦           msvc9compiler.cpython-38.pyc
¦   ¦       ¦   ¦           msvccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           npy_pkg_config.cpython-38.pyc
¦   ¦       ¦   ¦           numpy_distribution.cpython-38.pyc
¦   ¦       ¦   ¦           pathccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           system_info.cpython-38.pyc
¦   ¦       ¦   ¦           unixccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           _shell_utils.cpython-38.pyc
¦   ¦       ¦   ¦           __config__.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---doc
¦   ¦       ¦   ¦   ¦   constants.py
¦   ¦       ¦   ¦   ¦   ufuncs.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           constants.cpython-38.pyc
¦   ¦       ¦   ¦           ufuncs.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---f2py
¦   ¦       ¦   ¦   ¦   auxfuncs.py
¦   ¦       ¦   ¦   ¦   capi_maps.py
¦   ¦       ¦   ¦   ¦   cb_rules.py
¦   ¦       ¦   ¦   ¦   cfuncs.py
¦   ¦       ¦   ¦   ¦   common_rules.py
¦   ¦       ¦   ¦   ¦   crackfortran.py
¦   ¦       ¦   ¦   ¦   diagnose.py
¦   ¦       ¦   ¦   ¦   f2py2e.py
¦   ¦       ¦   ¦   ¦   f90mod_rules.py
¦   ¦       ¦   ¦   ¦   func2subr.py
¦   ¦       ¦   ¦   ¦   rules.py
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   symbolic.py
¦   ¦       ¦   ¦   ¦   use_rules.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   __version__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---src
¦   ¦       ¦   ¦   ¦       fortranobject.c
¦   ¦       ¦   ¦   ¦       fortranobject.h
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_abstract_interface.py
¦   ¦       ¦   ¦   ¦   ¦   test_array_from_pyobj.py
¦   ¦       ¦   ¦   ¦   ¦   test_assumed_shape.py
¦   ¦       ¦   ¦   ¦   ¦   test_block_docstring.py
¦   ¦       ¦   ¦   ¦   ¦   test_callback.py
¦   ¦       ¦   ¦   ¦   ¦   test_character.py
¦   ¦       ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   test_compile_function.py
¦   ¦       ¦   ¦   ¦   ¦   test_crackfortran.py
¦   ¦       ¦   ¦   ¦   ¦   test_docs.py
¦   ¦       ¦   ¦   ¦   ¦   test_f2cmap.py
¦   ¦       ¦   ¦   ¦   ¦   test_f2py2e.py
¦   ¦       ¦   ¦   ¦   ¦   test_kind.py
¦   ¦       ¦   ¦   ¦   ¦   test_mixed.py
¦   ¦       ¦   ¦   ¦   ¦   test_module_doc.py
¦   ¦       ¦   ¦   ¦   ¦   test_parameter.py
¦   ¦       ¦   ¦   ¦   ¦   test_quoted_character.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   test_return_character.py
¦   ¦       ¦   ¦   ¦   ¦   test_return_complex.py
¦   ¦       ¦   ¦   ¦   ¦   test_return_integer.py
¦   ¦       ¦   ¦   ¦   ¦   test_return_logical.py
¦   ¦       ¦   ¦   ¦   ¦   test_return_real.py
¦   ¦       ¦   ¦   ¦   ¦   test_semicolon_split.py
¦   ¦       ¦   ¦   ¦   ¦   test_size.py
¦   ¦       ¦   ¦   ¦   ¦   test_string.py
¦   ¦       ¦   ¦   ¦   ¦   test_symbolic.py
¦   ¦       ¦   ¦   ¦   ¦   test_value_attrspec.py
¦   ¦       ¦   ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---src
¦   ¦       ¦   ¦   ¦   ¦   +---abstract_interface
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       gh18403_mod.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---array_from_pyobj
¦   ¦       ¦   ¦   ¦   ¦   ¦       wrapmodule.c
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---assumed_shape
¦   ¦       ¦   ¦   ¦   ¦   ¦       .f2py_f2cmap
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo_free.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo_mod.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo_use.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       precision.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---block_docstring
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---callback
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       gh17797.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       gh18335.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---cli
¦   ¦       ¦   ¦   ¦   ¦   ¦       hi77.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       hiworld.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---common
¦   ¦       ¦   ¦   ¦   ¦   ¦       block.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---crackfortran
¦   ¦       ¦   ¦   ¦   ¦   ¦       accesstype.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo_deps.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       gh15035.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       gh17859.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       gh2848.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       operators.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       privatemod.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       publicmod.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       pubprivmod.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       unicode_comment.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---f2cmap
¦   ¦       ¦   ¦   ¦   ¦   ¦       .f2py_f2cmap
¦   ¦       ¦   ¦   ¦   ¦   ¦       isoFortranEnvMap.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---kind
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---mixed
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo_fixed.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo_free.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---module_data
¦   ¦       ¦   ¦   ¦   ¦   ¦       mod.mod
¦   ¦       ¦   ¦   ¦   ¦   ¦       module_data_docstring.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---negative_bounds
¦   ¦       ¦   ¦   ¦   ¦   ¦       issue_20853.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---parameter
¦   ¦       ¦   ¦   ¦   ¦   ¦       constant_both.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       constant_compound.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       constant_integer.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       constant_non_compound.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       constant_real.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---quoted_character
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---regression
¦   ¦       ¦   ¦   ¦   ¦   ¦       inout.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---return_character
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---return_complex
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---return_integer
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---return_logical
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---return_real
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo77.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo90.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---size
¦   ¦       ¦   ¦   ¦   ¦   ¦       foo.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---string
¦   ¦       ¦   ¦   ¦   ¦   ¦       char.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       fixed_string.f90
¦   ¦       ¦   ¦   ¦   ¦   ¦       string.f
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---value_attrspec
¦   ¦       ¦   ¦   ¦   ¦           gh21665.f90
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_abstract_interface.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_array_from_pyobj.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assumed_shape.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_block_docstring.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_callback.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_character.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_compile_function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_crackfortran.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_docs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_f2cmap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_f2py2e.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_kind.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_mixed.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_module_doc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_parameter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_quoted_character.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_return_character.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_return_complex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_return_integer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_return_logical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_return_real.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_semicolon_split.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_size.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_symbolic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_value_attrspec.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           auxfuncs.cpython-38.pyc
¦   ¦       ¦   ¦           capi_maps.cpython-38.pyc
¦   ¦       ¦   ¦           cb_rules.cpython-38.pyc
¦   ¦       ¦   ¦           cfuncs.cpython-38.pyc
¦   ¦       ¦   ¦           common_rules.cpython-38.pyc
¦   ¦       ¦   ¦           crackfortran.cpython-38.pyc
¦   ¦       ¦   ¦           diagnose.cpython-38.pyc
¦   ¦       ¦   ¦           f2py2e.cpython-38.pyc
¦   ¦       ¦   ¦           f90mod_rules.cpython-38.pyc
¦   ¦       ¦   ¦           func2subr.cpython-38.pyc
¦   ¦       ¦   ¦           rules.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           symbolic.cpython-38.pyc
¦   ¦       ¦   ¦           use_rules.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           __version__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---fft
¦   ¦       ¦   ¦   ¦   helper.py
¦   ¦       ¦   ¦   ¦   helper.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _pocketfft.py
¦   ¦       ¦   ¦   ¦   _pocketfft.pyi
¦   ¦       ¦   ¦   ¦   _pocketfft_internal.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_helper.py
¦   ¦       ¦   ¦   ¦   ¦   test_pocketfft.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_helper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_pocketfft.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           helper.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           _pocketfft.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---lib
¦   ¦       ¦   ¦   ¦   arraypad.py
¦   ¦       ¦   ¦   ¦   arraypad.pyi
¦   ¦       ¦   ¦   ¦   arraysetops.py
¦   ¦       ¦   ¦   ¦   arraysetops.pyi
¦   ¦       ¦   ¦   ¦   arrayterator.py
¦   ¦       ¦   ¦   ¦   arrayterator.pyi
¦   ¦       ¦   ¦   ¦   format.py
¦   ¦       ¦   ¦   ¦   format.pyi
¦   ¦       ¦   ¦   ¦   function_base.py
¦   ¦       ¦   ¦   ¦   function_base.pyi
¦   ¦       ¦   ¦   ¦   histograms.py
¦   ¦       ¦   ¦   ¦   histograms.pyi
¦   ¦       ¦   ¦   ¦   index_tricks.py
¦   ¦       ¦   ¦   ¦   index_tricks.pyi
¦   ¦       ¦   ¦   ¦   mixins.py
¦   ¦       ¦   ¦   ¦   mixins.pyi
¦   ¦       ¦   ¦   ¦   nanfunctions.py
¦   ¦       ¦   ¦   ¦   nanfunctions.pyi
¦   ¦       ¦   ¦   ¦   npyio.py
¦   ¦       ¦   ¦   ¦   npyio.pyi
¦   ¦       ¦   ¦   ¦   polynomial.py
¦   ¦       ¦   ¦   ¦   polynomial.pyi
¦   ¦       ¦   ¦   ¦   recfunctions.py
¦   ¦       ¦   ¦   ¦   scimath.py
¦   ¦       ¦   ¦   ¦   scimath.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   shape_base.py
¦   ¦       ¦   ¦   ¦   shape_base.pyi
¦   ¦       ¦   ¦   ¦   stride_tricks.py
¦   ¦       ¦   ¦   ¦   stride_tricks.pyi
¦   ¦       ¦   ¦   ¦   twodim_base.py
¦   ¦       ¦   ¦   ¦   twodim_base.pyi
¦   ¦       ¦   ¦   ¦   type_check.py
¦   ¦       ¦   ¦   ¦   type_check.pyi
¦   ¦       ¦   ¦   ¦   ufunclike.py
¦   ¦       ¦   ¦   ¦   ufunclike.pyi
¦   ¦       ¦   ¦   ¦   user_array.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   utils.pyi
¦   ¦       ¦   ¦   ¦   _datasource.py
¦   ¦       ¦   ¦   ¦   _iotools.py
¦   ¦       ¦   ¦   ¦   _version.py
¦   ¦       ¦   ¦   ¦   _version.pyi
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_arraypad.py
¦   ¦       ¦   ¦   ¦   ¦   test_arraysetops.py
¦   ¦       ¦   ¦   ¦   ¦   test_arrayterator.py
¦   ¦       ¦   ¦   ¦   ¦   test_financial_expired.py
¦   ¦       ¦   ¦   ¦   ¦   test_format.py
¦   ¦       ¦   ¦   ¦   ¦   test_function_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_histograms.py
¦   ¦       ¦   ¦   ¦   ¦   test_index_tricks.py
¦   ¦       ¦   ¦   ¦   ¦   test_io.py
¦   ¦       ¦   ¦   ¦   ¦   test_loadtxt.py
¦   ¦       ¦   ¦   ¦   ¦   test_mixins.py
¦   ¦       ¦   ¦   ¦   ¦   test_nanfunctions.py
¦   ¦       ¦   ¦   ¦   ¦   test_packbits.py
¦   ¦       ¦   ¦   ¦   ¦   test_polynomial.py
¦   ¦       ¦   ¦   ¦   ¦   test_recfunctions.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   test_shape_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_stride_tricks.py
¦   ¦       ¦   ¦   ¦   ¦   test_twodim_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_type_check.py
¦   ¦       ¦   ¦   ¦   ¦   test_ufunclike.py
¦   ¦       ¦   ¦   ¦   ¦   test_utils.py
¦   ¦       ¦   ¦   ¦   ¦   test__datasource.py
¦   ¦       ¦   ¦   ¦   ¦   test__iotools.py
¦   ¦       ¦   ¦   ¦   ¦   test__version.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---data
¦   ¦       ¦   ¦   ¦   ¦       py2-objarr.npy
¦   ¦       ¦   ¦   ¦   ¦       py2-objarr.npz
¦   ¦       ¦   ¦   ¦   ¦       py3-objarr.npy
¦   ¦       ¦   ¦   ¦   ¦       py3-objarr.npz
¦   ¦       ¦   ¦   ¦   ¦       python3.npy
¦   ¦       ¦   ¦   ¦   ¦       win64python2.npy
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_arraypad.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arraysetops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arrayterator.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_financial_expired.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_format.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_function_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_histograms.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_index_tricks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_io.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_loadtxt.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_mixins.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_nanfunctions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_packbits.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_polynomial.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_recfunctions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_shape_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_stride_tricks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_twodim_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_type_check.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ufunclike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test__datasource.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test__iotools.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test__version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           arraypad.cpython-38.pyc
¦   ¦       ¦   ¦           arraysetops.cpython-38.pyc
¦   ¦       ¦   ¦           arrayterator.cpython-38.pyc
¦   ¦       ¦   ¦           format.cpython-38.pyc
¦   ¦       ¦   ¦           function_base.cpython-38.pyc
¦   ¦       ¦   ¦           histograms.cpython-38.pyc
¦   ¦       ¦   ¦           index_tricks.cpython-38.pyc
¦   ¦       ¦   ¦           mixins.cpython-38.pyc
¦   ¦       ¦   ¦           nanfunctions.cpython-38.pyc
¦   ¦       ¦   ¦           npyio.cpython-38.pyc
¦   ¦       ¦   ¦           polynomial.cpython-38.pyc
¦   ¦       ¦   ¦           recfunctions.cpython-38.pyc
¦   ¦       ¦   ¦           scimath.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           shape_base.cpython-38.pyc
¦   ¦       ¦   ¦           stride_tricks.cpython-38.pyc
¦   ¦       ¦   ¦           twodim_base.cpython-38.pyc
¦   ¦       ¦   ¦           type_check.cpython-38.pyc
¦   ¦       ¦   ¦           ufunclike.cpython-38.pyc
¦   ¦       ¦   ¦           user_array.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           _datasource.cpython-38.pyc
¦   ¦       ¦   ¦           _iotools.cpython-38.pyc
¦   ¦       ¦   ¦           _version.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---linalg
¦   ¦       ¦   ¦   ¦   lapack_lite.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   linalg.py
¦   ¦       ¦   ¦   ¦   linalg.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _umath_linalg.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_deprecations.py
¦   ¦       ¦   ¦   ¦   ¦   test_linalg.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_deprecations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_linalg.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           linalg.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---ma
¦   ¦       ¦   ¦   ¦   bench.py
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   core.pyi
¦   ¦       ¦   ¦   ¦   extras.py
¦   ¦       ¦   ¦   ¦   extras.pyi
¦   ¦       ¦   ¦   ¦   mrecords.py
¦   ¦       ¦   ¦   ¦   mrecords.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   testutils.py
¦   ¦       ¦   ¦   ¦   timer_comparison.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_core.py
¦   ¦       ¦   ¦   ¦   ¦   test_deprecations.py
¦   ¦       ¦   ¦   ¦   ¦   test_extras.py
¦   ¦       ¦   ¦   ¦   ¦   test_mrecords.py
¦   ¦       ¦   ¦   ¦   ¦   test_old_ma.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   test_subclassing.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_core.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_deprecations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_extras.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_mrecords.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_old_ma.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_subclassing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           bench.cpython-38.pyc
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           extras.cpython-38.pyc
¦   ¦       ¦   ¦           mrecords.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           testutils.cpython-38.pyc
¦   ¦       ¦   ¦           timer_comparison.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---matrixlib
¦   ¦       ¦   ¦   ¦   defmatrix.py
¦   ¦       ¦   ¦   ¦   defmatrix.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_defmatrix.py
¦   ¦       ¦   ¦   ¦   ¦   test_interaction.py
¦   ¦       ¦   ¦   ¦   ¦   test_masked_matrix.py
¦   ¦       ¦   ¦   ¦   ¦   test_matrix_linalg.py
¦   ¦       ¦   ¦   ¦   ¦   test_multiarray.py
¦   ¦       ¦   ¦   ¦   ¦   test_numeric.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_defmatrix.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_interaction.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_masked_matrix.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_matrix_linalg.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_multiarray.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           defmatrix.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---polynomial
¦   ¦       ¦   ¦   ¦   chebyshev.py
¦   ¦       ¦   ¦   ¦   chebyshev.pyi
¦   ¦       ¦   ¦   ¦   hermite.py
¦   ¦       ¦   ¦   ¦   hermite.pyi
¦   ¦       ¦   ¦   ¦   hermite_e.py
¦   ¦       ¦   ¦   ¦   hermite_e.pyi
¦   ¦       ¦   ¦   ¦   laguerre.py
¦   ¦       ¦   ¦   ¦   laguerre.pyi
¦   ¦       ¦   ¦   ¦   legendre.py
¦   ¦       ¦   ¦   ¦   legendre.pyi
¦   ¦       ¦   ¦   ¦   polynomial.py
¦   ¦       ¦   ¦   ¦   polynomial.pyi
¦   ¦       ¦   ¦   ¦   polyutils.py
¦   ¦       ¦   ¦   ¦   polyutils.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _polybase.py
¦   ¦       ¦   ¦   ¦   _polybase.pyi
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_chebyshev.py
¦   ¦       ¦   ¦   ¦   ¦   test_classes.py
¦   ¦       ¦   ¦   ¦   ¦   test_hermite.py
¦   ¦       ¦   ¦   ¦   ¦   test_hermite_e.py
¦   ¦       ¦   ¦   ¦   ¦   test_laguerre.py
¦   ¦       ¦   ¦   ¦   ¦   test_legendre.py
¦   ¦       ¦   ¦   ¦   ¦   test_polynomial.py
¦   ¦       ¦   ¦   ¦   ¦   test_polyutils.py
¦   ¦       ¦   ¦   ¦   ¦   test_printing.py
¦   ¦       ¦   ¦   ¦   ¦   test_symbol.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_chebyshev.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_classes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_hermite.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_hermite_e.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_laguerre.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_legendre.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_polynomial.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_polyutils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_printing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_symbol.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           chebyshev.cpython-38.pyc
¦   ¦       ¦   ¦           hermite.cpython-38.pyc
¦   ¦       ¦   ¦           hermite_e.cpython-38.pyc
¦   ¦       ¦   ¦           laguerre.cpython-38.pyc
¦   ¦       ¦   ¦           legendre.cpython-38.pyc
¦   ¦       ¦   ¦           polynomial.cpython-38.pyc
¦   ¦       ¦   ¦           polyutils.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           _polybase.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---random
¦   ¦       ¦   ¦   ¦   bit_generator.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   bit_generator.pxd
¦   ¦       ¦   ¦   ¦   bit_generator.pyi
¦   ¦       ¦   ¦   ¦   c_distributions.pxd
¦   ¦       ¦   ¦   ¦   mtrand.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   mtrand.pyi
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _bounded_integers.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _bounded_integers.pxd
¦   ¦       ¦   ¦   ¦   _common.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _common.pxd
¦   ¦       ¦   ¦   ¦   _generator.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _generator.pyi
¦   ¦       ¦   ¦   ¦   _mt19937.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _mt19937.pyi
¦   ¦       ¦   ¦   ¦   _pcg64.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _pcg64.pyi
¦   ¦       ¦   ¦   ¦   _philox.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _philox.pyi
¦   ¦       ¦   ¦   ¦   _pickle.py
¦   ¦       ¦   ¦   ¦   _sfc64.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   _sfc64.pyi
¦   ¦       ¦   ¦   ¦   __init__.pxd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---lib
¦   ¦       ¦   ¦   ¦       npyrandom.lib
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_direct.py
¦   ¦       ¦   ¦   ¦   ¦   test_extending.py
¦   ¦       ¦   ¦   ¦   ¦   test_generator_mt19937.py
¦   ¦       ¦   ¦   ¦   ¦   test_generator_mt19937_regressions.py
¦   ¦       ¦   ¦   ¦   ¦   test_random.py
¦   ¦       ¦   ¦   ¦   ¦   test_randomstate.py
¦   ¦       ¦   ¦   ¦   ¦   test_randomstate_regression.py
¦   ¦       ¦   ¦   ¦   ¦   test_regression.py
¦   ¦       ¦   ¦   ¦   ¦   test_seed_sequence.py
¦   ¦       ¦   ¦   ¦   ¦   test_smoke.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---data
¦   ¦       ¦   ¦   ¦   ¦   ¦   mt19937-testset-1.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   mt19937-testset-2.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64-testset-1.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64-testset-2.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64dxsm-testset-1.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   pcg64dxsm-testset-2.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   philox-testset-1.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   philox-testset-2.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   sfc64-testset-1.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   sfc64-testset-2.csv
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_direct.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_extending.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_generator_mt19937.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_generator_mt19937_regressions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_random.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_randomstate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_randomstate_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_regression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_seed_sequence.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_smoke.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---_examples
¦   ¦       ¦   ¦   ¦   +---cffi
¦   ¦       ¦   ¦   ¦   ¦   ¦   extending.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   parse.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           extending.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           parse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---cython
¦   ¦       ¦   ¦   ¦   ¦   ¦   extending.pyx
¦   ¦       ¦   ¦   ¦   ¦   ¦   extending_distributions.pyx
¦   ¦       ¦   ¦   ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---numba
¦   ¦       ¦   ¦   ¦       ¦   extending.py
¦   ¦       ¦   ¦   ¦       ¦   extending_distributions.py
¦   ¦       ¦   ¦   ¦       ¦   
¦   ¦       ¦   ¦   ¦       +---__pycache__
¦   ¦       ¦   ¦   ¦               extending.cpython-38.pyc
¦   ¦       ¦   ¦   ¦               extending_distributions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦               
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           _pickle.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---testing
¦   ¦       ¦   ¦   ¦   print_coercion_tables.py
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_doctesting.py
¦   ¦       ¦   ¦   ¦   ¦   test_utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_doctesting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---_private
¦   ¦       ¦   ¦   ¦   ¦   decorators.py
¦   ¦       ¦   ¦   ¦   ¦   extbuild.py
¦   ¦       ¦   ¦   ¦   ¦   noseclasses.py
¦   ¦       ¦   ¦   ¦   ¦   nosetester.py
¦   ¦       ¦   ¦   ¦   ¦   parameterized.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   utils.pyi
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           decorators.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           extbuild.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           noseclasses.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           nosetester.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           parameterized.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           print_coercion_tables.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   test_ctypeslib.py
¦   ¦       ¦   ¦   ¦   test_lazyloading.py
¦   ¦       ¦   ¦   ¦   test_matlib.py
¦   ¦       ¦   ¦   ¦   test_numpy_version.py
¦   ¦       ¦   ¦   ¦   test_public_api.py
¦   ¦       ¦   ¦   ¦   test_reloading.py
¦   ¦       ¦   ¦   ¦   test_scripts.py
¦   ¦       ¦   ¦   ¦   test_warnings.py
¦   ¦       ¦   ¦   ¦   test__all__.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           test_ctypeslib.cpython-38.pyc
¦   ¦       ¦   ¦           test_lazyloading.cpython-38.pyc
¦   ¦       ¦   ¦           test_matlib.cpython-38.pyc
¦   ¦       ¦   ¦           test_numpy_version.cpython-38.pyc
¦   ¦       ¦   ¦           test_public_api.cpython-38.pyc
¦   ¦       ¦   ¦           test_reloading.cpython-38.pyc
¦   ¦       ¦   ¦           test_scripts.cpython-38.pyc
¦   ¦       ¦   ¦           test_warnings.cpython-38.pyc
¦   ¦       ¦   ¦           test__all__.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---typing
¦   ¦       ¦   ¦   ¦   mypy_plugin.py
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tests
¦   ¦       ¦   ¦   ¦   ¦   test_generic_alias.py
¦   ¦       ¦   ¦   ¦   ¦   test_isfile.py
¦   ¦       ¦   ¦   ¦   ¦   test_runtime.py
¦   ¦       ¦   ¦   ¦   ¦   test_typing.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---data
¦   ¦       ¦   ¦   ¦   ¦   ¦   mypy.ini
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---fail
¦   ¦       ¦   ¦   ¦   ¦   ¦       arithmetic.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       arrayprint.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       arrayterator.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       array_constructors.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       array_like.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       array_pad.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       bitwise_ops.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       char.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       chararray.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       comparisons.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       constants.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       datasource.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       dtype.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       einsumfunc.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       false_positives.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       flatiter.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       fromnumeric.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       histograms.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       index_tricks.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       lib_function_base.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       lib_polynomial.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       lib_utils.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       lib_version.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       linalg.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       memmap.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       modules.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       multiarray.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       ndarray.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       ndarray_misc.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       nditer.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       nested_sequence.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       npyio.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       numerictypes.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       random.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       rec.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       scalars.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       shape_base.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       stride_tricks.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       testing.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       twodim_base.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       type_check.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       ufunclike.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       ufuncs.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       ufunc_config.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       warnings_and_errors.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---misc
¦   ¦       ¦   ¦   ¦   ¦   ¦       extended_precision.pyi
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---pass
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   arrayprint.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   arrayterator.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   array_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   array_like.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   bitwise_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   comparisons.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   einsumfunc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   flatiter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   fromnumeric.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   index_tricks.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   lib_utils.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   lib_version.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   literal.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   mod.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   modules.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   multiarray.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ndarray_conversion.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ndarray_misc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ndarray_shape_manipulation.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   numeric.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   numerictypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   random.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   scalars.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   simple.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   simple_py3.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ufunclike.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ufuncs.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   ufunc_config.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   warnings_and_errors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           arrayprint.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           arrayterator.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           array_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           array_like.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           bitwise_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           comparisons.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           einsumfunc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           flatiter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           fromnumeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           index_tricks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           lib_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           lib_version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           literal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           mod.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           modules.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           multiarray.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           ndarray_conversion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           ndarray_misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           ndarray_shape_manipulation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           numerictypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           random.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           scalars.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           simple.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           simple_py3.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           ufunclike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           ufuncs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           ufunc_config.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           warnings_and_errors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---reveal
¦   ¦       ¦   ¦   ¦   ¦           arithmetic.pyi
¦   ¦       ¦   ¦   ¦   ¦           arraypad.pyi
¦   ¦       ¦   ¦   ¦   ¦           arrayprint.pyi
¦   ¦       ¦   ¦   ¦   ¦           arraysetops.pyi
¦   ¦       ¦   ¦   ¦   ¦           arrayterator.pyi
¦   ¦       ¦   ¦   ¦   ¦           array_constructors.pyi
¦   ¦       ¦   ¦   ¦   ¦           bitwise_ops.pyi
¦   ¦       ¦   ¦   ¦   ¦           char.pyi
¦   ¦       ¦   ¦   ¦   ¦           chararray.pyi
¦   ¦       ¦   ¦   ¦   ¦           comparisons.pyi
¦   ¦       ¦   ¦   ¦   ¦           constants.pyi
¦   ¦       ¦   ¦   ¦   ¦           ctypeslib.pyi
¦   ¦       ¦   ¦   ¦   ¦           datasource.pyi
¦   ¦       ¦   ¦   ¦   ¦           dtype.pyi
¦   ¦       ¦   ¦   ¦   ¦           einsumfunc.pyi
¦   ¦       ¦   ¦   ¦   ¦           emath.pyi
¦   ¦       ¦   ¦   ¦   ¦           false_positives.pyi
¦   ¦       ¦   ¦   ¦   ¦           fft.pyi
¦   ¦       ¦   ¦   ¦   ¦           flatiter.pyi
¦   ¦       ¦   ¦   ¦   ¦           fromnumeric.pyi
¦   ¦       ¦   ¦   ¦   ¦           getlimits.pyi
¦   ¦       ¦   ¦   ¦   ¦           histograms.pyi
¦   ¦       ¦   ¦   ¦   ¦           index_tricks.pyi
¦   ¦       ¦   ¦   ¦   ¦           lib_function_base.pyi
¦   ¦       ¦   ¦   ¦   ¦           lib_polynomial.pyi
¦   ¦       ¦   ¦   ¦   ¦           lib_utils.pyi
¦   ¦       ¦   ¦   ¦   ¦           lib_version.pyi
¦   ¦       ¦   ¦   ¦   ¦           linalg.pyi
¦   ¦       ¦   ¦   ¦   ¦           matrix.pyi
¦   ¦       ¦   ¦   ¦   ¦           memmap.pyi
¦   ¦       ¦   ¦   ¦   ¦           mod.pyi
¦   ¦       ¦   ¦   ¦   ¦           modules.pyi
¦   ¦       ¦   ¦   ¦   ¦           multiarray.pyi
¦   ¦       ¦   ¦   ¦   ¦           nbit_base_example.pyi
¦   ¦       ¦   ¦   ¦   ¦           ndarray_conversion.pyi
¦   ¦       ¦   ¦   ¦   ¦           ndarray_misc.pyi
¦   ¦       ¦   ¦   ¦   ¦           ndarray_shape_manipulation.pyi
¦   ¦       ¦   ¦   ¦   ¦           nditer.pyi
¦   ¦       ¦   ¦   ¦   ¦           nested_sequence.pyi
¦   ¦       ¦   ¦   ¦   ¦           npyio.pyi
¦   ¦       ¦   ¦   ¦   ¦           numeric.pyi
¦   ¦       ¦   ¦   ¦   ¦           numerictypes.pyi
¦   ¦       ¦   ¦   ¦   ¦           random.pyi
¦   ¦       ¦   ¦   ¦   ¦           rec.pyi
¦   ¦       ¦   ¦   ¦   ¦           scalars.pyi
¦   ¦       ¦   ¦   ¦   ¦           shape_base.pyi
¦   ¦       ¦   ¦   ¦   ¦           stride_tricks.pyi
¦   ¦       ¦   ¦   ¦   ¦           testing.pyi
¦   ¦       ¦   ¦   ¦   ¦           twodim_base.pyi
¦   ¦       ¦   ¦   ¦   ¦           type_check.pyi
¦   ¦       ¦   ¦   ¦   ¦           ufunclike.pyi
¦   ¦       ¦   ¦   ¦   ¦           ufuncs.pyi
¦   ¦       ¦   ¦   ¦   ¦           ufunc_config.pyi
¦   ¦       ¦   ¦   ¦   ¦           version.pyi
¦   ¦       ¦   ¦   ¦   ¦           warnings_and_errors.pyi
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_generic_alias.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_isfile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_runtime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_typing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           mypy_plugin.cpython-38.pyc
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_pyinstaller
¦   ¦       ¦   ¦   ¦   hook-numpy.py
¦   ¦       ¦   ¦   ¦   pyinstaller-smoke.py
¦   ¦       ¦   ¦   ¦   test_pyinstaller.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           hook-numpy.cpython-38.pyc
¦   ¦       ¦   ¦           pyinstaller-smoke.cpython-38.pyc
¦   ¦       ¦   ¦           test_pyinstaller.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_typing
¦   ¦       ¦   ¦   ¦   setup.py
¦   ¦       ¦   ¦   ¦   _add_docstring.py
¦   ¦       ¦   ¦   ¦   _array_like.py
¦   ¦       ¦   ¦   ¦   _callable.pyi
¦   ¦       ¦   ¦   ¦   _char_codes.py
¦   ¦       ¦   ¦   ¦   _dtype_like.py
¦   ¦       ¦   ¦   ¦   _extended_precision.py
¦   ¦       ¦   ¦   ¦   _generic_alias.py
¦   ¦       ¦   ¦   ¦   _nbit.py
¦   ¦       ¦   ¦   ¦   _nested_sequence.py
¦   ¦       ¦   ¦   ¦   _scalars.py
¦   ¦       ¦   ¦   ¦   _shape.py
¦   ¦       ¦   ¦   ¦   _ufunc.pyi
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           setup.cpython-38.pyc
¦   ¦       ¦   ¦           _add_docstring.cpython-38.pyc
¦   ¦       ¦   ¦           _array_like.cpython-38.pyc
¦   ¦       ¦   ¦           _char_codes.cpython-38.pyc
¦   ¦       ¦   ¦           _dtype_like.cpython-38.pyc
¦   ¦       ¦   ¦           _extended_precision.cpython-38.pyc
¦   ¦       ¦   ¦           _generic_alias.cpython-38.pyc
¦   ¦       ¦   ¦           _nbit.cpython-38.pyc
¦   ¦       ¦   ¦           _nested_sequence.cpython-38.pyc
¦   ¦       ¦   ¦           _scalars.cpython-38.pyc
¦   ¦       ¦   ¦           _shape.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           conftest.cpython-38.pyc
¦   ¦       ¦           ctypeslib.cpython-38.pyc
¦   ¦       ¦           dual.cpython-38.pyc
¦   ¦       ¦           matlib.cpython-38.pyc
¦   ¦       ¦           setup.cpython-38.pyc
¦   ¦       ¦           version.cpython-38.pyc
¦   ¦       ¦           _distributor_init.cpython-38.pyc
¦   ¦       ¦           _globals.cpython-38.pyc
¦   ¦       ¦           _pytesttester.cpython-38.pyc
¦   ¦       ¦           _version.cpython-38.pyc
¦   ¦       ¦           __config__.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---numpy-1.24.1.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       LICENSES_bundled.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pandas
¦   ¦       ¦   ¦   conftest.py
¦   ¦       ¦   ¦   testing.py
¦   ¦       ¦   ¦   _typing.py
¦   ¦       ¦   ¦   _version.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---api
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---extensions
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---indexers
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---interchange
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---types
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---arrays
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---compat
¦   ¦       ¦   ¦   ¦   compressors.py
¦   ¦       ¦   ¦   ¦   pickle_compat.py
¦   ¦       ¦   ¦   ¦   pyarrow.py
¦   ¦       ¦   ¦   ¦   _constants.py
¦   ¦       ¦   ¦   ¦   _optional.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---numpy
¦   ¦       ¦   ¦   ¦   ¦   function.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           compressors.cpython-38.pyc
¦   ¦       ¦   ¦           pickle_compat.cpython-38.pyc
¦   ¦       ¦   ¦           pyarrow.cpython-38.pyc
¦   ¦       ¦   ¦           _constants.cpython-38.pyc
¦   ¦       ¦   ¦           _optional.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---core
¦   ¦       ¦   ¦   ¦   accessor.py
¦   ¦       ¦   ¦   ¦   algorithms.py
¦   ¦       ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   apply.py
¦   ¦       ¦   ¦   ¦   arraylike.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   config_init.py
¦   ¦       ¦   ¦   ¦   construction.py
¦   ¦       ¦   ¦   ¦   flags.py
¦   ¦       ¦   ¦   ¦   frame.py
¦   ¦       ¦   ¦   ¦   generic.py
¦   ¦       ¦   ¦   ¦   indexing.py
¦   ¦       ¦   ¦   ¦   missing.py
¦   ¦       ¦   ¦   ¦   nanops.py
¦   ¦       ¦   ¦   ¦   resample.py
¦   ¦       ¦   ¦   ¦   roperator.py
¦   ¦       ¦   ¦   ¦   sample.py
¦   ¦       ¦   ¦   ¦   series.py
¦   ¦       ¦   ¦   ¦   shared_docs.py
¦   ¦       ¦   ¦   ¦   sorting.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---arrays
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   boolean.py
¦   ¦       ¦   ¦   ¦   ¦   categorical.py
¦   ¦       ¦   ¦   ¦   ¦   datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   datetimes.py
¦   ¦       ¦   ¦   ¦   ¦   floating.py
¦   ¦       ¦   ¦   ¦   ¦   integer.py
¦   ¦       ¦   ¦   ¦   ¦   interval.py
¦   ¦       ¦   ¦   ¦   ¦   masked.py
¦   ¦       ¦   ¦   ¦   ¦   numeric.py
¦   ¦       ¦   ¦   ¦   ¦   numpy_.py
¦   ¦       ¦   ¦   ¦   ¦   period.py
¦   ¦       ¦   ¦   ¦   ¦   string_.py
¦   ¦       ¦   ¦   ¦   ¦   string_arrow.py
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.py
¦   ¦       ¦   ¦   ¦   ¦   _mixins.py
¦   ¦       ¦   ¦   ¦   ¦   _ranges.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---arrow
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   extension_types.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   _arrow_utils.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           extension_types.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           _arrow_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---sparse
¦   ¦       ¦   ¦   ¦   ¦   ¦   accessor.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   scipy_sparse.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           scipy_sparse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           boolean.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           datetimes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           floating.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           integer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           masked.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           numpy_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           string_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           string_arrow.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           timedeltas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _mixins.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _ranges.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---array_algos
¦   ¦       ¦   ¦   ¦   ¦   datetimelike_accumulations.py
¦   ¦       ¦   ¦   ¦   ¦   masked_accumulations.py
¦   ¦       ¦   ¦   ¦   ¦   masked_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   putmask.py
¦   ¦       ¦   ¦   ¦   ¦   quantile.py
¦   ¦       ¦   ¦   ¦   ¦   replace.py
¦   ¦       ¦   ¦   ¦   ¦   take.py
¦   ¦       ¦   ¦   ¦   ¦   transforms.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           datetimelike_accumulations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           masked_accumulations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           masked_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           putmask.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           quantile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           replace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           take.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           transforms.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---computation
¦   ¦       ¦   ¦   ¦   ¦   align.py
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   check.py
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   engines.py
¦   ¦       ¦   ¦   ¦   ¦   eval.py
¦   ¦       ¦   ¦   ¦   ¦   expr.py
¦   ¦       ¦   ¦   ¦   ¦   expressions.py
¦   ¦       ¦   ¦   ¦   ¦   ops.py
¦   ¦       ¦   ¦   ¦   ¦   parsing.py
¦   ¦       ¦   ¦   ¦   ¦   pytables.py
¦   ¦       ¦   ¦   ¦   ¦   scope.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           align.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           check.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           engines.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           eval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           expr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           expressions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           parsing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pytables.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scope.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---dtypes
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   astype.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   cast.py
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   concat.py
¦   ¦       ¦   ¦   ¦   ¦   dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   generic.py
¦   ¦       ¦   ¦   ¦   ¦   inference.py
¦   ¦       ¦   ¦   ¦   ¦   missing.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cast.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           generic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           inference.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---groupby
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   categorical.py
¦   ¦       ¦   ¦   ¦   ¦   generic.py
¦   ¦       ¦   ¦   ¦   ¦   groupby.py
¦   ¦       ¦   ¦   ¦   ¦   grouper.py
¦   ¦       ¦   ¦   ¦   ¦   indexing.py
¦   ¦       ¦   ¦   ¦   ¦   numba_.py
¦   ¦       ¦   ¦   ¦   ¦   ops.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           generic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           grouper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           numba_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---indexers
¦   ¦       ¦   ¦   ¦   ¦   objects.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           objects.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---indexes
¦   ¦       ¦   ¦   ¦   ¦   accessors.py
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   category.py
¦   ¦       ¦   ¦   ¦   ¦   datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   datetimes.py
¦   ¦       ¦   ¦   ¦   ¦   extension.py
¦   ¦       ¦   ¦   ¦   ¦   frozen.py
¦   ¦       ¦   ¦   ¦   ¦   interval.py
¦   ¦       ¦   ¦   ¦   ¦   multi.py
¦   ¦       ¦   ¦   ¦   ¦   period.py
¦   ¦       ¦   ¦   ¦   ¦   range.py
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           accessors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           category.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           datetimes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           extension.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           frozen.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           multi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           range.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           timedeltas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---interchange
¦   ¦       ¦   ¦   ¦   ¦   buffer.py
¦   ¦       ¦   ¦   ¦   ¦   column.py
¦   ¦       ¦   ¦   ¦   ¦   dataframe.py
¦   ¦       ¦   ¦   ¦   ¦   dataframe_protocol.py
¦   ¦       ¦   ¦   ¦   ¦   from_dataframe.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           buffer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           column.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dataframe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dataframe_protocol.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           from_dataframe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---internals
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   array_manager.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   blocks.py
¦   ¦       ¦   ¦   ¦   ¦   concat.py
¦   ¦       ¦   ¦   ¦   ¦   construction.py
¦   ¦       ¦   ¦   ¦   ¦   managers.py
¦   ¦       ¦   ¦   ¦   ¦   ops.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           array_manager.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           blocks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           construction.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           managers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---methods
¦   ¦       ¦   ¦   ¦   ¦   describe.py
¦   ¦       ¦   ¦   ¦   ¦   selectn.py
¦   ¦       ¦   ¦   ¦   ¦   to_dict.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           describe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           selectn.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           to_dict.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ops
¦   ¦       ¦   ¦   ¦   ¦   array_ops.py
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   dispatch.py
¦   ¦       ¦   ¦   ¦   ¦   docstrings.py
¦   ¦       ¦   ¦   ¦   ¦   invalid.py
¦   ¦       ¦   ¦   ¦   ¦   mask_ops.py
¦   ¦       ¦   ¦   ¦   ¦   methods.py
¦   ¦       ¦   ¦   ¦   ¦   missing.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           array_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dispatch.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           docstrings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           invalid.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mask_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           methods.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---reshape
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   concat.py
¦   ¦       ¦   ¦   ¦   ¦   encoding.py
¦   ¦       ¦   ¦   ¦   ¦   melt.py
¦   ¦       ¦   ¦   ¦   ¦   merge.py
¦   ¦       ¦   ¦   ¦   ¦   pivot.py
¦   ¦       ¦   ¦   ¦   ¦   reshape.py
¦   ¦       ¦   ¦   ¦   ¦   tile.py
¦   ¦       ¦   ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           encoding.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           melt.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           merge.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pivot.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           reshape.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---sparse
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---strings
¦   ¦       ¦   ¦   ¦   ¦   accessor.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   object_array.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           object_array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tools
¦   ¦       ¦   ¦   ¦   ¦   datetimes.py
¦   ¦       ¦   ¦   ¦   ¦   numeric.py
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.py
¦   ¦       ¦   ¦   ¦   ¦   times.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           datetimes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           timedeltas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           times.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---util
¦   ¦       ¦   ¦   ¦   ¦   hashing.py
¦   ¦       ¦   ¦   ¦   ¦   numba_.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           hashing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           numba_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---window
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   doc.py
¦   ¦       ¦   ¦   ¦   ¦   ewm.py
¦   ¦       ¦   ¦   ¦   ¦   expanding.py
¦   ¦       ¦   ¦   ¦   ¦   numba_.py
¦   ¦       ¦   ¦   ¦   ¦   online.py
¦   ¦       ¦   ¦   ¦   ¦   rolling.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           doc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ewm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           expanding.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           numba_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           online.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           rolling.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---_numba
¦   ¦       ¦   ¦   ¦   ¦   executor.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---kernels
¦   ¦       ¦   ¦   ¦   ¦   ¦   mean_.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   min_max_.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   shared.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   sum_.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   var_.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           mean_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           min_max_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           shared.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           sum_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           var_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           executor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           accessor.cpython-38.pyc
¦   ¦       ¦   ¦           algorithms.cpython-38.pyc
¦   ¦       ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦           apply.cpython-38.pyc
¦   ¦       ¦   ¦           arraylike.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦           config_init.cpython-38.pyc
¦   ¦       ¦   ¦           construction.cpython-38.pyc
¦   ¦       ¦   ¦           flags.cpython-38.pyc
¦   ¦       ¦   ¦           frame.cpython-38.pyc
¦   ¦       ¦   ¦           generic.cpython-38.pyc
¦   ¦       ¦   ¦           indexing.cpython-38.pyc
¦   ¦       ¦   ¦           missing.cpython-38.pyc
¦   ¦       ¦   ¦           nanops.cpython-38.pyc
¦   ¦       ¦   ¦           resample.cpython-38.pyc
¦   ¦       ¦   ¦           roperator.cpython-38.pyc
¦   ¦       ¦   ¦           sample.cpython-38.pyc
¦   ¦       ¦   ¦           series.cpython-38.pyc
¦   ¦       ¦   ¦           shared_docs.cpython-38.pyc
¦   ¦       ¦   ¦           sorting.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---errors
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---io
¦   ¦       ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   clipboards.py
¦   ¦       ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   feather_format.py
¦   ¦       ¦   ¦   ¦   gbq.py
¦   ¦       ¦   ¦   ¦   html.py
¦   ¦       ¦   ¦   ¦   orc.py
¦   ¦       ¦   ¦   ¦   parquet.py
¦   ¦       ¦   ¦   ¦   pickle.py
¦   ¦       ¦   ¦   ¦   pytables.py
¦   ¦       ¦   ¦   ¦   spss.py
¦   ¦       ¦   ¦   ¦   sql.py
¦   ¦       ¦   ¦   ¦   stata.py
¦   ¦       ¦   ¦   ¦   xml.py
¦   ¦       ¦   ¦   ¦   _util.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---clipboard
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---excel
¦   ¦       ¦   ¦   ¦   ¦   _base.py
¦   ¦       ¦   ¦   ¦   ¦   _odfreader.py
¦   ¦       ¦   ¦   ¦   ¦   _odswriter.py
¦   ¦       ¦   ¦   ¦   ¦   _openpyxl.py
¦   ¦       ¦   ¦   ¦   ¦   _pyxlsb.py
¦   ¦       ¦   ¦   ¦   ¦   _util.py
¦   ¦       ¦   ¦   ¦   ¦   _xlrd.py
¦   ¦       ¦   ¦   ¦   ¦   _xlsxwriter.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           _base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _odfreader.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _odswriter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _openpyxl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _pyxlsb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _xlrd.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _xlsxwriter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---formats
¦   ¦       ¦   ¦   ¦   ¦   console.py
¦   ¦       ¦   ¦   ¦   ¦   css.py
¦   ¦       ¦   ¦   ¦   ¦   csvs.py
¦   ¦       ¦   ¦   ¦   ¦   excel.py
¦   ¦       ¦   ¦   ¦   ¦   format.py
¦   ¦       ¦   ¦   ¦   ¦   html.py
¦   ¦       ¦   ¦   ¦   ¦   info.py
¦   ¦       ¦   ¦   ¦   ¦   latex.py
¦   ¦       ¦   ¦   ¦   ¦   printing.py
¦   ¦       ¦   ¦   ¦   ¦   string.py
¦   ¦       ¦   ¦   ¦   ¦   style.py
¦   ¦       ¦   ¦   ¦   ¦   style_render.py
¦   ¦       ¦   ¦   ¦   ¦   xml.py
¦   ¦       ¦   ¦   ¦   ¦   _color_data.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---templates
¦   ¦       ¦   ¦   ¦   ¦       html.tpl
¦   ¦       ¦   ¦   ¦   ¦       html_style.tpl
¦   ¦       ¦   ¦   ¦   ¦       html_table.tpl
¦   ¦       ¦   ¦   ¦   ¦       latex.tpl
¦   ¦       ¦   ¦   ¦   ¦       latex_longtable.tpl
¦   ¦       ¦   ¦   ¦   ¦       latex_table.tpl
¦   ¦       ¦   ¦   ¦   ¦       string.tpl
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           console.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           css.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           csvs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           excel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           format.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           html.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           latex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           printing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           style.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           style_render.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           xml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _color_data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---json
¦   ¦       ¦   ¦   ¦   ¦   _json.py
¦   ¦       ¦   ¦   ¦   ¦   _normalize.py
¦   ¦       ¦   ¦   ¦   ¦   _table_schema.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           _json.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _normalize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _table_schema.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---parsers
¦   ¦       ¦   ¦   ¦   ¦   arrow_parser_wrapper.py
¦   ¦       ¦   ¦   ¦   ¦   base_parser.py
¦   ¦       ¦   ¦   ¦   ¦   c_parser_wrapper.py
¦   ¦       ¦   ¦   ¦   ¦   python_parser.py
¦   ¦       ¦   ¦   ¦   ¦   readers.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           arrow_parser_wrapper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base_parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           c_parser_wrapper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           python_parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           readers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---sas
¦   ¦       ¦   ¦   ¦   ¦   byteswap.pyx
¦   ¦       ¦   ¦   ¦   ¦   sas.pyx
¦   ¦       ¦   ¦   ¦   ¦   sas7bdat.py
¦   ¦       ¦   ¦   ¦   ¦   sasreader.py
¦   ¦       ¦   ¦   ¦   ¦   sas_constants.py
¦   ¦       ¦   ¦   ¦   ¦   sas_xport.py
¦   ¦       ¦   ¦   ¦   ¦   _byteswap.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   _byteswap.pyi
¦   ¦       ¦   ¦   ¦   ¦   _sas.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   _sas.pyi
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           sas7bdat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sasreader.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sas_constants.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sas_xport.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦           clipboards.cpython-38.pyc
¦   ¦       ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦           feather_format.cpython-38.pyc
¦   ¦       ¦   ¦           gbq.cpython-38.pyc
¦   ¦       ¦   ¦           html.cpython-38.pyc
¦   ¦       ¦   ¦           orc.cpython-38.pyc
¦   ¦       ¦   ¦           parquet.cpython-38.pyc
¦   ¦       ¦   ¦           pickle.cpython-38.pyc
¦   ¦       ¦   ¦           pytables.cpython-38.pyc
¦   ¦       ¦   ¦           spss.cpython-38.pyc
¦   ¦       ¦   ¦           sql.cpython-38.pyc
¦   ¦       ¦   ¦           stata.cpython-38.pyc
¦   ¦       ¦   ¦           xml.cpython-38.pyc
¦   ¦       ¦   ¦           _util.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---plotting
¦   ¦       ¦   ¦   ¦   _core.py
¦   ¦       ¦   ¦   ¦   _misc.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---_matplotlib
¦   ¦       ¦   ¦   ¦   ¦   boxplot.py
¦   ¦       ¦   ¦   ¦   ¦   converter.py
¦   ¦       ¦   ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   ¦   groupby.py
¦   ¦       ¦   ¦   ¦   ¦   hist.py
¦   ¦       ¦   ¦   ¦   ¦   misc.py
¦   ¦       ¦   ¦   ¦   ¦   style.py
¦   ¦       ¦   ¦   ¦   ¦   timeseries.py
¦   ¦       ¦   ¦   ¦   ¦   tools.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           boxplot.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           converter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           style.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           timeseries.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tools.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           _core.cpython-38.pyc
¦   ¦       ¦   ¦           _misc.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   test_aggregation.py
¦   ¦       ¦   ¦   ¦   test_algos.py
¦   ¦       ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   test_downstream.py
¦   ¦       ¦   ¦   ¦   test_errors.py
¦   ¦       ¦   ¦   ¦   test_expressions.py
¦   ¦       ¦   ¦   ¦   test_flags.py
¦   ¦       ¦   ¦   ¦   test_multilevel.py
¦   ¦       ¦   ¦   ¦   test_nanops.py
¦   ¦       ¦   ¦   ¦   test_optional_dependency.py
¦   ¦       ¦   ¦   ¦   test_register_accessor.py
¦   ¦       ¦   ¦   ¦   test_sorting.py
¦   ¦       ¦   ¦   ¦   test_take.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---api
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_types.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_types.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---apply
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_frame_apply.py
¦   ¦       ¦   ¦   ¦   ¦   test_frame_apply_relabeling.py
¦   ¦       ¦   ¦   ¦   ¦   test_frame_transform.py
¦   ¦       ¦   ¦   ¦   ¦   test_invalid_arg.py
¦   ¦       ¦   ¦   ¦   ¦   test_series_apply.py
¦   ¦       ¦   ¦   ¦   ¦   test_series_apply_relabeling.py
¦   ¦       ¦   ¦   ¦   ¦   test_series_transform.py
¦   ¦       ¦   ¦   ¦   ¦   test_str.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_frame_apply.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_frame_apply_relabeling.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_frame_transform.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_invalid_arg.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_series_apply.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_series_apply_relabeling.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_series_transform.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_str.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---arithmetic
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_array_ops.py
¦   ¦       ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetime64.py
¦   ¦       ¦   ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   ¦   test_numeric.py
¦   ¦       ¦   ¦   ¦   ¦   test_object.py
¦   ¦       ¦   ¦   ¦   ¦   test_period.py
¦   ¦       ¦   ¦   ¦   ¦   test_timedelta64.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_array_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetime64.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_object.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timedelta64.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---arrays
¦   ¦       ¦   ¦   ¦   ¦   masked_shared.py
¦   ¦       ¦   ¦   ¦   ¦   test_array.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetimes.py
¦   ¦       ¦   ¦   ¦   ¦   test_ndarray_backed.py
¦   ¦       ¦   ¦   ¦   ¦   test_period.py
¦   ¦       ¦   ¦   ¦   ¦   test_timedeltas.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---boolean
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_comparison.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_construction.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_function.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_logical.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reduction.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_repr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_comparison.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_construction.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_logical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reduction.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_repr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---categorical
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_algos.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_analytics.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_missing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_operators.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_replace.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_repr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sorting.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_subclass.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_take.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_warnings.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_algos.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_analytics.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_operators.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_replace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_repr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sorting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_subclass.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_take.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_warnings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---datetimes
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_cumulative.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_cumulative.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---floating
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_comparison.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_concat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_construction.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_function.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_repr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_numpy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_comparison.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_construction.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_repr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_numpy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---integer
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_comparison.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_concat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_construction.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_function.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_repr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_comparison.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_construction.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_repr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---interval
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---masked
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arrow_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_function.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_arrow_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---numpy_
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_numpy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_numpy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---period
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arrow_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_arrow_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---sparse
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_accessor.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetics.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_combine_concat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_libsparse.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_unary.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetics.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_combine_concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_libsparse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_unary.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---string_
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_string.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_string_arrow.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_string_arrow.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---timedeltas
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_cumulative.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_cumulative.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           masked_shared.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetimes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ndarray_backed.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timedeltas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---base
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   test_conversion.py
¦   ¦       ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   test_misc.py
¦   ¦       ¦   ¦   ¦   ¦   test_transpose.py
¦   ¦       ¦   ¦   ¦   ¦   test_unique.py
¦   ¦       ¦   ¦   ¦   ¦   test_value_counts.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_conversion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_transpose.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_unique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_value_counts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---computation
¦   ¦       ¦   ¦   ¦   ¦   test_compat.py
¦   ¦       ¦   ¦   ¦   ¦   test_eval.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_eval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---config
¦   ¦       ¦   ¦   ¦   ¦   test_config.py
¦   ¦       ¦   ¦   ¦   ¦   test_localization.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_config.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_localization.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---construction
¦   ¦       ¦   ¦   ¦   ¦   test_extract_array.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_extract_array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---copy_view
¦   ¦       ¦   ¦   ¦   ¦   test_array.py
¦   ¦       ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   test_clip.py
¦   ¦       ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   test_core_functionalities.py
¦   ¦       ¦   ¦   ¦   ¦   test_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   test_internals.py
¦   ¦       ¦   ¦   ¦   ¦   test_interp_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   test_methods.py
¦   ¦       ¦   ¦   ¦   ¦   test_replace.py
¦   ¦       ¦   ¦   ¦   ¦   test_setitem.py
¦   ¦       ¦   ¦   ¦   ¦   test_util.py
¦   ¦       ¦   ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---index
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_datetimeindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_periodindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timedeltaindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_datetimeindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_periodindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timedeltaindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_clip.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_core_functionalities.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_internals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_interp_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_methods.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_replace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_setitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---dtypes
¦   ¦       ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   test_concat.py
¦   ¦       ¦   ¦   ¦   ¦   test_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   test_generic.py
¦   ¦       ¦   ¦   ¦   ¦   test_inference.py
¦   ¦       ¦   ¦   ¦   ¦   test_missing.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---cast
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_can_hold_element.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_construct_from_scalar.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_construct_ndarray.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_construct_object_arr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dict_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_downcast.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_find_common_type.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_infer_datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_infer_dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_maybe_box_native.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_promote.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_can_hold_element.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_construct_from_scalar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_construct_ndarray.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_construct_object_arr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dict_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_downcast.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_find_common_type.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_infer_datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_infer_dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_maybe_box_native.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_promote.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_generic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_inference.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---extension
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_arrow.py
¦   ¦       ¦   ¦   ¦   ¦   test_boolean.py
¦   ¦       ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   test_extension.py
¦   ¦       ¦   ¦   ¦   ¦   test_external_block.py
¦   ¦       ¦   ¦   ¦   ¦   test_floating.py
¦   ¦       ¦   ¦   ¦   ¦   test_integer.py
¦   ¦       ¦   ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   ¦   test_numpy.py
¦   ¦       ¦   ¦   ¦   ¦   test_period.py
¦   ¦       ¦   ¦   ¦   ¦   test_sparse.py
¦   ¦       ¦   ¦   ¦   ¦   test_string.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---array_with_attr
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_array_with_attr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_array_with_attr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---base
¦   ¦       ¦   ¦   ¦   ¦   ¦   accumulate.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   casting.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   dim2.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   getitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   groupby.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   interface.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   io.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   methods.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   missing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   printing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   reduce.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   reshaping.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   setitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           accumulate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           casting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           dim2.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           getitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           interface.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           io.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           methods.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           printing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           reduce.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           reshaping.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           setitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---date
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---decimal
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_decimal.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_decimal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---json
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_json.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_json.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---list
¦   ¦       ¦   ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_list.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_list.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arrow.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_boolean.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_extension.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_external_block.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_floating.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_integer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numpy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_sparse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---frame
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_alter_axes.py
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   test_block_internals.py
¦   ¦       ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   test_cumulative.py
¦   ¦       ¦   ¦   ¦   ¦   test_iteration.py
¦   ¦       ¦   ¦   ¦   ¦   test_logical_ops.py
¦   ¦       ¦   ¦   ¦   ¦   test_nonunique_indexes.py
¦   ¦       ¦   ¦   ¦   ¦   test_npfuncs.py
¦   ¦       ¦   ¦   ¦   ¦   test_query_eval.py
¦   ¦       ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   test_repr_info.py
¦   ¦       ¦   ¦   ¦   ¦   test_stack_unstack.py
¦   ¦       ¦   ¦   ¦   ¦   test_subclass.py
¦   ¦       ¦   ¦   ¦   ¦   test_ufunc.py
¦   ¦       ¦   ¦   ¦   ¦   test_unary.py
¦   ¦       ¦   ¦   ¦   ¦   test_validate.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---constructors
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_from_dict.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_from_records.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_from_dict.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_from_records.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---indexing
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_coercion.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_delitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_getitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get_value.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_insert.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_mask.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_set_value.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_take.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_where.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xs.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_coercion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_delitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_getitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get_value.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_insert.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_mask.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_set_value.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_take.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_where.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---methods
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_add_prefix_suffix.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_align.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_asfreq.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_asof.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_assign.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_at_time.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_between_time.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_clip.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_combine.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_combine_first.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_compare.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_convert_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_copy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_count.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_cov_corr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_describe.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_diff.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dot.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_drop.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_droplevel.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dropna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_drop_duplicates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_duplicated.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_equals.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_explode.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_filter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_first_and_last.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_first_valid_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get_numeric_data.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_head_tail.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_infer_objects.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interpolate.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_isetitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_isin.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_is_homogeneous_dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_matmul.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_nlargest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pct_change.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pipe.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pop.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_quantile.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rank.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex_like.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rename.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rename_axis.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reorder_levels.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_replace.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reset_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_round.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sample.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_select_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_set_axis.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_set_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_shift.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sort_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sort_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_swapaxes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_swaplevel.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_csv.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_dict.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_dict_of_blocks.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_numpy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_period.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_records.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_timestamp.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_transpose.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_truncate.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_tz_convert.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_tz_localize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_update.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_value_counts.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_add_prefix_suffix.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_align.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_asfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_asof.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_assign.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_at_time.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_between_time.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_clip.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_combine.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_combine_first.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_compare.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_convert_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_copy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_count.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_cov_corr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_describe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_diff.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dot.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_drop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_droplevel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dropna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_drop_duplicates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_duplicated.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_equals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_explode.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_filter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_first_and_last.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_first_valid_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get_numeric_data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_head_tail.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_infer_objects.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interpolate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_isetitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_isin.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_is_homogeneous_dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_matmul.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_nlargest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pct_change.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pipe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_quantile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rank.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex_like.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rename.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rename_axis.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reorder_levels.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_replace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reset_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_round.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sample.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_select_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_set_axis.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_set_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_shift.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sort_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sort_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_swapaxes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_swaplevel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_csv.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_dict.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_dict_of_blocks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_numpy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_records.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_timestamp.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_transpose.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_truncate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_tz_convert.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_tz_localize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_update.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_value_counts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_alter_axes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_block_internals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cumulative.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_iteration.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_logical_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_nonunique_indexes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_npfuncs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_query_eval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_repr_info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_stack_unstack.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_subclass.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ufunc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_unary.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---generic
¦   ¦       ¦   ¦   ¦   ¦   test_duplicate_labels.py
¦   ¦       ¦   ¦   ¦   ¦   test_finalize.py
¦   ¦       ¦   ¦   ¦   ¦   test_frame.py
¦   ¦       ¦   ¦   ¦   ¦   test_generic.py
¦   ¦       ¦   ¦   ¦   ¦   test_label_or_level_utils.py
¦   ¦       ¦   ¦   ¦   ¦   test_series.py
¦   ¦       ¦   ¦   ¦   ¦   test_to_xarray.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_duplicate_labels.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_finalize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_frame.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_generic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_label_or_level_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_series.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_to_xarray.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---groupby
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_allowlist.py
¦   ¦       ¦   ¦   ¦   ¦   test_any_all.py
¦   ¦       ¦   ¦   ¦   ¦   test_api_consistency.py
¦   ¦       ¦   ¦   ¦   ¦   test_apply.py
¦   ¦       ¦   ¦   ¦   ¦   test_apply_mutate.py
¦   ¦       ¦   ¦   ¦   ¦   test_bin_groupby.py
¦   ¦       ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   test_counting.py
¦   ¦       ¦   ¦   ¦   ¦   test_filters.py
¦   ¦       ¦   ¦   ¦   ¦   test_function.py
¦   ¦       ¦   ¦   ¦   ¦   test_groupby.py
¦   ¦       ¦   ¦   ¦   ¦   test_groupby_dropna.py
¦   ¦       ¦   ¦   ¦   ¦   test_groupby_shift_diff.py
¦   ¦       ¦   ¦   ¦   ¦   test_groupby_subclass.py
¦   ¦       ¦   ¦   ¦   ¦   test_grouping.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   test_index_as_string.py
¦   ¦       ¦   ¦   ¦   ¦   test_libgroupby.py
¦   ¦       ¦   ¦   ¦   ¦   test_min_max.py
¦   ¦       ¦   ¦   ¦   ¦   test_missing.py
¦   ¦       ¦   ¦   ¦   ¦   test_nth.py
¦   ¦       ¦   ¦   ¦   ¦   test_numba.py
¦   ¦       ¦   ¦   ¦   ¦   test_nunique.py
¦   ¦       ¦   ¦   ¦   ¦   test_pipe.py
¦   ¦       ¦   ¦   ¦   ¦   test_quantile.py
¦   ¦       ¦   ¦   ¦   ¦   test_raises.py
¦   ¦       ¦   ¦   ¦   ¦   test_rank.py
¦   ¦       ¦   ¦   ¦   ¦   test_sample.py
¦   ¦       ¦   ¦   ¦   ¦   test_size.py
¦   ¦       ¦   ¦   ¦   ¦   test_timegrouper.py
¦   ¦       ¦   ¦   ¦   ¦   test_value_counts.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---aggregate
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_aggregate.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_cython.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_numba.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_other.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_aggregate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_cython.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_numba.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_other.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---transform
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_numba.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_transform.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_numba.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_transform.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_allowlist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_any_all.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_api_consistency.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_apply.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_apply_mutate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_bin_groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_counting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_filters.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_function.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_groupby_dropna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_groupby_shift_diff.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_groupby_subclass.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_grouping.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_index_as_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_libgroupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_min_max.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_nth.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numba.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_nunique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_pipe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_quantile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_raises.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rank.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_sample.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_size.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timegrouper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_value_counts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---indexes
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   test_any_index.py
¦   ¦       ¦   ¦   ¦   ¦   test_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   test_engines.py
¦   ¦       ¦   ¦   ¦   ¦   test_frozen.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   test_index_new.py
¦   ¦       ¦   ¦   ¦   ¦   test_numpy_compat.py
¦   ¦       ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   test_subclass.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---base_class
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reshape.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_where.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reshape.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_where.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---categorical
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_append.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_category.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_equals.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_map.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_append.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_category.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_equals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_map.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---datetimelike_
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_drop_duplicates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_equals.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_is_monotonic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_nat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sort_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_value_counts.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_drop_duplicates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_equals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_is_monotonic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_nat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sort_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_value_counts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---datetimes
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_asof.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_date_range.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_delete.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_freq_attr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_map.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_misc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_npfuncs.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_partial_slicing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_scalar_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timezones.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_unique.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---methods
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_factorize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_insert.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_isocalendar.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_repeat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_shift.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_snap.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_to_frame.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_to_period.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_to_series.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_factorize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_insert.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_isocalendar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_repeat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_shift.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_snap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_to_frame.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_to_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_to_series.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_asof.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_date_range.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_delete.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_freq_attr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_map.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_npfuncs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_partial_slicing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_scalar_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timezones.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_unique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---interval
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_equals.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval_range.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval_tree.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_equals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interval_range.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interval_tree.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---multi
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_analytics.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_conversion.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_copy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_drop.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_duplicates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_equivalence.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get_level_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get_set.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_integrity.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_isin.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_lexsort.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_missing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_monotonic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_names.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_partial_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reshape.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sorting.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_take.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_analytics.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_conversion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_copy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_drop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_duplicates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_equivalence.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get_level_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get_set.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_integrity.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_isin.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_lexsort.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_monotonic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_names.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_partial_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reshape.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sorting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_take.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---numeric
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_numeric.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---object
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---period
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_freq_attr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_monotonic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_partial_slicing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_period.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_period_range.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_resolution.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_scalar_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_searchsorted.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_tools.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---methods
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_asfreq.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_factorize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_insert.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_is_full.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_repeat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_shift.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_to_timestamp.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_asfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_factorize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_insert.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_is_full.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_repeat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_shift.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_to_timestamp.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_freq_attr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_monotonic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_partial_slicing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_period_range.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_resolution.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_scalar_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_searchsorted.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_tools.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---ranges
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_range.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_range.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---timedeltas
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_delete.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_freq_attr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_scalar_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_searchsorted.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timedelta.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timedelta_range.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---methods
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_factorize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_insert.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_repeat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_shift.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_factorize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_insert.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_repeat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_shift.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_delete.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_freq_attr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_scalar_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_searchsorted.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timedelta.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timedelta_range.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_any_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_engines.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_frozen.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_index_new.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numpy_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_setops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_subclass.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---indexing
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_at.py
¦   ¦       ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   test_chaining_and_caching.py
¦   ¦       ¦   ¦   ¦   ¦   test_check_indexer.py
¦   ¦       ¦   ¦   ¦   ¦   test_coercion.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   test_floats.py
¦   ¦       ¦   ¦   ¦   ¦   test_iat.py
¦   ¦       ¦   ¦   ¦   ¦   test_iloc.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexers.py
¦   ¦       ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   test_loc.py
¦   ¦       ¦   ¦   ¦   ¦   test_na_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   test_partial.py
¦   ¦       ¦   ¦   ¦   ¦   test_scalar.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---interval
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval_new.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interval_new.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---multiindex
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_chaining_and_caching.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_getitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_iloc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing_slow.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_loc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_multiindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_partial.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_slice.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sorted.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_chaining_and_caching.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_getitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_iloc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing_slow.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_loc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_multiindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_partial.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_slice.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sorted.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_at.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_chaining_and_caching.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_check_indexer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_coercion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_floats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_iat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_iloc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_loc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_na_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_partial.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_scalar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---interchange
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_impl.py
¦   ¦       ¦   ¦   ¦   ¦   test_spec_conformance.py
¦   ¦       ¦   ¦   ¦   ¦   test_utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_impl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_spec_conformance.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---internals
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_internals.py
¦   ¦       ¦   ¦   ¦   ¦   test_managers.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_internals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_managers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---io
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   generate_legacy_storage_files.py
¦   ¦       ¦   ¦   ¦   ¦   test_clipboard.py
¦   ¦       ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   test_compression.py
¦   ¦       ¦   ¦   ¦   ¦   test_feather.py
¦   ¦       ¦   ¦   ¦   ¦   test_fsspec.py
¦   ¦       ¦   ¦   ¦   ¦   test_gcs.py
¦   ¦       ¦   ¦   ¦   ¦   test_html.py
¦   ¦       ¦   ¦   ¦   ¦   test_orc.py
¦   ¦       ¦   ¦   ¦   ¦   test_parquet.py
¦   ¦       ¦   ¦   ¦   ¦   test_pickle.py
¦   ¦       ¦   ¦   ¦   ¦   test_s3.py
¦   ¦       ¦   ¦   ¦   ¦   test_spss.py
¦   ¦       ¦   ¦   ¦   ¦   test_sql.py
¦   ¦       ¦   ¦   ¦   ¦   test_stata.py
¦   ¦       ¦   ¦   ¦   ¦   test_user_agent.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---data
¦   ¦       ¦   ¦   ¦   ¦   ¦   gbq_fake_job.txt
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---fixed_width
¦   ¦       ¦   ¦   ¦   ¦   ¦       fixed_width_format.txt
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---legacy_pickle
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---1.2.4
¦   ¦       ¦   ¦   ¦   ¦   ¦           empty_frame_v1_2_4-GH#42345.pkl
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---parquet
¦   ¦       ¦   ¦   ¦   ¦   ¦       simple.parquet
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---pickle
¦   ¦       ¦   ¦   ¦   ¦   ¦       test_mi_py27.pkl
¦   ¦       ¦   ¦   ¦   ¦   ¦       test_py27.pkl
¦   ¦       ¦   ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   ¦   +---xml
¦   ¦       ¦   ¦   ¦   ¦           baby_names.xml
¦   ¦       ¦   ¦   ¦   ¦           books.xml
¦   ¦       ¦   ¦   ¦   ¦           cta_rail_lines.kml
¦   ¦       ¦   ¦   ¦   ¦           doc_ch_utf.xml
¦   ¦       ¦   ¦   ¦   ¦           flatten_doc.xsl
¦   ¦       ¦   ¦   ¦   ¦           row_field_output.xsl
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---excel
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_odf.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_odswriter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_openpyxl.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_readers.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_style.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_writers.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xlrd.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xlsxwriter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_odf.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_odswriter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_openpyxl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_readers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_style.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_writers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xlrd.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xlsxwriter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---formats
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_console.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_css.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_eng_formatting.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_format.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_info.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_printing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_series_info.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_csv.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_excel.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_html.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_latex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_markdown.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_string.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---style
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_bar.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_exceptions.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_format.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_highlight.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_html.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_matplotlib.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_non_unique.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_style.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_tooltip.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_to_latex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_to_string.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_bar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_exceptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_format.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_highlight.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_html.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_matplotlib.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_non_unique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_style.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_tooltip.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_to_latex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_to_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_console.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_css.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_eng_formatting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_format.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_printing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_series_info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_csv.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_excel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_html.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_latex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_markdown.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---json
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_compression.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_deprecated_kwargs.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_json_table_schema.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_json_table_schema_ext_dtype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_normalize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pandas.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_readlines.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ujson.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_compression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_deprecated_kwargs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_json_table_schema.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_json_table_schema_ext_dtype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_normalize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pandas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_readlines.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ujson.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---parser
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_comment.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_compression.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_concatenate_chunks.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_converters.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_c_parser_only.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dialect.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_encoding.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_header.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_index_col.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_mangle_dupes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_multi_thread.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_na_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_network.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_parse_dates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_python_parser_only.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_quoting.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_read_fwf.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_skiprows.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_textreader.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_unsupported.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_upcast.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---common
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_chunksize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_common_basic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_data_list.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_decimal.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_file_buffer_url.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_float.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_inf.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_ints.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_iterator.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_read_errors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_verbose.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_chunksize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_common_basic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_data_list.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_decimal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_file_buffer_url.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_float.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_inf.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_ints.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_iterator.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_read_errors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_verbose.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---dtypes
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_dtypes_basic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_empty.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_dtypes_basic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_empty.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---usecols
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_parse_dates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_strings.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   test_usecols_basic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_parse_dates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_strings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           test_usecols_basic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_comment.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_compression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_concatenate_chunks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_converters.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_c_parser_only.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dialect.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_encoding.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_header.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_index_col.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_mangle_dupes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_multi_thread.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_na_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_network.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_parse_dates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_python_parser_only.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_quoting.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_read_fwf.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_skiprows.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_textreader.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_unsupported.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_upcast.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---pytables
¦   ¦       ¦   ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_append.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_compat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_complex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_errors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_file_handling.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_keys.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_put.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pytables_missing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_read.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_retain_attributes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_round_trip.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_select.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_store.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_subclass.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timezones.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_time_series.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_append.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_complex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_errors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_file_handling.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_keys.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_put.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pytables_missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_read.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_retain_attributes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_round_trip.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_select.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_store.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_subclass.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timezones.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_time_series.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---sas
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_byteswap.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sas.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sas7bdat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xport.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_byteswap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sas7bdat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xport.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---xml
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_xml.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xml.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xml_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_to_xml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xml_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           generate_legacy_storage_files.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_clipboard.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_compression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_feather.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fsspec.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_gcs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_html.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_orc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_parquet.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_pickle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_s3.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_spss.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_sql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_stata.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_user_agent.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---libs
¦   ¦       ¦   ¦   ¦   ¦   test_hashtable.py
¦   ¦       ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   test_lib.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_hashtable.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_lib.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---plotting
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_backend.py
¦   ¦       ¦   ¦   ¦   ¦   test_boxplot_method.py
¦   ¦       ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   test_converter.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetimelike.py
¦   ¦       ¦   ¦   ¦   ¦   test_groupby.py
¦   ¦       ¦   ¦   ¦   ¦   test_hist_method.py
¦   ¦       ¦   ¦   ¦   ¦   test_misc.py
¦   ¦       ¦   ¦   ¦   ¦   test_series.py
¦   ¦       ¦   ¦   ¦   ¦   test_style.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---frame
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_frame.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_frame_color.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_frame_groupby.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_frame_legend.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_frame_subplots.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_hist_box_by.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_frame.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_frame_color.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_frame_groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_frame_legend.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_frame_subplots.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_hist_box_by.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_backend.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_boxplot_method.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_converter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetimelike.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_hist_method.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_series.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_style.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---reductions
¦   ¦       ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   test_stat_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_stat_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---resample
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_base.py
¦   ¦       ¦   ¦   ¦   ¦   test_datetime_index.py
¦   ¦       ¦   ¦   ¦   ¦   test_period_index.py
¦   ¦       ¦   ¦   ¦   ¦   test_resampler_grouper.py
¦   ¦       ¦   ¦   ¦   ¦   test_resample_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_timedelta.py
¦   ¦       ¦   ¦   ¦   ¦   test_time_grouper.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_datetime_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_period_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_resampler_grouper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_resample_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timedelta.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_time_grouper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---reshape
¦   ¦       ¦   ¦   ¦   ¦   test_crosstab.py
¦   ¦       ¦   ¦   ¦   ¦   test_cut.py
¦   ¦       ¦   ¦   ¦   ¦   test_from_dummies.py
¦   ¦       ¦   ¦   ¦   ¦   test_get_dummies.py
¦   ¦       ¦   ¦   ¦   ¦   test_melt.py
¦   ¦       ¦   ¦   ¦   ¦   test_pivot.py
¦   ¦       ¦   ¦   ¦   ¦   test_pivot_multilevel.py
¦   ¦       ¦   ¦   ¦   ¦   test_qcut.py
¦   ¦       ¦   ¦   ¦   ¦   test_union_categoricals.py
¦   ¦       ¦   ¦   ¦   ¦   test_util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---concat
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_append.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_append_common.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_categorical.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_concat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dataframe.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_datetimes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_empty.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_invalid.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_series.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sort.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_append.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_append_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_categorical.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_concat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dataframe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_datetimes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_empty.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_invalid.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_series.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sort.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---merge
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_join.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_merge.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_merge_asof.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_merge_cross.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_merge_index_as_string.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_merge_ordered.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_multi.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_join.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_merge.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_merge_asof.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_merge_cross.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_merge_index_as_string.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_merge_ordered.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_multi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_crosstab.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cut.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_from_dummies.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_get_dummies.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_melt.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_pivot.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_pivot_multilevel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_qcut.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_union_categoricals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---scalar
¦   ¦       ¦   ¦   ¦   ¦   test_nat.py
¦   ¦       ¦   ¦   ¦   ¦   test_na_scalar.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---interval
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interval.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interval.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---period
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_asfreq.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_period.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_asfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_period.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---timedelta
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timedelta.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timedelta.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---timestamp
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_comparisons.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_formats.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rendering.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timestamp.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_timezones.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_unary_ops.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_comparisons.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_formats.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rendering.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timestamp.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_timezones.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_unary_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_nat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_na_scalar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---series
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_arithmetic.py
¦   ¦       ¦   ¦   ¦   ¦   test_constructors.py
¦   ¦       ¦   ¦   ¦   ¦   test_cumulative.py
¦   ¦       ¦   ¦   ¦   ¦   test_iteration.py
¦   ¦       ¦   ¦   ¦   ¦   test_logical_ops.py
¦   ¦       ¦   ¦   ¦   ¦   test_missing.py
¦   ¦       ¦   ¦   ¦   ¦   test_npfuncs.py
¦   ¦       ¦   ¦   ¦   ¦   test_reductions.py
¦   ¦       ¦   ¦   ¦   ¦   test_repr.py
¦   ¦       ¦   ¦   ¦   ¦   test_subclass.py
¦   ¦       ¦   ¦   ¦   ¦   test_ufunc.py
¦   ¦       ¦   ¦   ¦   ¦   test_unary.py
¦   ¦       ¦   ¦   ¦   ¦   test_validate.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---accessors
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_cat_accessor.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dt_accessor.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sparse_accessor.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_str_accessor.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_cat_accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dt_accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sparse_accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_str_accessor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---indexing
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_delitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_getitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_indexing.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_mask.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_setitem.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_set_value.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_take.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_where.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_xs.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_delitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_getitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_indexing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_mask.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_setitem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_set_value.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_take.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_where.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_xs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---methods
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_add_prefix_suffix.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_align.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_argsort.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_asof.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_astype.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_autocorr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_between.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_clip.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_combine.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_combine_first.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_compare.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_convert_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_copy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_count.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_cov_corr.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_describe.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_diff.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_drop.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dropna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_drop_duplicates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_duplicated.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_equals.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_explode.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_fillna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_get_numeric_data.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_head_tail.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_infer_objects.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_interpolate.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_isin.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_isna.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_is_monotonic.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_is_unique.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_item.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_matmul.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_nlargest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_nunique.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pct_change.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_pop.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_quantile.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rank.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reindex_like.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rename.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_rename_axis.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_repeat.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_replace.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_reset_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_round.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_searchsorted.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_set_name.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sort_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_sort_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_tolist.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_csv.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_dict.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_frame.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_to_numpy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_truncate.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_tz_localize.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_unique.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_unstack.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_update.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_values.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_value_counts.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_view.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_add_prefix_suffix.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_align.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_argsort.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_asof.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_astype.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_autocorr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_between.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_clip.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_combine.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_combine_first.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_compare.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_convert_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_copy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_count.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_cov_corr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_describe.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_diff.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_drop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dropna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_drop_duplicates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_duplicated.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_equals.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_explode.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_fillna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_get_numeric_data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_head_tail.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_infer_objects.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_interpolate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_isin.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_isna.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_is_monotonic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_is_unique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_item.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_matmul.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_nlargest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_nunique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pct_change.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_pop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_quantile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rank.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reindex_like.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rename.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_rename_axis.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_repeat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_replace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_reset_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_round.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_searchsorted.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_set_name.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sort_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_sort_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_tolist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_csv.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_dict.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_frame.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_to_numpy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_truncate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_tz_localize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_unique.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_unstack.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_update.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_values.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_value_counts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_view.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_arithmetic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cumulative.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_iteration.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_logical_ops.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_missing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_npfuncs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_reductions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_repr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_subclass.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ufunc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_unary.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---strings
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_case_justify.py
¦   ¦       ¦   ¦   ¦   ¦   test_cat.py
¦   ¦       ¦   ¦   ¦   ¦   test_extract.py
¦   ¦       ¦   ¦   ¦   ¦   test_find_replace.py
¦   ¦       ¦   ¦   ¦   ¦   test_get_dummies.py
¦   ¦       ¦   ¦   ¦   ¦   test_split_partition.py
¦   ¦       ¦   ¦   ¦   ¦   test_strings.py
¦   ¦       ¦   ¦   ¦   ¦   test_string_array.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_case_justify.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_extract.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_find_replace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_get_dummies.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_split_partition.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_strings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_string_array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tools
¦   ¦       ¦   ¦   ¦   ¦   test_to_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   test_to_numeric.py
¦   ¦       ¦   ¦   ¦   ¦   test_to_time.py
¦   ¦       ¦   ¦   ¦   ¦   test_to_timedelta.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_to_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_to_numeric.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_to_time.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_to_timedelta.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tseries
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---frequencies
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_frequencies.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_freq_code.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_inference.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_frequencies.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_freq_code.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_inference.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---holiday
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_calendar.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_federal.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_holiday.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_observance.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           test_calendar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_federal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_holiday.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_observance.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---offsets
¦   ¦       ¦   ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_business_day.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_business_hour.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_business_month.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_business_quarter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_business_year.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_common.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_custom_business_day.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_custom_business_hour.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_custom_business_month.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_dst.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_easter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_fiscal.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_index.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_month.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_offsets.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_offsets_properties.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_quarter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_ticks.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_week.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_year.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_business_day.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_business_hour.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_business_month.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_business_quarter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_business_year.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_custom_business_day.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_custom_business_hour.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_custom_business_month.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_dst.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_easter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_fiscal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_month.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_offsets.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_offsets_properties.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_quarter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_ticks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_week.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_year.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tslibs
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_array_to_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   test_ccalendar.py
¦   ¦       ¦   ¦   ¦   ¦   test_conversion.py
¦   ¦       ¦   ¦   ¦   ¦   test_fields.py
¦   ¦       ¦   ¦   ¦   ¦   test_libfrequencies.py
¦   ¦       ¦   ¦   ¦   ¦   test_liboffsets.py
¦   ¦       ¦   ¦   ¦   ¦   test_np_datetime.py
¦   ¦       ¦   ¦   ¦   ¦   test_parse_iso8601.py
¦   ¦       ¦   ¦   ¦   ¦   test_parsing.py
¦   ¦       ¦   ¦   ¦   ¦   test_period_asfreq.py
¦   ¦       ¦   ¦   ¦   ¦   test_resolution.py
¦   ¦       ¦   ¦   ¦   ¦   test_timedeltas.py
¦   ¦       ¦   ¦   ¦   ¦   test_timezones.py
¦   ¦       ¦   ¦   ¦   ¦   test_to_offset.py
¦   ¦       ¦   ¦   ¦   ¦   test_tzconversion.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_array_to_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ccalendar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_conversion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_fields.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_libfrequencies.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_liboffsets.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_np_datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_parse_iso8601.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_parsing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_period_asfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_resolution.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timedeltas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timezones.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_to_offset.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_tzconversion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---util
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_almost_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_attr_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_categorical_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_extension_array_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_frame_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_index_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_interval_array_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_numpy_array_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_produces_warning.py
¦   ¦       ¦   ¦   ¦   ¦   test_assert_series_equal.py
¦   ¦       ¦   ¦   ¦   ¦   test_deprecate.py
¦   ¦       ¦   ¦   ¦   ¦   test_deprecate_kwarg.py
¦   ¦       ¦   ¦   ¦   ¦   test_deprecate_nonkeyword_arguments.py
¦   ¦       ¦   ¦   ¦   ¦   test_doc.py
¦   ¦       ¦   ¦   ¦   ¦   test_hashing.py
¦   ¦       ¦   ¦   ¦   ¦   test_make_objects.py
¦   ¦       ¦   ¦   ¦   ¦   test_numba.py
¦   ¦       ¦   ¦   ¦   ¦   test_rewrite_warning.py
¦   ¦       ¦   ¦   ¦   ¦   test_safe_import.py
¦   ¦       ¦   ¦   ¦   ¦   test_shares_memory.py
¦   ¦       ¦   ¦   ¦   ¦   test_show_versions.py
¦   ¦       ¦   ¦   ¦   ¦   test_str_methods.py
¦   ¦       ¦   ¦   ¦   ¦   test_util.py
¦   ¦       ¦   ¦   ¦   ¦   test_validate_args.py
¦   ¦       ¦   ¦   ¦   ¦   test_validate_args_and_kwargs.py
¦   ¦       ¦   ¦   ¦   ¦   test_validate_inclusive.py
¦   ¦       ¦   ¦   ¦   ¦   test_validate_kwargs.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_almost_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_attr_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_categorical_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_extension_array_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_frame_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_index_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_interval_array_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_numpy_array_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_produces_warning.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_assert_series_equal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_deprecate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_deprecate_kwarg.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_deprecate_nonkeyword_arguments.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_doc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_hashing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_make_objects.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numba.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rewrite_warning.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_safe_import.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_shares_memory.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_show_versions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_str_methods.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validate_args.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validate_args_and_kwargs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validate_inclusive.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_validate_kwargs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---window
¦   ¦       ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   test_api.py
¦   ¦       ¦   ¦   ¦   ¦   test_apply.py
¦   ¦       ¦   ¦   ¦   ¦   test_base_indexer.py
¦   ¦       ¦   ¦   ¦   ¦   test_cython_aggregations.py
¦   ¦       ¦   ¦   ¦   ¦   test_dtypes.py
¦   ¦       ¦   ¦   ¦   ¦   test_ewm.py
¦   ¦       ¦   ¦   ¦   ¦   test_expanding.py
¦   ¦       ¦   ¦   ¦   ¦   test_groupby.py
¦   ¦       ¦   ¦   ¦   ¦   test_numba.py
¦   ¦       ¦   ¦   ¦   ¦   test_online.py
¦   ¦       ¦   ¦   ¦   ¦   test_pairwise.py
¦   ¦       ¦   ¦   ¦   ¦   test_rolling.py
¦   ¦       ¦   ¦   ¦   ¦   test_rolling_functions.py
¦   ¦       ¦   ¦   ¦   ¦   test_rolling_quantile.py
¦   ¦       ¦   ¦   ¦   ¦   test_rolling_skew_kurt.py
¦   ¦       ¦   ¦   ¦   ¦   test_timeseries_window.py
¦   ¦       ¦   ¦   ¦   ¦   test_win_type.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---moments
¦   ¦       ¦   ¦   ¦   ¦   ¦   conftest.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_moments_consistency_ewm.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_moments_consistency_expanding.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   test_moments_consistency_rolling.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_moments_consistency_ewm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_moments_consistency_expanding.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           test_moments_consistency_rolling.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           conftest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_apply.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_base_indexer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_cython_aggregations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_dtypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ewm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_expanding.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_groupby.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_numba.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_online.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_pairwise.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rolling.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rolling_functions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rolling_quantile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rolling_skew_kurt.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_timeseries_window.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_win_type.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           test_aggregation.cpython-38.pyc
¦   ¦       ¦   ¦           test_algos.cpython-38.pyc
¦   ¦       ¦   ¦           test_common.cpython-38.pyc
¦   ¦       ¦   ¦           test_downstream.cpython-38.pyc
¦   ¦       ¦   ¦           test_errors.cpython-38.pyc
¦   ¦       ¦   ¦           test_expressions.cpython-38.pyc
¦   ¦       ¦   ¦           test_flags.cpython-38.pyc
¦   ¦       ¦   ¦           test_multilevel.cpython-38.pyc
¦   ¦       ¦   ¦           test_nanops.cpython-38.pyc
¦   ¦       ¦   ¦           test_optional_dependency.cpython-38.pyc
¦   ¦       ¦   ¦           test_register_accessor.cpython-38.pyc
¦   ¦       ¦   ¦           test_sorting.cpython-38.pyc
¦   ¦       ¦   ¦           test_take.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tseries
¦   ¦       ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   frequencies.py
¦   ¦       ¦   ¦   ¦   holiday.py
¦   ¦       ¦   ¦   ¦   offsets.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦           frequencies.cpython-38.pyc
¦   ¦       ¦   ¦           holiday.cpython-38.pyc
¦   ¦       ¦   ¦           offsets.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---util
¦   ¦       ¦   ¦   ¦   _decorators.py
¦   ¦       ¦   ¦   ¦   _doctools.py
¦   ¦       ¦   ¦   ¦   _exceptions.py
¦   ¦       ¦   ¦   ¦   _print_versions.py
¦   ¦       ¦   ¦   ¦   _str_methods.py
¦   ¦       ¦   ¦   ¦   _tester.py
¦   ¦       ¦   ¦   ¦   _test_decorators.py
¦   ¦       ¦   ¦   ¦   _validators.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---version
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           _decorators.cpython-38.pyc
¦   ¦       ¦   ¦           _doctools.cpython-38.pyc
¦   ¦       ¦   ¦           _exceptions.cpython-38.pyc
¦   ¦       ¦   ¦           _print_versions.cpython-38.pyc
¦   ¦       ¦   ¦           _str_methods.cpython-38.pyc
¦   ¦       ¦   ¦           _tester.cpython-38.pyc
¦   ¦       ¦   ¦           _test_decorators.cpython-38.pyc
¦   ¦       ¦   ¦           _validators.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_config
¦   ¦       ¦   ¦   ¦   config.py
¦   ¦       ¦   ¦   ¦   dates.py
¦   ¦       ¦   ¦   ¦   display.py
¦   ¦       ¦   ¦   ¦   localization.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           config.cpython-38.pyc
¦   ¦       ¦   ¦           dates.cpython-38.pyc
¦   ¦       ¦   ¦           display.cpython-38.pyc
¦   ¦       ¦   ¦           localization.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_libs
¦   ¦       ¦   ¦   ¦   algos.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   algos.pxd
¦   ¦       ¦   ¦   ¦   algos.pyi
¦   ¦       ¦   ¦   ¦   algos.pyx
¦   ¦       ¦   ¦   ¦   algos_common_helper.pxi.in
¦   ¦       ¦   ¦   ¦   algos_take_helper.pxi.in
¦   ¦       ¦   ¦   ¦   arrays.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   arrays.pxd
¦   ¦       ¦   ¦   ¦   arrays.pyi
¦   ¦       ¦   ¦   ¦   arrays.pyx
¦   ¦       ¦   ¦   ¦   dtypes.pxd
¦   ¦       ¦   ¦   ¦   groupby.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   groupby.pyi
¦   ¦       ¦   ¦   ¦   groupby.pyx
¦   ¦       ¦   ¦   ¦   hashing.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   hashing.pyi
¦   ¦       ¦   ¦   ¦   hashing.pyx
¦   ¦       ¦   ¦   ¦   hashtable.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   hashtable.pxd
¦   ¦       ¦   ¦   ¦   hashtable.pyi
¦   ¦       ¦   ¦   ¦   hashtable.pyx
¦   ¦       ¦   ¦   ¦   hashtable_class_helper.pxi.in
¦   ¦       ¦   ¦   ¦   hashtable_func_helper.pxi.in
¦   ¦       ¦   ¦   ¦   index.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   index.pyi
¦   ¦       ¦   ¦   ¦   index.pyx
¦   ¦       ¦   ¦   ¦   indexing.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   indexing.pyi
¦   ¦       ¦   ¦   ¦   indexing.pyx
¦   ¦       ¦   ¦   ¦   index_class_helper.pxi.in
¦   ¦       ¦   ¦   ¦   internals.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   internals.pyi
¦   ¦       ¦   ¦   ¦   internals.pyx
¦   ¦       ¦   ¦   ¦   interval.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   interval.pyi
¦   ¦       ¦   ¦   ¦   interval.pyx
¦   ¦       ¦   ¦   ¦   intervaltree.pxi.in
¦   ¦       ¦   ¦   ¦   join.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   join.pyi
¦   ¦       ¦   ¦   ¦   join.pyx
¦   ¦       ¦   ¦   ¦   json.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   json.pyi
¦   ¦       ¦   ¦   ¦   khash.pxd
¦   ¦       ¦   ¦   ¦   khash_for_primitive_helper.pxi.in
¦   ¦       ¦   ¦   ¦   lib.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   lib.pxd
¦   ¦       ¦   ¦   ¦   lib.pyi
¦   ¦       ¦   ¦   ¦   lib.pyx
¦   ¦       ¦   ¦   ¦   missing.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   missing.pxd
¦   ¦       ¦   ¦   ¦   missing.pyi
¦   ¦       ¦   ¦   ¦   missing.pyx
¦   ¦       ¦   ¦   ¦   ops.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ops.pyi
¦   ¦       ¦   ¦   ¦   ops.pyx
¦   ¦       ¦   ¦   ¦   ops_dispatch.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ops_dispatch.pyi
¦   ¦       ¦   ¦   ¦   ops_dispatch.pyx
¦   ¦       ¦   ¦   ¦   parsers.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   parsers.pyi
¦   ¦       ¦   ¦   ¦   parsers.pyx
¦   ¦       ¦   ¦   ¦   properties.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   properties.pyi
¦   ¦       ¦   ¦   ¦   properties.pyx
¦   ¦       ¦   ¦   ¦   reduction.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   reduction.pyi
¦   ¦       ¦   ¦   ¦   reduction.pyx
¦   ¦       ¦   ¦   ¦   reshape.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   reshape.pyi
¦   ¦       ¦   ¦   ¦   reshape.pyx
¦   ¦       ¦   ¦   ¦   sparse.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   sparse.pyi
¦   ¦       ¦   ¦   ¦   sparse.pyx
¦   ¦       ¦   ¦   ¦   sparse_op_helper.pxi.in
¦   ¦       ¦   ¦   ¦   testing.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   testing.pyi
¦   ¦       ¦   ¦   ¦   testing.pyx
¦   ¦       ¦   ¦   ¦   tslib.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   tslib.pyi
¦   ¦       ¦   ¦   ¦   tslib.pyx
¦   ¦       ¦   ¦   ¦   util.pxd
¦   ¦       ¦   ¦   ¦   writers.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   writers.pyi
¦   ¦       ¦   ¦   ¦   writers.pyx
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---tslibs
¦   ¦       ¦   ¦   ¦   ¦   base.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   base.pxd
¦   ¦       ¦   ¦   ¦   ¦   base.pyx
¦   ¦       ¦   ¦   ¦   ¦   ccalendar.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   ccalendar.pxd
¦   ¦       ¦   ¦   ¦   ¦   ccalendar.pyi
¦   ¦       ¦   ¦   ¦   ¦   ccalendar.pyx
¦   ¦       ¦   ¦   ¦   ¦   conversion.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   conversion.pxd
¦   ¦       ¦   ¦   ¦   ¦   conversion.pyi
¦   ¦       ¦   ¦   ¦   ¦   conversion.pyx
¦   ¦       ¦   ¦   ¦   ¦   dtypes.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   dtypes.pxd
¦   ¦       ¦   ¦   ¦   ¦   dtypes.pyi
¦   ¦       ¦   ¦   ¦   ¦   dtypes.pyx
¦   ¦       ¦   ¦   ¦   ¦   fields.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   fields.pyi
¦   ¦       ¦   ¦   ¦   ¦   fields.pyx
¦   ¦       ¦   ¦   ¦   ¦   nattype.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   nattype.pxd
¦   ¦       ¦   ¦   ¦   ¦   nattype.pyi
¦   ¦       ¦   ¦   ¦   ¦   nattype.pyx
¦   ¦       ¦   ¦   ¦   ¦   np_datetime.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   np_datetime.pxd
¦   ¦       ¦   ¦   ¦   ¦   np_datetime.pyi
¦   ¦       ¦   ¦   ¦   ¦   np_datetime.pyx
¦   ¦       ¦   ¦   ¦   ¦   offsets.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   offsets.pxd
¦   ¦       ¦   ¦   ¦   ¦   offsets.pyi
¦   ¦       ¦   ¦   ¦   ¦   offsets.pyx
¦   ¦       ¦   ¦   ¦   ¦   parsing.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   parsing.pxd
¦   ¦       ¦   ¦   ¦   ¦   parsing.pyi
¦   ¦       ¦   ¦   ¦   ¦   parsing.pyx
¦   ¦       ¦   ¦   ¦   ¦   period.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   period.pxd
¦   ¦       ¦   ¦   ¦   ¦   period.pyi
¦   ¦       ¦   ¦   ¦   ¦   period.pyx
¦   ¦       ¦   ¦   ¦   ¦   strptime.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   strptime.pxd
¦   ¦       ¦   ¦   ¦   ¦   strptime.pyi
¦   ¦       ¦   ¦   ¦   ¦   strptime.pyx
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.pxd
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.pyi
¦   ¦       ¦   ¦   ¦   ¦   timedeltas.pyx
¦   ¦       ¦   ¦   ¦   ¦   timestamps.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   timestamps.pxd
¦   ¦       ¦   ¦   ¦   ¦   timestamps.pyi
¦   ¦       ¦   ¦   ¦   ¦   timestamps.pyx
¦   ¦       ¦   ¦   ¦   ¦   timezones.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   timezones.pxd
¦   ¦       ¦   ¦   ¦   ¦   timezones.pyi
¦   ¦       ¦   ¦   ¦   ¦   timezones.pyx
¦   ¦       ¦   ¦   ¦   ¦   tzconversion.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   tzconversion.pxd
¦   ¦       ¦   ¦   ¦   ¦   tzconversion.pyi
¦   ¦       ¦   ¦   ¦   ¦   tzconversion.pyx
¦   ¦       ¦   ¦   ¦   ¦   util.pxd
¦   ¦       ¦   ¦   ¦   ¦   vectorized.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   vectorized.pyi
¦   ¦       ¦   ¦   ¦   ¦   vectorized.pyx
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---window
¦   ¦       ¦   ¦   ¦   ¦   aggregations.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   aggregations.pyi
¦   ¦       ¦   ¦   ¦   ¦   aggregations.pyx
¦   ¦       ¦   ¦   ¦   ¦   concrt140.dll
¦   ¦       ¦   ¦   ¦   ¦   indexers.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   ¦   indexers.pyi
¦   ¦       ¦   ¦   ¦   ¦   indexers.pyx
¦   ¦       ¦   ¦   ¦   ¦   msvcp140.dll
¦   ¦       ¦   ¦   ¦   ¦   vcruntime140_1.dll
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_testing
¦   ¦       ¦   ¦   ¦   asserters.py
¦   ¦       ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   contexts.py
¦   ¦       ¦   ¦   ¦   _hypothesis.py
¦   ¦       ¦   ¦   ¦   _io.py
¦   ¦       ¦   ¦   ¦   _random.py
¦   ¦       ¦   ¦   ¦   _warnings.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           asserters.cpython-38.pyc
¦   ¦       ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦           contexts.cpython-38.pyc
¦   ¦       ¦   ¦           _hypothesis.cpython-38.pyc
¦   ¦       ¦   ¦           _io.cpython-38.pyc
¦   ¦       ¦   ¦           _random.cpython-38.pyc
¦   ¦       ¦   ¦           _warnings.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           conftest.cpython-38.pyc
¦   ¦       ¦           testing.cpython-38.pyc
¦   ¦       ¦           _typing.cpython-38.pyc
¦   ¦       ¦           _version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pandas-2.0.0.dist-info
¦   ¦       ¦       AUTHORS.md
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---passlib
¦   ¦       ¦   ¦   apache.py
¦   ¦       ¦   ¦   apps.py
¦   ¦       ¦   ¦   context.py
¦   ¦       ¦   ¦   exc.py
¦   ¦       ¦   ¦   hash.py
¦   ¦       ¦   ¦   hosts.py
¦   ¦       ¦   ¦   ifc.py
¦   ¦       ¦   ¦   pwd.py
¦   ¦       ¦   ¦   registry.py
¦   ¦       ¦   ¦   totp.py
¦   ¦       ¦   ¦   win32.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---crypto
¦   ¦       ¦   ¦   ¦   des.py
¦   ¦       ¦   ¦   ¦   digest.py
¦   ¦       ¦   ¦   ¦   _md4.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---scrypt
¦   ¦       ¦   ¦   ¦   ¦   _builtin.py
¦   ¦       ¦   ¦   ¦   ¦   _gen_files.py
¦   ¦       ¦   ¦   ¦   ¦   _salsa.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           _builtin.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _gen_files.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _salsa.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---_blowfish
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   unrolled.py
¦   ¦       ¦   ¦   ¦   ¦   _gen_files.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           unrolled.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _gen_files.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           des.cpython-38.pyc
¦   ¦       ¦   ¦           digest.cpython-38.pyc
¦   ¦       ¦   ¦           _md4.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---ext
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---django
¦   ¦       ¦   ¦   ¦   ¦   models.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           models.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---handlers
¦   ¦       ¦   ¦   ¦   argon2.py
¦   ¦       ¦   ¦   ¦   bcrypt.py
¦   ¦       ¦   ¦   ¦   cisco.py
¦   ¦       ¦   ¦   ¦   des_crypt.py
¦   ¦       ¦   ¦   ¦   digests.py
¦   ¦       ¦   ¦   ¦   django.py
¦   ¦       ¦   ¦   ¦   fshp.py
¦   ¦       ¦   ¦   ¦   ldap_digests.py
¦   ¦       ¦   ¦   ¦   md5_crypt.py
¦   ¦       ¦   ¦   ¦   misc.py
¦   ¦       ¦   ¦   ¦   mssql.py
¦   ¦       ¦   ¦   ¦   mysql.py
¦   ¦       ¦   ¦   ¦   oracle.py
¦   ¦       ¦   ¦   ¦   pbkdf2.py
¦   ¦       ¦   ¦   ¦   phpass.py
¦   ¦       ¦   ¦   ¦   postgres.py
¦   ¦       ¦   ¦   ¦   roundup.py
¦   ¦       ¦   ¦   ¦   scram.py
¦   ¦       ¦   ¦   ¦   scrypt.py
¦   ¦       ¦   ¦   ¦   sha1_crypt.py
¦   ¦       ¦   ¦   ¦   sha2_crypt.py
¦   ¦       ¦   ¦   ¦   sun_md5_crypt.py
¦   ¦       ¦   ¦   ¦   windows.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           argon2.cpython-38.pyc
¦   ¦       ¦   ¦           bcrypt.cpython-38.pyc
¦   ¦       ¦   ¦           cisco.cpython-38.pyc
¦   ¦       ¦   ¦           des_crypt.cpython-38.pyc
¦   ¦       ¦   ¦           digests.cpython-38.pyc
¦   ¦       ¦   ¦           django.cpython-38.pyc
¦   ¦       ¦   ¦           fshp.cpython-38.pyc
¦   ¦       ¦   ¦           ldap_digests.cpython-38.pyc
¦   ¦       ¦   ¦           md5_crypt.cpython-38.pyc
¦   ¦       ¦   ¦           misc.cpython-38.pyc
¦   ¦       ¦   ¦           mssql.cpython-38.pyc
¦   ¦       ¦   ¦           mysql.cpython-38.pyc
¦   ¦       ¦   ¦           oracle.cpython-38.pyc
¦   ¦       ¦   ¦           pbkdf2.cpython-38.pyc
¦   ¦       ¦   ¦           phpass.cpython-38.pyc
¦   ¦       ¦   ¦           postgres.cpython-38.pyc
¦   ¦       ¦   ¦           roundup.cpython-38.pyc
¦   ¦       ¦   ¦           scram.cpython-38.pyc
¦   ¦       ¦   ¦           scrypt.cpython-38.pyc
¦   ¦       ¦   ¦           sha1_crypt.cpython-38.pyc
¦   ¦       ¦   ¦           sha2_crypt.cpython-38.pyc
¦   ¦       ¦   ¦           sun_md5_crypt.cpython-38.pyc
¦   ¦       ¦   ¦           windows.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   ¦   backports.py
¦   ¦       ¦   ¦   ¦   sample1.cfg
¦   ¦       ¦   ¦   ¦   sample1b.cfg
¦   ¦       ¦   ¦   ¦   sample1c.cfg
¦   ¦       ¦   ¦   ¦   sample_config_1s.cfg
¦   ¦       ¦   ¦   ¦   test_apache.py
¦   ¦       ¦   ¦   ¦   test_apps.py
¦   ¦       ¦   ¦   ¦   test_context.py
¦   ¦       ¦   ¦   ¦   test_context_deprecated.py
¦   ¦       ¦   ¦   ¦   test_crypto_builtin_md4.py
¦   ¦       ¦   ¦   ¦   test_crypto_des.py
¦   ¦       ¦   ¦   ¦   test_crypto_digest.py
¦   ¦       ¦   ¦   ¦   test_crypto_scrypt.py
¦   ¦       ¦   ¦   ¦   test_ext_django.py
¦   ¦       ¦   ¦   ¦   test_ext_django_source.py
¦   ¦       ¦   ¦   ¦   test_handlers.py
¦   ¦       ¦   ¦   ¦   test_handlers_argon2.py
¦   ¦       ¦   ¦   ¦   test_handlers_bcrypt.py
¦   ¦       ¦   ¦   ¦   test_handlers_cisco.py
¦   ¦       ¦   ¦   ¦   test_handlers_django.py
¦   ¦       ¦   ¦   ¦   test_handlers_pbkdf2.py
¦   ¦       ¦   ¦   ¦   test_handlers_scrypt.py
¦   ¦       ¦   ¦   ¦   test_hosts.py
¦   ¦       ¦   ¦   ¦   test_pwd.py
¦   ¦       ¦   ¦   ¦   test_registry.py
¦   ¦       ¦   ¦   ¦   test_totp.py
¦   ¦       ¦   ¦   ¦   test_utils.py
¦   ¦       ¦   ¦   ¦   test_utils_handlers.py
¦   ¦       ¦   ¦   ¦   test_utils_md4.py
¦   ¦       ¦   ¦   ¦   test_utils_pbkdf2.py
¦   ¦       ¦   ¦   ¦   test_win32.py
¦   ¦       ¦   ¦   ¦   tox_support.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   _test_bad_register.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           backports.cpython-38.pyc
¦   ¦       ¦   ¦           test_apache.cpython-38.pyc
¦   ¦       ¦   ¦           test_apps.cpython-38.pyc
¦   ¦       ¦   ¦           test_context.cpython-38.pyc
¦   ¦       ¦   ¦           test_context_deprecated.cpython-38.pyc
¦   ¦       ¦   ¦           test_crypto_builtin_md4.cpython-38.pyc
¦   ¦       ¦   ¦           test_crypto_des.cpython-38.pyc
¦   ¦       ¦   ¦           test_crypto_digest.cpython-38.pyc
¦   ¦       ¦   ¦           test_crypto_scrypt.cpython-38.pyc
¦   ¦       ¦   ¦           test_ext_django.cpython-38.pyc
¦   ¦       ¦   ¦           test_ext_django_source.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers_argon2.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers_bcrypt.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers_cisco.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers_django.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers_pbkdf2.cpython-38.pyc
¦   ¦       ¦   ¦           test_handlers_scrypt.cpython-38.pyc
¦   ¦       ¦   ¦           test_hosts.cpython-38.pyc
¦   ¦       ¦   ¦           test_pwd.cpython-38.pyc
¦   ¦       ¦   ¦           test_registry.cpython-38.pyc
¦   ¦       ¦   ¦           test_totp.cpython-38.pyc
¦   ¦       ¦   ¦           test_utils.cpython-38.pyc
¦   ¦       ¦   ¦           test_utils_handlers.cpython-38.pyc
¦   ¦       ¦   ¦           test_utils_md4.cpython-38.pyc
¦   ¦       ¦   ¦           test_utils_pbkdf2.cpython-38.pyc
¦   ¦       ¦   ¦           test_win32.cpython-38.pyc
¦   ¦       ¦   ¦           tox_support.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           _test_bad_register.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---utils
¦   ¦       ¦   ¦   ¦   binary.py
¦   ¦       ¦   ¦   ¦   decor.py
¦   ¦       ¦   ¦   ¦   des.py
¦   ¦       ¦   ¦   ¦   handlers.py
¦   ¦       ¦   ¦   ¦   md4.py
¦   ¦       ¦   ¦   ¦   pbkdf2.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---compat
¦   ¦       ¦   ¦   ¦   ¦   _ordered_dict.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           _ordered_dict.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           binary.cpython-38.pyc
¦   ¦       ¦   ¦           decor.cpython-38.pyc
¦   ¦       ¦   ¦           des.cpython-38.pyc
¦   ¦       ¦   ¦           handlers.cpython-38.pyc
¦   ¦       ¦   ¦           md4.cpython-38.pyc
¦   ¦       ¦   ¦           pbkdf2.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_data
¦   ¦       ¦   ¦   +---wordsets
¦   ¦       ¦   ¦           bip39.txt
¦   ¦       ¦   ¦           eff_long.txt
¦   ¦       ¦   ¦           eff_prefixed.txt
¦   ¦       ¦   ¦           eff_short.txt
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           apache.cpython-38.pyc
¦   ¦       ¦           apps.cpython-38.pyc
¦   ¦       ¦           context.cpython-38.pyc
¦   ¦       ¦           exc.cpython-38.pyc
¦   ¦       ¦           hash.cpython-38.pyc
¦   ¦       ¦           hosts.cpython-38.pyc
¦   ¦       ¦           ifc.cpython-38.pyc
¦   ¦       ¦           pwd.cpython-38.pyc
¦   ¦       ¦           registry.cpython-38.pyc
¦   ¦       ¦           totp.cpython-38.pyc
¦   ¦       ¦           win32.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---passlib-1.7.4.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---pdfkit
¦   ¦       ¦   ¦   api.py
¦   ¦       ¦   ¦   configuration.py
¦   ¦       ¦   ¦   pdfkit.py
¦   ¦       ¦   ¦   source.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           api.cpython-38.pyc
¦   ¦       ¦           configuration.cpython-38.pyc
¦   ¦       ¦           pdfkit.cpython-38.pyc
¦   ¦       ¦           source.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pdfkit-1.0.0.dist-info
¦   ¦       ¦       AUTHORS.rst
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---PIL
¦   ¦       ¦   ¦   BdfFontFile.py
¦   ¦       ¦   ¦   BlpImagePlugin.py
¦   ¦       ¦   ¦   BmpImagePlugin.py
¦   ¦       ¦   ¦   BufrStubImagePlugin.py
¦   ¦       ¦   ¦   ContainerIO.py
¦   ¦       ¦   ¦   CurImagePlugin.py
¦   ¦       ¦   ¦   DcxImagePlugin.py
¦   ¦       ¦   ¦   DdsImagePlugin.py
¦   ¦       ¦   ¦   EpsImagePlugin.py
¦   ¦       ¦   ¦   ExifTags.py
¦   ¦       ¦   ¦   features.py
¦   ¦       ¦   ¦   FitsImagePlugin.py
¦   ¦       ¦   ¦   FitsStubImagePlugin.py
¦   ¦       ¦   ¦   FliImagePlugin.py
¦   ¦       ¦   ¦   FontFile.py
¦   ¦       ¦   ¦   FpxImagePlugin.py
¦   ¦       ¦   ¦   FtexImagePlugin.py
¦   ¦       ¦   ¦   GbrImagePlugin.py
¦   ¦       ¦   ¦   GdImageFile.py
¦   ¦       ¦   ¦   GifImagePlugin.py
¦   ¦       ¦   ¦   GimpGradientFile.py
¦   ¦       ¦   ¦   GimpPaletteFile.py
¦   ¦       ¦   ¦   GribStubImagePlugin.py
¦   ¦       ¦   ¦   Hdf5StubImagePlugin.py
¦   ¦       ¦   ¦   IcnsImagePlugin.py
¦   ¦       ¦   ¦   IcoImagePlugin.py
¦   ¦       ¦   ¦   Image.py
¦   ¦       ¦   ¦   ImageChops.py
¦   ¦       ¦   ¦   ImageCms.py
¦   ¦       ¦   ¦   ImageColor.py
¦   ¦       ¦   ¦   ImageDraw.py
¦   ¦       ¦   ¦   ImageDraw2.py
¦   ¦       ¦   ¦   ImageEnhance.py
¦   ¦       ¦   ¦   ImageFile.py
¦   ¦       ¦   ¦   ImageFilter.py
¦   ¦       ¦   ¦   ImageFont.py
¦   ¦       ¦   ¦   ImageGrab.py
¦   ¦       ¦   ¦   ImageMath.py
¦   ¦       ¦   ¦   ImageMode.py
¦   ¦       ¦   ¦   ImageMorph.py
¦   ¦       ¦   ¦   ImageOps.py
¦   ¦       ¦   ¦   ImagePalette.py
¦   ¦       ¦   ¦   ImagePath.py
¦   ¦       ¦   ¦   ImageQt.py
¦   ¦       ¦   ¦   ImageSequence.py
¦   ¦       ¦   ¦   ImageShow.py
¦   ¦       ¦   ¦   ImageStat.py
¦   ¦       ¦   ¦   ImageTk.py
¦   ¦       ¦   ¦   ImageTransform.py
¦   ¦       ¦   ¦   ImageWin.py
¦   ¦       ¦   ¦   ImImagePlugin.py
¦   ¦       ¦   ¦   ImtImagePlugin.py
¦   ¦       ¦   ¦   IptcImagePlugin.py
¦   ¦       ¦   ¦   Jpeg2KImagePlugin.py
¦   ¦       ¦   ¦   JpegImagePlugin.py
¦   ¦       ¦   ¦   JpegPresets.py
¦   ¦       ¦   ¦   McIdasImagePlugin.py
¦   ¦       ¦   ¦   MicImagePlugin.py
¦   ¦       ¦   ¦   MpegImagePlugin.py
¦   ¦       ¦   ¦   MpoImagePlugin.py
¦   ¦       ¦   ¦   MspImagePlugin.py
¦   ¦       ¦   ¦   PaletteFile.py
¦   ¦       ¦   ¦   PalmImagePlugin.py
¦   ¦       ¦   ¦   PcdImagePlugin.py
¦   ¦       ¦   ¦   PcfFontFile.py
¦   ¦       ¦   ¦   PcxImagePlugin.py
¦   ¦       ¦   ¦   PdfImagePlugin.py
¦   ¦       ¦   ¦   PdfParser.py
¦   ¦       ¦   ¦   PixarImagePlugin.py
¦   ¦       ¦   ¦   PngImagePlugin.py
¦   ¦       ¦   ¦   PpmImagePlugin.py
¦   ¦       ¦   ¦   PsdImagePlugin.py
¦   ¦       ¦   ¦   PSDraw.py
¦   ¦       ¦   ¦   PyAccess.py
¦   ¦       ¦   ¦   SgiImagePlugin.py
¦   ¦       ¦   ¦   SpiderImagePlugin.py
¦   ¦       ¦   ¦   SunImagePlugin.py
¦   ¦       ¦   ¦   TarIO.py
¦   ¦       ¦   ¦   TgaImagePlugin.py
¦   ¦       ¦   ¦   TiffImagePlugin.py
¦   ¦       ¦   ¦   TiffTags.py
¦   ¦       ¦   ¦   WalImageFile.py
¦   ¦       ¦   ¦   WebPImagePlugin.py
¦   ¦       ¦   ¦   WmfImagePlugin.py
¦   ¦       ¦   ¦   XbmImagePlugin.py
¦   ¦       ¦   ¦   XpmImagePlugin.py
¦   ¦       ¦   ¦   XVThumbImagePlugin.py
¦   ¦       ¦   ¦   _binary.py
¦   ¦       ¦   ¦   _deprecate.py
¦   ¦       ¦   ¦   _imaging.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _imagingcms.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _imagingft.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _imagingmath.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _imagingmorph.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _imagingtk.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _tkinter_finder.py
¦   ¦       ¦   ¦   _util.py
¦   ¦       ¦   ¦   _version.py
¦   ¦       ¦   ¦   _webp.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           BdfFontFile.cpython-38.pyc
¦   ¦       ¦           BlpImagePlugin.cpython-38.pyc
¦   ¦       ¦           BmpImagePlugin.cpython-38.pyc
¦   ¦       ¦           BufrStubImagePlugin.cpython-38.pyc
¦   ¦       ¦           ContainerIO.cpython-38.pyc
¦   ¦       ¦           CurImagePlugin.cpython-38.pyc
¦   ¦       ¦           DcxImagePlugin.cpython-38.pyc
¦   ¦       ¦           DdsImagePlugin.cpython-38.pyc
¦   ¦       ¦           EpsImagePlugin.cpython-38.pyc
¦   ¦       ¦           ExifTags.cpython-38.pyc
¦   ¦       ¦           features.cpython-38.pyc
¦   ¦       ¦           FitsImagePlugin.cpython-38.pyc
¦   ¦       ¦           FitsStubImagePlugin.cpython-38.pyc
¦   ¦       ¦           FliImagePlugin.cpython-38.pyc
¦   ¦       ¦           FontFile.cpython-38.pyc
¦   ¦       ¦           FpxImagePlugin.cpython-38.pyc
¦   ¦       ¦           FtexImagePlugin.cpython-38.pyc
¦   ¦       ¦           GbrImagePlugin.cpython-38.pyc
¦   ¦       ¦           GdImageFile.cpython-38.pyc
¦   ¦       ¦           GifImagePlugin.cpython-38.pyc
¦   ¦       ¦           GimpGradientFile.cpython-38.pyc
¦   ¦       ¦           GimpPaletteFile.cpython-38.pyc
¦   ¦       ¦           GribStubImagePlugin.cpython-38.pyc
¦   ¦       ¦           Hdf5StubImagePlugin.cpython-38.pyc
¦   ¦       ¦           IcnsImagePlugin.cpython-38.pyc
¦   ¦       ¦           IcoImagePlugin.cpython-38.pyc
¦   ¦       ¦           Image.cpython-38.pyc
¦   ¦       ¦           ImageChops.cpython-38.pyc
¦   ¦       ¦           ImageCms.cpython-38.pyc
¦   ¦       ¦           ImageColor.cpython-38.pyc
¦   ¦       ¦           ImageDraw.cpython-38.pyc
¦   ¦       ¦           ImageDraw2.cpython-38.pyc
¦   ¦       ¦           ImageEnhance.cpython-38.pyc
¦   ¦       ¦           ImageFile.cpython-38.pyc
¦   ¦       ¦           ImageFilter.cpython-38.pyc
¦   ¦       ¦           ImageFont.cpython-38.pyc
¦   ¦       ¦           ImageGrab.cpython-38.pyc
¦   ¦       ¦           ImageMath.cpython-38.pyc
¦   ¦       ¦           ImageMode.cpython-38.pyc
¦   ¦       ¦           ImageMorph.cpython-38.pyc
¦   ¦       ¦           ImageOps.cpython-38.pyc
¦   ¦       ¦           ImagePalette.cpython-38.pyc
¦   ¦       ¦           ImagePath.cpython-38.pyc
¦   ¦       ¦           ImageQt.cpython-38.pyc
¦   ¦       ¦           ImageSequence.cpython-38.pyc
¦   ¦       ¦           ImageShow.cpython-38.pyc
¦   ¦       ¦           ImageStat.cpython-38.pyc
¦   ¦       ¦           ImageTk.cpython-38.pyc
¦   ¦       ¦           ImageTransform.cpython-38.pyc
¦   ¦       ¦           ImageWin.cpython-38.pyc
¦   ¦       ¦           ImImagePlugin.cpython-38.pyc
¦   ¦       ¦           ImtImagePlugin.cpython-38.pyc
¦   ¦       ¦           IptcImagePlugin.cpython-38.pyc
¦   ¦       ¦           Jpeg2KImagePlugin.cpython-38.pyc
¦   ¦       ¦           JpegImagePlugin.cpython-38.pyc
¦   ¦       ¦           JpegPresets.cpython-38.pyc
¦   ¦       ¦           McIdasImagePlugin.cpython-38.pyc
¦   ¦       ¦           MicImagePlugin.cpython-38.pyc
¦   ¦       ¦           MpegImagePlugin.cpython-38.pyc
¦   ¦       ¦           MpoImagePlugin.cpython-38.pyc
¦   ¦       ¦           MspImagePlugin.cpython-38.pyc
¦   ¦       ¦           PaletteFile.cpython-38.pyc
¦   ¦       ¦           PalmImagePlugin.cpython-38.pyc
¦   ¦       ¦           PcdImagePlugin.cpython-38.pyc
¦   ¦       ¦           PcfFontFile.cpython-38.pyc
¦   ¦       ¦           PcxImagePlugin.cpython-38.pyc
¦   ¦       ¦           PdfImagePlugin.cpython-38.pyc
¦   ¦       ¦           PdfParser.cpython-38.pyc
¦   ¦       ¦           PixarImagePlugin.cpython-38.pyc
¦   ¦       ¦           PngImagePlugin.cpython-38.pyc
¦   ¦       ¦           PpmImagePlugin.cpython-38.pyc
¦   ¦       ¦           PsdImagePlugin.cpython-38.pyc
¦   ¦       ¦           PSDraw.cpython-38.pyc
¦   ¦       ¦           PyAccess.cpython-38.pyc
¦   ¦       ¦           SgiImagePlugin.cpython-38.pyc
¦   ¦       ¦           SpiderImagePlugin.cpython-38.pyc
¦   ¦       ¦           SunImagePlugin.cpython-38.pyc
¦   ¦       ¦           TarIO.cpython-38.pyc
¦   ¦       ¦           TgaImagePlugin.cpython-38.pyc
¦   ¦       ¦           TiffImagePlugin.cpython-38.pyc
¦   ¦       ¦           TiffTags.cpython-38.pyc
¦   ¦       ¦           WalImageFile.cpython-38.pyc
¦   ¦       ¦           WebPImagePlugin.cpython-38.pyc
¦   ¦       ¦           WmfImagePlugin.cpython-38.pyc
¦   ¦       ¦           XbmImagePlugin.cpython-38.pyc
¦   ¦       ¦           XpmImagePlugin.cpython-38.pyc
¦   ¦       ¦           XVThumbImagePlugin.cpython-38.pyc
¦   ¦       ¦           _binary.cpython-38.pyc
¦   ¦       ¦           _deprecate.cpython-38.pyc
¦   ¦       ¦           _tkinter_finder.cpython-38.pyc
¦   ¦       ¦           _util.cpython-38.pyc
¦   ¦       ¦           _version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Pillow-9.4.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---pip
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---_internal
¦   ¦       ¦   ¦   ¦   build_env.py
¦   ¦       ¦   ¦   ¦   cache.py
¦   ¦       ¦   ¦   ¦   configuration.py
¦   ¦       ¦   ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ¦   main.py
¦   ¦       ¦   ¦   ¦   pyproject.py
¦   ¦       ¦   ¦   ¦   self_outdated_check.py
¦   ¦       ¦   ¦   ¦   wheel_builder.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---cli
¦   ¦       ¦   ¦   ¦   ¦   autocompletion.py
¦   ¦       ¦   ¦   ¦   ¦   base_command.py
¦   ¦       ¦   ¦   ¦   ¦   cmdoptions.py
¦   ¦       ¦   ¦   ¦   ¦   command_context.py
¦   ¦       ¦   ¦   ¦   ¦   main.py
¦   ¦       ¦   ¦   ¦   ¦   main_parser.py
¦   ¦       ¦   ¦   ¦   ¦   parser.py
¦   ¦       ¦   ¦   ¦   ¦   progress_bars.py
¦   ¦       ¦   ¦   ¦   ¦   req_command.py
¦   ¦       ¦   ¦   ¦   ¦   spinners.py
¦   ¦       ¦   ¦   ¦   ¦   status_codes.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           autocompletion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base_command.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cmdoptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           command_context.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           main.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           main_parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           progress_bars.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           req_command.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           spinners.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           status_codes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---commands
¦   ¦       ¦   ¦   ¦   ¦   cache.py
¦   ¦       ¦   ¦   ¦   ¦   check.py
¦   ¦       ¦   ¦   ¦   ¦   completion.py
¦   ¦       ¦   ¦   ¦   ¦   configuration.py
¦   ¦       ¦   ¦   ¦   ¦   debug.py
¦   ¦       ¦   ¦   ¦   ¦   download.py
¦   ¦       ¦   ¦   ¦   ¦   freeze.py
¦   ¦       ¦   ¦   ¦   ¦   hash.py
¦   ¦       ¦   ¦   ¦   ¦   help.py
¦   ¦       ¦   ¦   ¦   ¦   install.py
¦   ¦       ¦   ¦   ¦   ¦   list.py
¦   ¦       ¦   ¦   ¦   ¦   search.py
¦   ¦       ¦   ¦   ¦   ¦   show.py
¦   ¦       ¦   ¦   ¦   ¦   uninstall.py
¦   ¦       ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           cache.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           check.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           completion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           configuration.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           debug.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           download.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           freeze.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hash.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           help.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           list.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           search.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           show.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           uninstall.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---distributions
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   installed.py
¦   ¦       ¦   ¦   ¦   ¦   sdist.py
¦   ¦       ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           installed.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sdist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---index
¦   ¦       ¦   ¦   ¦   ¦   collector.py
¦   ¦       ¦   ¦   ¦   ¦   package_finder.py
¦   ¦       ¦   ¦   ¦   ¦   sources.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           collector.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           package_finder.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sources.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---locations
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   _distutils.py
¦   ¦       ¦   ¦   ¦   ¦   _sysconfig.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _distutils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _sysconfig.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---metadata
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   pkg_resources.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pkg_resources.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---models
¦   ¦       ¦   ¦   ¦   ¦   candidate.py
¦   ¦       ¦   ¦   ¦   ¦   direct_url.py
¦   ¦       ¦   ¦   ¦   ¦   format_control.py
¦   ¦       ¦   ¦   ¦   ¦   index.py
¦   ¦       ¦   ¦   ¦   ¦   link.py
¦   ¦       ¦   ¦   ¦   ¦   scheme.py
¦   ¦       ¦   ¦   ¦   ¦   search_scope.py
¦   ¦       ¦   ¦   ¦   ¦   selection_prefs.py
¦   ¦       ¦   ¦   ¦   ¦   target_python.py
¦   ¦       ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           candidate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           direct_url.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           format_control.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           link.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scheme.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           search_scope.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           selection_prefs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           target_python.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---network
¦   ¦       ¦   ¦   ¦   ¦   auth.py
¦   ¦       ¦   ¦   ¦   ¦   cache.py
¦   ¦       ¦   ¦   ¦   ¦   download.py
¦   ¦       ¦   ¦   ¦   ¦   lazy_wheel.py
¦   ¦       ¦   ¦   ¦   ¦   session.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   xmlrpc.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           auth.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cache.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           download.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           lazy_wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           session.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           xmlrpc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---operations
¦   ¦       ¦   ¦   ¦   ¦   check.py
¦   ¦       ¦   ¦   ¦   ¦   freeze.py
¦   ¦       ¦   ¦   ¦   ¦   prepare.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---build
¦   ¦       ¦   ¦   ¦   ¦   ¦   metadata.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   metadata_legacy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   wheel_legacy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           metadata.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           metadata_legacy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           wheel_legacy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---install
¦   ¦       ¦   ¦   ¦   ¦   ¦   editable_legacy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   legacy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           editable_legacy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           legacy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           check.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           freeze.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           prepare.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---req
¦   ¦       ¦   ¦   ¦   ¦   constructors.py
¦   ¦       ¦   ¦   ¦   ¦   req_file.py
¦   ¦       ¦   ¦   ¦   ¦   req_install.py
¦   ¦       ¦   ¦   ¦   ¦   req_set.py
¦   ¦       ¦   ¦   ¦   ¦   req_tracker.py
¦   ¦       ¦   ¦   ¦   ¦   req_uninstall.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           constructors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           req_file.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           req_install.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           req_set.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           req_tracker.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           req_uninstall.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---resolution
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---legacy
¦   ¦       ¦   ¦   ¦   ¦   ¦   resolver.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           resolver.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---resolvelib
¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   candidates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   factory.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   found_candidates.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   provider.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   reporter.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   requirements.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   resolver.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           candidates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           factory.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           found_candidates.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           provider.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           reporter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           requirements.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           resolver.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---utils
¦   ¦       ¦   ¦   ¦   ¦   appdirs.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   compatibility_tags.py
¦   ¦       ¦   ¦   ¦   ¦   datetime.py
¦   ¦       ¦   ¦   ¦   ¦   deprecation.py
¦   ¦       ¦   ¦   ¦   ¦   direct_url_helpers.py
¦   ¦       ¦   ¦   ¦   ¦   distutils_args.py
¦   ¦       ¦   ¦   ¦   ¦   encoding.py
¦   ¦       ¦   ¦   ¦   ¦   entrypoints.py
¦   ¦       ¦   ¦   ¦   ¦   filesystem.py
¦   ¦       ¦   ¦   ¦   ¦   filetypes.py
¦   ¦       ¦   ¦   ¦   ¦   glibc.py
¦   ¦       ¦   ¦   ¦   ¦   hashes.py
¦   ¦       ¦   ¦   ¦   ¦   inject_securetransport.py
¦   ¦       ¦   ¦   ¦   ¦   logging.py
¦   ¦       ¦   ¦   ¦   ¦   misc.py
¦   ¦       ¦   ¦   ¦   ¦   models.py
¦   ¦       ¦   ¦   ¦   ¦   packaging.py
¦   ¦       ¦   ¦   ¦   ¦   parallel.py
¦   ¦       ¦   ¦   ¦   ¦   pkg_resources.py
¦   ¦       ¦   ¦   ¦   ¦   setuptools_build.py
¦   ¦       ¦   ¦   ¦   ¦   subprocess.py
¦   ¦       ¦   ¦   ¦   ¦   temp_dir.py
¦   ¦       ¦   ¦   ¦   ¦   unpacking.py
¦   ¦       ¦   ¦   ¦   ¦   urls.py
¦   ¦       ¦   ¦   ¦   ¦   virtualenv.py
¦   ¦       ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           appdirs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compatibility_tags.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           datetime.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           deprecation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           direct_url_helpers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           distutils_args.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           encoding.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           entrypoints.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           filesystem.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           filetypes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           glibc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hashes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           inject_securetransport.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           logging.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           models.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           packaging.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           parallel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pkg_resources.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           setuptools_build.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           subprocess.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           temp_dir.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           unpacking.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           urls.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           virtualenv.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---vcs
¦   ¦       ¦   ¦   ¦   ¦   bazaar.py
¦   ¦       ¦   ¦   ¦   ¦   git.py
¦   ¦       ¦   ¦   ¦   ¦   mercurial.py
¦   ¦       ¦   ¦   ¦   ¦   subversion.py
¦   ¦       ¦   ¦   ¦   ¦   versioncontrol.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           bazaar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           git.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mercurial.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           subversion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           versioncontrol.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           build_env.cpython-38.pyc
¦   ¦       ¦   ¦           cache.cpython-38.pyc
¦   ¦       ¦   ¦           configuration.cpython-38.pyc
¦   ¦       ¦   ¦           exceptions.cpython-38.pyc
¦   ¦       ¦   ¦           main.cpython-38.pyc
¦   ¦       ¦   ¦           pyproject.cpython-38.pyc
¦   ¦       ¦   ¦           self_outdated_check.cpython-38.pyc
¦   ¦       ¦   ¦           wheel_builder.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_vendor
¦   ¦       ¦   ¦   ¦   appdirs.py
¦   ¦       ¦   ¦   ¦   distro.py
¦   ¦       ¦   ¦   ¦   pyparsing.py
¦   ¦       ¦   ¦   ¦   six.py
¦   ¦       ¦   ¦   ¦   vendor.txt
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---cachecontrol
¦   ¦       ¦   ¦   ¦   ¦   adapter.py
¦   ¦       ¦   ¦   ¦   ¦   cache.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   controller.py
¦   ¦       ¦   ¦   ¦   ¦   filewrapper.py
¦   ¦       ¦   ¦   ¦   ¦   heuristics.py
¦   ¦       ¦   ¦   ¦   ¦   serialize.py
¦   ¦       ¦   ¦   ¦   ¦   wrapper.py
¦   ¦       ¦   ¦   ¦   ¦   _cmd.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---caches
¦   ¦       ¦   ¦   ¦   ¦   ¦   file_cache.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   redis_cache.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           file_cache.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           redis_cache.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           adapter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cache.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           controller.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           filewrapper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           heuristics.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           serialize.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wrapper.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _cmd.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---certifi
¦   ¦       ¦   ¦   ¦   ¦   cacert.pem
¦   ¦       ¦   ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   __main__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __main__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---chardet
¦   ¦       ¦   ¦   ¦   ¦   big5freq.py
¦   ¦       ¦   ¦   ¦   ¦   big5prober.py
¦   ¦       ¦   ¦   ¦   ¦   chardistribution.py
¦   ¦       ¦   ¦   ¦   ¦   charsetgroupprober.py
¦   ¦       ¦   ¦   ¦   ¦   charsetprober.py
¦   ¦       ¦   ¦   ¦   ¦   codingstatemachine.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   cp949prober.py
¦   ¦       ¦   ¦   ¦   ¦   enums.py
¦   ¦       ¦   ¦   ¦   ¦   escprober.py
¦   ¦       ¦   ¦   ¦   ¦   escsm.py
¦   ¦       ¦   ¦   ¦   ¦   eucjpprober.py
¦   ¦       ¦   ¦   ¦   ¦   euckrfreq.py
¦   ¦       ¦   ¦   ¦   ¦   euckrprober.py
¦   ¦       ¦   ¦   ¦   ¦   euctwfreq.py
¦   ¦       ¦   ¦   ¦   ¦   euctwprober.py
¦   ¦       ¦   ¦   ¦   ¦   gb2312freq.py
¦   ¦       ¦   ¦   ¦   ¦   gb2312prober.py
¦   ¦       ¦   ¦   ¦   ¦   hebrewprober.py
¦   ¦       ¦   ¦   ¦   ¦   jisfreq.py
¦   ¦       ¦   ¦   ¦   ¦   jpcntx.py
¦   ¦       ¦   ¦   ¦   ¦   langbulgarianmodel.py
¦   ¦       ¦   ¦   ¦   ¦   langgreekmodel.py
¦   ¦       ¦   ¦   ¦   ¦   langhebrewmodel.py
¦   ¦       ¦   ¦   ¦   ¦   langhungarianmodel.py
¦   ¦       ¦   ¦   ¦   ¦   langrussianmodel.py
¦   ¦       ¦   ¦   ¦   ¦   langthaimodel.py
¦   ¦       ¦   ¦   ¦   ¦   langturkishmodel.py
¦   ¦       ¦   ¦   ¦   ¦   latin1prober.py
¦   ¦       ¦   ¦   ¦   ¦   mbcharsetprober.py
¦   ¦       ¦   ¦   ¦   ¦   mbcsgroupprober.py
¦   ¦       ¦   ¦   ¦   ¦   mbcssm.py
¦   ¦       ¦   ¦   ¦   ¦   sbcharsetprober.py
¦   ¦       ¦   ¦   ¦   ¦   sbcsgroupprober.py
¦   ¦       ¦   ¦   ¦   ¦   sjisprober.py
¦   ¦       ¦   ¦   ¦   ¦   universaldetector.py
¦   ¦       ¦   ¦   ¦   ¦   utf8prober.py
¦   ¦       ¦   ¦   ¦   ¦   version.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---cli
¦   ¦       ¦   ¦   ¦   ¦   ¦   chardetect.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           chardetect.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---metadata
¦   ¦       ¦   ¦   ¦   ¦   ¦   languages.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           languages.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           big5freq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           big5prober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           chardistribution.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           charsetgroupprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           charsetprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           codingstatemachine.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cp949prober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           enums.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           escprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           escsm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           eucjpprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           euckrfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           euckrprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           euctwfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           euctwprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           gb2312freq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           gb2312prober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hebrewprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           jisfreq.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           jpcntx.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langbulgarianmodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langgreekmodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langhebrewmodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langhungarianmodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langrussianmodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langthaimodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           langturkishmodel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           latin1prober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mbcharsetprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mbcsgroupprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mbcssm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sbcharsetprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sbcsgroupprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sjisprober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           universaldetector.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utf8prober.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---colorama
¦   ¦       ¦   ¦   ¦   ¦   ansi.py
¦   ¦       ¦   ¦   ¦   ¦   ansitowin32.py
¦   ¦       ¦   ¦   ¦   ¦   initialise.py
¦   ¦       ¦   ¦   ¦   ¦   win32.py
¦   ¦       ¦   ¦   ¦   ¦   winterm.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           ansi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ansitowin32.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           initialise.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           win32.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           winterm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---distlib
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   database.py
¦   ¦       ¦   ¦   ¦   ¦   index.py
¦   ¦       ¦   ¦   ¦   ¦   locators.py
¦   ¦       ¦   ¦   ¦   ¦   manifest.py
¦   ¦       ¦   ¦   ¦   ¦   markers.py
¦   ¦       ¦   ¦   ¦   ¦   metadata.py
¦   ¦       ¦   ¦   ¦   ¦   resources.py
¦   ¦       ¦   ¦   ¦   ¦   scripts.py
¦   ¦       ¦   ¦   ¦   ¦   t32.exe
¦   ¦       ¦   ¦   ¦   ¦   t64.exe
¦   ¦       ¦   ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   ¦   version.py
¦   ¦       ¦   ¦   ¦   ¦   w32.exe
¦   ¦       ¦   ¦   ¦   ¦   w64.exe
¦   ¦       ¦   ¦   ¦   ¦   wheel.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---_backport
¦   ¦       ¦   ¦   ¦   ¦   ¦   misc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   shutil.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   sysconfig.cfg
¦   ¦       ¦   ¦   ¦   ¦   ¦   sysconfig.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   tarfile.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           misc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           shutil.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           sysconfig.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           tarfile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           database.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           index.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           locators.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           manifest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           metadata.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           resources.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scripts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wheel.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---html5lib
¦   ¦       ¦   ¦   ¦   ¦   constants.py
¦   ¦       ¦   ¦   ¦   ¦   html5parser.py
¦   ¦       ¦   ¦   ¦   ¦   serializer.py
¦   ¦       ¦   ¦   ¦   ¦   _ihatexml.py
¦   ¦       ¦   ¦   ¦   ¦   _inputstream.py
¦   ¦       ¦   ¦   ¦   ¦   _tokenizer.py
¦   ¦       ¦   ¦   ¦   ¦   _utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---filters
¦   ¦       ¦   ¦   ¦   ¦   ¦   alphabeticalattributes.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   inject_meta_charset.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   lint.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   optionaltags.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   sanitizer.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   whitespace.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           alphabeticalattributes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           inject_meta_charset.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           lint.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           optionaltags.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           sanitizer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           whitespace.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---treeadapters
¦   ¦       ¦   ¦   ¦   ¦   ¦   genshi.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   sax.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           genshi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           sax.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---treebuilders
¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   dom.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   etree.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   etree_lxml.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           dom.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           etree.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           etree_lxml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---treewalkers
¦   ¦       ¦   ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   dom.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   etree.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   etree_lxml.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   genshi.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           dom.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           etree.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           etree_lxml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           genshi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---_trie
¦   ¦       ¦   ¦   ¦   ¦   ¦   py.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   _base.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           py.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           _base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           constants.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           html5parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           serializer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _ihatexml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _inputstream.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _tokenizer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---idna
¦   ¦       ¦   ¦   ¦   ¦   codec.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   ¦   idnadata.py
¦   ¦       ¦   ¦   ¦   ¦   intranges.py
¦   ¦       ¦   ¦   ¦   ¦   package_data.py
¦   ¦       ¦   ¦   ¦   ¦   uts46data.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           codec.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           idnadata.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           intranges.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           package_data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           uts46data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---msgpack
¦   ¦       ¦   ¦   ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ¦   ¦   ext.py
¦   ¦       ¦   ¦   ¦   ¦   fallback.py
¦   ¦       ¦   ¦   ¦   ¦   _version.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           exceptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           fallback.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---packaging
¦   ¦       ¦   ¦   ¦   ¦   markers.py
¦   ¦       ¦   ¦   ¦   ¦   requirements.py
¦   ¦       ¦   ¦   ¦   ¦   specifiers.py
¦   ¦       ¦   ¦   ¦   ¦   tags.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   version.py
¦   ¦       ¦   ¦   ¦   ¦   _compat.py
¦   ¦       ¦   ¦   ¦   ¦   _structures.py
¦   ¦       ¦   ¦   ¦   ¦   _typing.py
¦   ¦       ¦   ¦   ¦   ¦   __about__.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           requirements.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           specifiers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tags.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _structures.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _typing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __about__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pep517
¦   ¦       ¦   ¦   ¦   ¦   build.py
¦   ¦       ¦   ¦   ¦   ¦   check.py
¦   ¦       ¦   ¦   ¦   ¦   colorlog.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   dirtools.py
¦   ¦       ¦   ¦   ¦   ¦   envbuild.py
¦   ¦       ¦   ¦   ¦   ¦   meta.py
¦   ¦       ¦   ¦   ¦   ¦   wrappers.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---in_process
¦   ¦       ¦   ¦   ¦   ¦   ¦   _in_process.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           _in_process.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           build.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           check.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           colorlog.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dirtools.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           envbuild.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           meta.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wrappers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pkg_resources
¦   ¦       ¦   ¦   ¦   ¦   py31compat.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           py31compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---progress
¦   ¦       ¦   ¦   ¦   ¦   bar.py
¦   ¦       ¦   ¦   ¦   ¦   counter.py
¦   ¦       ¦   ¦   ¦   ¦   spinner.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           bar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           counter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           spinner.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---requests
¦   ¦       ¦   ¦   ¦   ¦   adapters.py
¦   ¦       ¦   ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   ¦   auth.py
¦   ¦       ¦   ¦   ¦   ¦   certs.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   cookies.py
¦   ¦       ¦   ¦   ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ¦   ¦   help.py
¦   ¦       ¦   ¦   ¦   ¦   hooks.py
¦   ¦       ¦   ¦   ¦   ¦   models.py
¦   ¦       ¦   ¦   ¦   ¦   packages.py
¦   ¦       ¦   ¦   ¦   ¦   sessions.py
¦   ¦       ¦   ¦   ¦   ¦   status_codes.py
¦   ¦       ¦   ¦   ¦   ¦   structures.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   _internal_utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   __version__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           adapters.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           auth.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           certs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cookies.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           exceptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           help.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hooks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           models.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           packages.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sessions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           status_codes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           structures.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _internal_utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __version__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---resolvelib
¦   ¦       ¦   ¦   ¦   ¦   providers.py
¦   ¦       ¦   ¦   ¦   ¦   reporters.py
¦   ¦       ¦   ¦   ¦   ¦   resolvers.py
¦   ¦       ¦   ¦   ¦   ¦   structs.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---compat
¦   ¦       ¦   ¦   ¦   ¦   ¦   collections_abc.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           collections_abc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           providers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           reporters.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           resolvers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           structs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tenacity
¦   ¦       ¦   ¦   ¦   ¦   after.py
¦   ¦       ¦   ¦   ¦   ¦   before.py
¦   ¦       ¦   ¦   ¦   ¦   before_sleep.py
¦   ¦       ¦   ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   ¦   nap.py
¦   ¦       ¦   ¦   ¦   ¦   retry.py
¦   ¦       ¦   ¦   ¦   ¦   stop.py
¦   ¦       ¦   ¦   ¦   ¦   tornadoweb.py
¦   ¦       ¦   ¦   ¦   ¦   wait.py
¦   ¦       ¦   ¦   ¦   ¦   _asyncio.py
¦   ¦       ¦   ¦   ¦   ¦   _utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           after.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           before.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           before_sleep.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           nap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           retry.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           stop.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tornadoweb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           wait.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _asyncio.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---toml
¦   ¦       ¦   ¦   ¦   ¦   decoder.py
¦   ¦       ¦   ¦   ¦   ¦   encoder.py
¦   ¦       ¦   ¦   ¦   ¦   ordered.py
¦   ¦       ¦   ¦   ¦   ¦   tz.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           decoder.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           encoder.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ordered.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tz.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---urllib3
¦   ¦       ¦   ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   ¦   connectionpool.py
¦   ¦       ¦   ¦   ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ¦   ¦   fields.py
¦   ¦       ¦   ¦   ¦   ¦   filepost.py
¦   ¦       ¦   ¦   ¦   ¦   poolmanager.py
¦   ¦       ¦   ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   ¦   response.py
¦   ¦       ¦   ¦   ¦   ¦   _collections.py
¦   ¦       ¦   ¦   ¦   ¦   _version.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---contrib
¦   ¦       ¦   ¦   ¦   ¦   ¦   appengine.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ntlmpool.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   pyopenssl.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   securetransport.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   socks.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   _appengine_environ.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---_securetransport
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   bindings.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   low_level.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           bindings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           low_level.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           appengine.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           ntlmpool.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           pyopenssl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           securetransport.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           socks.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           _appengine_environ.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---packages
¦   ¦       ¦   ¦   ¦   ¦   ¦   six.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---backports
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   makefile.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           makefile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---ssl_match_hostname
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   _implementation.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦   ¦           _implementation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           six.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---util
¦   ¦       ¦   ¦   ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   proxy.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   queue.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   response.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   retry.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ssltransport.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   ssl_.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   timeout.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   url.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   wait.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           proxy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           queue.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           response.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           retry.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           ssltransport.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           ssl_.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           timeout.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           url.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           wait.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           connectionpool.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           exceptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           fields.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           filepost.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           poolmanager.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           response.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _collections.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---webencodings
¦   ¦       ¦   ¦   ¦   ¦   labels.py
¦   ¦       ¦   ¦   ¦   ¦   mklabels.py
¦   ¦       ¦   ¦   ¦   ¦   tests.py
¦   ¦       ¦   ¦   ¦   ¦   x_user_defined.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           labels.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mklabels.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tests.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           x_user_defined.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           appdirs.cpython-38.pyc
¦   ¦       ¦   ¦           distro.cpython-38.pyc
¦   ¦       ¦   ¦           pyparsing.cpython-38.pyc
¦   ¦       ¦   ¦           six.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pip-21.1.1.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pkgutil_resolve_name-1.3.10.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pkg_resources
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---extern
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---tests
¦   ¦       ¦   ¦   +---data
¦   ¦       ¦   ¦       +---my-test-package-source
¦   ¦       ¦   ¦           ¦   setup.py
¦   ¦       ¦   ¦           ¦   
¦   ¦       ¦   ¦           +---__pycache__
¦   ¦       ¦   ¦                   setup.cpython-38.pyc
¦   ¦       ¦   ¦                   
¦   ¦       ¦   +---_vendor
¦   ¦       ¦   ¦   ¦   appdirs.py
¦   ¦       ¦   ¦   ¦   pyparsing.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---packaging
¦   ¦       ¦   ¦   ¦   ¦   markers.py
¦   ¦       ¦   ¦   ¦   ¦   requirements.py
¦   ¦       ¦   ¦   ¦   ¦   specifiers.py
¦   ¦       ¦   ¦   ¦   ¦   tags.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   version.py
¦   ¦       ¦   ¦   ¦   ¦   _compat.py
¦   ¦       ¦   ¦   ¦   ¦   _structures.py
¦   ¦       ¦   ¦   ¦   ¦   _typing.py
¦   ¦       ¦   ¦   ¦   ¦   __about__.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           requirements.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           specifiers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tags.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _structures.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _typing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __about__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           appdirs.cpython-38.pyc
¦   ¦       ¦   ¦           pyparsing.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---premailer
¦   ¦       ¦   ¦   cache.py
¦   ¦       ¦   ¦   merge_style.py
¦   ¦       ¦   ¦   premailer.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           cache.cpython-38.pyc
¦   ¦       ¦           merge_style.cpython-38.pyc
¦   ¦       ¦           premailer.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---premailer-3.10.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---prompt_toolkit
¦   ¦       ¦   ¦   auto_suggest.py
¦   ¦       ¦   ¦   buffer.py
¦   ¦       ¦   ¦   cache.py
¦   ¦       ¦   ¦   cursor_shapes.py
¦   ¦       ¦   ¦   data_structures.py
¦   ¦       ¦   ¦   document.py
¦   ¦       ¦   ¦   enums.py
¦   ¦       ¦   ¦   history.py
¦   ¦       ¦   ¦   keys.py
¦   ¦       ¦   ¦   log.py
¦   ¦       ¦   ¦   mouse_events.py
¦   ¦       ¦   ¦   patch_stdout.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   renderer.py
¦   ¦       ¦   ¦   search.py
¦   ¦       ¦   ¦   selection.py
¦   ¦       ¦   ¦   token.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   validation.py
¦   ¦       ¦   ¦   win32_types.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---application
¦   ¦       ¦   ¦   ¦   application.py
¦   ¦       ¦   ¦   ¦   current.py
¦   ¦       ¦   ¦   ¦   dummy.py
¦   ¦       ¦   ¦   ¦   run_in_terminal.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           application.cpython-38.pyc
¦   ¦       ¦   ¦           current.cpython-38.pyc
¦   ¦       ¦   ¦           dummy.cpython-38.pyc
¦   ¦       ¦   ¦           run_in_terminal.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---clipboard
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   in_memory.py
¦   ¦       ¦   ¦   ¦   pyperclip.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           in_memory.cpython-38.pyc
¦   ¦       ¦   ¦           pyperclip.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---completion
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   deduplicate.py
¦   ¦       ¦   ¦   ¦   filesystem.py
¦   ¦       ¦   ¦   ¦   fuzzy_completer.py
¦   ¦       ¦   ¦   ¦   nested.py
¦   ¦       ¦   ¦   ¦   word_completer.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           deduplicate.cpython-38.pyc
¦   ¦       ¦   ¦           filesystem.cpython-38.pyc
¦   ¦       ¦   ¦           fuzzy_completer.cpython-38.pyc
¦   ¦       ¦   ¦           nested.cpython-38.pyc
¦   ¦       ¦   ¦           word_completer.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---contrib
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---completers
¦   ¦       ¦   ¦   ¦   ¦   system.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           system.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---regular_languages
¦   ¦       ¦   ¦   ¦   ¦   compiler.py
¦   ¦       ¦   ¦   ¦   ¦   completion.py
¦   ¦       ¦   ¦   ¦   ¦   lexer.py
¦   ¦       ¦   ¦   ¦   ¦   regex_parser.py
¦   ¦       ¦   ¦   ¦   ¦   validation.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           compiler.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           completion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           lexer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           regex_parser.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           validation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ssh
¦   ¦       ¦   ¦   ¦   ¦   server.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           server.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---telnet
¦   ¦       ¦   ¦   ¦   ¦   log.py
¦   ¦       ¦   ¦   ¦   ¦   protocol.py
¦   ¦       ¦   ¦   ¦   ¦   server.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           log.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           protocol.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           server.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---eventloop
¦   ¦       ¦   ¦   ¦   async_generator.py
¦   ¦       ¦   ¦   ¦   inputhook.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   win32.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           async_generator.cpython-38.pyc
¦   ¦       ¦   ¦           inputhook.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           win32.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---filters
¦   ¦       ¦   ¦   ¦   app.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   cli.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           app.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           cli.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---formatted_text
¦   ¦       ¦   ¦   ¦   ansi.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   html.py
¦   ¦       ¦   ¦   ¦   pygments.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           ansi.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           html.cpython-38.pyc
¦   ¦       ¦   ¦           pygments.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---input
¦   ¦       ¦   ¦   ¦   ansi_escape_sequences.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   defaults.py
¦   ¦       ¦   ¦   ¦   posix_pipe.py
¦   ¦       ¦   ¦   ¦   posix_utils.py
¦   ¦       ¦   ¦   ¦   typeahead.py
¦   ¦       ¦   ¦   ¦   vt100.py
¦   ¦       ¦   ¦   ¦   vt100_parser.py
¦   ¦       ¦   ¦   ¦   win32.py
¦   ¦       ¦   ¦   ¦   win32_pipe.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           ansi_escape_sequences.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           defaults.cpython-38.pyc
¦   ¦       ¦   ¦           posix_pipe.cpython-38.pyc
¦   ¦       ¦   ¦           posix_utils.cpython-38.pyc
¦   ¦       ¦   ¦           typeahead.cpython-38.pyc
¦   ¦       ¦   ¦           vt100.cpython-38.pyc
¦   ¦       ¦   ¦           vt100_parser.cpython-38.pyc
¦   ¦       ¦   ¦           win32.cpython-38.pyc
¦   ¦       ¦   ¦           win32_pipe.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---key_binding
¦   ¦       ¦   ¦   ¦   defaults.py
¦   ¦       ¦   ¦   ¦   digraphs.py
¦   ¦       ¦   ¦   ¦   emacs_state.py
¦   ¦       ¦   ¦   ¦   key_bindings.py
¦   ¦       ¦   ¦   ¦   key_processor.py
¦   ¦       ¦   ¦   ¦   vi_state.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---bindings
¦   ¦       ¦   ¦   ¦   ¦   auto_suggest.py
¦   ¦       ¦   ¦   ¦   ¦   basic.py
¦   ¦       ¦   ¦   ¦   ¦   completion.py
¦   ¦       ¦   ¦   ¦   ¦   cpr.py
¦   ¦       ¦   ¦   ¦   ¦   emacs.py
¦   ¦       ¦   ¦   ¦   ¦   focus.py
¦   ¦       ¦   ¦   ¦   ¦   mouse.py
¦   ¦       ¦   ¦   ¦   ¦   named_commands.py
¦   ¦       ¦   ¦   ¦   ¦   open_in_editor.py
¦   ¦       ¦   ¦   ¦   ¦   page_navigation.py
¦   ¦       ¦   ¦   ¦   ¦   scroll.py
¦   ¦       ¦   ¦   ¦   ¦   search.py
¦   ¦       ¦   ¦   ¦   ¦   vi.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           auto_suggest.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           basic.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           completion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cpr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           emacs.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           focus.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mouse.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           named_commands.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           open_in_editor.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           page_navigation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scroll.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           search.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           vi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           defaults.cpython-38.pyc
¦   ¦       ¦   ¦           digraphs.cpython-38.pyc
¦   ¦       ¦   ¦           emacs_state.cpython-38.pyc
¦   ¦       ¦   ¦           key_bindings.cpython-38.pyc
¦   ¦       ¦   ¦           key_processor.cpython-38.pyc
¦   ¦       ¦   ¦           vi_state.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---layout
¦   ¦       ¦   ¦   ¦   containers.py
¦   ¦       ¦   ¦   ¦   controls.py
¦   ¦       ¦   ¦   ¦   dimension.py
¦   ¦       ¦   ¦   ¦   dummy.py
¦   ¦       ¦   ¦   ¦   layout.py
¦   ¦       ¦   ¦   ¦   margins.py
¦   ¦       ¦   ¦   ¦   menus.py
¦   ¦       ¦   ¦   ¦   mouse_handlers.py
¦   ¦       ¦   ¦   ¦   processors.py
¦   ¦       ¦   ¦   ¦   screen.py
¦   ¦       ¦   ¦   ¦   scrollable_pane.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           containers.cpython-38.pyc
¦   ¦       ¦   ¦           controls.cpython-38.pyc
¦   ¦       ¦   ¦           dimension.cpython-38.pyc
¦   ¦       ¦   ¦           dummy.cpython-38.pyc
¦   ¦       ¦   ¦           layout.cpython-38.pyc
¦   ¦       ¦   ¦           margins.cpython-38.pyc
¦   ¦       ¦   ¦           menus.cpython-38.pyc
¦   ¦       ¦   ¦           mouse_handlers.cpython-38.pyc
¦   ¦       ¦   ¦           processors.cpython-38.pyc
¦   ¦       ¦   ¦           screen.cpython-38.pyc
¦   ¦       ¦   ¦           scrollable_pane.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---lexers
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   pygments.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           pygments.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---output
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   color_depth.py
¦   ¦       ¦   ¦   ¦   conemu.py
¦   ¦       ¦   ¦   ¦   defaults.py
¦   ¦       ¦   ¦   ¦   flush_stdout.py
¦   ¦       ¦   ¦   ¦   plain_text.py
¦   ¦       ¦   ¦   ¦   vt100.py
¦   ¦       ¦   ¦   ¦   win32.py
¦   ¦       ¦   ¦   ¦   windows10.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           color_depth.cpython-38.pyc
¦   ¦       ¦   ¦           conemu.cpython-38.pyc
¦   ¦       ¦   ¦           defaults.cpython-38.pyc
¦   ¦       ¦   ¦           flush_stdout.cpython-38.pyc
¦   ¦       ¦   ¦           plain_text.cpython-38.pyc
¦   ¦       ¦   ¦           vt100.cpython-38.pyc
¦   ¦       ¦   ¦           win32.cpython-38.pyc
¦   ¦       ¦   ¦           windows10.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---shortcuts
¦   ¦       ¦   ¦   ¦   dialogs.py
¦   ¦       ¦   ¦   ¦   prompt.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---progress_bar
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   formatters.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           formatters.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           dialogs.cpython-38.pyc
¦   ¦       ¦   ¦           prompt.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---styles
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   defaults.py
¦   ¦       ¦   ¦   ¦   named_colors.py
¦   ¦       ¦   ¦   ¦   pygments.py
¦   ¦       ¦   ¦   ¦   style.py
¦   ¦       ¦   ¦   ¦   style_transformation.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           defaults.cpython-38.pyc
¦   ¦       ¦   ¦           named_colors.cpython-38.pyc
¦   ¦       ¦   ¦           pygments.cpython-38.pyc
¦   ¦       ¦   ¦           style.cpython-38.pyc
¦   ¦       ¦   ¦           style_transformation.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---widgets
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   dialogs.py
¦   ¦       ¦   ¦   ¦   menus.py
¦   ¦       ¦   ¦   ¦   toolbars.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           dialogs.cpython-38.pyc
¦   ¦       ¦   ¦           menus.cpython-38.pyc
¦   ¦       ¦   ¦           toolbars.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           auto_suggest.cpython-38.pyc
¦   ¦       ¦           buffer.cpython-38.pyc
¦   ¦       ¦           cache.cpython-38.pyc
¦   ¦       ¦           cursor_shapes.cpython-38.pyc
¦   ¦       ¦           data_structures.cpython-38.pyc
¦   ¦       ¦           document.cpython-38.pyc
¦   ¦       ¦           enums.cpython-38.pyc
¦   ¦       ¦           history.cpython-38.pyc
¦   ¦       ¦           keys.cpython-38.pyc
¦   ¦       ¦           log.cpython-38.pyc
¦   ¦       ¦           mouse_events.cpython-38.pyc
¦   ¦       ¦           patch_stdout.cpython-38.pyc
¦   ¦       ¦           renderer.cpython-38.pyc
¦   ¦       ¦           search.cpython-38.pyc
¦   ¦       ¦           selection.cpython-38.pyc
¦   ¦       ¦           token.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           validation.cpython-38.pyc
¦   ¦       ¦           win32_types.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---prompt_toolkit-3.0.38.dist-info
¦   ¦       ¦       AUTHORS.rst
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pycparser
¦   ¦       ¦   ¦   ast_transforms.py
¦   ¦       ¦   ¦   c_ast.py
¦   ¦       ¦   ¦   c_generator.py
¦   ¦       ¦   ¦   c_lexer.py
¦   ¦       ¦   ¦   c_parser.py
¦   ¦       ¦   ¦   lextab.py
¦   ¦       ¦   ¦   plyparser.py
¦   ¦       ¦   ¦   yacctab.py
¦   ¦       ¦   ¦   _ast_gen.py
¦   ¦       ¦   ¦   _build_tables.py
¦   ¦       ¦   ¦   _c_ast.cfg
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---ply
¦   ¦       ¦   ¦   ¦   cpp.py
¦   ¦       ¦   ¦   ¦   ctokens.py
¦   ¦       ¦   ¦   ¦   lex.py
¦   ¦       ¦   ¦   ¦   yacc.py
¦   ¦       ¦   ¦   ¦   ygen.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           cpp.cpython-38.pyc
¦   ¦       ¦   ¦           ctokens.cpython-38.pyc
¦   ¦       ¦   ¦           lex.cpython-38.pyc
¦   ¦       ¦   ¦           yacc.cpython-38.pyc
¦   ¦       ¦   ¦           ygen.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           ast_transforms.cpython-38.pyc
¦   ¦       ¦           c_ast.cpython-38.pyc
¦   ¦       ¦           c_generator.cpython-38.pyc
¦   ¦       ¦           c_lexer.cpython-38.pyc
¦   ¦       ¦           c_parser.cpython-38.pyc
¦   ¦       ¦           lextab.cpython-38.pyc
¦   ¦       ¦           plyparser.cpython-38.pyc
¦   ¦       ¦           yacctab.cpython-38.pyc
¦   ¦       ¦           _ast_gen.cpython-38.pyc
¦   ¦       ¦           _build_tables.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pycparser-2.21.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pydyf
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pydyf-0.6.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pyphen
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---dictionaries
¦   ¦       ¦   ¦       hyph_af_ZA.dic
¦   ¦       ¦   ¦       hyph_be_BY.dic
¦   ¦       ¦   ¦       hyph_bg_BG.dic
¦   ¦       ¦   ¦       hyph_ca.dic
¦   ¦       ¦   ¦       hyph_cs_CZ.dic
¦   ¦       ¦   ¦       hyph_da_DK.dic
¦   ¦       ¦   ¦       hyph_de_AT.dic
¦   ¦       ¦   ¦       hyph_de_CH.dic
¦   ¦       ¦   ¦       hyph_de_DE.dic
¦   ¦       ¦   ¦       hyph_el_GR.dic
¦   ¦       ¦   ¦       hyph_en_GB.dic
¦   ¦       ¦   ¦       hyph_en_US.dic
¦   ¦       ¦   ¦       hyph_eo.dic
¦   ¦       ¦   ¦       hyph_es.dic
¦   ¦       ¦   ¦       hyph_et_EE.dic
¦   ¦       ¦   ¦       hyph_fr.dic
¦   ¦       ¦   ¦       hyph_gl.dic
¦   ¦       ¦   ¦       hyph_hr_HR.dic
¦   ¦       ¦   ¦       hyph_hu_HU.dic
¦   ¦       ¦   ¦       hyph_id_ID.dic
¦   ¦       ¦   ¦       hyph_is.dic
¦   ¦       ¦   ¦       hyph_it_IT.dic
¦   ¦       ¦   ¦       hyph_lt.dic
¦   ¦       ¦   ¦       hyph_lv_LV.dic
¦   ¦       ¦   ¦       hyph_mn_MN.dic
¦   ¦       ¦   ¦       hyph_nb_NO.dic
¦   ¦       ¦   ¦       hyph_nl_NL.dic
¦   ¦       ¦   ¦       hyph_nn_NO.dic
¦   ¦       ¦   ¦       hyph_pl_PL.dic
¦   ¦       ¦   ¦       hyph_pt_BR.dic
¦   ¦       ¦   ¦       hyph_pt_PT.dic
¦   ¦       ¦   ¦       hyph_ro_RO.dic
¦   ¦       ¦   ¦       hyph_ru_RU.dic
¦   ¦       ¦   ¦       hyph_sk_SK.dic
¦   ¦       ¦   ¦       hyph_sl_SI.dic
¦   ¦       ¦   ¦       hyph_sq_AL.dic
¦   ¦       ¦   ¦       hyph_sr.dic
¦   ¦       ¦   ¦       hyph_sr_Latn.dic
¦   ¦       ¦   ¦       hyph_sv.dic
¦   ¦       ¦   ¦       hyph_te_IN.dic
¦   ¦       ¦   ¦       hyph_th_TH.dic
¦   ¦       ¦   ¦       hyph_uk_UA.dic
¦   ¦       ¦   ¦       hyph_zu_ZA.dic
¦   ¦       ¦   ¦       update.sh
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pyphen-0.14.0.dist-info
¦   ¦       ¦       COPYING.GPL
¦   ¦       ¦       COPYING.LGPL
¦   ¦       ¦       COPYING.MPL
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---pyrsistent
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   typing.py
¦   ¦       ¦   ¦   typing.pyi
¦   ¦       ¦   ¦   _checked_types.py
¦   ¦       ¦   ¦   _field_common.py
¦   ¦       ¦   ¦   _helpers.py
¦   ¦       ¦   ¦   _immutable.py
¦   ¦       ¦   ¦   _pbag.py
¦   ¦       ¦   ¦   _pclass.py
¦   ¦       ¦   ¦   _pdeque.py
¦   ¦       ¦   ¦   _plist.py
¦   ¦       ¦   ¦   _pmap.py
¦   ¦       ¦   ¦   _precord.py
¦   ¦       ¦   ¦   _pset.py
¦   ¦       ¦   ¦   _pvector.py
¦   ¦       ¦   ¦   _toolz.py
¦   ¦       ¦   ¦   _transformations.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __init__.pyi
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           typing.cpython-38.pyc
¦   ¦       ¦           _checked_types.cpython-38.pyc
¦   ¦       ¦           _field_common.cpython-38.pyc
¦   ¦       ¦           _helpers.cpython-38.pyc
¦   ¦       ¦           _immutable.cpython-38.pyc
¦   ¦       ¦           _pbag.cpython-38.pyc
¦   ¦       ¦           _pclass.cpython-38.pyc
¦   ¦       ¦           _pdeque.cpython-38.pyc
¦   ¦       ¦           _plist.cpython-38.pyc
¦   ¦       ¦           _pmap.cpython-38.pyc
¦   ¦       ¦           _precord.cpython-38.pyc
¦   ¦       ¦           _pset.cpython-38.pyc
¦   ¦       ¦           _pvector.cpython-38.pyc
¦   ¦       ¦           _toolz.cpython-38.pyc
¦   ¦       ¦           _transformations.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pyrsistent-0.19.3.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.mit
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---python_dateutil-2.8.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---pytz
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   lazy.py
¦   ¦       ¦   ¦   reference.py
¦   ¦       ¦   ¦   tzfile.py
¦   ¦       ¦   ¦   tzinfo.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---zoneinfo
¦   ¦       ¦   ¦   ¦   CET
¦   ¦       ¦   ¦   ¦   CST6CDT
¦   ¦       ¦   ¦   ¦   Cuba
¦   ¦       ¦   ¦   ¦   EET
¦   ¦       ¦   ¦   ¦   Egypt
¦   ¦       ¦   ¦   ¦   Eire
¦   ¦       ¦   ¦   ¦   EST
¦   ¦       ¦   ¦   ¦   EST5EDT
¦   ¦       ¦   ¦   ¦   Factory
¦   ¦       ¦   ¦   ¦   GB
¦   ¦       ¦   ¦   ¦   GB-Eire
¦   ¦       ¦   ¦   ¦   GMT
¦   ¦       ¦   ¦   ¦   GMT+0
¦   ¦       ¦   ¦   ¦   GMT-0
¦   ¦       ¦   ¦   ¦   GMT0
¦   ¦       ¦   ¦   ¦   Greenwich
¦   ¦       ¦   ¦   ¦   Hongkong
¦   ¦       ¦   ¦   ¦   HST
¦   ¦       ¦   ¦   ¦   Iceland
¦   ¦       ¦   ¦   ¦   Iran
¦   ¦       ¦   ¦   ¦   iso3166.tab
¦   ¦       ¦   ¦   ¦   Israel
¦   ¦       ¦   ¦   ¦   Jamaica
¦   ¦       ¦   ¦   ¦   Japan
¦   ¦       ¦   ¦   ¦   Kwajalein
¦   ¦       ¦   ¦   ¦   leapseconds
¦   ¦       ¦   ¦   ¦   Libya
¦   ¦       ¦   ¦   ¦   MET
¦   ¦       ¦   ¦   ¦   MST
¦   ¦       ¦   ¦   ¦   MST7MDT
¦   ¦       ¦   ¦   ¦   Navajo
¦   ¦       ¦   ¦   ¦   NZ
¦   ¦       ¦   ¦   ¦   NZ-CHAT
¦   ¦       ¦   ¦   ¦   Poland
¦   ¦       ¦   ¦   ¦   Portugal
¦   ¦       ¦   ¦   ¦   PRC
¦   ¦       ¦   ¦   ¦   PST8PDT
¦   ¦       ¦   ¦   ¦   ROC
¦   ¦       ¦   ¦   ¦   ROK
¦   ¦       ¦   ¦   ¦   Singapore
¦   ¦       ¦   ¦   ¦   Turkey
¦   ¦       ¦   ¦   ¦   tzdata.zi
¦   ¦       ¦   ¦   ¦   UCT
¦   ¦       ¦   ¦   ¦   Universal
¦   ¦       ¦   ¦   ¦   UTC
¦   ¦       ¦   ¦   ¦   W-SU
¦   ¦       ¦   ¦   ¦   WET
¦   ¦       ¦   ¦   ¦   zone.tab
¦   ¦       ¦   ¦   ¦   zone1970.tab
¦   ¦       ¦   ¦   ¦   Zulu
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---Africa
¦   ¦       ¦   ¦   ¦       Abidjan
¦   ¦       ¦   ¦   ¦       Accra
¦   ¦       ¦   ¦   ¦       Addis_Ababa
¦   ¦       ¦   ¦   ¦       Algiers
¦   ¦       ¦   ¦   ¦       Asmara
¦   ¦       ¦   ¦   ¦       Asmera
¦   ¦       ¦   ¦   ¦       Bamako
¦   ¦       ¦   ¦   ¦       Bangui
¦   ¦       ¦   ¦   ¦       Banjul
¦   ¦       ¦   ¦   ¦       Bissau
¦   ¦       ¦   ¦   ¦       Blantyre
¦   ¦       ¦   ¦   ¦       Brazzaville
¦   ¦       ¦   ¦   ¦       Bujumbura
¦   ¦       ¦   ¦   ¦       Cairo
¦   ¦       ¦   ¦   ¦       Casablanca
¦   ¦       ¦   ¦   ¦       Ceuta
¦   ¦       ¦   ¦   ¦       Conakry
¦   ¦       ¦   ¦   ¦       Dakar
¦   ¦       ¦   ¦   ¦       Dar_es_Salaam
¦   ¦       ¦   ¦   ¦       Djibouti
¦   ¦       ¦   ¦   ¦       Douala
¦   ¦       ¦   ¦   ¦       El_Aaiun
¦   ¦       ¦   ¦   ¦       Freetown
¦   ¦       ¦   ¦   ¦       Gaborone
¦   ¦       ¦   ¦   ¦       Harare
¦   ¦       ¦   ¦   ¦       Johannesburg
¦   ¦       ¦   ¦   ¦       Juba
¦   ¦       ¦   ¦   ¦       Kampala
¦   ¦       ¦   ¦   ¦       Khartoum
¦   ¦       ¦   ¦   ¦       Kigali
¦   ¦       ¦   ¦   ¦       Kinshasa
¦   ¦       ¦   ¦   ¦       Lagos
¦   ¦       ¦   ¦   ¦       Libreville
¦   ¦       ¦   ¦   ¦       Lome
¦   ¦       ¦   ¦   ¦       Luanda
¦   ¦       ¦   ¦   ¦       Lubumbashi
¦   ¦       ¦   ¦   ¦       Lusaka
¦   ¦       ¦   ¦   ¦       Malabo
¦   ¦       ¦   ¦   ¦       Maputo
¦   ¦       ¦   ¦   ¦       Maseru
¦   ¦       ¦   ¦   ¦       Mbabane
¦   ¦       ¦   ¦   ¦       Mogadishu
¦   ¦       ¦   ¦   ¦       Monrovia
¦   ¦       ¦   ¦   ¦       Nairobi
¦   ¦       ¦   ¦   ¦       Ndjamena
¦   ¦       ¦   ¦   ¦       Niamey
¦   ¦       ¦   ¦   ¦       Nouakchott
¦   ¦       ¦   ¦   ¦       Ouagadougou
¦   ¦       ¦   ¦   ¦       Porto-Novo
¦   ¦       ¦   ¦   ¦       Sao_Tome
¦   ¦       ¦   ¦   ¦       Timbuktu
¦   ¦       ¦   ¦   ¦       Tripoli
¦   ¦       ¦   ¦   ¦       Tunis
¦   ¦       ¦   ¦   ¦       Windhoek
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---America
¦   ¦       ¦   ¦   ¦   ¦   Adak
¦   ¦       ¦   ¦   ¦   ¦   Anchorage
¦   ¦       ¦   ¦   ¦   ¦   Anguilla
¦   ¦       ¦   ¦   ¦   ¦   Antigua
¦   ¦       ¦   ¦   ¦   ¦   Araguaina
¦   ¦       ¦   ¦   ¦   ¦   Aruba
¦   ¦       ¦   ¦   ¦   ¦   Asuncion
¦   ¦       ¦   ¦   ¦   ¦   Atikokan
¦   ¦       ¦   ¦   ¦   ¦   Atka
¦   ¦       ¦   ¦   ¦   ¦   Bahia
¦   ¦       ¦   ¦   ¦   ¦   Bahia_Banderas
¦   ¦       ¦   ¦   ¦   ¦   Barbados
¦   ¦       ¦   ¦   ¦   ¦   Belem
¦   ¦       ¦   ¦   ¦   ¦   Belize
¦   ¦       ¦   ¦   ¦   ¦   Blanc-Sablon
¦   ¦       ¦   ¦   ¦   ¦   Boa_Vista
¦   ¦       ¦   ¦   ¦   ¦   Bogota
¦   ¦       ¦   ¦   ¦   ¦   Boise
¦   ¦       ¦   ¦   ¦   ¦   Buenos_Aires
¦   ¦       ¦   ¦   ¦   ¦   Cambridge_Bay
¦   ¦       ¦   ¦   ¦   ¦   Campo_Grande
¦   ¦       ¦   ¦   ¦   ¦   Cancun
¦   ¦       ¦   ¦   ¦   ¦   Caracas
¦   ¦       ¦   ¦   ¦   ¦   Catamarca
¦   ¦       ¦   ¦   ¦   ¦   Cayenne
¦   ¦       ¦   ¦   ¦   ¦   Cayman
¦   ¦       ¦   ¦   ¦   ¦   Chicago
¦   ¦       ¦   ¦   ¦   ¦   Chihuahua
¦   ¦       ¦   ¦   ¦   ¦   Ciudad_Juarez
¦   ¦       ¦   ¦   ¦   ¦   Coral_Harbour
¦   ¦       ¦   ¦   ¦   ¦   Cordoba
¦   ¦       ¦   ¦   ¦   ¦   Costa_Rica
¦   ¦       ¦   ¦   ¦   ¦   Creston
¦   ¦       ¦   ¦   ¦   ¦   Cuiaba
¦   ¦       ¦   ¦   ¦   ¦   Curacao
¦   ¦       ¦   ¦   ¦   ¦   Danmarkshavn
¦   ¦       ¦   ¦   ¦   ¦   Dawson
¦   ¦       ¦   ¦   ¦   ¦   Dawson_Creek
¦   ¦       ¦   ¦   ¦   ¦   Denver
¦   ¦       ¦   ¦   ¦   ¦   Detroit
¦   ¦       ¦   ¦   ¦   ¦   Dominica
¦   ¦       ¦   ¦   ¦   ¦   Edmonton
¦   ¦       ¦   ¦   ¦   ¦   Eirunepe
¦   ¦       ¦   ¦   ¦   ¦   El_Salvador
¦   ¦       ¦   ¦   ¦   ¦   Ensenada
¦   ¦       ¦   ¦   ¦   ¦   Fortaleza
¦   ¦       ¦   ¦   ¦   ¦   Fort_Nelson
¦   ¦       ¦   ¦   ¦   ¦   Fort_Wayne
¦   ¦       ¦   ¦   ¦   ¦   Glace_Bay
¦   ¦       ¦   ¦   ¦   ¦   Godthab
¦   ¦       ¦   ¦   ¦   ¦   Goose_Bay
¦   ¦       ¦   ¦   ¦   ¦   Grand_Turk
¦   ¦       ¦   ¦   ¦   ¦   Grenada
¦   ¦       ¦   ¦   ¦   ¦   Guadeloupe
¦   ¦       ¦   ¦   ¦   ¦   Guatemala
¦   ¦       ¦   ¦   ¦   ¦   Guayaquil
¦   ¦       ¦   ¦   ¦   ¦   Guyana
¦   ¦       ¦   ¦   ¦   ¦   Halifax
¦   ¦       ¦   ¦   ¦   ¦   Havana
¦   ¦       ¦   ¦   ¦   ¦   Hermosillo
¦   ¦       ¦   ¦   ¦   ¦   Indianapolis
¦   ¦       ¦   ¦   ¦   ¦   Inuvik
¦   ¦       ¦   ¦   ¦   ¦   Iqaluit
¦   ¦       ¦   ¦   ¦   ¦   Jamaica
¦   ¦       ¦   ¦   ¦   ¦   Jujuy
¦   ¦       ¦   ¦   ¦   ¦   Juneau
¦   ¦       ¦   ¦   ¦   ¦   Knox_IN
¦   ¦       ¦   ¦   ¦   ¦   Kralendijk
¦   ¦       ¦   ¦   ¦   ¦   La_Paz
¦   ¦       ¦   ¦   ¦   ¦   Lima
¦   ¦       ¦   ¦   ¦   ¦   Los_Angeles
¦   ¦       ¦   ¦   ¦   ¦   Louisville
¦   ¦       ¦   ¦   ¦   ¦   Lower_Princes
¦   ¦       ¦   ¦   ¦   ¦   Maceio
¦   ¦       ¦   ¦   ¦   ¦   Managua
¦   ¦       ¦   ¦   ¦   ¦   Manaus
¦   ¦       ¦   ¦   ¦   ¦   Marigot
¦   ¦       ¦   ¦   ¦   ¦   Martinique
¦   ¦       ¦   ¦   ¦   ¦   Matamoros
¦   ¦       ¦   ¦   ¦   ¦   Mazatlan
¦   ¦       ¦   ¦   ¦   ¦   Mendoza
¦   ¦       ¦   ¦   ¦   ¦   Menominee
¦   ¦       ¦   ¦   ¦   ¦   Merida
¦   ¦       ¦   ¦   ¦   ¦   Metlakatla
¦   ¦       ¦   ¦   ¦   ¦   Mexico_City
¦   ¦       ¦   ¦   ¦   ¦   Miquelon
¦   ¦       ¦   ¦   ¦   ¦   Moncton
¦   ¦       ¦   ¦   ¦   ¦   Monterrey
¦   ¦       ¦   ¦   ¦   ¦   Montevideo
¦   ¦       ¦   ¦   ¦   ¦   Montreal
¦   ¦       ¦   ¦   ¦   ¦   Montserrat
¦   ¦       ¦   ¦   ¦   ¦   Nassau
¦   ¦       ¦   ¦   ¦   ¦   New_York
¦   ¦       ¦   ¦   ¦   ¦   Nipigon
¦   ¦       ¦   ¦   ¦   ¦   Nome
¦   ¦       ¦   ¦   ¦   ¦   Noronha
¦   ¦       ¦   ¦   ¦   ¦   Nuuk
¦   ¦       ¦   ¦   ¦   ¦   Ojinaga
¦   ¦       ¦   ¦   ¦   ¦   Panama
¦   ¦       ¦   ¦   ¦   ¦   Pangnirtung
¦   ¦       ¦   ¦   ¦   ¦   Paramaribo
¦   ¦       ¦   ¦   ¦   ¦   Phoenix
¦   ¦       ¦   ¦   ¦   ¦   Port-au-Prince
¦   ¦       ¦   ¦   ¦   ¦   Porto_Acre
¦   ¦       ¦   ¦   ¦   ¦   Porto_Velho
¦   ¦       ¦   ¦   ¦   ¦   Port_of_Spain
¦   ¦       ¦   ¦   ¦   ¦   Puerto_Rico
¦   ¦       ¦   ¦   ¦   ¦   Punta_Arenas
¦   ¦       ¦   ¦   ¦   ¦   Rainy_River
¦   ¦       ¦   ¦   ¦   ¦   Rankin_Inlet
¦   ¦       ¦   ¦   ¦   ¦   Recife
¦   ¦       ¦   ¦   ¦   ¦   Regina
¦   ¦       ¦   ¦   ¦   ¦   Resolute
¦   ¦       ¦   ¦   ¦   ¦   Rio_Branco
¦   ¦       ¦   ¦   ¦   ¦   Rosario
¦   ¦       ¦   ¦   ¦   ¦   Santarem
¦   ¦       ¦   ¦   ¦   ¦   Santa_Isabel
¦   ¦       ¦   ¦   ¦   ¦   Santiago
¦   ¦       ¦   ¦   ¦   ¦   Santo_Domingo
¦   ¦       ¦   ¦   ¦   ¦   Sao_Paulo
¦   ¦       ¦   ¦   ¦   ¦   Scoresbysund
¦   ¦       ¦   ¦   ¦   ¦   Shiprock
¦   ¦       ¦   ¦   ¦   ¦   Sitka
¦   ¦       ¦   ¦   ¦   ¦   St_Barthelemy
¦   ¦       ¦   ¦   ¦   ¦   St_Johns
¦   ¦       ¦   ¦   ¦   ¦   St_Kitts
¦   ¦       ¦   ¦   ¦   ¦   St_Lucia
¦   ¦       ¦   ¦   ¦   ¦   St_Thomas
¦   ¦       ¦   ¦   ¦   ¦   St_Vincent
¦   ¦       ¦   ¦   ¦   ¦   Swift_Current
¦   ¦       ¦   ¦   ¦   ¦   Tegucigalpa
¦   ¦       ¦   ¦   ¦   ¦   Thule
¦   ¦       ¦   ¦   ¦   ¦   Thunder_Bay
¦   ¦       ¦   ¦   ¦   ¦   Tijuana
¦   ¦       ¦   ¦   ¦   ¦   Toronto
¦   ¦       ¦   ¦   ¦   ¦   Tortola
¦   ¦       ¦   ¦   ¦   ¦   Vancouver
¦   ¦       ¦   ¦   ¦   ¦   Virgin
¦   ¦       ¦   ¦   ¦   ¦   Whitehorse
¦   ¦       ¦   ¦   ¦   ¦   Winnipeg
¦   ¦       ¦   ¦   ¦   ¦   Yakutat
¦   ¦       ¦   ¦   ¦   ¦   Yellowknife
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---Argentina
¦   ¦       ¦   ¦   ¦   ¦       Buenos_Aires
¦   ¦       ¦   ¦   ¦   ¦       Catamarca
¦   ¦       ¦   ¦   ¦   ¦       ComodRivadavia
¦   ¦       ¦   ¦   ¦   ¦       Cordoba
¦   ¦       ¦   ¦   ¦   ¦       Jujuy
¦   ¦       ¦   ¦   ¦   ¦       La_Rioja
¦   ¦       ¦   ¦   ¦   ¦       Mendoza
¦   ¦       ¦   ¦   ¦   ¦       Rio_Gallegos
¦   ¦       ¦   ¦   ¦   ¦       Salta
¦   ¦       ¦   ¦   ¦   ¦       San_Juan
¦   ¦       ¦   ¦   ¦   ¦       San_Luis
¦   ¦       ¦   ¦   ¦   ¦       Tucuman
¦   ¦       ¦   ¦   ¦   ¦       Ushuaia
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---Indiana
¦   ¦       ¦   ¦   ¦   ¦       Indianapolis
¦   ¦       ¦   ¦   ¦   ¦       Knox
¦   ¦       ¦   ¦   ¦   ¦       Marengo
¦   ¦       ¦   ¦   ¦   ¦       Petersburg
¦   ¦       ¦   ¦   ¦   ¦       Tell_City
¦   ¦       ¦   ¦   ¦   ¦       Vevay
¦   ¦       ¦   ¦   ¦   ¦       Vincennes
¦   ¦       ¦   ¦   ¦   ¦       Winamac
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---Kentucky
¦   ¦       ¦   ¦   ¦   ¦       Louisville
¦   ¦       ¦   ¦   ¦   ¦       Monticello
¦   ¦       ¦   ¦   ¦   ¦       
¦   ¦       ¦   ¦   ¦   +---North_Dakota
¦   ¦       ¦   ¦   ¦           Beulah
¦   ¦       ¦   ¦   ¦           Center
¦   ¦       ¦   ¦   ¦           New_Salem
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Antarctica
¦   ¦       ¦   ¦   ¦       Casey
¦   ¦       ¦   ¦   ¦       Davis
¦   ¦       ¦   ¦   ¦       DumontDUrville
¦   ¦       ¦   ¦   ¦       Macquarie
¦   ¦       ¦   ¦   ¦       Mawson
¦   ¦       ¦   ¦   ¦       McMurdo
¦   ¦       ¦   ¦   ¦       Palmer
¦   ¦       ¦   ¦   ¦       Rothera
¦   ¦       ¦   ¦   ¦       South_Pole
¦   ¦       ¦   ¦   ¦       Syowa
¦   ¦       ¦   ¦   ¦       Troll
¦   ¦       ¦   ¦   ¦       Vostok
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Arctic
¦   ¦       ¦   ¦   ¦       Longyearbyen
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Asia
¦   ¦       ¦   ¦   ¦       Aden
¦   ¦       ¦   ¦   ¦       Almaty
¦   ¦       ¦   ¦   ¦       Amman
¦   ¦       ¦   ¦   ¦       Anadyr
¦   ¦       ¦   ¦   ¦       Aqtau
¦   ¦       ¦   ¦   ¦       Aqtobe
¦   ¦       ¦   ¦   ¦       Ashgabat
¦   ¦       ¦   ¦   ¦       Ashkhabad
¦   ¦       ¦   ¦   ¦       Atyrau
¦   ¦       ¦   ¦   ¦       Baghdad
¦   ¦       ¦   ¦   ¦       Bahrain
¦   ¦       ¦   ¦   ¦       Baku
¦   ¦       ¦   ¦   ¦       Bangkok
¦   ¦       ¦   ¦   ¦       Barnaul
¦   ¦       ¦   ¦   ¦       Beirut
¦   ¦       ¦   ¦   ¦       Bishkek
¦   ¦       ¦   ¦   ¦       Brunei
¦   ¦       ¦   ¦   ¦       Calcutta
¦   ¦       ¦   ¦   ¦       Chita
¦   ¦       ¦   ¦   ¦       Choibalsan
¦   ¦       ¦   ¦   ¦       Chongqing
¦   ¦       ¦   ¦   ¦       Chungking
¦   ¦       ¦   ¦   ¦       Colombo
¦   ¦       ¦   ¦   ¦       Dacca
¦   ¦       ¦   ¦   ¦       Damascus
¦   ¦       ¦   ¦   ¦       Dhaka
¦   ¦       ¦   ¦   ¦       Dili
¦   ¦       ¦   ¦   ¦       Dubai
¦   ¦       ¦   ¦   ¦       Dushanbe
¦   ¦       ¦   ¦   ¦       Famagusta
¦   ¦       ¦   ¦   ¦       Gaza
¦   ¦       ¦   ¦   ¦       Harbin
¦   ¦       ¦   ¦   ¦       Hebron
¦   ¦       ¦   ¦   ¦       Hong_Kong
¦   ¦       ¦   ¦   ¦       Hovd
¦   ¦       ¦   ¦   ¦       Ho_Chi_Minh
¦   ¦       ¦   ¦   ¦       Irkutsk
¦   ¦       ¦   ¦   ¦       Istanbul
¦   ¦       ¦   ¦   ¦       Jakarta
¦   ¦       ¦   ¦   ¦       Jayapura
¦   ¦       ¦   ¦   ¦       Jerusalem
¦   ¦       ¦   ¦   ¦       Kabul
¦   ¦       ¦   ¦   ¦       Kamchatka
¦   ¦       ¦   ¦   ¦       Karachi
¦   ¦       ¦   ¦   ¦       Kashgar
¦   ¦       ¦   ¦   ¦       Kathmandu
¦   ¦       ¦   ¦   ¦       Katmandu
¦   ¦       ¦   ¦   ¦       Khandyga
¦   ¦       ¦   ¦   ¦       Kolkata
¦   ¦       ¦   ¦   ¦       Krasnoyarsk
¦   ¦       ¦   ¦   ¦       Kuala_Lumpur
¦   ¦       ¦   ¦   ¦       Kuching
¦   ¦       ¦   ¦   ¦       Kuwait
¦   ¦       ¦   ¦   ¦       Macao
¦   ¦       ¦   ¦   ¦       Macau
¦   ¦       ¦   ¦   ¦       Magadan
¦   ¦       ¦   ¦   ¦       Makassar
¦   ¦       ¦   ¦   ¦       Manila
¦   ¦       ¦   ¦   ¦       Muscat
¦   ¦       ¦   ¦   ¦       Nicosia
¦   ¦       ¦   ¦   ¦       Novokuznetsk
¦   ¦       ¦   ¦   ¦       Novosibirsk
¦   ¦       ¦   ¦   ¦       Omsk
¦   ¦       ¦   ¦   ¦       Oral
¦   ¦       ¦   ¦   ¦       Phnom_Penh
¦   ¦       ¦   ¦   ¦       Pontianak
¦   ¦       ¦   ¦   ¦       Pyongyang
¦   ¦       ¦   ¦   ¦       Qatar
¦   ¦       ¦   ¦   ¦       Qostanay
¦   ¦       ¦   ¦   ¦       Qyzylorda
¦   ¦       ¦   ¦   ¦       Rangoon
¦   ¦       ¦   ¦   ¦       Riyadh
¦   ¦       ¦   ¦   ¦       Saigon
¦   ¦       ¦   ¦   ¦       Sakhalin
¦   ¦       ¦   ¦   ¦       Samarkand
¦   ¦       ¦   ¦   ¦       Seoul
¦   ¦       ¦   ¦   ¦       Shanghai
¦   ¦       ¦   ¦   ¦       Singapore
¦   ¦       ¦   ¦   ¦       Srednekolymsk
¦   ¦       ¦   ¦   ¦       Taipei
¦   ¦       ¦   ¦   ¦       Tashkent
¦   ¦       ¦   ¦   ¦       Tbilisi
¦   ¦       ¦   ¦   ¦       Tehran
¦   ¦       ¦   ¦   ¦       Tel_Aviv
¦   ¦       ¦   ¦   ¦       Thimbu
¦   ¦       ¦   ¦   ¦       Thimphu
¦   ¦       ¦   ¦   ¦       Tokyo
¦   ¦       ¦   ¦   ¦       Tomsk
¦   ¦       ¦   ¦   ¦       Ujung_Pandang
¦   ¦       ¦   ¦   ¦       Ulaanbaatar
¦   ¦       ¦   ¦   ¦       Ulan_Bator
¦   ¦       ¦   ¦   ¦       Urumqi
¦   ¦       ¦   ¦   ¦       Ust-Nera
¦   ¦       ¦   ¦   ¦       Vientiane
¦   ¦       ¦   ¦   ¦       Vladivostok
¦   ¦       ¦   ¦   ¦       Yakutsk
¦   ¦       ¦   ¦   ¦       Yangon
¦   ¦       ¦   ¦   ¦       Yekaterinburg
¦   ¦       ¦   ¦   ¦       Yerevan
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Atlantic
¦   ¦       ¦   ¦   ¦       Azores
¦   ¦       ¦   ¦   ¦       Bermuda
¦   ¦       ¦   ¦   ¦       Canary
¦   ¦       ¦   ¦   ¦       Cape_Verde
¦   ¦       ¦   ¦   ¦       Faeroe
¦   ¦       ¦   ¦   ¦       Faroe
¦   ¦       ¦   ¦   ¦       Jan_Mayen
¦   ¦       ¦   ¦   ¦       Madeira
¦   ¦       ¦   ¦   ¦       Reykjavik
¦   ¦       ¦   ¦   ¦       South_Georgia
¦   ¦       ¦   ¦   ¦       Stanley
¦   ¦       ¦   ¦   ¦       St_Helena
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Australia
¦   ¦       ¦   ¦   ¦       ACT
¦   ¦       ¦   ¦   ¦       Adelaide
¦   ¦       ¦   ¦   ¦       Brisbane
¦   ¦       ¦   ¦   ¦       Broken_Hill
¦   ¦       ¦   ¦   ¦       Canberra
¦   ¦       ¦   ¦   ¦       Currie
¦   ¦       ¦   ¦   ¦       Darwin
¦   ¦       ¦   ¦   ¦       Eucla
¦   ¦       ¦   ¦   ¦       Hobart
¦   ¦       ¦   ¦   ¦       LHI
¦   ¦       ¦   ¦   ¦       Lindeman
¦   ¦       ¦   ¦   ¦       Lord_Howe
¦   ¦       ¦   ¦   ¦       Melbourne
¦   ¦       ¦   ¦   ¦       North
¦   ¦       ¦   ¦   ¦       NSW
¦   ¦       ¦   ¦   ¦       Perth
¦   ¦       ¦   ¦   ¦       Queensland
¦   ¦       ¦   ¦   ¦       South
¦   ¦       ¦   ¦   ¦       Sydney
¦   ¦       ¦   ¦   ¦       Tasmania
¦   ¦       ¦   ¦   ¦       Victoria
¦   ¦       ¦   ¦   ¦       West
¦   ¦       ¦   ¦   ¦       Yancowinna
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Brazil
¦   ¦       ¦   ¦   ¦       Acre
¦   ¦       ¦   ¦   ¦       DeNoronha
¦   ¦       ¦   ¦   ¦       East
¦   ¦       ¦   ¦   ¦       West
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Canada
¦   ¦       ¦   ¦   ¦       Atlantic
¦   ¦       ¦   ¦   ¦       Central
¦   ¦       ¦   ¦   ¦       Eastern
¦   ¦       ¦   ¦   ¦       Mountain
¦   ¦       ¦   ¦   ¦       Newfoundland
¦   ¦       ¦   ¦   ¦       Pacific
¦   ¦       ¦   ¦   ¦       Saskatchewan
¦   ¦       ¦   ¦   ¦       Yukon
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Chile
¦   ¦       ¦   ¦   ¦       Continental
¦   ¦       ¦   ¦   ¦       EasterIsland
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Etc
¦   ¦       ¦   ¦   ¦       GMT
¦   ¦       ¦   ¦   ¦       GMT+0
¦   ¦       ¦   ¦   ¦       GMT+1
¦   ¦       ¦   ¦   ¦       GMT+10
¦   ¦       ¦   ¦   ¦       GMT+11
¦   ¦       ¦   ¦   ¦       GMT+12
¦   ¦       ¦   ¦   ¦       GMT+2
¦   ¦       ¦   ¦   ¦       GMT+3
¦   ¦       ¦   ¦   ¦       GMT+4
¦   ¦       ¦   ¦   ¦       GMT+5
¦   ¦       ¦   ¦   ¦       GMT+6
¦   ¦       ¦   ¦   ¦       GMT+7
¦   ¦       ¦   ¦   ¦       GMT+8
¦   ¦       ¦   ¦   ¦       GMT+9
¦   ¦       ¦   ¦   ¦       GMT-0
¦   ¦       ¦   ¦   ¦       GMT-1
¦   ¦       ¦   ¦   ¦       GMT-10
¦   ¦       ¦   ¦   ¦       GMT-11
¦   ¦       ¦   ¦   ¦       GMT-12
¦   ¦       ¦   ¦   ¦       GMT-13
¦   ¦       ¦   ¦   ¦       GMT-14
¦   ¦       ¦   ¦   ¦       GMT-2
¦   ¦       ¦   ¦   ¦       GMT-3
¦   ¦       ¦   ¦   ¦       GMT-4
¦   ¦       ¦   ¦   ¦       GMT-5
¦   ¦       ¦   ¦   ¦       GMT-6
¦   ¦       ¦   ¦   ¦       GMT-7
¦   ¦       ¦   ¦   ¦       GMT-8
¦   ¦       ¦   ¦   ¦       GMT-9
¦   ¦       ¦   ¦   ¦       GMT0
¦   ¦       ¦   ¦   ¦       Greenwich
¦   ¦       ¦   ¦   ¦       UCT
¦   ¦       ¦   ¦   ¦       Universal
¦   ¦       ¦   ¦   ¦       UTC
¦   ¦       ¦   ¦   ¦       Zulu
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Europe
¦   ¦       ¦   ¦   ¦       Amsterdam
¦   ¦       ¦   ¦   ¦       Andorra
¦   ¦       ¦   ¦   ¦       Astrakhan
¦   ¦       ¦   ¦   ¦       Athens
¦   ¦       ¦   ¦   ¦       Belfast
¦   ¦       ¦   ¦   ¦       Belgrade
¦   ¦       ¦   ¦   ¦       Berlin
¦   ¦       ¦   ¦   ¦       Bratislava
¦   ¦       ¦   ¦   ¦       Brussels
¦   ¦       ¦   ¦   ¦       Bucharest
¦   ¦       ¦   ¦   ¦       Budapest
¦   ¦       ¦   ¦   ¦       Busingen
¦   ¦       ¦   ¦   ¦       Chisinau
¦   ¦       ¦   ¦   ¦       Copenhagen
¦   ¦       ¦   ¦   ¦       Dublin
¦   ¦       ¦   ¦   ¦       Gibraltar
¦   ¦       ¦   ¦   ¦       Guernsey
¦   ¦       ¦   ¦   ¦       Helsinki
¦   ¦       ¦   ¦   ¦       Isle_of_Man
¦   ¦       ¦   ¦   ¦       Istanbul
¦   ¦       ¦   ¦   ¦       Jersey
¦   ¦       ¦   ¦   ¦       Kaliningrad
¦   ¦       ¦   ¦   ¦       Kiev
¦   ¦       ¦   ¦   ¦       Kirov
¦   ¦       ¦   ¦   ¦       Kyiv
¦   ¦       ¦   ¦   ¦       Lisbon
¦   ¦       ¦   ¦   ¦       Ljubljana
¦   ¦       ¦   ¦   ¦       London
¦   ¦       ¦   ¦   ¦       Luxembourg
¦   ¦       ¦   ¦   ¦       Madrid
¦   ¦       ¦   ¦   ¦       Malta
¦   ¦       ¦   ¦   ¦       Mariehamn
¦   ¦       ¦   ¦   ¦       Minsk
¦   ¦       ¦   ¦   ¦       Monaco
¦   ¦       ¦   ¦   ¦       Moscow
¦   ¦       ¦   ¦   ¦       Nicosia
¦   ¦       ¦   ¦   ¦       Oslo
¦   ¦       ¦   ¦   ¦       Paris
¦   ¦       ¦   ¦   ¦       Podgorica
¦   ¦       ¦   ¦   ¦       Prague
¦   ¦       ¦   ¦   ¦       Riga
¦   ¦       ¦   ¦   ¦       Rome
¦   ¦       ¦   ¦   ¦       Samara
¦   ¦       ¦   ¦   ¦       San_Marino
¦   ¦       ¦   ¦   ¦       Sarajevo
¦   ¦       ¦   ¦   ¦       Saratov
¦   ¦       ¦   ¦   ¦       Simferopol
¦   ¦       ¦   ¦   ¦       Skopje
¦   ¦       ¦   ¦   ¦       Sofia
¦   ¦       ¦   ¦   ¦       Stockholm
¦   ¦       ¦   ¦   ¦       Tallinn
¦   ¦       ¦   ¦   ¦       Tirane
¦   ¦       ¦   ¦   ¦       Tiraspol
¦   ¦       ¦   ¦   ¦       Ulyanovsk
¦   ¦       ¦   ¦   ¦       Uzhgorod
¦   ¦       ¦   ¦   ¦       Vaduz
¦   ¦       ¦   ¦   ¦       Vatican
¦   ¦       ¦   ¦   ¦       Vienna
¦   ¦       ¦   ¦   ¦       Vilnius
¦   ¦       ¦   ¦   ¦       Volgograd
¦   ¦       ¦   ¦   ¦       Warsaw
¦   ¦       ¦   ¦   ¦       Zagreb
¦   ¦       ¦   ¦   ¦       Zaporozhye
¦   ¦       ¦   ¦   ¦       Zurich
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Indian
¦   ¦       ¦   ¦   ¦       Antananarivo
¦   ¦       ¦   ¦   ¦       Chagos
¦   ¦       ¦   ¦   ¦       Christmas
¦   ¦       ¦   ¦   ¦       Cocos
¦   ¦       ¦   ¦   ¦       Comoro
¦   ¦       ¦   ¦   ¦       Kerguelen
¦   ¦       ¦   ¦   ¦       Mahe
¦   ¦       ¦   ¦   ¦       Maldives
¦   ¦       ¦   ¦   ¦       Mauritius
¦   ¦       ¦   ¦   ¦       Mayotte
¦   ¦       ¦   ¦   ¦       Reunion
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Mexico
¦   ¦       ¦   ¦   ¦       BajaNorte
¦   ¦       ¦   ¦   ¦       BajaSur
¦   ¦       ¦   ¦   ¦       General
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---Pacific
¦   ¦       ¦   ¦   ¦       Apia
¦   ¦       ¦   ¦   ¦       Auckland
¦   ¦       ¦   ¦   ¦       Bougainville
¦   ¦       ¦   ¦   ¦       Chatham
¦   ¦       ¦   ¦   ¦       Chuuk
¦   ¦       ¦   ¦   ¦       Easter
¦   ¦       ¦   ¦   ¦       Efate
¦   ¦       ¦   ¦   ¦       Enderbury
¦   ¦       ¦   ¦   ¦       Fakaofo
¦   ¦       ¦   ¦   ¦       Fiji
¦   ¦       ¦   ¦   ¦       Funafuti
¦   ¦       ¦   ¦   ¦       Galapagos
¦   ¦       ¦   ¦   ¦       Gambier
¦   ¦       ¦   ¦   ¦       Guadalcanal
¦   ¦       ¦   ¦   ¦       Guam
¦   ¦       ¦   ¦   ¦       Honolulu
¦   ¦       ¦   ¦   ¦       Johnston
¦   ¦       ¦   ¦   ¦       Kanton
¦   ¦       ¦   ¦   ¦       Kiritimati
¦   ¦       ¦   ¦   ¦       Kosrae
¦   ¦       ¦   ¦   ¦       Kwajalein
¦   ¦       ¦   ¦   ¦       Majuro
¦   ¦       ¦   ¦   ¦       Marquesas
¦   ¦       ¦   ¦   ¦       Midway
¦   ¦       ¦   ¦   ¦       Nauru
¦   ¦       ¦   ¦   ¦       Niue
¦   ¦       ¦   ¦   ¦       Norfolk
¦   ¦       ¦   ¦   ¦       Noumea
¦   ¦       ¦   ¦   ¦       Pago_Pago
¦   ¦       ¦   ¦   ¦       Palau
¦   ¦       ¦   ¦   ¦       Pitcairn
¦   ¦       ¦   ¦   ¦       Pohnpei
¦   ¦       ¦   ¦   ¦       Ponape
¦   ¦       ¦   ¦   ¦       Port_Moresby
¦   ¦       ¦   ¦   ¦       Rarotonga
¦   ¦       ¦   ¦   ¦       Saipan
¦   ¦       ¦   ¦   ¦       Samoa
¦   ¦       ¦   ¦   ¦       Tahiti
¦   ¦       ¦   ¦   ¦       Tarawa
¦   ¦       ¦   ¦   ¦       Tongatapu
¦   ¦       ¦   ¦   ¦       Truk
¦   ¦       ¦   ¦   ¦       Wake
¦   ¦       ¦   ¦   ¦       Wallis
¦   ¦       ¦   ¦   ¦       Yap
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---US
¦   ¦       ¦   ¦           Alaska
¦   ¦       ¦   ¦           Aleutian
¦   ¦       ¦   ¦           Arizona
¦   ¦       ¦   ¦           Central
¦   ¦       ¦   ¦           East-Indiana
¦   ¦       ¦   ¦           Eastern
¦   ¦       ¦   ¦           Hawaii
¦   ¦       ¦   ¦           Indiana-Starke
¦   ¦       ¦   ¦           Michigan
¦   ¦       ¦   ¦           Mountain
¦   ¦       ¦   ¦           Pacific
¦   ¦       ¦   ¦           Samoa
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           lazy.cpython-38.pyc
¦   ¦       ¦           reference.cpython-38.pyc
¦   ¦       ¦           tzfile.cpython-38.pyc
¦   ¦       ¦           tzinfo.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---pytz-2022.7.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---redis
¦   ¦       ¦   ¦   backoff.py
¦   ¦       ¦   ¦   client.py
¦   ¦       ¦   ¦   cluster.py
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   connection.py
¦   ¦       ¦   ¦   crc.py
¦   ¦       ¦   ¦   credentials.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   lock.py
¦   ¦       ¦   ¦   ocsp.py
¦   ¦       ¦   ¦   retry.py
¦   ¦       ¦   ¦   sentinel.py
¦   ¦       ¦   ¦   typing.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---asyncio
¦   ¦       ¦   ¦   ¦   client.py
¦   ¦       ¦   ¦   ¦   cluster.py
¦   ¦       ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   lock.py
¦   ¦       ¦   ¦   ¦   parser.py
¦   ¦       ¦   ¦   ¦   retry.py
¦   ¦       ¦   ¦   ¦   sentinel.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           client.cpython-38.pyc
¦   ¦       ¦   ¦           cluster.cpython-38.pyc
¦   ¦       ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦           lock.cpython-38.pyc
¦   ¦       ¦   ¦           parser.cpython-38.pyc
¦   ¦       ¦   ¦           retry.cpython-38.pyc
¦   ¦       ¦   ¦           sentinel.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---commands
¦   ¦       ¦   ¦   ¦   cluster.py
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   helpers.py
¦   ¦       ¦   ¦   ¦   parser.py
¦   ¦       ¦   ¦   ¦   redismodules.py
¦   ¦       ¦   ¦   ¦   sentinel.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---bf
¦   ¦       ¦   ¦   ¦   ¦   commands.py
¦   ¦       ¦   ¦   ¦   ¦   info.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           commands.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---graph
¦   ¦       ¦   ¦   ¦   ¦   commands.py
¦   ¦       ¦   ¦   ¦   ¦   edge.py
¦   ¦       ¦   ¦   ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ¦   ¦   execution_plan.py
¦   ¦       ¦   ¦   ¦   ¦   node.py
¦   ¦       ¦   ¦   ¦   ¦   path.py
¦   ¦       ¦   ¦   ¦   ¦   query_result.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           commands.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           edge.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           exceptions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           execution_plan.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           node.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           path.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           query_result.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---json
¦   ¦       ¦   ¦   ¦   ¦   commands.py
¦   ¦       ¦   ¦   ¦   ¦   decoders.py
¦   ¦       ¦   ¦   ¦   ¦   path.py
¦   ¦       ¦   ¦   ¦   ¦   _util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           commands.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           decoders.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           path.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---search
¦   ¦       ¦   ¦   ¦   ¦   aggregation.py
¦   ¦       ¦   ¦   ¦   ¦   commands.py
¦   ¦       ¦   ¦   ¦   ¦   document.py
¦   ¦       ¦   ¦   ¦   ¦   field.py
¦   ¦       ¦   ¦   ¦   ¦   indexDefinition.py
¦   ¦       ¦   ¦   ¦   ¦   query.py
¦   ¦       ¦   ¦   ¦   ¦   querystring.py
¦   ¦       ¦   ¦   ¦   ¦   reducers.py
¦   ¦       ¦   ¦   ¦   ¦   result.py
¦   ¦       ¦   ¦   ¦   ¦   suggestion.py
¦   ¦       ¦   ¦   ¦   ¦   _util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           aggregation.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           commands.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           document.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           field.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           indexDefinition.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           query.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           querystring.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           reducers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           result.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           suggestion.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---timeseries
¦   ¦       ¦   ¦   ¦   ¦   commands.py
¦   ¦       ¦   ¦   ¦   ¦   info.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           commands.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           cluster.cpython-38.pyc
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           helpers.cpython-38.pyc
¦   ¦       ¦   ¦           parser.cpython-38.pyc
¦   ¦       ¦   ¦           redismodules.cpython-38.pyc
¦   ¦       ¦   ¦           sentinel.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           backoff.cpython-38.pyc
¦   ¦       ¦           client.cpython-38.pyc
¦   ¦       ¦           cluster.cpython-38.pyc
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           connection.cpython-38.pyc
¦   ¦       ¦           crc.cpython-38.pyc
¦   ¦       ¦           credentials.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           lock.cpython-38.pyc
¦   ¦       ¦           ocsp.cpython-38.pyc
¦   ¦       ¦           retry.cpython-38.pyc
¦   ¦       ¦           sentinel.cpython-38.pyc
¦   ¦       ¦           typing.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---redis-4.5.4.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---reportlab
¦   ¦       ¦   ¦   rl_config.py
¦   ¦       ¦   ¦   rl_settings.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---fonts
¦   ¦       ¦   ¦       00readme.txt
¦   ¦       ¦   ¦       bitstream-vera-license.txt
¦   ¦       ¦   ¦       callig15.afm
¦   ¦       ¦   ¦       callig15.pfb
¦   ¦       ¦   ¦       cobo____.pfb
¦   ¦       ¦   ¦       cob_____.pfb
¦   ¦       ¦   ¦       com_____.pfb
¦   ¦       ¦   ¦       coo_____.pfb
¦   ¦       ¦   ¦       DarkGarden-changelog.txt
¦   ¦       ¦   ¦       DarkGarden-copying-gpl.txt
¦   ¦       ¦   ¦       DarkGarden-copying.txt
¦   ¦       ¦   ¦       DarkGarden-readme.txt
¦   ¦       ¦   ¦       DarkGarden.sfd
¦   ¦       ¦   ¦       DarkGardenMK.afm
¦   ¦       ¦   ¦       DarkGardenMK.pfb
¦   ¦       ¦   ¦       sy______.pfb
¦   ¦       ¦   ¦       Vera.ttf
¦   ¦       ¦   ¦       VeraBd.ttf
¦   ¦       ¦   ¦       VeraBI.ttf
¦   ¦       ¦   ¦       VeraIt.ttf
¦   ¦       ¦   ¦       zd______.pfb
¦   ¦       ¦   ¦       zx______.pfb
¦   ¦       ¦   ¦       zy______.pfb
¦   ¦       ¦   ¦       _abi____.pfb
¦   ¦       ¦   ¦       _ab_____.pfb
¦   ¦       ¦   ¦       _ai_____.pfb
¦   ¦       ¦   ¦       _a______.pfb
¦   ¦       ¦   ¦       _ebi____.pfb
¦   ¦       ¦   ¦       _eb_____.pfb
¦   ¦       ¦   ¦       _ei_____.pfb
¦   ¦       ¦   ¦       _er_____.pfb
¦   ¦       ¦   ¦       
¦   ¦       ¦   +---graphics
¦   ¦       ¦   ¦   ¦   renderbase.py
¦   ¦       ¦   ¦   ¦   renderPDF.py
¦   ¦       ¦   ¦   ¦   renderPM.py
¦   ¦       ¦   ¦   ¦   renderPS.py
¦   ¦       ¦   ¦   ¦   renderSVG.py
¦   ¦       ¦   ¦   ¦   shapes.py
¦   ¦       ¦   ¦   ¦   testdrawings.py
¦   ¦       ¦   ¦   ¦   testshapes.py
¦   ¦       ¦   ¦   ¦   transform.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   widgetbase.py
¦   ¦       ¦   ¦   ¦   _renderPM.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---barcode
¦   ¦       ¦   ¦   ¦   ¦   code128.py
¦   ¦       ¦   ¦   ¦   ¦   code39.py
¦   ¦       ¦   ¦   ¦   ¦   code93.py
¦   ¦       ¦   ¦   ¦   ¦   common.py
¦   ¦       ¦   ¦   ¦   ¦   dmtx.py
¦   ¦       ¦   ¦   ¦   ¦   eanbc.py
¦   ¦       ¦   ¦   ¦   ¦   ecc200datamatrix.py
¦   ¦       ¦   ¦   ¦   ¦   fourstate.py
¦   ¦       ¦   ¦   ¦   ¦   lto.py
¦   ¦       ¦   ¦   ¦   ¦   qr.py
¦   ¦       ¦   ¦   ¦   ¦   qrencoder.py
¦   ¦       ¦   ¦   ¦   ¦   test.py
¦   ¦       ¦   ¦   ¦   ¦   usps.py
¦   ¦       ¦   ¦   ¦   ¦   usps4s.py
¦   ¦       ¦   ¦   ¦   ¦   widgets.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           code128.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           code39.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           code93.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           common.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dmtx.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           eanbc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ecc200datamatrix.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           fourstate.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           lto.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           qr.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           qrencoder.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           usps.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           usps4s.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           widgets.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---charts
¦   ¦       ¦   ¦   ¦   ¦   areas.py
¦   ¦       ¦   ¦   ¦   ¦   axes.py
¦   ¦       ¦   ¦   ¦   ¦   barcharts.py
¦   ¦       ¦   ¦   ¦   ¦   dotbox.py
¦   ¦       ¦   ¦   ¦   ¦   doughnut.py
¦   ¦       ¦   ¦   ¦   ¦   legends.py
¦   ¦       ¦   ¦   ¦   ¦   linecharts.py
¦   ¦       ¦   ¦   ¦   ¦   lineplots.py
¦   ¦       ¦   ¦   ¦   ¦   markers.py
¦   ¦       ¦   ¦   ¦   ¦   piecharts.py
¦   ¦       ¦   ¦   ¦   ¦   slidebox.py
¦   ¦       ¦   ¦   ¦   ¦   spider.py
¦   ¦       ¦   ¦   ¦   ¦   textlabels.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   utils3d.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           areas.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           axes.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           barcharts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dotbox.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           doughnut.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           legends.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           linecharts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           lineplots.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           piecharts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           slidebox.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           spider.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           textlabels.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils3d.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---samples
¦   ¦       ¦   ¦   ¦   ¦   bubble.py
¦   ¦       ¦   ¦   ¦   ¦   clustered_bar.py
¦   ¦       ¦   ¦   ¦   ¦   clustered_column.py
¦   ¦       ¦   ¦   ¦   ¦   excelcolors.py
¦   ¦       ¦   ¦   ¦   ¦   exploded_pie.py
¦   ¦       ¦   ¦   ¦   ¦   filled_radar.py
¦   ¦       ¦   ¦   ¦   ¦   linechart_with_markers.py
¦   ¦       ¦   ¦   ¦   ¦   line_chart.py
¦   ¦       ¦   ¦   ¦   ¦   radar.py
¦   ¦       ¦   ¦   ¦   ¦   runall.py
¦   ¦       ¦   ¦   ¦   ¦   scatter.py
¦   ¦       ¦   ¦   ¦   ¦   scatter_lines.py
¦   ¦       ¦   ¦   ¦   ¦   scatter_lines_markers.py
¦   ¦       ¦   ¦   ¦   ¦   simple_pie.py
¦   ¦       ¦   ¦   ¦   ¦   stacked_bar.py
¦   ¦       ¦   ¦   ¦   ¦   stacked_column.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           bubble.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           clustered_bar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           clustered_column.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           excelcolors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           exploded_pie.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           filled_radar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           linechart_with_markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           line_chart.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           radar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           runall.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scatter.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scatter_lines.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scatter_lines_markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           simple_pie.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           stacked_bar.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           stacked_column.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---widgets
¦   ¦       ¦   ¦   ¦   ¦   adjustableArrow.py
¦   ¦       ¦   ¦   ¦   ¦   eventcal.py
¦   ¦       ¦   ¦   ¦   ¦   flags.py
¦   ¦       ¦   ¦   ¦   ¦   grids.py
¦   ¦       ¦   ¦   ¦   ¦   markers.py
¦   ¦       ¦   ¦   ¦   ¦   signsandsymbols.py
¦   ¦       ¦   ¦   ¦   ¦   table.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           adjustableArrow.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           eventcal.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           flags.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           grids.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           signsandsymbols.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           table.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           renderbase.cpython-38.pyc
¦   ¦       ¦   ¦           renderPDF.cpython-38.pyc
¦   ¦       ¦   ¦           renderPM.cpython-38.pyc
¦   ¦       ¦   ¦           renderPS.cpython-38.pyc
¦   ¦       ¦   ¦           renderSVG.cpython-38.pyc
¦   ¦       ¦   ¦           shapes.cpython-38.pyc
¦   ¦       ¦   ¦           testdrawings.cpython-38.pyc
¦   ¦       ¦   ¦           testshapes.cpython-38.pyc
¦   ¦       ¦   ¦           transform.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           widgetbase.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---lib
¦   ¦       ¦   ¦   ¦   abag.py
¦   ¦       ¦   ¦   ¦   arciv.py
¦   ¦       ¦   ¦   ¦   attrmap.py
¦   ¦       ¦   ¦   ¦   boxstuff.py
¦   ¦       ¦   ¦   ¦   codecharts.py
¦   ¦       ¦   ¦   ¦   colors.py
¦   ¦       ¦   ¦   ¦   corp.py
¦   ¦       ¦   ¦   ¦   enums.py
¦   ¦       ¦   ¦   ¦   extformat.py
¦   ¦       ¦   ¦   ¦   fontfinder.py
¦   ¦       ¦   ¦   ¦   fonts.py
¦   ¦       ¦   ¦   ¦   formatters.py
¦   ¦       ¦   ¦   ¦   geomutils.py
¦   ¦       ¦   ¦   ¦   logger.py
¦   ¦       ¦   ¦   ¦   normalDate.py
¦   ¦       ¦   ¦   ¦   pagesizes.py
¦   ¦       ¦   ¦   ¦   pdfencrypt.py
¦   ¦       ¦   ¦   ¦   PyFontify.py
¦   ¦       ¦   ¦   ¦   pygments2xpre.py
¦   ¦       ¦   ¦   ¦   randomtext.py
¦   ¦       ¦   ¦   ¦   rltempfile.py
¦   ¦       ¦   ¦   ¦   rl_accel.py
¦   ¦       ¦   ¦   ¦   rl_safe_eval.py
¦   ¦       ¦   ¦   ¦   rparsexml.py
¦   ¦       ¦   ¦   ¦   sequencer.py
¦   ¦       ¦   ¦   ¦   styles.py
¦   ¦       ¦   ¦   ¦   testutils.py
¦   ¦       ¦   ¦   ¦   textsplit.py
¦   ¦       ¦   ¦   ¦   units.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   validators.py
¦   ¦       ¦   ¦   ¦   yaml.py
¦   ¦       ¦   ¦   ¦   _rl_accel.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           abag.cpython-38.pyc
¦   ¦       ¦   ¦           arciv.cpython-38.pyc
¦   ¦       ¦   ¦           attrmap.cpython-38.pyc
¦   ¦       ¦   ¦           boxstuff.cpython-38.pyc
¦   ¦       ¦   ¦           codecharts.cpython-38.pyc
¦   ¦       ¦   ¦           colors.cpython-38.pyc
¦   ¦       ¦   ¦           corp.cpython-38.pyc
¦   ¦       ¦   ¦           enums.cpython-38.pyc
¦   ¦       ¦   ¦           extformat.cpython-38.pyc
¦   ¦       ¦   ¦           fontfinder.cpython-38.pyc
¦   ¦       ¦   ¦           fonts.cpython-38.pyc
¦   ¦       ¦   ¦           formatters.cpython-38.pyc
¦   ¦       ¦   ¦           geomutils.cpython-38.pyc
¦   ¦       ¦   ¦           logger.cpython-38.pyc
¦   ¦       ¦   ¦           normalDate.cpython-38.pyc
¦   ¦       ¦   ¦           pagesizes.cpython-38.pyc
¦   ¦       ¦   ¦           pdfencrypt.cpython-38.pyc
¦   ¦       ¦   ¦           PyFontify.cpython-38.pyc
¦   ¦       ¦   ¦           pygments2xpre.cpython-38.pyc
¦   ¦       ¦   ¦           randomtext.cpython-38.pyc
¦   ¦       ¦   ¦           rltempfile.cpython-38.pyc
¦   ¦       ¦   ¦           rl_accel.cpython-38.pyc
¦   ¦       ¦   ¦           rl_safe_eval.cpython-38.pyc
¦   ¦       ¦   ¦           rparsexml.cpython-38.pyc
¦   ¦       ¦   ¦           sequencer.cpython-38.pyc
¦   ¦       ¦   ¦           styles.cpython-38.pyc
¦   ¦       ¦   ¦           testutils.cpython-38.pyc
¦   ¦       ¦   ¦           textsplit.cpython-38.pyc
¦   ¦       ¦   ¦           units.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           validators.cpython-38.pyc
¦   ¦       ¦   ¦           yaml.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---pdfbase
¦   ¦       ¦   ¦   ¦   acroform.py
¦   ¦       ¦   ¦   ¦   cidfonts.py
¦   ¦       ¦   ¦   ¦   pdfdoc.py
¦   ¦       ¦   ¦   ¦   pdfform.py
¦   ¦       ¦   ¦   ¦   pdfmetrics.py
¦   ¦       ¦   ¦   ¦   pdfpattern.py
¦   ¦       ¦   ¦   ¦   pdfutils.py
¦   ¦       ¦   ¦   ¦   rl_codecs.py
¦   ¦       ¦   ¦   ¦   ttfonts.py
¦   ¦       ¦   ¦   ¦   _can_cmap_data.py
¦   ¦       ¦   ¦   ¦   _cidfontdata.py
¦   ¦       ¦   ¦   ¦   _fontdata.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_macexpert.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_macroman.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_pdfdoc.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_standard.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_symbol.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_winansi.py
¦   ¦       ¦   ¦   ¦   _fontdata_enc_zapfdingbats.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_courier.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_courierbold.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_courierboldoblique.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_courieroblique.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_helvetica.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_helveticabold.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_helveticaboldoblique.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_helveticaoblique.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_symbol.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_timesbold.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_timesbolditalic.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_timesitalic.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_timesroman.py
¦   ¦       ¦   ¦   ¦   _fontdata_widths_zapfdingbats.py
¦   ¦       ¦   ¦   ¦   _glyphlist.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           acroform.cpython-38.pyc
¦   ¦       ¦   ¦           cidfonts.cpython-38.pyc
¦   ¦       ¦   ¦           pdfdoc.cpython-38.pyc
¦   ¦       ¦   ¦           pdfform.cpython-38.pyc
¦   ¦       ¦   ¦           pdfmetrics.cpython-38.pyc
¦   ¦       ¦   ¦           pdfpattern.cpython-38.pyc
¦   ¦       ¦   ¦           pdfutils.cpython-38.pyc
¦   ¦       ¦   ¦           rl_codecs.cpython-38.pyc
¦   ¦       ¦   ¦           ttfonts.cpython-38.pyc
¦   ¦       ¦   ¦           _can_cmap_data.cpython-38.pyc
¦   ¦       ¦   ¦           _cidfontdata.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_macexpert.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_macroman.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_pdfdoc.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_standard.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_symbol.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_winansi.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_enc_zapfdingbats.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_courier.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_courierbold.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_courierboldoblique.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_courieroblique.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_helvetica.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_helveticabold.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_helveticaboldoblique.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_helveticaoblique.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_symbol.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_timesbold.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_timesbolditalic.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_timesitalic.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_timesroman.cpython-38.pyc
¦   ¦       ¦   ¦           _fontdata_widths_zapfdingbats.cpython-38.pyc
¦   ¦       ¦   ¦           _glyphlist.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---pdfgen
¦   ¦       ¦   ¦   ¦   canvas.py
¦   ¦       ¦   ¦   ¦   pathobject.py
¦   ¦       ¦   ¦   ¦   pdfgeom.py
¦   ¦       ¦   ¦   ¦   pdfimages.py
¦   ¦       ¦   ¦   ¦   textobject.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           canvas.cpython-38.pyc
¦   ¦       ¦   ¦           pathobject.cpython-38.pyc
¦   ¦       ¦   ¦           pdfgeom.cpython-38.pyc
¦   ¦       ¦   ¦           pdfimages.cpython-38.pyc
¦   ¦       ¦   ¦           textobject.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---platypus
¦   ¦       ¦   ¦   ¦   doctemplate.py
¦   ¦       ¦   ¦   ¦   figures.py
¦   ¦       ¦   ¦   ¦   flowables.py
¦   ¦       ¦   ¦   ¦   frames.py
¦   ¦       ¦   ¦   ¦   multicol.py
¦   ¦       ¦   ¦   ¦   para.py
¦   ¦       ¦   ¦   ¦   paragraph.py
¦   ¦       ¦   ¦   ¦   paraparser.py
¦   ¦       ¦   ¦   ¦   tableofcontents.py
¦   ¦       ¦   ¦   ¦   tables.py
¦   ¦       ¦   ¦   ¦   xpreformatted.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           doctemplate.cpython-38.pyc
¦   ¦       ¦   ¦           figures.cpython-38.pyc
¦   ¦       ¦   ¦           flowables.cpython-38.pyc
¦   ¦       ¦   ¦           frames.cpython-38.pyc
¦   ¦       ¦   ¦           multicol.cpython-38.pyc
¦   ¦       ¦   ¦           para.cpython-38.pyc
¦   ¦       ¦   ¦           paragraph.cpython-38.pyc
¦   ¦       ¦   ¦           paraparser.cpython-38.pyc
¦   ¦       ¦   ¦           tableofcontents.cpython-38.pyc
¦   ¦       ¦   ¦           tables.cpython-38.pyc
¦   ¦       ¦   ¦           xpreformatted.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           rl_config.cpython-38.pyc
¦   ¦       ¦           rl_settings.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---reportlab-3.6.12.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---requests
¦   ¦       ¦   ¦   adapters.py
¦   ¦       ¦   ¦   api.py
¦   ¦       ¦   ¦   auth.py
¦   ¦       ¦   ¦   certs.py
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   cookies.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   help.py
¦   ¦       ¦   ¦   hooks.py
¦   ¦       ¦   ¦   models.py
¦   ¦       ¦   ¦   packages.py
¦   ¦       ¦   ¦   sessions.py
¦   ¦       ¦   ¦   status_codes.py
¦   ¦       ¦   ¦   structures.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   _internal_utils.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __version__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           adapters.cpython-38.pyc
¦   ¦       ¦           api.cpython-38.pyc
¦   ¦       ¦           auth.cpython-38.pyc
¦   ¦       ¦           certs.cpython-38.pyc
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           cookies.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           help.cpython-38.pyc
¦   ¦       ¦           hooks.cpython-38.pyc
¦   ¦       ¦           models.cpython-38.pyc
¦   ¦       ¦           packages.cpython-38.pyc
¦   ¦       ¦           sessions.cpython-38.pyc
¦   ¦       ¦           status_codes.cpython-38.pyc
¦   ¦       ¦           structures.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           _internal_utils.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __version__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---requests-2.28.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---setuptools
¦   ¦       ¦   ¦   archive_util.py
¦   ¦       ¦   ¦   build_meta.py
¦   ¦       ¦   ¦   cli-32.exe
¦   ¦       ¦   ¦   cli-64.exe
¦   ¦       ¦   ¦   cli.exe
¦   ¦       ¦   ¦   config.py
¦   ¦       ¦   ¦   depends.py
¦   ¦       ¦   ¦   dep_util.py
¦   ¦       ¦   ¦   dist.py
¦   ¦       ¦   ¦   errors.py
¦   ¦       ¦   ¦   extension.py
¦   ¦       ¦   ¦   glob.py
¦   ¦       ¦   ¦   gui-32.exe
¦   ¦       ¦   ¦   gui-64.exe
¦   ¦       ¦   ¦   gui.exe
¦   ¦       ¦   ¦   installer.py
¦   ¦       ¦   ¦   launch.py
¦   ¦       ¦   ¦   lib2to3_ex.py
¦   ¦       ¦   ¦   monkey.py
¦   ¦       ¦   ¦   msvc.py
¦   ¦       ¦   ¦   namespaces.py
¦   ¦       ¦   ¦   package_index.py
¦   ¦       ¦   ¦   py34compat.py
¦   ¦       ¦   ¦   sandbox.py
¦   ¦       ¦   ¦   script (dev).tmpl
¦   ¦       ¦   ¦   script.tmpl
¦   ¦       ¦   ¦   ssl_support.py
¦   ¦       ¦   ¦   unicode_utils.py
¦   ¦       ¦   ¦   version.py
¦   ¦       ¦   ¦   wheel.py
¦   ¦       ¦   ¦   windows_support.py
¦   ¦       ¦   ¦   _deprecation_warning.py
¦   ¦       ¦   ¦   _imp.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---command
¦   ¦       ¦   ¦   ¦   alias.py
¦   ¦       ¦   ¦   ¦   bdist_egg.py
¦   ¦       ¦   ¦   ¦   bdist_rpm.py
¦   ¦       ¦   ¦   ¦   build_clib.py
¦   ¦       ¦   ¦   ¦   build_ext.py
¦   ¦       ¦   ¦   ¦   build_py.py
¦   ¦       ¦   ¦   ¦   develop.py
¦   ¦       ¦   ¦   ¦   dist_info.py
¦   ¦       ¦   ¦   ¦   easy_install.py
¦   ¦       ¦   ¦   ¦   egg_info.py
¦   ¦       ¦   ¦   ¦   install.py
¦   ¦       ¦   ¦   ¦   install_egg_info.py
¦   ¦       ¦   ¦   ¦   install_lib.py
¦   ¦       ¦   ¦   ¦   install_scripts.py
¦   ¦       ¦   ¦   ¦   launcher manifest.xml
¦   ¦       ¦   ¦   ¦   py36compat.py
¦   ¦       ¦   ¦   ¦   register.py
¦   ¦       ¦   ¦   ¦   rotate.py
¦   ¦       ¦   ¦   ¦   saveopts.py
¦   ¦       ¦   ¦   ¦   sdist.py
¦   ¦       ¦   ¦   ¦   setopt.py
¦   ¦       ¦   ¦   ¦   test.py
¦   ¦       ¦   ¦   ¦   upload.py
¦   ¦       ¦   ¦   ¦   upload_docs.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           alias.cpython-38.pyc
¦   ¦       ¦   ¦           bdist_egg.cpython-38.pyc
¦   ¦       ¦   ¦           bdist_rpm.cpython-38.pyc
¦   ¦       ¦   ¦           build_clib.cpython-38.pyc
¦   ¦       ¦   ¦           build_ext.cpython-38.pyc
¦   ¦       ¦   ¦           build_py.cpython-38.pyc
¦   ¦       ¦   ¦           develop.cpython-38.pyc
¦   ¦       ¦   ¦           dist_info.cpython-38.pyc
¦   ¦       ¦   ¦           easy_install.cpython-38.pyc
¦   ¦       ¦   ¦           egg_info.cpython-38.pyc
¦   ¦       ¦   ¦           install.cpython-38.pyc
¦   ¦       ¦   ¦           install_egg_info.cpython-38.pyc
¦   ¦       ¦   ¦           install_lib.cpython-38.pyc
¦   ¦       ¦   ¦           install_scripts.cpython-38.pyc
¦   ¦       ¦   ¦           py36compat.cpython-38.pyc
¦   ¦       ¦   ¦           register.cpython-38.pyc
¦   ¦       ¦   ¦           rotate.cpython-38.pyc
¦   ¦       ¦   ¦           saveopts.cpython-38.pyc
¦   ¦       ¦   ¦           sdist.cpython-38.pyc
¦   ¦       ¦   ¦           setopt.cpython-38.pyc
¦   ¦       ¦   ¦           test.cpython-38.pyc
¦   ¦       ¦   ¦           upload.cpython-38.pyc
¦   ¦       ¦   ¦           upload_docs.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---extern
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_distutils
¦   ¦       ¦   ¦   ¦   archive_util.py
¦   ¦       ¦   ¦   ¦   bcppcompiler.py
¦   ¦       ¦   ¦   ¦   ccompiler.py
¦   ¦       ¦   ¦   ¦   cmd.py
¦   ¦       ¦   ¦   ¦   config.py
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   cygwinccompiler.py
¦   ¦       ¦   ¦   ¦   debug.py
¦   ¦       ¦   ¦   ¦   dep_util.py
¦   ¦       ¦   ¦   ¦   dir_util.py
¦   ¦       ¦   ¦   ¦   dist.py
¦   ¦       ¦   ¦   ¦   errors.py
¦   ¦       ¦   ¦   ¦   extension.py
¦   ¦       ¦   ¦   ¦   fancy_getopt.py
¦   ¦       ¦   ¦   ¦   filelist.py
¦   ¦       ¦   ¦   ¦   file_util.py
¦   ¦       ¦   ¦   ¦   log.py
¦   ¦       ¦   ¦   ¦   msvc9compiler.py
¦   ¦       ¦   ¦   ¦   msvccompiler.py
¦   ¦       ¦   ¦   ¦   py35compat.py
¦   ¦       ¦   ¦   ¦   py38compat.py
¦   ¦       ¦   ¦   ¦   spawn.py
¦   ¦       ¦   ¦   ¦   sysconfig.py
¦   ¦       ¦   ¦   ¦   text_file.py
¦   ¦       ¦   ¦   ¦   unixccompiler.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   version.py
¦   ¦       ¦   ¦   ¦   versionpredicate.py
¦   ¦       ¦   ¦   ¦   _msvccompiler.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---command
¦   ¦       ¦   ¦   ¦   ¦   bdist.py
¦   ¦       ¦   ¦   ¦   ¦   bdist_dumb.py
¦   ¦       ¦   ¦   ¦   ¦   bdist_msi.py
¦   ¦       ¦   ¦   ¦   ¦   bdist_rpm.py
¦   ¦       ¦   ¦   ¦   ¦   bdist_wininst.py
¦   ¦       ¦   ¦   ¦   ¦   build.py
¦   ¦       ¦   ¦   ¦   ¦   build_clib.py
¦   ¦       ¦   ¦   ¦   ¦   build_ext.py
¦   ¦       ¦   ¦   ¦   ¦   build_py.py
¦   ¦       ¦   ¦   ¦   ¦   build_scripts.py
¦   ¦       ¦   ¦   ¦   ¦   check.py
¦   ¦       ¦   ¦   ¦   ¦   clean.py
¦   ¦       ¦   ¦   ¦   ¦   config.py
¦   ¦       ¦   ¦   ¦   ¦   install.py
¦   ¦       ¦   ¦   ¦   ¦   install_data.py
¦   ¦       ¦   ¦   ¦   ¦   install_egg_info.py
¦   ¦       ¦   ¦   ¦   ¦   install_headers.py
¦   ¦       ¦   ¦   ¦   ¦   install_lib.py
¦   ¦       ¦   ¦   ¦   ¦   install_scripts.py
¦   ¦       ¦   ¦   ¦   ¦   py37compat.py
¦   ¦       ¦   ¦   ¦   ¦   register.py
¦   ¦       ¦   ¦   ¦   ¦   sdist.py
¦   ¦       ¦   ¦   ¦   ¦   upload.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           bdist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           bdist_dumb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           bdist_msi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           bdist_rpm.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           bdist_wininst.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_clib.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_py.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           build_scripts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           check.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           clean.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           config.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_data.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_egg_info.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_headers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_lib.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           install_scripts.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           py37compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           register.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           sdist.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           upload.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           archive_util.cpython-38.pyc
¦   ¦       ¦   ¦           bcppcompiler.cpython-38.pyc
¦   ¦       ¦   ¦           ccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           cmd.cpython-38.pyc
¦   ¦       ¦   ¦           config.cpython-38.pyc
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           cygwinccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           debug.cpython-38.pyc
¦   ¦       ¦   ¦           dep_util.cpython-38.pyc
¦   ¦       ¦   ¦           dir_util.cpython-38.pyc
¦   ¦       ¦   ¦           dist.cpython-38.pyc
¦   ¦       ¦   ¦           errors.cpython-38.pyc
¦   ¦       ¦   ¦           extension.cpython-38.pyc
¦   ¦       ¦   ¦           fancy_getopt.cpython-38.pyc
¦   ¦       ¦   ¦           filelist.cpython-38.pyc
¦   ¦       ¦   ¦           file_util.cpython-38.pyc
¦   ¦       ¦   ¦           log.cpython-38.pyc
¦   ¦       ¦   ¦           msvc9compiler.cpython-38.pyc
¦   ¦       ¦   ¦           msvccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           py35compat.cpython-38.pyc
¦   ¦       ¦   ¦           py38compat.cpython-38.pyc
¦   ¦       ¦   ¦           spawn.cpython-38.pyc
¦   ¦       ¦   ¦           sysconfig.cpython-38.pyc
¦   ¦       ¦   ¦           text_file.cpython-38.pyc
¦   ¦       ¦   ¦           unixccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           version.cpython-38.pyc
¦   ¦       ¦   ¦           versionpredicate.cpython-38.pyc
¦   ¦       ¦   ¦           _msvccompiler.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---_vendor
¦   ¦       ¦   ¦   ¦   ordered_set.py
¦   ¦       ¦   ¦   ¦   pyparsing.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---packaging
¦   ¦       ¦   ¦   ¦   ¦   markers.py
¦   ¦       ¦   ¦   ¦   ¦   requirements.py
¦   ¦       ¦   ¦   ¦   ¦   specifiers.py
¦   ¦       ¦   ¦   ¦   ¦   tags.py
¦   ¦       ¦   ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   ¦   version.py
¦   ¦       ¦   ¦   ¦   ¦   _compat.py
¦   ¦       ¦   ¦   ¦   ¦   _structures.py
¦   ¦       ¦   ¦   ¦   ¦   _typing.py
¦   ¦       ¦   ¦   ¦   ¦   __about__.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           markers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           requirements.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           specifiers.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           tags.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           version.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _compat.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _structures.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           _typing.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __about__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           ordered_set.cpython-38.pyc
¦   ¦       ¦   ¦           pyparsing.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           archive_util.cpython-38.pyc
¦   ¦       ¦           build_meta.cpython-38.pyc
¦   ¦       ¦           config.cpython-38.pyc
¦   ¦       ¦           depends.cpython-38.pyc
¦   ¦       ¦           dep_util.cpython-38.pyc
¦   ¦       ¦           dist.cpython-38.pyc
¦   ¦       ¦           errors.cpython-38.pyc
¦   ¦       ¦           extension.cpython-38.pyc
¦   ¦       ¦           glob.cpython-38.pyc
¦   ¦       ¦           installer.cpython-38.pyc
¦   ¦       ¦           launch.cpython-38.pyc
¦   ¦       ¦           lib2to3_ex.cpython-38.pyc
¦   ¦       ¦           monkey.cpython-38.pyc
¦   ¦       ¦           msvc.cpython-38.pyc
¦   ¦       ¦           namespaces.cpython-38.pyc
¦   ¦       ¦           package_index.cpython-38.pyc
¦   ¦       ¦           py34compat.cpython-38.pyc
¦   ¦       ¦           sandbox.cpython-38.pyc
¦   ¦       ¦           ssl_support.cpython-38.pyc
¦   ¦       ¦           unicode_utils.cpython-38.pyc
¦   ¦       ¦           version.cpython-38.pyc
¦   ¦       ¦           wheel.cpython-38.pyc
¦   ¦       ¦           windows_support.cpython-38.pyc
¦   ¦       ¦           _deprecation_warning.cpython-38.pyc
¦   ¦       ¦           _imp.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---setuptools-56.0.0.dist-info
¦   ¦       ¦       dependency_links.txt
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---six-1.16.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---sqlalchemy
¦   ¦       ¦   ¦   cimmutabledict.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   cprocessors.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   cresultproxy.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   events.py
¦   ¦       ¦   ¦   exc.py
¦   ¦       ¦   ¦   inspection.py
¦   ¦       ¦   ¦   log.py
¦   ¦       ¦   ¦   processors.py
¦   ¦       ¦   ¦   schema.py
¦   ¦       ¦   ¦   types.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---connectors
¦   ¦       ¦   ¦   ¦   mxodbc.py
¦   ¦       ¦   ¦   ¦   pyodbc.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           mxodbc.cpython-38.pyc
¦   ¦       ¦   ¦           pyodbc.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---databases
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---dialects
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---firebird
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   fdb.py
¦   ¦       ¦   ¦   ¦   ¦   kinterbasdb.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           fdb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           kinterbasdb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---mssql
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   information_schema.py
¦   ¦       ¦   ¦   ¦   ¦   json.py
¦   ¦       ¦   ¦   ¦   ¦   mxodbc.py
¦   ¦       ¦   ¦   ¦   ¦   provision.py
¦   ¦       ¦   ¦   ¦   ¦   pymssql.py
¦   ¦       ¦   ¦   ¦   ¦   pyodbc.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           information_schema.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           json.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mxodbc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           provision.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pymssql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pyodbc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---mysql
¦   ¦       ¦   ¦   ¦   ¦   aiomysql.py
¦   ¦       ¦   ¦   ¦   ¦   asyncmy.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   cymysql.py
¦   ¦       ¦   ¦   ¦   ¦   dml.py
¦   ¦       ¦   ¦   ¦   ¦   enumerated.py
¦   ¦       ¦   ¦   ¦   ¦   expression.py
¦   ¦       ¦   ¦   ¦   ¦   json.py
¦   ¦       ¦   ¦   ¦   ¦   mariadb.py
¦   ¦       ¦   ¦   ¦   ¦   mariadbconnector.py
¦   ¦       ¦   ¦   ¦   ¦   mysqlconnector.py
¦   ¦       ¦   ¦   ¦   ¦   mysqldb.py
¦   ¦       ¦   ¦   ¦   ¦   oursql.py
¦   ¦       ¦   ¦   ¦   ¦   provision.py
¦   ¦       ¦   ¦   ¦   ¦   pymysql.py
¦   ¦       ¦   ¦   ¦   ¦   pyodbc.py
¦   ¦       ¦   ¦   ¦   ¦   reflection.py
¦   ¦       ¦   ¦   ¦   ¦   reserved_words.py
¦   ¦       ¦   ¦   ¦   ¦   types.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           aiomysql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           asyncmy.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cymysql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           enumerated.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           expression.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           json.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mariadb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mariadbconnector.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mysqlconnector.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mysqldb.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           oursql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           provision.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pymysql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pyodbc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           reflection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           reserved_words.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           types.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---oracle
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   cx_oracle.py
¦   ¦       ¦   ¦   ¦   ¦   provision.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           cx_oracle.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           provision.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---postgresql
¦   ¦       ¦   ¦   ¦   ¦   array.py
¦   ¦       ¦   ¦   ¦   ¦   asyncpg.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   dml.py
¦   ¦       ¦   ¦   ¦   ¦   ext.py
¦   ¦       ¦   ¦   ¦   ¦   hstore.py
¦   ¦       ¦   ¦   ¦   ¦   json.py
¦   ¦       ¦   ¦   ¦   ¦   pg8000.py
¦   ¦       ¦   ¦   ¦   ¦   provision.py
¦   ¦       ¦   ¦   ¦   ¦   psycopg2.py
¦   ¦       ¦   ¦   ¦   ¦   psycopg2cffi.py
¦   ¦       ¦   ¦   ¦   ¦   pygresql.py
¦   ¦       ¦   ¦   ¦   ¦   pypostgresql.py
¦   ¦       ¦   ¦   ¦   ¦   ranges.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           array.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           asyncpg.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ext.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           hstore.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           json.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pg8000.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           provision.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           psycopg2.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           psycopg2cffi.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pygresql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pypostgresql.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           ranges.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---sqlite
¦   ¦       ¦   ¦   ¦   ¦   aiosqlite.py
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   dml.py
¦   ¦       ¦   ¦   ¦   ¦   json.py
¦   ¦       ¦   ¦   ¦   ¦   provision.py
¦   ¦       ¦   ¦   ¦   ¦   pysqlcipher.py
¦   ¦       ¦   ¦   ¦   ¦   pysqlite.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           aiosqlite.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           dml.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           json.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           provision.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pysqlcipher.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pysqlite.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---sybase
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   mxodbc.py
¦   ¦       ¦   ¦   ¦   ¦   pyodbc.py
¦   ¦       ¦   ¦   ¦   ¦   pysybase.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           mxodbc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pyodbc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pysybase.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---engine
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   characteristics.py
¦   ¦       ¦   ¦   ¦   create.py
¦   ¦       ¦   ¦   ¦   cursor.py
¦   ¦       ¦   ¦   ¦   default.py
¦   ¦       ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   interfaces.py
¦   ¦       ¦   ¦   ¦   mock.py
¦   ¦       ¦   ¦   ¦   reflection.py
¦   ¦       ¦   ¦   ¦   result.py
¦   ¦       ¦   ¦   ¦   row.py
¦   ¦       ¦   ¦   ¦   strategies.py
¦   ¦       ¦   ¦   ¦   url.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           characteristics.cpython-38.pyc
¦   ¦       ¦   ¦           create.cpython-38.pyc
¦   ¦       ¦   ¦           cursor.cpython-38.pyc
¦   ¦       ¦   ¦           default.cpython-38.pyc
¦   ¦       ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦           interfaces.cpython-38.pyc
¦   ¦       ¦   ¦           mock.cpython-38.pyc
¦   ¦       ¦   ¦           reflection.cpython-38.pyc
¦   ¦       ¦   ¦           result.cpython-38.pyc
¦   ¦       ¦   ¦           row.cpython-38.pyc
¦   ¦       ¦   ¦           strategies.cpython-38.pyc
¦   ¦       ¦   ¦           url.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---event
¦   ¦       ¦   ¦   ¦   api.py
¦   ¦       ¦   ¦   ¦   attr.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   legacy.py
¦   ¦       ¦   ¦   ¦   registry.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           api.cpython-38.pyc
¦   ¦       ¦   ¦           attr.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           legacy.cpython-38.pyc
¦   ¦       ¦   ¦           registry.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---ext
¦   ¦       ¦   ¦   ¦   associationproxy.py
¦   ¦       ¦   ¦   ¦   automap.py
¦   ¦       ¦   ¦   ¦   baked.py
¦   ¦       ¦   ¦   ¦   compiler.py
¦   ¦       ¦   ¦   ¦   horizontal_shard.py
¦   ¦       ¦   ¦   ¦   hybrid.py
¦   ¦       ¦   ¦   ¦   indexable.py
¦   ¦       ¦   ¦   ¦   instrumentation.py
¦   ¦       ¦   ¦   ¦   mutable.py
¦   ¦       ¦   ¦   ¦   orderinglist.py
¦   ¦       ¦   ¦   ¦   serializer.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---asyncio
¦   ¦       ¦   ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   ¦   engine.py
¦   ¦       ¦   ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   ¦   exc.py
¦   ¦       ¦   ¦   ¦   ¦   result.py
¦   ¦       ¦   ¦   ¦   ¦   scoping.py
¦   ¦       ¦   ¦   ¦   ¦   session.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           engine.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           exc.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           result.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           scoping.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           session.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---declarative
¦   ¦       ¦   ¦   ¦   ¦   extensions.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           extensions.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---mypy
¦   ¦       ¦   ¦   ¦   ¦   apply.py
¦   ¦       ¦   ¦   ¦   ¦   decl_class.py
¦   ¦       ¦   ¦   ¦   ¦   infer.py
¦   ¦       ¦   ¦   ¦   ¦   names.py
¦   ¦       ¦   ¦   ¦   ¦   plugin.py
¦   ¦       ¦   ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           apply.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           decl_class.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           infer.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           names.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           plugin.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           associationproxy.cpython-38.pyc
¦   ¦       ¦   ¦           automap.cpython-38.pyc
¦   ¦       ¦   ¦           baked.cpython-38.pyc
¦   ¦       ¦   ¦           compiler.cpython-38.pyc
¦   ¦       ¦   ¦           horizontal_shard.cpython-38.pyc
¦   ¦       ¦   ¦           hybrid.cpython-38.pyc
¦   ¦       ¦   ¦           indexable.cpython-38.pyc
¦   ¦       ¦   ¦           instrumentation.cpython-38.pyc
¦   ¦       ¦   ¦           mutable.cpython-38.pyc
¦   ¦       ¦   ¦           orderinglist.cpython-38.pyc
¦   ¦       ¦   ¦           serializer.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---future
¦   ¦       ¦   ¦   ¦   engine.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---orm
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           engine.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---orm
¦   ¦       ¦   ¦   ¦   attributes.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   clsregistry.py
¦   ¦       ¦   ¦   ¦   collections.py
¦   ¦       ¦   ¦   ¦   context.py
¦   ¦       ¦   ¦   ¦   decl_api.py
¦   ¦       ¦   ¦   ¦   decl_base.py
¦   ¦       ¦   ¦   ¦   dependency.py
¦   ¦       ¦   ¦   ¦   descriptor_props.py
¦   ¦       ¦   ¦   ¦   dynamic.py
¦   ¦       ¦   ¦   ¦   evaluator.py
¦   ¦       ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   exc.py
¦   ¦       ¦   ¦   ¦   identity.py
¦   ¦       ¦   ¦   ¦   instrumentation.py
¦   ¦       ¦   ¦   ¦   interfaces.py
¦   ¦       ¦   ¦   ¦   loading.py
¦   ¦       ¦   ¦   ¦   mapper.py
¦   ¦       ¦   ¦   ¦   path_registry.py
¦   ¦       ¦   ¦   ¦   persistence.py
¦   ¦       ¦   ¦   ¦   properties.py
¦   ¦       ¦   ¦   ¦   query.py
¦   ¦       ¦   ¦   ¦   relationships.py
¦   ¦       ¦   ¦   ¦   scoping.py
¦   ¦       ¦   ¦   ¦   session.py
¦   ¦       ¦   ¦   ¦   state.py
¦   ¦       ¦   ¦   ¦   strategies.py
¦   ¦       ¦   ¦   ¦   strategy_options.py
¦   ¦       ¦   ¦   ¦   sync.py
¦   ¦       ¦   ¦   ¦   unitofwork.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           attributes.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           clsregistry.cpython-38.pyc
¦   ¦       ¦   ¦           collections.cpython-38.pyc
¦   ¦       ¦   ¦           context.cpython-38.pyc
¦   ¦       ¦   ¦           decl_api.cpython-38.pyc
¦   ¦       ¦   ¦           decl_base.cpython-38.pyc
¦   ¦       ¦   ¦           dependency.cpython-38.pyc
¦   ¦       ¦   ¦           descriptor_props.cpython-38.pyc
¦   ¦       ¦   ¦           dynamic.cpython-38.pyc
¦   ¦       ¦   ¦           evaluator.cpython-38.pyc
¦   ¦       ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦           exc.cpython-38.pyc
¦   ¦       ¦   ¦           identity.cpython-38.pyc
¦   ¦       ¦   ¦           instrumentation.cpython-38.pyc
¦   ¦       ¦   ¦           interfaces.cpython-38.pyc
¦   ¦       ¦   ¦           loading.cpython-38.pyc
¦   ¦       ¦   ¦           mapper.cpython-38.pyc
¦   ¦       ¦   ¦           path_registry.cpython-38.pyc
¦   ¦       ¦   ¦           persistence.cpython-38.pyc
¦   ¦       ¦   ¦           properties.cpython-38.pyc
¦   ¦       ¦   ¦           query.cpython-38.pyc
¦   ¦       ¦   ¦           relationships.cpython-38.pyc
¦   ¦       ¦   ¦           scoping.cpython-38.pyc
¦   ¦       ¦   ¦           session.cpython-38.pyc
¦   ¦       ¦   ¦           state.cpython-38.pyc
¦   ¦       ¦   ¦           strategies.cpython-38.pyc
¦   ¦       ¦   ¦           strategy_options.cpython-38.pyc
¦   ¦       ¦   ¦           sync.cpython-38.pyc
¦   ¦       ¦   ¦           unitofwork.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---pool
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   dbapi_proxy.py
¦   ¦       ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   impl.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           dbapi_proxy.cpython-38.pyc
¦   ¦       ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦           impl.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---sql
¦   ¦       ¦   ¦   ¦   annotation.py
¦   ¦       ¦   ¦   ¦   base.py
¦   ¦       ¦   ¦   ¦   coercions.py
¦   ¦       ¦   ¦   ¦   compiler.py
¦   ¦       ¦   ¦   ¦   crud.py
¦   ¦       ¦   ¦   ¦   ddl.py
¦   ¦       ¦   ¦   ¦   default_comparator.py
¦   ¦       ¦   ¦   ¦   dml.py
¦   ¦       ¦   ¦   ¦   elements.py
¦   ¦       ¦   ¦   ¦   events.py
¦   ¦       ¦   ¦   ¦   expression.py
¦   ¦       ¦   ¦   ¦   functions.py
¦   ¦       ¦   ¦   ¦   lambdas.py
¦   ¦       ¦   ¦   ¦   naming.py
¦   ¦       ¦   ¦   ¦   operators.py
¦   ¦       ¦   ¦   ¦   roles.py
¦   ¦       ¦   ¦   ¦   schema.py
¦   ¦       ¦   ¦   ¦   selectable.py
¦   ¦       ¦   ¦   ¦   sqltypes.py
¦   ¦       ¦   ¦   ¦   traversals.py
¦   ¦       ¦   ¦   ¦   type_api.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   visitors.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           annotation.cpython-38.pyc
¦   ¦       ¦   ¦           base.cpython-38.pyc
¦   ¦       ¦   ¦           coercions.cpython-38.pyc
¦   ¦       ¦   ¦           compiler.cpython-38.pyc
¦   ¦       ¦   ¦           crud.cpython-38.pyc
¦   ¦       ¦   ¦           ddl.cpython-38.pyc
¦   ¦       ¦   ¦           default_comparator.cpython-38.pyc
¦   ¦       ¦   ¦           dml.cpython-38.pyc
¦   ¦       ¦   ¦           elements.cpython-38.pyc
¦   ¦       ¦   ¦           events.cpython-38.pyc
¦   ¦       ¦   ¦           expression.cpython-38.pyc
¦   ¦       ¦   ¦           functions.cpython-38.pyc
¦   ¦       ¦   ¦           lambdas.cpython-38.pyc
¦   ¦       ¦   ¦           naming.cpython-38.pyc
¦   ¦       ¦   ¦           operators.cpython-38.pyc
¦   ¦       ¦   ¦           roles.cpython-38.pyc
¦   ¦       ¦   ¦           schema.cpython-38.pyc
¦   ¦       ¦   ¦           selectable.cpython-38.pyc
¦   ¦       ¦   ¦           sqltypes.cpython-38.pyc
¦   ¦       ¦   ¦           traversals.cpython-38.pyc
¦   ¦       ¦   ¦           type_api.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           visitors.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---testing
¦   ¦       ¦   ¦   ¦   assertions.py
¦   ¦       ¦   ¦   ¦   assertsql.py
¦   ¦       ¦   ¦   ¦   asyncio.py
¦   ¦       ¦   ¦   ¦   config.py
¦   ¦       ¦   ¦   ¦   engines.py
¦   ¦       ¦   ¦   ¦   entities.py
¦   ¦       ¦   ¦   ¦   exclusions.py
¦   ¦       ¦   ¦   ¦   fixtures.py
¦   ¦       ¦   ¦   ¦   mock.py
¦   ¦       ¦   ¦   ¦   pickleable.py
¦   ¦       ¦   ¦   ¦   profiling.py
¦   ¦       ¦   ¦   ¦   provision.py
¦   ¦       ¦   ¦   ¦   requirements.py
¦   ¦       ¦   ¦   ¦   schema.py
¦   ¦       ¦   ¦   ¦   util.py
¦   ¦       ¦   ¦   ¦   warnings.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---plugin
¦   ¦       ¦   ¦   ¦   ¦   bootstrap.py
¦   ¦       ¦   ¦   ¦   ¦   plugin_base.py
¦   ¦       ¦   ¦   ¦   ¦   pytestplugin.py
¦   ¦       ¦   ¦   ¦   ¦   reinvent_fixtures_py2k.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           bootstrap.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           plugin_base.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           pytestplugin.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           reinvent_fixtures_py2k.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---suite
¦   ¦       ¦   ¦   ¦   ¦   test_cte.py
¦   ¦       ¦   ¦   ¦   ¦   test_ddl.py
¦   ¦       ¦   ¦   ¦   ¦   test_deprecations.py
¦   ¦       ¦   ¦   ¦   ¦   test_dialect.py
¦   ¦       ¦   ¦   ¦   ¦   test_insert.py
¦   ¦       ¦   ¦   ¦   ¦   test_reflection.py
¦   ¦       ¦   ¦   ¦   ¦   test_results.py
¦   ¦       ¦   ¦   ¦   ¦   test_rowcount.py
¦   ¦       ¦   ¦   ¦   ¦   test_select.py
¦   ¦       ¦   ¦   ¦   ¦   test_sequence.py
¦   ¦       ¦   ¦   ¦   ¦   test_types.py
¦   ¦       ¦   ¦   ¦   ¦   test_unicode_ddl.py
¦   ¦       ¦   ¦   ¦   ¦   test_update_delete.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           test_cte.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_ddl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_deprecations.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_dialect.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_insert.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_reflection.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_results.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_rowcount.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_select.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_sequence.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_types.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_unicode_ddl.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           test_update_delete.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           assertions.cpython-38.pyc
¦   ¦       ¦   ¦           assertsql.cpython-38.pyc
¦   ¦       ¦   ¦           asyncio.cpython-38.pyc
¦   ¦       ¦   ¦           config.cpython-38.pyc
¦   ¦       ¦   ¦           engines.cpython-38.pyc
¦   ¦       ¦   ¦           entities.cpython-38.pyc
¦   ¦       ¦   ¦           exclusions.cpython-38.pyc
¦   ¦       ¦   ¦           fixtures.cpython-38.pyc
¦   ¦       ¦   ¦           mock.cpython-38.pyc
¦   ¦       ¦   ¦           pickleable.cpython-38.pyc
¦   ¦       ¦   ¦           profiling.cpython-38.pyc
¦   ¦       ¦   ¦           provision.cpython-38.pyc
¦   ¦       ¦   ¦           requirements.cpython-38.pyc
¦   ¦       ¦   ¦           schema.cpython-38.pyc
¦   ¦       ¦   ¦           util.cpython-38.pyc
¦   ¦       ¦   ¦           warnings.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---util
¦   ¦       ¦   ¦   ¦   compat.py
¦   ¦       ¦   ¦   ¦   concurrency.py
¦   ¦       ¦   ¦   ¦   deprecations.py
¦   ¦       ¦   ¦   ¦   langhelpers.py
¦   ¦       ¦   ¦   ¦   queue.py
¦   ¦       ¦   ¦   ¦   topological.py
¦   ¦       ¦   ¦   ¦   _collections.py
¦   ¦       ¦   ¦   ¦   _compat_py3k.py
¦   ¦       ¦   ¦   ¦   _concurrency_py3k.py
¦   ¦       ¦   ¦   ¦   _preloaded.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           compat.cpython-38.pyc
¦   ¦       ¦   ¦           concurrency.cpython-38.pyc
¦   ¦       ¦   ¦           deprecations.cpython-38.pyc
¦   ¦       ¦   ¦           langhelpers.cpython-38.pyc
¦   ¦       ¦   ¦           queue.cpython-38.pyc
¦   ¦       ¦   ¦           topological.cpython-38.pyc
¦   ¦       ¦   ¦           _collections.cpython-38.pyc
¦   ¦       ¦   ¦           _compat_py3k.cpython-38.pyc
¦   ¦       ¦   ¦           _concurrency_py3k.cpython-38.pyc
¦   ¦       ¦   ¦           _preloaded.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           events.cpython-38.pyc
¦   ¦       ¦           exc.cpython-38.pyc
¦   ¦       ¦           inspection.cpython-38.pyc
¦   ¦       ¦           log.cpython-38.pyc
¦   ¦       ¦           processors.cpython-38.pyc
¦   ¦       ¦           schema.cpython-38.pyc
¦   ¦       ¦           types.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---SQLAlchemy-1.4.45.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---tinycss2
¦   ¦       ¦   ¦   ast.py
¦   ¦       ¦   ¦   bytes.py
¦   ¦       ¦   ¦   color3.py
¦   ¦       ¦   ¦   nth.py
¦   ¦       ¦   ¦   parser.py
¦   ¦       ¦   ¦   serializer.py
¦   ¦       ¦   ¦   tokenizer.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           ast.cpython-38.pyc
¦   ¦       ¦           bytes.cpython-38.pyc
¦   ¦       ¦           color3.cpython-38.pyc
¦   ¦       ¦           nth.cpython-38.pyc
¦   ¦       ¦           parser.cpython-38.pyc
¦   ¦       ¦           serializer.cpython-38.pyc
¦   ¦       ¦           tokenizer.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---tinycss2-1.2.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---tzdata
¦   ¦       ¦   ¦   zones
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---zoneinfo
¦   ¦       ¦   ¦   ¦   CET
¦   ¦       ¦   ¦   ¦   CST6CDT
¦   ¦       ¦   ¦   ¦   Cuba
¦   ¦       ¦   ¦   ¦   EET
¦   ¦       ¦   ¦   ¦   Egypt
¦   ¦       ¦   ¦   ¦   Eire
¦   ¦       ¦   ¦   ¦   EST
¦   ¦       ¦   ¦   ¦   EST5EDT
¦   ¦       ¦   ¦   ¦   Factory
¦   ¦       ¦   ¦   ¦   GB
¦   ¦       ¦   ¦   ¦   GB-Eire
¦   ¦       ¦   ¦   ¦   GMT
¦   ¦       ¦   ¦   ¦   GMT+0
¦   ¦       ¦   ¦   ¦   GMT-0
¦   ¦       ¦   ¦   ¦   GMT0
¦   ¦       ¦   ¦   ¦   Greenwich
¦   ¦       ¦   ¦   ¦   Hongkong
¦   ¦       ¦   ¦   ¦   HST
¦   ¦       ¦   ¦   ¦   Iceland
¦   ¦       ¦   ¦   ¦   Iran
¦   ¦       ¦   ¦   ¦   iso3166.tab
¦   ¦       ¦   ¦   ¦   Israel
¦   ¦       ¦   ¦   ¦   Jamaica
¦   ¦       ¦   ¦   ¦   Japan
¦   ¦       ¦   ¦   ¦   Kwajalein
¦   ¦       ¦   ¦   ¦   leapseconds
¦   ¦       ¦   ¦   ¦   Libya
¦   ¦       ¦   ¦   ¦   MET
¦   ¦       ¦   ¦   ¦   MST
¦   ¦       ¦   ¦   ¦   MST7MDT
¦   ¦       ¦   ¦   ¦   Navajo
¦   ¦       ¦   ¦   ¦   NZ
¦   ¦       ¦   ¦   ¦   NZ-CHAT
¦   ¦       ¦   ¦   ¦   Poland
¦   ¦       ¦   ¦   ¦   Portugal
¦   ¦       ¦   ¦   ¦   PRC
¦   ¦       ¦   ¦   ¦   PST8PDT
¦   ¦       ¦   ¦   ¦   ROC
¦   ¦       ¦   ¦   ¦   ROK
¦   ¦       ¦   ¦   ¦   Singapore
¦   ¦       ¦   ¦   ¦   Turkey
¦   ¦       ¦   ¦   ¦   tzdata.zi
¦   ¦       ¦   ¦   ¦   UCT
¦   ¦       ¦   ¦   ¦   Universal
¦   ¦       ¦   ¦   ¦   UTC
¦   ¦       ¦   ¦   ¦   W-SU
¦   ¦       ¦   ¦   ¦   WET
¦   ¦       ¦   ¦   ¦   zone.tab
¦   ¦       ¦   ¦   ¦   zone1970.tab
¦   ¦       ¦   ¦   ¦   Zulu
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---Africa
¦   ¦       ¦   ¦   ¦   ¦   Abidjan
¦   ¦       ¦   ¦   ¦   ¦   Accra
¦   ¦       ¦   ¦   ¦   ¦   Addis_Ababa
¦   ¦       ¦   ¦   ¦   ¦   Algiers
¦   ¦       ¦   ¦   ¦   ¦   Asmara
¦   ¦       ¦   ¦   ¦   ¦   Asmera
¦   ¦       ¦   ¦   ¦   ¦   Bamako
¦   ¦       ¦   ¦   ¦   ¦   Bangui
¦   ¦       ¦   ¦   ¦   ¦   Banjul
¦   ¦       ¦   ¦   ¦   ¦   Bissau
¦   ¦       ¦   ¦   ¦   ¦   Blantyre
¦   ¦       ¦   ¦   ¦   ¦   Brazzaville
¦   ¦       ¦   ¦   ¦   ¦   Bujumbura
¦   ¦       ¦   ¦   ¦   ¦   Cairo
¦   ¦       ¦   ¦   ¦   ¦   Casablanca
¦   ¦       ¦   ¦   ¦   ¦   Ceuta
¦   ¦       ¦   ¦   ¦   ¦   Conakry
¦   ¦       ¦   ¦   ¦   ¦   Dakar
¦   ¦       ¦   ¦   ¦   ¦   Dar_es_Salaam
¦   ¦       ¦   ¦   ¦   ¦   Djibouti
¦   ¦       ¦   ¦   ¦   ¦   Douala
¦   ¦       ¦   ¦   ¦   ¦   El_Aaiun
¦   ¦       ¦   ¦   ¦   ¦   Freetown
¦   ¦       ¦   ¦   ¦   ¦   Gaborone
¦   ¦       ¦   ¦   ¦   ¦   Harare
¦   ¦       ¦   ¦   ¦   ¦   Johannesburg
¦   ¦       ¦   ¦   ¦   ¦   Juba
¦   ¦       ¦   ¦   ¦   ¦   Kampala
¦   ¦       ¦   ¦   ¦   ¦   Khartoum
¦   ¦       ¦   ¦   ¦   ¦   Kigali
¦   ¦       ¦   ¦   ¦   ¦   Kinshasa
¦   ¦       ¦   ¦   ¦   ¦   Lagos
¦   ¦       ¦   ¦   ¦   ¦   Libreville
¦   ¦       ¦   ¦   ¦   ¦   Lome
¦   ¦       ¦   ¦   ¦   ¦   Luanda
¦   ¦       ¦   ¦   ¦   ¦   Lubumbashi
¦   ¦       ¦   ¦   ¦   ¦   Lusaka
¦   ¦       ¦   ¦   ¦   ¦   Malabo
¦   ¦       ¦   ¦   ¦   ¦   Maputo
¦   ¦       ¦   ¦   ¦   ¦   Maseru
¦   ¦       ¦   ¦   ¦   ¦   Mbabane
¦   ¦       ¦   ¦   ¦   ¦   Mogadishu
¦   ¦       ¦   ¦   ¦   ¦   Monrovia
¦   ¦       ¦   ¦   ¦   ¦   Nairobi
¦   ¦       ¦   ¦   ¦   ¦   Ndjamena
¦   ¦       ¦   ¦   ¦   ¦   Niamey
¦   ¦       ¦   ¦   ¦   ¦   Nouakchott
¦   ¦       ¦   ¦   ¦   ¦   Ouagadougou
¦   ¦       ¦   ¦   ¦   ¦   Porto-Novo
¦   ¦       ¦   ¦   ¦   ¦   Sao_Tome
¦   ¦       ¦   ¦   ¦   ¦   Timbuktu
¦   ¦       ¦   ¦   ¦   ¦   Tripoli
¦   ¦       ¦   ¦   ¦   ¦   Tunis
¦   ¦       ¦   ¦   ¦   ¦   Windhoek
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---America
¦   ¦       ¦   ¦   ¦   ¦   Adak
¦   ¦       ¦   ¦   ¦   ¦   Anchorage
¦   ¦       ¦   ¦   ¦   ¦   Anguilla
¦   ¦       ¦   ¦   ¦   ¦   Antigua
¦   ¦       ¦   ¦   ¦   ¦   Araguaina
¦   ¦       ¦   ¦   ¦   ¦   Aruba
¦   ¦       ¦   ¦   ¦   ¦   Asuncion
¦   ¦       ¦   ¦   ¦   ¦   Atikokan
¦   ¦       ¦   ¦   ¦   ¦   Atka
¦   ¦       ¦   ¦   ¦   ¦   Bahia
¦   ¦       ¦   ¦   ¦   ¦   Bahia_Banderas
¦   ¦       ¦   ¦   ¦   ¦   Barbados
¦   ¦       ¦   ¦   ¦   ¦   Belem
¦   ¦       ¦   ¦   ¦   ¦   Belize
¦   ¦       ¦   ¦   ¦   ¦   Blanc-Sablon
¦   ¦       ¦   ¦   ¦   ¦   Boa_Vista
¦   ¦       ¦   ¦   ¦   ¦   Bogota
¦   ¦       ¦   ¦   ¦   ¦   Boise
¦   ¦       ¦   ¦   ¦   ¦   Buenos_Aires
¦   ¦       ¦   ¦   ¦   ¦   Cambridge_Bay
¦   ¦       ¦   ¦   ¦   ¦   Campo_Grande
¦   ¦       ¦   ¦   ¦   ¦   Cancun
¦   ¦       ¦   ¦   ¦   ¦   Caracas
¦   ¦       ¦   ¦   ¦   ¦   Catamarca
¦   ¦       ¦   ¦   ¦   ¦   Cayenne
¦   ¦       ¦   ¦   ¦   ¦   Cayman
¦   ¦       ¦   ¦   ¦   ¦   Chicago
¦   ¦       ¦   ¦   ¦   ¦   Chihuahua
¦   ¦       ¦   ¦   ¦   ¦   Ciudad_Juarez
¦   ¦       ¦   ¦   ¦   ¦   Coral_Harbour
¦   ¦       ¦   ¦   ¦   ¦   Cordoba
¦   ¦       ¦   ¦   ¦   ¦   Costa_Rica
¦   ¦       ¦   ¦   ¦   ¦   Creston
¦   ¦       ¦   ¦   ¦   ¦   Cuiaba
¦   ¦       ¦   ¦   ¦   ¦   Curacao
¦   ¦       ¦   ¦   ¦   ¦   Danmarkshavn
¦   ¦       ¦   ¦   ¦   ¦   Dawson
¦   ¦       ¦   ¦   ¦   ¦   Dawson_Creek
¦   ¦       ¦   ¦   ¦   ¦   Denver
¦   ¦       ¦   ¦   ¦   ¦   Detroit
¦   ¦       ¦   ¦   ¦   ¦   Dominica
¦   ¦       ¦   ¦   ¦   ¦   Edmonton
¦   ¦       ¦   ¦   ¦   ¦   Eirunepe
¦   ¦       ¦   ¦   ¦   ¦   El_Salvador
¦   ¦       ¦   ¦   ¦   ¦   Ensenada
¦   ¦       ¦   ¦   ¦   ¦   Fortaleza
¦   ¦       ¦   ¦   ¦   ¦   Fort_Nelson
¦   ¦       ¦   ¦   ¦   ¦   Fort_Wayne
¦   ¦       ¦   ¦   ¦   ¦   Glace_Bay
¦   ¦       ¦   ¦   ¦   ¦   Godthab
¦   ¦       ¦   ¦   ¦   ¦   Goose_Bay
¦   ¦       ¦   ¦   ¦   ¦   Grand_Turk
¦   ¦       ¦   ¦   ¦   ¦   Grenada
¦   ¦       ¦   ¦   ¦   ¦   Guadeloupe
¦   ¦       ¦   ¦   ¦   ¦   Guatemala
¦   ¦       ¦   ¦   ¦   ¦   Guayaquil
¦   ¦       ¦   ¦   ¦   ¦   Guyana
¦   ¦       ¦   ¦   ¦   ¦   Halifax
¦   ¦       ¦   ¦   ¦   ¦   Havana
¦   ¦       ¦   ¦   ¦   ¦   Hermosillo
¦   ¦       ¦   ¦   ¦   ¦   Indianapolis
¦   ¦       ¦   ¦   ¦   ¦   Inuvik
¦   ¦       ¦   ¦   ¦   ¦   Iqaluit
¦   ¦       ¦   ¦   ¦   ¦   Jamaica
¦   ¦       ¦   ¦   ¦   ¦   Jujuy
¦   ¦       ¦   ¦   ¦   ¦   Juneau
¦   ¦       ¦   ¦   ¦   ¦   Knox_IN
¦   ¦       ¦   ¦   ¦   ¦   Kralendijk
¦   ¦       ¦   ¦   ¦   ¦   La_Paz
¦   ¦       ¦   ¦   ¦   ¦   Lima
¦   ¦       ¦   ¦   ¦   ¦   Los_Angeles
¦   ¦       ¦   ¦   ¦   ¦   Louisville
¦   ¦       ¦   ¦   ¦   ¦   Lower_Princes
¦   ¦       ¦   ¦   ¦   ¦   Maceio
¦   ¦       ¦   ¦   ¦   ¦   Managua
¦   ¦       ¦   ¦   ¦   ¦   Manaus
¦   ¦       ¦   ¦   ¦   ¦   Marigot
¦   ¦       ¦   ¦   ¦   ¦   Martinique
¦   ¦       ¦   ¦   ¦   ¦   Matamoros
¦   ¦       ¦   ¦   ¦   ¦   Mazatlan
¦   ¦       ¦   ¦   ¦   ¦   Mendoza
¦   ¦       ¦   ¦   ¦   ¦   Menominee
¦   ¦       ¦   ¦   ¦   ¦   Merida
¦   ¦       ¦   ¦   ¦   ¦   Metlakatla
¦   ¦       ¦   ¦   ¦   ¦   Mexico_City
¦   ¦       ¦   ¦   ¦   ¦   Miquelon
¦   ¦       ¦   ¦   ¦   ¦   Moncton
¦   ¦       ¦   ¦   ¦   ¦   Monterrey
¦   ¦       ¦   ¦   ¦   ¦   Montevideo
¦   ¦       ¦   ¦   ¦   ¦   Montreal
¦   ¦       ¦   ¦   ¦   ¦   Montserrat
¦   ¦       ¦   ¦   ¦   ¦   Nassau
¦   ¦       ¦   ¦   ¦   ¦   New_York
¦   ¦       ¦   ¦   ¦   ¦   Nipigon
¦   ¦       ¦   ¦   ¦   ¦   Nome
¦   ¦       ¦   ¦   ¦   ¦   Noronha
¦   ¦       ¦   ¦   ¦   ¦   Nuuk
¦   ¦       ¦   ¦   ¦   ¦   Ojinaga
¦   ¦       ¦   ¦   ¦   ¦   Panama
¦   ¦       ¦   ¦   ¦   ¦   Pangnirtung
¦   ¦       ¦   ¦   ¦   ¦   Paramaribo
¦   ¦       ¦   ¦   ¦   ¦   Phoenix
¦   ¦       ¦   ¦   ¦   ¦   Port-au-Prince
¦   ¦       ¦   ¦   ¦   ¦   Porto_Acre
¦   ¦       ¦   ¦   ¦   ¦   Porto_Velho
¦   ¦       ¦   ¦   ¦   ¦   Port_of_Spain
¦   ¦       ¦   ¦   ¦   ¦   Puerto_Rico
¦   ¦       ¦   ¦   ¦   ¦   Punta_Arenas
¦   ¦       ¦   ¦   ¦   ¦   Rainy_River
¦   ¦       ¦   ¦   ¦   ¦   Rankin_Inlet
¦   ¦       ¦   ¦   ¦   ¦   Recife
¦   ¦       ¦   ¦   ¦   ¦   Regina
¦   ¦       ¦   ¦   ¦   ¦   Resolute
¦   ¦       ¦   ¦   ¦   ¦   Rio_Branco
¦   ¦       ¦   ¦   ¦   ¦   Rosario
¦   ¦       ¦   ¦   ¦   ¦   Santarem
¦   ¦       ¦   ¦   ¦   ¦   Santa_Isabel
¦   ¦       ¦   ¦   ¦   ¦   Santiago
¦   ¦       ¦   ¦   ¦   ¦   Santo_Domingo
¦   ¦       ¦   ¦   ¦   ¦   Sao_Paulo
¦   ¦       ¦   ¦   ¦   ¦   Scoresbysund
¦   ¦       ¦   ¦   ¦   ¦   Shiprock
¦   ¦       ¦   ¦   ¦   ¦   Sitka
¦   ¦       ¦   ¦   ¦   ¦   St_Barthelemy
¦   ¦       ¦   ¦   ¦   ¦   St_Johns
¦   ¦       ¦   ¦   ¦   ¦   St_Kitts
¦   ¦       ¦   ¦   ¦   ¦   St_Lucia
¦   ¦       ¦   ¦   ¦   ¦   St_Thomas
¦   ¦       ¦   ¦   ¦   ¦   St_Vincent
¦   ¦       ¦   ¦   ¦   ¦   Swift_Current
¦   ¦       ¦   ¦   ¦   ¦   Tegucigalpa
¦   ¦       ¦   ¦   ¦   ¦   Thule
¦   ¦       ¦   ¦   ¦   ¦   Thunder_Bay
¦   ¦       ¦   ¦   ¦   ¦   Tijuana
¦   ¦       ¦   ¦   ¦   ¦   Toronto
¦   ¦       ¦   ¦   ¦   ¦   Tortola
¦   ¦       ¦   ¦   ¦   ¦   Vancouver
¦   ¦       ¦   ¦   ¦   ¦   Virgin
¦   ¦       ¦   ¦   ¦   ¦   Whitehorse
¦   ¦       ¦   ¦   ¦   ¦   Winnipeg
¦   ¦       ¦   ¦   ¦   ¦   Yakutat
¦   ¦       ¦   ¦   ¦   ¦   Yellowknife
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---Argentina
¦   ¦       ¦   ¦   ¦   ¦   ¦   Buenos_Aires
¦   ¦       ¦   ¦   ¦   ¦   ¦   Catamarca
¦   ¦       ¦   ¦   ¦   ¦   ¦   ComodRivadavia
¦   ¦       ¦   ¦   ¦   ¦   ¦   Cordoba
¦   ¦       ¦   ¦   ¦   ¦   ¦   Jujuy
¦   ¦       ¦   ¦   ¦   ¦   ¦   La_Rioja
¦   ¦       ¦   ¦   ¦   ¦   ¦   Mendoza
¦   ¦       ¦   ¦   ¦   ¦   ¦   Rio_Gallegos
¦   ¦       ¦   ¦   ¦   ¦   ¦   Salta
¦   ¦       ¦   ¦   ¦   ¦   ¦   San_Juan
¦   ¦       ¦   ¦   ¦   ¦   ¦   San_Luis
¦   ¦       ¦   ¦   ¦   ¦   ¦   Tucuman
¦   ¦       ¦   ¦   ¦   ¦   ¦   Ushuaia
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---Indiana
¦   ¦       ¦   ¦   ¦   ¦   ¦   Indianapolis
¦   ¦       ¦   ¦   ¦   ¦   ¦   Knox
¦   ¦       ¦   ¦   ¦   ¦   ¦   Marengo
¦   ¦       ¦   ¦   ¦   ¦   ¦   Petersburg
¦   ¦       ¦   ¦   ¦   ¦   ¦   Tell_City
¦   ¦       ¦   ¦   ¦   ¦   ¦   Vevay
¦   ¦       ¦   ¦   ¦   ¦   ¦   Vincennes
¦   ¦       ¦   ¦   ¦   ¦   ¦   Winamac
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---Kentucky
¦   ¦       ¦   ¦   ¦   ¦   ¦   Louisville
¦   ¦       ¦   ¦   ¦   ¦   ¦   Monticello
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---North_Dakota
¦   ¦       ¦   ¦   ¦   ¦   ¦   Beulah
¦   ¦       ¦   ¦   ¦   ¦   ¦   Center
¦   ¦       ¦   ¦   ¦   ¦   ¦   New_Salem
¦   ¦       ¦   ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦   ¦           
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Antarctica
¦   ¦       ¦   ¦   ¦   ¦   Casey
¦   ¦       ¦   ¦   ¦   ¦   Davis
¦   ¦       ¦   ¦   ¦   ¦   DumontDUrville
¦   ¦       ¦   ¦   ¦   ¦   Macquarie
¦   ¦       ¦   ¦   ¦   ¦   Mawson
¦   ¦       ¦   ¦   ¦   ¦   McMurdo
¦   ¦       ¦   ¦   ¦   ¦   Palmer
¦   ¦       ¦   ¦   ¦   ¦   Rothera
¦   ¦       ¦   ¦   ¦   ¦   South_Pole
¦   ¦       ¦   ¦   ¦   ¦   Syowa
¦   ¦       ¦   ¦   ¦   ¦   Troll
¦   ¦       ¦   ¦   ¦   ¦   Vostok
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Arctic
¦   ¦       ¦   ¦   ¦   ¦   Longyearbyen
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Asia
¦   ¦       ¦   ¦   ¦   ¦   Aden
¦   ¦       ¦   ¦   ¦   ¦   Almaty
¦   ¦       ¦   ¦   ¦   ¦   Amman
¦   ¦       ¦   ¦   ¦   ¦   Anadyr
¦   ¦       ¦   ¦   ¦   ¦   Aqtau
¦   ¦       ¦   ¦   ¦   ¦   Aqtobe
¦   ¦       ¦   ¦   ¦   ¦   Ashgabat
¦   ¦       ¦   ¦   ¦   ¦   Ashkhabad
¦   ¦       ¦   ¦   ¦   ¦   Atyrau
¦   ¦       ¦   ¦   ¦   ¦   Baghdad
¦   ¦       ¦   ¦   ¦   ¦   Bahrain
¦   ¦       ¦   ¦   ¦   ¦   Baku
¦   ¦       ¦   ¦   ¦   ¦   Bangkok
¦   ¦       ¦   ¦   ¦   ¦   Barnaul
¦   ¦       ¦   ¦   ¦   ¦   Beirut
¦   ¦       ¦   ¦   ¦   ¦   Bishkek
¦   ¦       ¦   ¦   ¦   ¦   Brunei
¦   ¦       ¦   ¦   ¦   ¦   Calcutta
¦   ¦       ¦   ¦   ¦   ¦   Chita
¦   ¦       ¦   ¦   ¦   ¦   Choibalsan
¦   ¦       ¦   ¦   ¦   ¦   Chongqing
¦   ¦       ¦   ¦   ¦   ¦   Chungking
¦   ¦       ¦   ¦   ¦   ¦   Colombo
¦   ¦       ¦   ¦   ¦   ¦   Dacca
¦   ¦       ¦   ¦   ¦   ¦   Damascus
¦   ¦       ¦   ¦   ¦   ¦   Dhaka
¦   ¦       ¦   ¦   ¦   ¦   Dili
¦   ¦       ¦   ¦   ¦   ¦   Dubai
¦   ¦       ¦   ¦   ¦   ¦   Dushanbe
¦   ¦       ¦   ¦   ¦   ¦   Famagusta
¦   ¦       ¦   ¦   ¦   ¦   Gaza
¦   ¦       ¦   ¦   ¦   ¦   Harbin
¦   ¦       ¦   ¦   ¦   ¦   Hebron
¦   ¦       ¦   ¦   ¦   ¦   Hong_Kong
¦   ¦       ¦   ¦   ¦   ¦   Hovd
¦   ¦       ¦   ¦   ¦   ¦   Ho_Chi_Minh
¦   ¦       ¦   ¦   ¦   ¦   Irkutsk
¦   ¦       ¦   ¦   ¦   ¦   Istanbul
¦   ¦       ¦   ¦   ¦   ¦   Jakarta
¦   ¦       ¦   ¦   ¦   ¦   Jayapura
¦   ¦       ¦   ¦   ¦   ¦   Jerusalem
¦   ¦       ¦   ¦   ¦   ¦   Kabul
¦   ¦       ¦   ¦   ¦   ¦   Kamchatka
¦   ¦       ¦   ¦   ¦   ¦   Karachi
¦   ¦       ¦   ¦   ¦   ¦   Kashgar
¦   ¦       ¦   ¦   ¦   ¦   Kathmandu
¦   ¦       ¦   ¦   ¦   ¦   Katmandu
¦   ¦       ¦   ¦   ¦   ¦   Khandyga
¦   ¦       ¦   ¦   ¦   ¦   Kolkata
¦   ¦       ¦   ¦   ¦   ¦   Krasnoyarsk
¦   ¦       ¦   ¦   ¦   ¦   Kuala_Lumpur
¦   ¦       ¦   ¦   ¦   ¦   Kuching
¦   ¦       ¦   ¦   ¦   ¦   Kuwait
¦   ¦       ¦   ¦   ¦   ¦   Macao
¦   ¦       ¦   ¦   ¦   ¦   Macau
¦   ¦       ¦   ¦   ¦   ¦   Magadan
¦   ¦       ¦   ¦   ¦   ¦   Makassar
¦   ¦       ¦   ¦   ¦   ¦   Manila
¦   ¦       ¦   ¦   ¦   ¦   Muscat
¦   ¦       ¦   ¦   ¦   ¦   Nicosia
¦   ¦       ¦   ¦   ¦   ¦   Novokuznetsk
¦   ¦       ¦   ¦   ¦   ¦   Novosibirsk
¦   ¦       ¦   ¦   ¦   ¦   Omsk
¦   ¦       ¦   ¦   ¦   ¦   Oral
¦   ¦       ¦   ¦   ¦   ¦   Phnom_Penh
¦   ¦       ¦   ¦   ¦   ¦   Pontianak
¦   ¦       ¦   ¦   ¦   ¦   Pyongyang
¦   ¦       ¦   ¦   ¦   ¦   Qatar
¦   ¦       ¦   ¦   ¦   ¦   Qostanay
¦   ¦       ¦   ¦   ¦   ¦   Qyzylorda
¦   ¦       ¦   ¦   ¦   ¦   Rangoon
¦   ¦       ¦   ¦   ¦   ¦   Riyadh
¦   ¦       ¦   ¦   ¦   ¦   Saigon
¦   ¦       ¦   ¦   ¦   ¦   Sakhalin
¦   ¦       ¦   ¦   ¦   ¦   Samarkand
¦   ¦       ¦   ¦   ¦   ¦   Seoul
¦   ¦       ¦   ¦   ¦   ¦   Shanghai
¦   ¦       ¦   ¦   ¦   ¦   Singapore
¦   ¦       ¦   ¦   ¦   ¦   Srednekolymsk
¦   ¦       ¦   ¦   ¦   ¦   Taipei
¦   ¦       ¦   ¦   ¦   ¦   Tashkent
¦   ¦       ¦   ¦   ¦   ¦   Tbilisi
¦   ¦       ¦   ¦   ¦   ¦   Tehran
¦   ¦       ¦   ¦   ¦   ¦   Tel_Aviv
¦   ¦       ¦   ¦   ¦   ¦   Thimbu
¦   ¦       ¦   ¦   ¦   ¦   Thimphu
¦   ¦       ¦   ¦   ¦   ¦   Tokyo
¦   ¦       ¦   ¦   ¦   ¦   Tomsk
¦   ¦       ¦   ¦   ¦   ¦   Ujung_Pandang
¦   ¦       ¦   ¦   ¦   ¦   Ulaanbaatar
¦   ¦       ¦   ¦   ¦   ¦   Ulan_Bator
¦   ¦       ¦   ¦   ¦   ¦   Urumqi
¦   ¦       ¦   ¦   ¦   ¦   Ust-Nera
¦   ¦       ¦   ¦   ¦   ¦   Vientiane
¦   ¦       ¦   ¦   ¦   ¦   Vladivostok
¦   ¦       ¦   ¦   ¦   ¦   Yakutsk
¦   ¦       ¦   ¦   ¦   ¦   Yangon
¦   ¦       ¦   ¦   ¦   ¦   Yekaterinburg
¦   ¦       ¦   ¦   ¦   ¦   Yerevan
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Atlantic
¦   ¦       ¦   ¦   ¦   ¦   Azores
¦   ¦       ¦   ¦   ¦   ¦   Bermuda
¦   ¦       ¦   ¦   ¦   ¦   Canary
¦   ¦       ¦   ¦   ¦   ¦   Cape_Verde
¦   ¦       ¦   ¦   ¦   ¦   Faeroe
¦   ¦       ¦   ¦   ¦   ¦   Faroe
¦   ¦       ¦   ¦   ¦   ¦   Jan_Mayen
¦   ¦       ¦   ¦   ¦   ¦   Madeira
¦   ¦       ¦   ¦   ¦   ¦   Reykjavik
¦   ¦       ¦   ¦   ¦   ¦   South_Georgia
¦   ¦       ¦   ¦   ¦   ¦   Stanley
¦   ¦       ¦   ¦   ¦   ¦   St_Helena
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Australia
¦   ¦       ¦   ¦   ¦   ¦   ACT
¦   ¦       ¦   ¦   ¦   ¦   Adelaide
¦   ¦       ¦   ¦   ¦   ¦   Brisbane
¦   ¦       ¦   ¦   ¦   ¦   Broken_Hill
¦   ¦       ¦   ¦   ¦   ¦   Canberra
¦   ¦       ¦   ¦   ¦   ¦   Currie
¦   ¦       ¦   ¦   ¦   ¦   Darwin
¦   ¦       ¦   ¦   ¦   ¦   Eucla
¦   ¦       ¦   ¦   ¦   ¦   Hobart
¦   ¦       ¦   ¦   ¦   ¦   LHI
¦   ¦       ¦   ¦   ¦   ¦   Lindeman
¦   ¦       ¦   ¦   ¦   ¦   Lord_Howe
¦   ¦       ¦   ¦   ¦   ¦   Melbourne
¦   ¦       ¦   ¦   ¦   ¦   North
¦   ¦       ¦   ¦   ¦   ¦   NSW
¦   ¦       ¦   ¦   ¦   ¦   Perth
¦   ¦       ¦   ¦   ¦   ¦   Queensland
¦   ¦       ¦   ¦   ¦   ¦   South
¦   ¦       ¦   ¦   ¦   ¦   Sydney
¦   ¦       ¦   ¦   ¦   ¦   Tasmania
¦   ¦       ¦   ¦   ¦   ¦   Victoria
¦   ¦       ¦   ¦   ¦   ¦   West
¦   ¦       ¦   ¦   ¦   ¦   Yancowinna
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Brazil
¦   ¦       ¦   ¦   ¦   ¦   Acre
¦   ¦       ¦   ¦   ¦   ¦   DeNoronha
¦   ¦       ¦   ¦   ¦   ¦   East
¦   ¦       ¦   ¦   ¦   ¦   West
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Canada
¦   ¦       ¦   ¦   ¦   ¦   Atlantic
¦   ¦       ¦   ¦   ¦   ¦   Central
¦   ¦       ¦   ¦   ¦   ¦   Eastern
¦   ¦       ¦   ¦   ¦   ¦   Mountain
¦   ¦       ¦   ¦   ¦   ¦   Newfoundland
¦   ¦       ¦   ¦   ¦   ¦   Pacific
¦   ¦       ¦   ¦   ¦   ¦   Saskatchewan
¦   ¦       ¦   ¦   ¦   ¦   Yukon
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Chile
¦   ¦       ¦   ¦   ¦   ¦   Continental
¦   ¦       ¦   ¦   ¦   ¦   EasterIsland
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Etc
¦   ¦       ¦   ¦   ¦   ¦   GMT
¦   ¦       ¦   ¦   ¦   ¦   GMT+0
¦   ¦       ¦   ¦   ¦   ¦   GMT+1
¦   ¦       ¦   ¦   ¦   ¦   GMT+10
¦   ¦       ¦   ¦   ¦   ¦   GMT+11
¦   ¦       ¦   ¦   ¦   ¦   GMT+12
¦   ¦       ¦   ¦   ¦   ¦   GMT+2
¦   ¦       ¦   ¦   ¦   ¦   GMT+3
¦   ¦       ¦   ¦   ¦   ¦   GMT+4
¦   ¦       ¦   ¦   ¦   ¦   GMT+5
¦   ¦       ¦   ¦   ¦   ¦   GMT+6
¦   ¦       ¦   ¦   ¦   ¦   GMT+7
¦   ¦       ¦   ¦   ¦   ¦   GMT+8
¦   ¦       ¦   ¦   ¦   ¦   GMT+9
¦   ¦       ¦   ¦   ¦   ¦   GMT-0
¦   ¦       ¦   ¦   ¦   ¦   GMT-1
¦   ¦       ¦   ¦   ¦   ¦   GMT-10
¦   ¦       ¦   ¦   ¦   ¦   GMT-11
¦   ¦       ¦   ¦   ¦   ¦   GMT-12
¦   ¦       ¦   ¦   ¦   ¦   GMT-13
¦   ¦       ¦   ¦   ¦   ¦   GMT-14
¦   ¦       ¦   ¦   ¦   ¦   GMT-2
¦   ¦       ¦   ¦   ¦   ¦   GMT-3
¦   ¦       ¦   ¦   ¦   ¦   GMT-4
¦   ¦       ¦   ¦   ¦   ¦   GMT-5
¦   ¦       ¦   ¦   ¦   ¦   GMT-6
¦   ¦       ¦   ¦   ¦   ¦   GMT-7
¦   ¦       ¦   ¦   ¦   ¦   GMT-8
¦   ¦       ¦   ¦   ¦   ¦   GMT-9
¦   ¦       ¦   ¦   ¦   ¦   GMT0
¦   ¦       ¦   ¦   ¦   ¦   Greenwich
¦   ¦       ¦   ¦   ¦   ¦   UCT
¦   ¦       ¦   ¦   ¦   ¦   Universal
¦   ¦       ¦   ¦   ¦   ¦   UTC
¦   ¦       ¦   ¦   ¦   ¦   Zulu
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Europe
¦   ¦       ¦   ¦   ¦   ¦   Amsterdam
¦   ¦       ¦   ¦   ¦   ¦   Andorra
¦   ¦       ¦   ¦   ¦   ¦   Astrakhan
¦   ¦       ¦   ¦   ¦   ¦   Athens
¦   ¦       ¦   ¦   ¦   ¦   Belfast
¦   ¦       ¦   ¦   ¦   ¦   Belgrade
¦   ¦       ¦   ¦   ¦   ¦   Berlin
¦   ¦       ¦   ¦   ¦   ¦   Bratislava
¦   ¦       ¦   ¦   ¦   ¦   Brussels
¦   ¦       ¦   ¦   ¦   ¦   Bucharest
¦   ¦       ¦   ¦   ¦   ¦   Budapest
¦   ¦       ¦   ¦   ¦   ¦   Busingen
¦   ¦       ¦   ¦   ¦   ¦   Chisinau
¦   ¦       ¦   ¦   ¦   ¦   Copenhagen
¦   ¦       ¦   ¦   ¦   ¦   Dublin
¦   ¦       ¦   ¦   ¦   ¦   Gibraltar
¦   ¦       ¦   ¦   ¦   ¦   Guernsey
¦   ¦       ¦   ¦   ¦   ¦   Helsinki
¦   ¦       ¦   ¦   ¦   ¦   Isle_of_Man
¦   ¦       ¦   ¦   ¦   ¦   Istanbul
¦   ¦       ¦   ¦   ¦   ¦   Jersey
¦   ¦       ¦   ¦   ¦   ¦   Kaliningrad
¦   ¦       ¦   ¦   ¦   ¦   Kiev
¦   ¦       ¦   ¦   ¦   ¦   Kirov
¦   ¦       ¦   ¦   ¦   ¦   Kyiv
¦   ¦       ¦   ¦   ¦   ¦   Lisbon
¦   ¦       ¦   ¦   ¦   ¦   Ljubljana
¦   ¦       ¦   ¦   ¦   ¦   London
¦   ¦       ¦   ¦   ¦   ¦   Luxembourg
¦   ¦       ¦   ¦   ¦   ¦   Madrid
¦   ¦       ¦   ¦   ¦   ¦   Malta
¦   ¦       ¦   ¦   ¦   ¦   Mariehamn
¦   ¦       ¦   ¦   ¦   ¦   Minsk
¦   ¦       ¦   ¦   ¦   ¦   Monaco
¦   ¦       ¦   ¦   ¦   ¦   Moscow
¦   ¦       ¦   ¦   ¦   ¦   Nicosia
¦   ¦       ¦   ¦   ¦   ¦   Oslo
¦   ¦       ¦   ¦   ¦   ¦   Paris
¦   ¦       ¦   ¦   ¦   ¦   Podgorica
¦   ¦       ¦   ¦   ¦   ¦   Prague
¦   ¦       ¦   ¦   ¦   ¦   Riga
¦   ¦       ¦   ¦   ¦   ¦   Rome
¦   ¦       ¦   ¦   ¦   ¦   Samara
¦   ¦       ¦   ¦   ¦   ¦   San_Marino
¦   ¦       ¦   ¦   ¦   ¦   Sarajevo
¦   ¦       ¦   ¦   ¦   ¦   Saratov
¦   ¦       ¦   ¦   ¦   ¦   Simferopol
¦   ¦       ¦   ¦   ¦   ¦   Skopje
¦   ¦       ¦   ¦   ¦   ¦   Sofia
¦   ¦       ¦   ¦   ¦   ¦   Stockholm
¦   ¦       ¦   ¦   ¦   ¦   Tallinn
¦   ¦       ¦   ¦   ¦   ¦   Tirane
¦   ¦       ¦   ¦   ¦   ¦   Tiraspol
¦   ¦       ¦   ¦   ¦   ¦   Ulyanovsk
¦   ¦       ¦   ¦   ¦   ¦   Uzhgorod
¦   ¦       ¦   ¦   ¦   ¦   Vaduz
¦   ¦       ¦   ¦   ¦   ¦   Vatican
¦   ¦       ¦   ¦   ¦   ¦   Vienna
¦   ¦       ¦   ¦   ¦   ¦   Vilnius
¦   ¦       ¦   ¦   ¦   ¦   Volgograd
¦   ¦       ¦   ¦   ¦   ¦   Warsaw
¦   ¦       ¦   ¦   ¦   ¦   Zagreb
¦   ¦       ¦   ¦   ¦   ¦   Zaporozhye
¦   ¦       ¦   ¦   ¦   ¦   Zurich
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Indian
¦   ¦       ¦   ¦   ¦   ¦   Antananarivo
¦   ¦       ¦   ¦   ¦   ¦   Chagos
¦   ¦       ¦   ¦   ¦   ¦   Christmas
¦   ¦       ¦   ¦   ¦   ¦   Cocos
¦   ¦       ¦   ¦   ¦   ¦   Comoro
¦   ¦       ¦   ¦   ¦   ¦   Kerguelen
¦   ¦       ¦   ¦   ¦   ¦   Mahe
¦   ¦       ¦   ¦   ¦   ¦   Maldives
¦   ¦       ¦   ¦   ¦   ¦   Mauritius
¦   ¦       ¦   ¦   ¦   ¦   Mayotte
¦   ¦       ¦   ¦   ¦   ¦   Reunion
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Mexico
¦   ¦       ¦   ¦   ¦   ¦   BajaNorte
¦   ¦       ¦   ¦   ¦   ¦   BajaSur
¦   ¦       ¦   ¦   ¦   ¦   General
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---Pacific
¦   ¦       ¦   ¦   ¦   ¦   Apia
¦   ¦       ¦   ¦   ¦   ¦   Auckland
¦   ¦       ¦   ¦   ¦   ¦   Bougainville
¦   ¦       ¦   ¦   ¦   ¦   Chatham
¦   ¦       ¦   ¦   ¦   ¦   Chuuk
¦   ¦       ¦   ¦   ¦   ¦   Easter
¦   ¦       ¦   ¦   ¦   ¦   Efate
¦   ¦       ¦   ¦   ¦   ¦   Enderbury
¦   ¦       ¦   ¦   ¦   ¦   Fakaofo
¦   ¦       ¦   ¦   ¦   ¦   Fiji
¦   ¦       ¦   ¦   ¦   ¦   Funafuti
¦   ¦       ¦   ¦   ¦   ¦   Galapagos
¦   ¦       ¦   ¦   ¦   ¦   Gambier
¦   ¦       ¦   ¦   ¦   ¦   Guadalcanal
¦   ¦       ¦   ¦   ¦   ¦   Guam
¦   ¦       ¦   ¦   ¦   ¦   Honolulu
¦   ¦       ¦   ¦   ¦   ¦   Johnston
¦   ¦       ¦   ¦   ¦   ¦   Kanton
¦   ¦       ¦   ¦   ¦   ¦   Kiritimati
¦   ¦       ¦   ¦   ¦   ¦   Kosrae
¦   ¦       ¦   ¦   ¦   ¦   Kwajalein
¦   ¦       ¦   ¦   ¦   ¦   Majuro
¦   ¦       ¦   ¦   ¦   ¦   Marquesas
¦   ¦       ¦   ¦   ¦   ¦   Midway
¦   ¦       ¦   ¦   ¦   ¦   Nauru
¦   ¦       ¦   ¦   ¦   ¦   Niue
¦   ¦       ¦   ¦   ¦   ¦   Norfolk
¦   ¦       ¦   ¦   ¦   ¦   Noumea
¦   ¦       ¦   ¦   ¦   ¦   Pago_Pago
¦   ¦       ¦   ¦   ¦   ¦   Palau
¦   ¦       ¦   ¦   ¦   ¦   Pitcairn
¦   ¦       ¦   ¦   ¦   ¦   Pohnpei
¦   ¦       ¦   ¦   ¦   ¦   Ponape
¦   ¦       ¦   ¦   ¦   ¦   Port_Moresby
¦   ¦       ¦   ¦   ¦   ¦   Rarotonga
¦   ¦       ¦   ¦   ¦   ¦   Saipan
¦   ¦       ¦   ¦   ¦   ¦   Samoa
¦   ¦       ¦   ¦   ¦   ¦   Tahiti
¦   ¦       ¦   ¦   ¦   ¦   Tarawa
¦   ¦       ¦   ¦   ¦   ¦   Tongatapu
¦   ¦       ¦   ¦   ¦   ¦   Truk
¦   ¦       ¦   ¦   ¦   ¦   Wake
¦   ¦       ¦   ¦   ¦   ¦   Wallis
¦   ¦       ¦   ¦   ¦   ¦   Yap
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---US
¦   ¦       ¦   ¦   ¦   ¦   Alaska
¦   ¦       ¦   ¦   ¦   ¦   Aleutian
¦   ¦       ¦   ¦   ¦   ¦   Arizona
¦   ¦       ¦   ¦   ¦   ¦   Central
¦   ¦       ¦   ¦   ¦   ¦   East-Indiana
¦   ¦       ¦   ¦   ¦   ¦   Eastern
¦   ¦       ¦   ¦   ¦   ¦   Hawaii
¦   ¦       ¦   ¦   ¦   ¦   Indiana-Starke
¦   ¦       ¦   ¦   ¦   ¦   Michigan
¦   ¦       ¦   ¦   ¦   ¦   Mountain
¦   ¦       ¦   ¦   ¦   ¦   Pacific
¦   ¦       ¦   ¦   ¦   ¦   Samoa
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---tzdata-2023.3.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       LICENSE_APACHE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---urllib3
¦   ¦       ¦   ¦   connection.py
¦   ¦       ¦   ¦   connectionpool.py
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   fields.py
¦   ¦       ¦   ¦   filepost.py
¦   ¦       ¦   ¦   poolmanager.py
¦   ¦       ¦   ¦   request.py
¦   ¦       ¦   ¦   response.py
¦   ¦       ¦   ¦   _collections.py
¦   ¦       ¦   ¦   _version.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---contrib
¦   ¦       ¦   ¦   ¦   appengine.py
¦   ¦       ¦   ¦   ¦   ntlmpool.py
¦   ¦       ¦   ¦   ¦   pyopenssl.py
¦   ¦       ¦   ¦   ¦   securetransport.py
¦   ¦       ¦   ¦   ¦   socks.py
¦   ¦       ¦   ¦   ¦   _appengine_environ.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---_securetransport
¦   ¦       ¦   ¦   ¦   ¦   bindings.py
¦   ¦       ¦   ¦   ¦   ¦   low_level.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           bindings.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           low_level.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           appengine.cpython-38.pyc
¦   ¦       ¦   ¦           ntlmpool.cpython-38.pyc
¦   ¦       ¦   ¦           pyopenssl.cpython-38.pyc
¦   ¦       ¦   ¦           securetransport.cpython-38.pyc
¦   ¦       ¦   ¦           socks.cpython-38.pyc
¦   ¦       ¦   ¦           _appengine_environ.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---packages
¦   ¦       ¦   ¦   ¦   six.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---backports
¦   ¦       ¦   ¦   ¦   ¦   makefile.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           makefile.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           six.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---util
¦   ¦       ¦   ¦   ¦   connection.py
¦   ¦       ¦   ¦   ¦   proxy.py
¦   ¦       ¦   ¦   ¦   queue.py
¦   ¦       ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   response.py
¦   ¦       ¦   ¦   ¦   retry.py
¦   ¦       ¦   ¦   ¦   ssltransport.py
¦   ¦       ¦   ¦   ¦   ssl_.py
¦   ¦       ¦   ¦   ¦   ssl_match_hostname.py
¦   ¦       ¦   ¦   ¦   timeout.py
¦   ¦       ¦   ¦   ¦   url.py
¦   ¦       ¦   ¦   ¦   wait.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           connection.cpython-38.pyc
¦   ¦       ¦   ¦           proxy.cpython-38.pyc
¦   ¦       ¦   ¦           queue.cpython-38.pyc
¦   ¦       ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦           response.cpython-38.pyc
¦   ¦       ¦   ¦           retry.cpython-38.pyc
¦   ¦       ¦   ¦           ssltransport.cpython-38.pyc
¦   ¦       ¦   ¦           ssl_.cpython-38.pyc
¦   ¦       ¦   ¦           ssl_match_hostname.cpython-38.pyc
¦   ¦       ¦   ¦           timeout.cpython-38.pyc
¦   ¦       ¦   ¦           url.cpython-38.pyc
¦   ¦       ¦   ¦           wait.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           connection.cpython-38.pyc
¦   ¦       ¦           connectionpool.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           fields.cpython-38.pyc
¦   ¦       ¦           filepost.cpython-38.pyc
¦   ¦       ¦           poolmanager.cpython-38.pyc
¦   ¦       ¦           request.cpython-38.pyc
¦   ¦       ¦           response.cpython-38.pyc
¦   ¦       ¦           _collections.cpython-38.pyc
¦   ¦       ¦           _version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---urllib3-1.26.15.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.txt
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---vine
¦   ¦       ¦   ¦   abstract.py
¦   ¦       ¦   ¦   funtools.py
¦   ¦       ¦   ¦   promises.py
¦   ¦       ¦   ¦   synchronization.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           abstract.cpython-38.pyc
¦   ¦       ¦           funtools.cpython-38.pyc
¦   ¦       ¦           promises.cpython-38.pyc
¦   ¦       ¦           synchronization.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---vine-5.0.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---wcwidth
¦   ¦       ¦   ¦   table_wide.py
¦   ¦       ¦   ¦   table_zero.py
¦   ¦       ¦   ¦   unicode_versions.py
¦   ¦       ¦   ¦   wcwidth.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           table_wide.cpython-38.pyc
¦   ¦       ¦           table_zero.cpython-38.pyc
¦   ¦       ¦           unicode_versions.cpython-38.pyc
¦   ¦       ¦           wcwidth.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---wcwidth-0.2.6.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---weasyprint
¦   ¦       ¦   ¦   anchors.py
¦   ¦       ¦   ¦   document.py
¦   ¦       ¦   ¦   draw.py
¦   ¦       ¦   ¦   html.py
¦   ¦       ¦   ¦   images.py
¦   ¦       ¦   ¦   logger.py
¦   ¦       ¦   ¦   matrix.py
¦   ¦       ¦   ¦   stacking.py
¦   ¦       ¦   ¦   urls.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---css
¦   ¦       ¦   ¦   ¦   computed_values.py
¦   ¦       ¦   ¦   ¦   counters.py
¦   ¦       ¦   ¦   ¦   html5_ph.css
¦   ¦       ¦   ¦   ¦   html5_ua.css
¦   ¦       ¦   ¦   ¦   html5_ua_form.css
¦   ¦       ¦   ¦   ¦   media_queries.py
¦   ¦       ¦   ¦   ¦   properties.py
¦   ¦       ¦   ¦   ¦   targets.py
¦   ¦       ¦   ¦   ¦   tests_ua.css
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---validation
¦   ¦       ¦   ¦   ¦   ¦   descriptors.py
¦   ¦       ¦   ¦   ¦   ¦   expanders.py
¦   ¦       ¦   ¦   ¦   ¦   properties.py
¦   ¦       ¦   ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   ¦   
¦   ¦       ¦   ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦   ¦           descriptors.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           expanders.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           properties.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           computed_values.cpython-38.pyc
¦   ¦       ¦   ¦           counters.cpython-38.pyc
¦   ¦       ¦   ¦           media_queries.cpython-38.pyc
¦   ¦       ¦   ¦           properties.cpython-38.pyc
¦   ¦       ¦   ¦           targets.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---formatting_structure
¦   ¦       ¦   ¦   ¦   boxes.py
¦   ¦       ¦   ¦   ¦   build.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           boxes.cpython-38.pyc
¦   ¦       ¦   ¦           build.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---layout
¦   ¦       ¦   ¦   ¦   absolute.py
¦   ¦       ¦   ¦   ¦   background.py
¦   ¦       ¦   ¦   ¦   block.py
¦   ¦       ¦   ¦   ¦   column.py
¦   ¦       ¦   ¦   ¦   flex.py
¦   ¦       ¦   ¦   ¦   float.py
¦   ¦       ¦   ¦   ¦   inline.py
¦   ¦       ¦   ¦   ¦   leader.py
¦   ¦       ¦   ¦   ¦   min_max.py
¦   ¦       ¦   ¦   ¦   page.py
¦   ¦       ¦   ¦   ¦   percent.py
¦   ¦       ¦   ¦   ¦   preferred.py
¦   ¦       ¦   ¦   ¦   replaced.py
¦   ¦       ¦   ¦   ¦   table.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           absolute.cpython-38.pyc
¦   ¦       ¦   ¦           background.cpython-38.pyc
¦   ¦       ¦   ¦           block.cpython-38.pyc
¦   ¦       ¦   ¦           column.cpython-38.pyc
¦   ¦       ¦   ¦           flex.cpython-38.pyc
¦   ¦       ¦   ¦           float.cpython-38.pyc
¦   ¦       ¦   ¦           inline.cpython-38.pyc
¦   ¦       ¦   ¦           leader.cpython-38.pyc
¦   ¦       ¦   ¦           min_max.cpython-38.pyc
¦   ¦       ¦   ¦           page.cpython-38.pyc
¦   ¦       ¦   ¦           percent.cpython-38.pyc
¦   ¦       ¦   ¦           preferred.cpython-38.pyc
¦   ¦       ¦   ¦           replaced.cpython-38.pyc
¦   ¦       ¦   ¦           table.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---pdf
¦   ¦       ¦   ¦   ¦   anchors.py
¦   ¦       ¦   ¦   ¦   fonts.py
¦   ¦       ¦   ¦   ¦   metadata.py
¦   ¦       ¦   ¦   ¦   pdfa.py
¦   ¦       ¦   ¦   ¦   pdfua.py
¦   ¦       ¦   ¦   ¦   sRGB2014.icc
¦   ¦       ¦   ¦   ¦   stream.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           anchors.cpython-38.pyc
¦   ¦       ¦   ¦           fonts.cpython-38.pyc
¦   ¦       ¦   ¦           metadata.cpython-38.pyc
¦   ¦       ¦   ¦           pdfa.cpython-38.pyc
¦   ¦       ¦   ¦           pdfua.cpython-38.pyc
¦   ¦       ¦   ¦           stream.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---svg
¦   ¦       ¦   ¦   ¦   bounding_box.py
¦   ¦       ¦   ¦   ¦   css.py
¦   ¦       ¦   ¦   ¦   defs.py
¦   ¦       ¦   ¦   ¦   images.py
¦   ¦       ¦   ¦   ¦   path.py
¦   ¦       ¦   ¦   ¦   shapes.py
¦   ¦       ¦   ¦   ¦   text.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           bounding_box.cpython-38.pyc
¦   ¦       ¦   ¦           css.cpython-38.pyc
¦   ¦       ¦   ¦           defs.cpython-38.pyc
¦   ¦       ¦   ¦           images.cpython-38.pyc
¦   ¦       ¦   ¦           path.cpython-38.pyc
¦   ¦       ¦   ¦           shapes.cpython-38.pyc
¦   ¦       ¦   ¦           text.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---text
¦   ¦       ¦   ¦   ¦   constants.py
¦   ¦       ¦   ¦   ¦   ffi.py
¦   ¦       ¦   ¦   ¦   fonts.py
¦   ¦       ¦   ¦   ¦   line_break.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           constants.cpython-38.pyc
¦   ¦       ¦   ¦           ffi.cpython-38.pyc
¦   ¦       ¦   ¦           fonts.cpython-38.pyc
¦   ¦       ¦   ¦           line_break.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           anchors.cpython-38.pyc
¦   ¦       ¦           document.cpython-38.pyc
¦   ¦       ¦           draw.cpython-38.pyc
¦   ¦       ¦           html.cpython-38.pyc
¦   ¦       ¦           images.cpython-38.pyc
¦   ¦       ¦           logger.cpython-38.pyc
¦   ¦       ¦           matrix.cpython-38.pyc
¦   ¦       ¦           stacking.cpython-38.pyc
¦   ¦       ¦           urls.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---weasyprint-58.1.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---webencodings
¦   ¦       ¦   ¦   labels.py
¦   ¦       ¦   ¦   mklabels.py
¦   ¦       ¦   ¦   tests.py
¦   ¦       ¦   ¦   x_user_defined.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           labels.cpython-38.pyc
¦   ¦       ¦           mklabels.cpython-38.pyc
¦   ¦       ¦           tests.cpython-38.pyc
¦   ¦       ¦           x_user_defined.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---webencodings-0.5.1.dist-info
¦   ¦       ¦       DESCRIPTION.rst
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       METADATA
¦   ¦       ¦       metadata.json
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---werkzeug
¦   ¦       ¦   ¦   datastructures.py
¦   ¦       ¦   ¦   datastructures.pyi
¦   ¦       ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   formparser.py
¦   ¦       ¦   ¦   http.py
¦   ¦       ¦   ¦   local.py
¦   ¦       ¦   ¦   py.typed
¦   ¦       ¦   ¦   security.py
¦   ¦       ¦   ¦   serving.py
¦   ¦       ¦   ¦   test.py
¦   ¦       ¦   ¦   testapp.py
¦   ¦       ¦   ¦   urls.py
¦   ¦       ¦   ¦   user_agent.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   wsgi.py
¦   ¦       ¦   ¦   _internal.py
¦   ¦       ¦   ¦   _reloader.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---debug
¦   ¦       ¦   ¦   ¦   console.py
¦   ¦       ¦   ¦   ¦   repr.py
¦   ¦       ¦   ¦   ¦   tbtools.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---shared
¦   ¦       ¦   ¦   ¦       console.png
¦   ¦       ¦   ¦   ¦       debugger.js
¦   ¦       ¦   ¦   ¦       ICON_LICENSE.md
¦   ¦       ¦   ¦   ¦       less.png
¦   ¦       ¦   ¦   ¦       more.png
¦   ¦       ¦   ¦   ¦       style.css
¦   ¦       ¦   ¦   ¦       
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           console.cpython-38.pyc
¦   ¦       ¦   ¦           repr.cpython-38.pyc
¦   ¦       ¦   ¦           tbtools.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---middleware
¦   ¦       ¦   ¦   ¦   dispatcher.py
¦   ¦       ¦   ¦   ¦   http_proxy.py
¦   ¦       ¦   ¦   ¦   lint.py
¦   ¦       ¦   ¦   ¦   profiler.py
¦   ¦       ¦   ¦   ¦   proxy_fix.py
¦   ¦       ¦   ¦   ¦   shared_data.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           dispatcher.cpython-38.pyc
¦   ¦       ¦   ¦           http_proxy.cpython-38.pyc
¦   ¦       ¦   ¦           lint.cpython-38.pyc
¦   ¦       ¦   ¦           profiler.cpython-38.pyc
¦   ¦       ¦   ¦           proxy_fix.cpython-38.pyc
¦   ¦       ¦   ¦           shared_data.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---routing
¦   ¦       ¦   ¦   ¦   converters.py
¦   ¦       ¦   ¦   ¦   exceptions.py
¦   ¦       ¦   ¦   ¦   map.py
¦   ¦       ¦   ¦   ¦   matcher.py
¦   ¦       ¦   ¦   ¦   rules.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           converters.cpython-38.pyc
¦   ¦       ¦   ¦           exceptions.cpython-38.pyc
¦   ¦       ¦   ¦           map.cpython-38.pyc
¦   ¦       ¦   ¦           matcher.cpython-38.pyc
¦   ¦       ¦   ¦           rules.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---sansio
¦   ¦       ¦   ¦   ¦   http.py
¦   ¦       ¦   ¦   ¦   multipart.py
¦   ¦       ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   response.py
¦   ¦       ¦   ¦   ¦   utils.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           http.cpython-38.pyc
¦   ¦       ¦   ¦           multipart.cpython-38.pyc
¦   ¦       ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦           response.cpython-38.pyc
¦   ¦       ¦   ¦           utils.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---wrappers
¦   ¦       ¦   ¦   ¦   request.py
¦   ¦       ¦   ¦   ¦   response.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           request.cpython-38.pyc
¦   ¦       ¦   ¦           response.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           datastructures.cpython-38.pyc
¦   ¦       ¦           exceptions.cpython-38.pyc
¦   ¦       ¦           formparser.cpython-38.pyc
¦   ¦       ¦           http.cpython-38.pyc
¦   ¦       ¦           local.cpython-38.pyc
¦   ¦       ¦           security.cpython-38.pyc
¦   ¦       ¦           serving.cpython-38.pyc
¦   ¦       ¦           test.cpython-38.pyc
¦   ¦       ¦           testapp.cpython-38.pyc
¦   ¦       ¦           urls.cpython-38.pyc
¦   ¦       ¦           user_agent.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           wsgi.cpython-38.pyc
¦   ¦       ¦           _internal.cpython-38.pyc
¦   ¦       ¦           _reloader.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---Werkzeug-2.2.2.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---wtforms
¦   ¦       ¦   ¦   form.py
¦   ¦       ¦   ¦   i18n.py
¦   ¦       ¦   ¦   meta.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   validators.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---csrf
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   session.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           session.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---fields
¦   ¦       ¦   ¦   ¦   choices.py
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   datetime.py
¦   ¦       ¦   ¦   ¦   form.py
¦   ¦       ¦   ¦   ¦   list.py
¦   ¦       ¦   ¦   ¦   numeric.py
¦   ¦       ¦   ¦   ¦   simple.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           choices.cpython-38.pyc
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           datetime.cpython-38.pyc
¦   ¦       ¦   ¦           form.cpython-38.pyc
¦   ¦       ¦   ¦           list.cpython-38.pyc
¦   ¦       ¦   ¦           numeric.cpython-38.pyc
¦   ¦       ¦   ¦           simple.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---locale
¦   ¦       ¦   ¦   ¦   README.md
¦   ¦       ¦   ¦   ¦   wtforms.pot
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---ar
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---bg
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ca
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---cs_CZ
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---cy
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---de
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---de_CH
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---el
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---en
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---es
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---et
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---fa
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---fi
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---fr
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---he
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---hu
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---it
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ja
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ko
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---nb
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---nl
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pl
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---pt
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---ru
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---sk
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---sv
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---tr
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---uk
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---zh
¦   ¦       ¦   ¦   ¦   +---LC_MESSAGES
¦   ¦       ¦   ¦   ¦           wtforms.mo
¦   ¦       ¦   ¦   ¦           wtforms.po
¦   ¦       ¦   ¦   ¦           
¦   ¦       ¦   ¦   +---zh_TW
¦   ¦       ¦   ¦       +---LC_MESSAGES
¦   ¦       ¦   ¦               wtforms.mo
¦   ¦       ¦   ¦               wtforms.po
¦   ¦       ¦   ¦               
¦   ¦       ¦   +---widgets
¦   ¦       ¦   ¦   ¦   core.py
¦   ¦       ¦   ¦   ¦   __init__.py
¦   ¦       ¦   ¦   ¦   
¦   ¦       ¦   ¦   +---__pycache__
¦   ¦       ¦   ¦           core.cpython-38.pyc
¦   ¦       ¦   ¦           __init__.cpython-38.pyc
¦   ¦       ¦   ¦           
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           form.cpython-38.pyc
¦   ¦       ¦           i18n.cpython-38.pyc
¦   ¦       ¦           meta.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           validators.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---WTForms-3.0.1.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE.rst
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---yagmail
¦   ¦       ¦   ¦   compat.py
¦   ¦       ¦   ¦   dkim.py
¦   ¦       ¦   ¦   error.py
¦   ¦       ¦   ¦   headers.py
¦   ¦       ¦   ¦   log.py
¦   ¦       ¦   ¦   message.py
¦   ¦       ¦   ¦   oauth2.py
¦   ¦       ¦   ¦   password.py
¦   ¦       ¦   ¦   sender.py
¦   ¦       ¦   ¦   utils.py
¦   ¦       ¦   ¦   validate.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   __main__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           compat.cpython-38.pyc
¦   ¦       ¦           dkim.cpython-38.pyc
¦   ¦       ¦           error.cpython-38.pyc
¦   ¦       ¦           headers.cpython-38.pyc
¦   ¦       ¦           log.cpython-38.pyc
¦   ¦       ¦           message.cpython-38.pyc
¦   ¦       ¦           oauth2.cpython-38.pyc
¦   ¦       ¦           password.cpython-38.pyc
¦   ¦       ¦           sender.cpython-38.pyc
¦   ¦       ¦           utils.cpython-38.pyc
¦   ¦       ¦           validate.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           __main__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---yagmail-0.15.293.dist-info
¦   ¦       ¦       entry_points.txt
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---zipp
¦   ¦       ¦   ¦   py310compat.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           py310compat.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---zipp-3.11.0.dist-info
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       LICENSE
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       REQUESTED
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       
¦   ¦       +---zopfli
¦   ¦       ¦   ¦   gzip.py
¦   ¦       ¦   ¦   png.py
¦   ¦       ¦   ¦   zlib.py
¦   ¦       ¦   ¦   zopfli.cp38-win_amd64.pyd
¦   ¦       ¦   ¦   _version.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           gzip.cpython-38.pyc
¦   ¦       ¦           png.cpython-38.pyc
¦   ¦       ¦           zlib.cpython-38.pyc
¦   ¦       ¦           _version.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---zopfli-0.2.2.dist-info
¦   ¦       ¦       COPYING
¦   ¦       ¦       INSTALLER
¦   ¦       ¦       METADATA
¦   ¦       ¦       RECORD
¦   ¦       ¦       top_level.txt
¦   ¦       ¦       WHEEL
¦   ¦       ¦       zip-safe
¦   ¦       ¦       
¦   ¦       +---_distutils_hack
¦   ¦       ¦   ¦   override.py
¦   ¦       ¦   ¦   __init__.py
¦   ¦       ¦   ¦   
¦   ¦       ¦   +---__pycache__
¦   ¦       ¦           override.cpython-38.pyc
¦   ¦       ¦           __init__.cpython-38.pyc
¦   ¦       ¦           
¦   ¦       +---__pycache__
¦   ¦               brotli.cpython-38.pyc
¦   ¦               flask_bcrypt.cpython-38.pyc
¦   ¦               flask_principal.cpython-38.pyc
¦   ¦               pkgutil_resolve_name.cpython-38.pyc
¦   ¦               six.cpython-38.pyc
¦   ¦               _pyrsistent_version.cpython-38.pyc
¦   ¦               
¦   +---Scripts
¦   ¦       activate
¦   ¦       activate.bat
¦   ¦       Activate.ps1
¦   ¦       celery.exe
¦   ¦       csscapture.exe
¦   ¦       csscombine.exe
¦   ¦       cssparse.exe
¦   ¦       deactivate.bat
¦   ¦       email_validator.exe
¦   ¦       f2py.exe
¦   ¦       flask.exe
¦   ¦       fonttools.exe
¦   ¦       imageio_download_bin.exe
¦   ¦       imageio_remove_bin.exe
¦   ¦       jsonschema.exe
¦   ¦       normalizer.exe
¦   ¦       pip.exe
¦   ¦       pip3.8.exe
¦   ¦       pip3.exe
¦   ¦       pyftmerge.exe
¦   ¦       pyftsubset.exe
¦   ¦       python.exe
¦   ¦       pythonw.exe
¦   ¦       ttx.exe
¦   ¦       weasyprint.exe
¦   ¦       yagmail.exe
¦   ¦       
¦   +---share
¦       +---man
¦           +---man1
¦                   ttx.1
¦                   
+---application
¦   ¦   api.py
¦   ¦   cache.py
¦   ¦   config.py
¦   ¦   controllers.py
¦   ¦   dataaccess.py
¦   ¦   database.py
¦   ¦   models.py
¦   ¦   myfunctions.py
¦   ¦   tasks.py
¦   ¦   validation.py
¦   ¦   workers.py
¦   ¦   __init__.py
¦   ¦   
¦   +---__pycache__
¦           api.cpython-310.pyc
¦           api.cpython-38.pyc
¦           cache.cpython-310.pyc
¦           cache.cpython-38.pyc
¦           config.cpython-310.pyc
¦           config.cpython-38.pyc
¦           controllers.cpython-310.pyc
¦           controllers.cpython-38.pyc
¦           dataaccess.cpython-310.pyc
¦           dataaccess.cpython-38.pyc
¦           database.cpython-310.pyc
¦           database.cpython-38.pyc
¦           models.cpython-310.pyc
¦           models.cpython-38.pyc
¦           myfunctions.cpython-310.pyc
¦           myfunctions.cpython-38.pyc
¦           tasks.cpython-310.pyc
¦           tasks.cpython-38.pyc
¦           validation.cpython-310.pyc
¦           validation.cpython-38.pyc
¦           workers.cpython-310.pyc
¦           workers.cpython-38.pyc
¦           __init__.cpython-310.pyc
¦           __init__.cpython-38.pyc
¦           
+---db_directory
¦       bloglitedb.sqlite3
¦       
+---static
¦   ¦   add_edit_post.css
¦   ¦   followers-following.css
¦   ¦   header.css
¦   ¦   home.css
¦   ¦   profile.css
¦   ¦   search.css
¦   ¦   signup.css
¦   ¦   style.css
¦   ¦   
¦   +---bootstrap
¦   ¦   +---css
¦   ¦   ¦       bootstrap-grid.css
¦   ¦   ¦       bootstrap-grid.css.map
¦   ¦   ¦       bootstrap-grid.min.css
¦   ¦   ¦       bootstrap-grid.min.css.map
¦   ¦   ¦       bootstrap-grid.rtl.css
¦   ¦   ¦       bootstrap-grid.rtl.css.map
¦   ¦   ¦       bootstrap-grid.rtl.min.css
¦   ¦   ¦       bootstrap-grid.rtl.min.css.map
¦   ¦   ¦       bootstrap-reboot.css
¦   ¦   ¦       bootstrap-reboot.css.map
¦   ¦   ¦       bootstrap-reboot.min.css
¦   ¦   ¦       bootstrap-reboot.min.css.map
¦   ¦   ¦       bootstrap-reboot.rtl.css
¦   ¦   ¦       bootstrap-reboot.rtl.css.map
¦   ¦   ¦       bootstrap-reboot.rtl.min.css
¦   ¦   ¦       bootstrap-reboot.rtl.min.css.map
¦   ¦   ¦       bootstrap-utilities.css
¦   ¦   ¦       bootstrap-utilities.css.map
¦   ¦   ¦       bootstrap-utilities.min.css
¦   ¦   ¦       bootstrap-utilities.min.css.map
¦   ¦   ¦       bootstrap-utilities.rtl.css
¦   ¦   ¦       bootstrap-utilities.rtl.css.map
¦   ¦   ¦       bootstrap-utilities.rtl.min.css
¦   ¦   ¦       bootstrap-utilities.rtl.min.css.map
¦   ¦   ¦       bootstrap.css
¦   ¦   ¦       bootstrap.css.map
¦   ¦   ¦       bootstrap.min.css
¦   ¦   ¦       bootstrap.min.css.map
¦   ¦   ¦       bootstrap.rtl.css
¦   ¦   ¦       bootstrap.rtl.css.map
¦   ¦   ¦       bootstrap.rtl.min.css
¦   ¦   ¦       bootstrap.rtl.min.css.map
¦   ¦   ¦       
¦   ¦   +---js
¦   ¦           bootstrap.bundle.js
¦   ¦           bootstrap.bundle.js.map
¦   ¦           bootstrap.bundle.min.js
¦   ¦           bootstrap.bundle.min.js.map
¦   ¦           bootstrap.esm.js
¦   ¦           bootstrap.esm.js.map
¦   ¦           bootstrap.esm.min.js
¦   ¦           bootstrap.esm.min.js.map
¦   ¦           bootstrap.js
¦   ¦           bootstrap.js.map
¦   ¦           bootstrap.min.js
¦   ¦           bootstrap.min.js.map
¦   ¦           
¦   +---images
¦   ¦       blank-profile-picture.png
¦   ¦       blogliteimg.png
¦   ¦       no-image-selected.jpg
¦   ¦       
¦   +---js
¦           custom_validations.js
¦           like_post.js
¦           signup_validations.js
¦           
+---templates
¦       addpost.html
¦       archived_posts.html
¦       base.html
¦       edit_post.html
¦       edit_profile.html
¦       error.html
¦       home.html
¦       index.html
¦       monthly_report.html
¦       profile.html
¦       search.html
¦       search_response.html
¦       session_expired.html
¦       signup.html
¦       test.html
¦       view_followers.html
¦       view_following.html
¦       view_post.html
¦       view_profile.html
¦       
+---__pycache__
        main.cpython-310.pyc
        

```