from flask_restful import Resource, Api
from flask_restful import fields, marshal
from flask_restful import reqparse
from application.validation import *
from application.myfunctions import getcurrentformatteddatetime, validPassword
from application.models import *
from application.database import db
from flask import abort
from flask_security import auth_required
import random
import string
import csv
from flask import current_app as app
import yagmail
from flask import send_file

comment = fields.Nested({
    "comment_id": fields.Integer,
    "user_id": fields.Integer,
    "post_id": fields.Integer,
    "text": fields.String,
    "created_date": fields.String,
    "username": fields.String
})

like = fields.Nested({
    "like_id": fields.Integer,
    "user_id": fields.Integer,
    "post_id": fields.Integer,
    "created_date": fields.String
})

followers = fields.Nested({
    "user_id": fields.Integer,
    "follower_id": fields.Integer
})

following = fields.Nested({
    "user_id": fields.Integer,
    "following_id": fields.Integer
})

userposts = fields.List(fields.Nested({
    "post_id" : fields.Integer,
    "user_id" : fields.Integer,
    "username" : fields.String,
    "post_name" : fields.String,
    "post_caption" : fields.String,
    "post_img": fields.String,
    "img_filename" : fields.String,
    "created_date" : fields.String,
    "updated_date" : fields.String,
    "isArchive" : fields.Boolean,
    "likes" : fields.List(like),
    "comments": fields.List(comment)
}))

user_profile_output = {
    "id" : fields.Integer,
    "username" : fields.String,
    "fullname" : fields.String,
    "email" : fields.String,
    "mobile_number": fields.Integer,
    "userposts" : userposts,
    "followers_list": followers,
    "following_list": following
}


user_output = {
    "id" : fields.Integer,
    "username" : fields.String,
    "fullname": fields.String,
    "email" : fields.String,
    "mobile_number" : fields.Integer,
}

update_user_output = {
    "user_id" : fields.Integer,
    "username" : fields.String,
    "fullname": fields.String(attribute="name"),
    "email" : fields.String,
    "mobile_number" : fields.Integer
}

