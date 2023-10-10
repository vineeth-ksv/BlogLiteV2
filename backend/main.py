import os
from flask import Flask
from flask_restful import Resource, Api
from flask_security import Security, SQLAlchemyUserDatastore
from application import config, workers
from application.config import LocalDevelopmentConfig
from application.database import db
from application.models import User, Role
from flask_cors import CORS

app = None
api = None
celery = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    IMAGES_FOLDER = os.path.join('static', 'images')
    app.config['IMAGES_FOLDER'] = IMAGES_FOLDER

    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # Initialize Celery
    celery = workers.celery
    celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        result_backend=app.config["CELERY_RESULT_BACKEND"],
    )
    celery.Task = workers.ContextTask
    app.app_context().push()

    api = Api(app)
    app.app_context().push()

    CORS(app, supports_credentials=True)
    app.config['CORS_HEADERS'] = 'application/json'
    
    return app, api, celery

app, api, celery = create_app()
app.secret_key = os.urandom(24)

# Import all the controllers so they are loaded
from application.controllers import *

# Import all tasks
from application.tasks import *

# Add all restful controllers
from application.api import *

api.add_resource(UserAPI, "/api/<email>", "/api/register", '/api/delete_profile', '/api/edit_profile')
api.add_resource(UserProfileAPI, "/api/profile/<username>")
api.add_resource(ConnectionsAPI, '/api/connections/<username>')
api.add_resource(FeedAPI, '/api/feed/<username>')
api.add_resource(BlogAPI,  '/api/post/<post_id>' ,'/api/addpost', '/api/edit_post' ,'/api/delete_post')
api.add_resource(LikeAPI, '/api/toggle_like')
api.add_resource(CommentAPI, '/api/add_comment', '/api/delete_comment')
api.add_resource(ArchiveBlog, '/api/archive_post', '/api/<username>/archived_posts')
api.add_resource(FollowUnfollowAPI, '/api/follow', '/api/unfollow', '/api/remove_follower')
api.add_resource(SearchAPI, "/api/search")
api.add_resource(ExportBlogsAPI, '/api/export_blogs/<username>')

api.add_resource(TestAPI, '/api/test')

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=5555, debug=True)
