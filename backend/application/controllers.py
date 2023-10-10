from flask import Flask, request, jsonify, json
from flask import render_template
from flask import current_app as app
from application.models import *
from application.myfunctions import getcurrentformatteddatetime
import datetime

# @app.route('/')
# def index():
#     return "<h1>Hello World..</h1>"

@app.route('/monthly_report/<username>')
def monthly_report_test(username):
    last_month = (datetime.datetime.now() - datetime.timedelta(days=31)).strftime("%d/%m/%Y %H:%M:%S")
    users = User.query.all()
    usernames = {}
    for user in users:
        usernames[user.id] = user.username
        
    

    user = User.query.filter_by(username = username).first()
    
    labels = [post.post_name for post in user.userposts]
    no_likes = [len(post.likes)  for post in user.userposts]
    return render_template('monthly_report.html', user = user, usernames = usernames, labels = json.dumps(labels), data1=json.dumps(no_likes))


@app.route('/daily_remainder_test')
def daily_remainder_test():
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S")

    users = User.query.all()
    visited = {}
    for user in users:
        visited_flag = False
        for post in user.userposts:
            if post.updated_date >= yesterday:
                visited_flag = True
                break
                
        if visited_flag == False:
            for comment in user.comments:
                if comment.created_date >= yesterday:
                    visited_flag = True
                    break
        
        if visited_flag == False:
            for like in user.likes:
                if like.created_date >= yesterday:
                    visited_flag = True
                    break
        
            
        visited[user.email] = visited_flag
    return jsonify(visited)