archived_posts_output = {
    "archived_posts": userposts
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument("email")
create_user_parser.add_argument("mobile")
create_user_parser.add_argument("name")
create_user_parser.add_argument("username")
create_user_parser.add_argument("password")

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument("email")
update_user_parser.add_argument("mobile_number")
update_user_parser.add_argument("full_name")

comments = fields.List(fields.Nested({
    "comment_id": fields.Integer,
    "user_id": fields.Integer,
    "post_id": fields.Integer,
    "comment_text": fields.String(attribute="text"),
    "comment_date": fields.String(attribute="created_date")
}))

likes = fields.List(fields.Nested({
    "like_id": fields.Integer,
    "user_id": fields.Integer,
    "post_id": fields.Integer,
    "liked_date": fields.String(attribute="created_date")
}))

blog_output = {
    "user_id" : fields.Integer,
    "username" : fields.String,
    "blog_id" : fields.Integer(attribute="post_id"),
    "blog_name" : fields.String(attribute="post_name"),
    "blog_caption" : fields.String(attribute="post_caption"),
    "is_archive": fields.Boolean(attribute="isArchive"),
    "comments": comments,
    "likes": likes
}

followers2 = fields.List(fields.Nested({
    "user_id": fields.Integer,
    "follower_id": fields.Integer,
    "follower_name": fields.String
}))

following2 = fields.List(fields.Nested({
    "user_id": fields.Integer,
    "following_id": fields.Integer,
    "following_name": fields.String
}))

connections_output = {
    "followers": followers2,
    "followings": following2
}



create_blog_parser = reqparse.RequestParser()
create_blog_parser.add_argument("username", type=str, required=True)
create_blog_parser.add_argument("blogName", type=str, required=True)
create_blog_parser.add_argument("blogDescription", type=str, required=True)
create_blog_parser.add_argument("blogImage", type=str, required=True)
create_blog_parser.add_argument("imageName", type=str, required=True)

update_blog_parser = reqparse.RequestParser()
update_blog_parser.add_argument("username", type=str)
update_blog_parser.add_argument("blogId", required=True)
update_blog_parser.add_argument("blogName", type=str)
update_blog_parser.add_argument("blogDescription", type=str)
update_blog_parser.add_argument("blogImage", type=str)
update_blog_parser.add_argument("imageName", type=str)

user_login = reqparse.RequestParser()
user_login.add_argument("email")

edit_profile_parser = reqparse.RequestParser()
edit_profile_parser.add_argument("username")
edit_profile_parser.add_argument("fullname")
edit_profile_parser.add_argument("mobile_number")

delete_profile_parser = reqparse.RequestParser()
delete_profile_parser.add_argument("username")

search_user_parser = reqparse.RequestParser()
search_user_parser.add_argument("query")
search_user_parser.add_argument("search_by")

archive_blog_parser = reqparse.RequestParser()
archive_blog_parser.add_argument("username")
archive_blog_parser.add_argument("postId")

delete_blog_parser = reqparse.RequestParser()
delete_blog_parser.add_argument("username")
delete_blog_parser.add_argument("postId")

follow_parser = reqparse.RequestParser()
follow_parser.add_argument("user_id")
follow_parser.add_argument("follow_id")
follow_parser.add_argument("follow_username")

unfollow_parser = reqparse.RequestParser()
unfollow_parser.add_argument("user_id")
unfollow_parser.add_argument("unfollow_id")
unfollow_parser.add_argument("unfollow_username")

remove_follower_parser = reqparse.RequestParser()
remove_follower_parser.add_argument("follower_username")
remove_follower_parser.add_argument("user_id")
remove_follower_parser.add_argument("follower_id")

like_parser = reqparse.RequestParser()
like_parser.add_argument("user_id")
like_parser.add_argument("post_id")

comment_parser = reqparse.RequestParser()
comment_parser.add_argument("user_id")
comment_parser.add_argument("post_id")
comment_parser.add_argument("comment")

delete_comment_parser = reqparse.RequestParser()
delete_comment_parser.add_argument("comment_id")

class User_Data():
    def __init__(self, user_id, username, name, email, mobile_number, no_of_posts, followers, following):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.no_of_posts = no_of_posts
        self.followers = followers
        self.following = following


class UserAPI(Resource):
    @auth_required('token')
    def get(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            return marshal(user, user_output)
        return marshal({"msg": "user not found.."}, test_api_resource_fields)

    def post(self):
        args = create_user_parser.parse_args()
        email = args.get("email", None)
        mobile_number = args.get("mobile", None)
        fullname = args.get("name", None)
        username = args.get("username", None)
        password = args.get("password", None)

        if email is None or email == "":
            raise BusinessValidationError(status_code=400, error_code = "BE1001", error_message = "Email is required")
        
        if mobile_number is None or mobile_number == "":
            raise BusinessValidationError(status_code=400, error_code="BE1002", error_message="Mobile Number is required")
        
        if fullname is None or fullname == "":
            raise BusinessValidationError(status_code=400, error_code="BE1003", error_message="Full Name is required")
        
        if username is None or username == "":
            raise BusinessValidationError(status_code=400, error_code="BE1004", error_message="Username is required")
        
        if password is None or password == "":
            raise BusinessValidationError(status_code=400, error_code="BE1005", error_message="Password is required")
        
        if ('@' not in email) or (email[-4:] != ".com" and email[-6:]!=".co.in"):
            raise BusinessValidationError(status_code=400, error_code="BE1006", error_message="Invalid Email")
        
        if len(str(mobile_number))!=10:
            raise BusinessValidationError(status_code=400, error_code="BE1007", error_message="Invalid Mobile Number")
        
        if not validPassword(password):
            raise BusinessValidationError(status_code=400, error_code="BE1008", error_message="Password must have 8-16 characters, a capital letter, small letter, number & special character[!@#$%_]")

        duplicate_user = User.query.filter((User.email == email) | (User.mobile_number == mobile_number) | (User.username == username)).first()
        if duplicate_user:
            raise BusinessValidationError(status_code=400, error_code="BE1009", error_message="User already exists.")
        
        try:
            created_date = getcurrentformatteddatetime()
            active = True
            fs_uniquifier = ''.join(random.choices(string.ascii_letters,k=32))
            new_user = User(email = email, mobile_number = mobile_number, fullname = fullname, username = username, 
                            password = password, created_date = created_date, updated_date = created_date,
                            active = active,fs_uniquifier = fs_uniquifier)
            db.session.add(new_user)
            
        
        except Exception as e:
            print(e)
            return "Oops! There's an error. Could not register the user.", 500
        
        else:
            db.session.commit()
            return "User registered successfully", 200

    @auth_required('token')    
    def delete(self):
        args = delete_profile_parser.parse_args()
        username = args.get("username", None)
        user = User.query.filter_by(username = username).first()

        if user:
            try:
                db.session.delete(user)
                db.session.commit()

            except Exception as e:
                db.session.rollback()
                return marshal({"msg": "Could not delete the profile. Please try later.."}, test_api_resource_fields)
            
            else:
                return marshal({"msg": "Profile deleted successfully.."}, test_api_resource_fields)

        return marshal({"msg": "user not found.."}, test_api_resource_fields)
    
    @auth_required('token')
    def put(self):
        print("editing profile...")
        args = edit_profile_parser.parse_args()
        username = args.get("username", None)
        fullname = args.get("fullname", None)
        mobile_number = args.get("mobile_number", None)

        user = User.query.filter_by(username = username).first()
        if user:
            if fullname!="" and fullname!=None and fullname != user.fullname:
                user.fullname = fullname
            
            if mobile_number!="" and mobile_number!=None and mobile_number != user.mobile_number:
                user.mobile_number = mobile_number
            
            db.session.commit()
            return marshal(user, user_output)
        return marshal({"msg": "user not found.."}, test_api_resource_fields)

class UserProfileAPI(Resource):
    @auth_required('token')
    def get(self, username):
        user = User.query.filter_by(username = username).first()

        if user:
            profile_userposts = UserPosts.query.filter_by(user_id = user.id, isArchive = False).all()
            user.userposts = profile_userposts

            return { 'profiledata': user.to_dict() }
            # return marshal(user, user_profile_output)
        return marshal({"msg": "user not found.."}, test_api_resource_fields)
    
class ConnectionsAPI(Resource):
    @auth_required('token')
    def get(self, username):
        user = User.query.filter_by(username = username).first()

        if user:
            followers, followings = [], []
            for follower in user.followers_list:
                follower_user = User.query.filter_by(id=follower.follower_id).first()  
                followers.append({
                    "user_id": follower.user_id,
                    "follower_id": follower.follower_id,
                    "follower_name": follower_user.username
                })

            for following in user.following_list:
                following_user = User.query.filter_by(id=following.following_id).first()                
                followings.append({
                    "user_id": following.user_id,
                    "following_id": following.following_id,
                    "following_name": following_user.username
                })

            response_data = {
                "followers": followers,
                "followings": followings
            }

            return marshal(response_data, connections_output)

        return marshal({"msg": "user not found.."}, test_api_resource_fields)

class FeedAPI(Resource):
    @auth_required('token')
    def get(self, username):
        user = User.query.filter_by(username = username).first()
        # following_list = Following_List.query.filter_by(user_id = user.user_id).all()
        if user:
            if user.following_list!= []:
                following_ids = [user.id]
                for following in user.following_list:
                    following_ids.append(following.following_id)
                
                feed = UserPosts.query.filter(UserPosts.user_id.in_(following_ids)).filter_by(isArchive = False).order_by(UserPosts.updated_date.desc()).all()
            else:
                feed = UserPosts.query.filter_by(user_id = user.id).filter_by(isArchive = False).order_by(UserPosts.updated_date.desc()).all()

            return {'feed': [post.to_dict() for post in feed]}, 200
        
        else:
            return marshal({"msg": "user not found.."}, test_api_resource_fields)

class BlogAPI(Resource):
    @auth_required('token')
    def get(self, post_id):
        pass

    @auth_required('token')
    def put(self):
        print("updating post...")
        args = update_blog_parser.parse_args()
        username = args.get("username", None)
        post_id =  args.get("blogId", None)
        post_name = args.get("blogName", None)
        post_caption = args.get("blogDescription", None)
        post_img = args.get("blogImage", None)
        img_filename = args.get("imageName", None)
        
        updated_date = getcurrentformatteddatetime()

        user = User.query.filter_by(username = username).first()
        if not user:
            return {'message' : 'User not found.'}, 400
        
        try:
            post = UserPosts.query.filter_by(post_id = post_id).first()
            if post_name!="" and post_name != post.post_name:
                post.post_name = post_name
                post.updated_date = updated_date

            if post_caption != post.post_caption:
                post.post_caption = post_caption
                post.updated_date = updated_date
            
            # if img_filename!='':
            if post_img != post.post_img:
                post.post_img = post_img
                post.img_filename = img_filename
                mimetype = "image/"+img_filename.split(".")[-1]
                post.mimetype = mimetype
                post.updated_date = updated_date
            
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
            print(e)
            return {'message': 'Sorry, could not upload the blog'}, 400
        
        else:
            profile_userposts = UserPosts.query.filter_by(user_id = user.id, isArchive = False).all()
            user.userposts = profile_userposts
            return marshal(user, user_profile_output)

    @auth_required('token')
    def post(self):
        args = create_blog_parser.parse_args()
        username = args.get("username", None)
        post_name = args.get("blogName", None)
        post_caption = args.get("blogDescription", None)
        post_img = args.get("blogImage", None)
        img_filename = args.get("imageName", None)
        mimetype = "image/"+img_filename.split(".")[-1]
        created_date = getcurrentformatteddatetime()

        user = User.query.filter_by(username = username).first()
        if not user:
            return {'message' : 'User not found.'}, 400
        
        try:
            new_post = UserPosts(user_id = user.id, username = username, post_img = post_img, img_filename = img_filename, 
                                 mimetype = mimetype, post_name = post_name, post_caption = post_caption, 
                                 created_date = created_date, updated_date = created_date)
            
            db.session.add(new_post)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(e)
            return {'message': 'Sorry, could not upload the blog'}, 400

        return {'message': 'Blog created successfully.'}, 200 

    @auth_required('token')
    def delete(self):
        print("deleting post")
        args = delete_blog_parser.parse_args()
        username = args.get("username", None)
        post_id = args.get("postId", None)

        try:
            post = UserPosts.query.filter_by(post_id = post_id).first()
            db.session.delete(post)
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
        
        else:
            user = User.query.filter_by(username = username).first()
            if user:
                profile_userposts = UserPosts.query.filter_by(user_id = user.id, isArchive = False).all()
                user.userposts = profile_userposts
                return marshal(user, user_profile_output)

class LikeAPI(Resource):
    @auth_required('token')
    def put(self):
        args = like_parser.parse_args()
        user_id = args.get("user_id", None)
        post_id = args.get("post_id", None)

        post = UserPosts.query.filter_by(post_id = post_id).first()

        if not post:
            return marshal({"msg":"Post does not exists.."}, test_api_resource_fields)

        like = Likes.query.filter_by(user_id=user_id, post_id=post_id).first()

        if like:
            try:
                db.session.delete(like)
                db.session.commit()
            
            except Exception as e:
                db.session.rollback()
                return marshal({"msg":"Could not unlike the post.."}, test_api_resource_fields)
            
            else:
                return marshal({"msg":"Unliked the post successfully..."}, test_api_resource_fields)
        else:
            try:
                new_like = Likes(user_id = user_id, post_id = post_id, created_date = getcurrentformatteddatetime())
                db.session.add(new_like)
                db.session.commit()
        
            except Exception as e:
                db.session.rollback()
                return marshal({"msg":"Could not like the post.."}, test_api_resource_fields)

            else:
                return marshal({"msg":"Liked the post successfully..."}, test_api_resource_fields)

class CommentAPI(Resource):
    @auth_required('token')
    def post(self):
        args = comment_parser.parse_args()
        user_id = args.get("user_id", None)
        post_id = args.get("post_id", None)
        text = args.get("comment", None)

        post = UserPosts.query.filter_by(post_id = post_id).first()

        if not post:
            return marshal({"msg":"Post does not exists.."}, test_api_resource_fields)
        
        try:
            new_comment = Comments(user_id = user_id, post_id = post_id, text = text, created_date = getcurrentformatteddatetime())
            db.session.add(new_comment)
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
            return marshal({"msg":"Could not add comment on the post.."}, test_api_resource_fields)

        else:
            return marshal({"msg":"Commented the post successfully..."}, test_api_resource_fields)

    @auth_required('token')
    def delete(self):
        args = delete_comment_parser.parse_args()
        comment_id = args.get("comment_id", None)

        if comment_id:
            comment = Comments.query.filter_by(comment_id=comment_id).first()
            if comment:
                try:
                    db.session.delete(comment)
                    db.session.commit()
                
                except Exception as e:
                    db.session.rollback()
                    return marshal({"msg":"Could not delete the comment.."}, test_api_resource_fields)
                
                else:
                    return marshal({"msg":"Comment deleted successfully..."}, test_api_resource_fields)
            else:
                return marshal({"msg":"Comment not found..."}, test_api_resource_fields)
        else:
            return marshal({"msg":"Could not delete the comment.."}, test_api_resource_fields)


class ArchiveBlog(Resource):
    @auth_required('token')
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            archived_posts = UserPosts.query.filter_by(user_id = user.id, isArchive = True).all()
            print(archived_posts)
            return marshal({"archived_posts" : archived_posts}, archived_posts_output)
        
        return {'message' : 'User not found.'}, 400
        
    @auth_required('token')
    def put(self):
        print("archiving post")
        args = archive_blog_parser.parse_args()
        username = args.get("username", None)
        post_id = args.get("postId", None)

        try:
            post = UserPosts.query.filter_by(post_id = post_id).first()
            if post.isArchive == True:
                post.isArchive = False
            else:
                post.isArchive = True
            db.session.commit()

        except Exception as e:
            db.session.rollback()

        else:
            user = User.query.filter_by(username = username).first()
            if user:
                profile_userposts = UserPosts.query.filter_by(user_id = user.id, isArchive = False).all()
                user.userposts = profile_userposts
                return marshal(user, user_profile_output)


class FollowUnfollowAPI(Resource):
    @auth_required('token')
    def post(self):
        args = follow_parser.parse_args()
        user_id = args.get("user_id", None)
        follow_id = args.get("follow_id", None)
        follow_username = args.get("follow_username", None)
        try:
            following = Following_List(user_id = user_id, following_id = follow_id)
            follower = Followers_List(user_id = follow_id, follower_id = user_id)

            db.session.add(following)
            db.session.add(follower)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return marshal({"msg": f"Couldn't follow @{follow_username}..."}, test_api_resource_fields)
        
        else:
            return marshal({"msg": f"following @{follow_username}"}, test_api_resource_fields) 

    @auth_required('token')
    def put(self):
        args = unfollow_parser.parse_args()
        user_id = args.get("user_id", None)
        unfollow_id = args.get("unfollow_id", None)
        unfollow_username = args.get("unfollow_username", None)

        try:
            following = Following_List.query.filter_by(user_id = user_id).filter_by(following_id = unfollow_id).first()
            follower = Followers_List.query.filter_by(user_id = unfollow_id).filter_by(follower_id = user_id).first()

            db.session.delete(following)
            db.session.delete(follower)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return marshal({"msg": f"Couldn't unfollow @{unfollow_username}..."}, test_api_resource_fields)
        
        else:
            return marshal({"msg": f"unfollowed @{unfollow_username}"}, test_api_resource_fields) 
    
    @auth_required('token')
    def delete(self):
        args = remove_follower_parser.parse_args()
        follower_username = args.get("follower_username", None)
        user_id = args.get("user_id", None)
        follower_id = args.get("follower_id",  None)

        follower = Followers_List.query.filter_by(user_id = user_id, follower_id = follower_id).first()
        following = Following_List.query.filter_by(user_id = follower_id, following_id = user_id).first()
        
        if follower and following:
            try:
                db.session.delete(follower)
                db.session.delete(following)
                db.session.commit()
            
            except Exception as e:
                db.session.rollback()
                return marshal({"msg": f"Couldn't remove @{follower_username}..."}, test_api_resource_fields)
            
            else:
                return marshal({"msg": f"Removed @{follower_username} from followers!"}, test_api_resource_fields)
        else:
            return marshal({"msg": f"@{follower_username} not found in followers!"}, test_api_resource_fields)


class SearchAPI(Resource):
    @auth_required('token')
    def post(self):
        args = search_user_parser.parse_args()
        search_word = args.get("query", None)
        search_by = args.get("search_by", None)

        if search_word == None or search_word == "":
            search_users = []

        else:
            search = "%{}%".format(search_word)
            search_users = User.query.filter(User.username.like(search)).all()

        search_by_user = User.query.filter_by(username = search_by).first()


        return {'users': [user.to_dict() for user in search_users], 'following_ids': [f.following_id for f in search_by_user.following_list]}, 200


class ExportBlogsAPI(Resource):
    @auth_required('token')
    def get(self, username):
        user_posts = UserPosts.query.filter_by(username=username).all()
        data ={}
        data["posts"] = [posts.to_dict() for posts in user_posts]
        file_name = f"{username}_posts.csv"
        header = ["post_id", "user_id", "username", "post_name", "post_caption", "post_img", "created_date", "updated_date", "isArchive", "comments", "likes"]
        with open(file_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for post in data["posts"]:
                try:
                    writer.writerow(post)
                except Exception as e:
                    print(e)
            # current_time = datetime.utcnow()
            # time_window = current_time - timedelta(hours=24)
            try:
                app.config['YAGMAIL_USERNAME'] = 'madtwoproject@gmail.com'
                app.config['YAGMAIL_PASSWORD'] = 'dvclhvoyaazgqjqe'
                yag = yagmail.SMTP(app.config['YAGMAIL_USERNAME'], app.config['YAGMAIL_PASSWORD'])
                yag.send(to='saivineeth.ksv@gmail.com', subject="Export Posts", contents="Hi , Here is the export of your blogs. Thank you.",attachments=[file_name])
            except Exception as e:
                    print('Error sending email:', e)
        return send_file(file_name, as_attachment=True)


test_api_resource_fields = {
    'msg': fields.String,
}

class TestAPI(Resource):
    # @auth_required("Authentication-Token")
    def get(self):
        return marshal({"msg":"returned from Test API "}, test_api_resource_fields)
