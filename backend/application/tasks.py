import io
from application.workers import celery
from application.models import *
from celery.schedules import crontab
import yagmail
from flask import current_app as app, render_template, json
import datetime
from application.dataaccess import getAllUsers
import os
import pdfkit

# from weasyprint import HTML


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=18, minute=0), daily_reminder.s(), name='Daily Reminder at 6pm')
    sender.add_periodic_task(crontab(minute=0, hour=0, day_of_month=1), monthly_report.s(), name='At 00:00 on day-of-month 1')
    # sender.add_periodic_task(10.0, daily_reminder.s(), name='Daily Reminder for every 10 seconds')
    # sender.add_periodic_task(20.0, monthly_report.s(), name='Monthly remainder for every 20 seconds')
        


@celery.task()
def daily_reminder():
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S")

    users = User.query.all()

    for user in users:
        not_visited = True
        if len(user.userposts) > 0: 
            for post in user.userposts:
                if post.updated_date >= yesterday:
                    not_visited = False
                    break
                
        if not_visited == True and len(user.comments) > 0:
            for comment in user.comments:
                if comment.created_date >= yesterday:
                    not_visited = False
                    break
        
        if not_visited == True and len(user.likes) > 0:
            for like in user.likes:
                if like.created_date >= yesterday:
                    not_visited = False
                    break
        
        if not_visited:
            try:
                app.config['YAGMAIL_USERNAME'] = 'madtwoproject@gmail.com'
                app.config['YAGMAIL_PASSWORD'] = 'dvclhvoyaazgqjqe'
                
                subject = "Daily Remainder - Blog Lite"
                contents = f"Hi {user.username},\nIt looks like you haven't visited/posted anything in 24 hours.\nPlease visit BlogLite and visit/post something.\nThank you."

                yag = yagmail.SMTP(app.config['YAGMAIL_USERNAME'], app.config['YAGMAIL_PASSWORD'])
                yag.send(to=user.email, subject = subject, contents = contents)

            except Exception as e:
                print('Error sending email:', e)

            else:
                print(f"{user.username} not visited/posted in last 24 hours")
                print(f"daily reminder sent for {user.username}")
        else:
            print(f"{user.username} visited/posted in last 24 hours")
            pass
    
    return "Daily reminder mail's sent successfully.."

@celery.task()
def monthly_report():
    last_month = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%d/%m/%Y %H:%M:%S")
    
    users = User.query.all()
    usernames = {}
    for user in users:
        usernames[user.id] = user.username

        labels = [post.post_name for post in user.userposts]
        no_likes = [len(post.likes)  for post in user.userposts]

        html_template = render_template('monthly_report.html', user = user, usernames = usernames, labels = json.dumps(labels), data1=json.dumps(no_likes))
        pdf_content = pdfkit.from_string(html_template, False)

        pdf_file = io.BytesIO(pdf_content)
        pdf_file.seek(0)

        # Generate a unique filename for the PDF file
        filename = f"monthly_report-{user.username}_{datetime.datetime.now().strftime('%Y-%m_%H-%M-%S')}.pdf"

        # Save the PDF file to disk
        with open(filename, 'wb') as f:
            f.write(pdf_file.read())


        subject = 'Monthly Report - Blog Lite'
        body = f'Hello {user.username}, Please find the below attachment for the Monthly report of Blog Lite Application.'
        attachments = [filename]

        
        try:
            receiver = user.email

            app.config['YAGMAIL_USERNAME'] = 'madtwoproject@gmail.com'
            app.config['YAGMAIL_PASSWORD'] = 'dvclhvoyaazgqjqe'
            yag = yagmail.SMTP(app.config['YAGMAIL_USERNAME'], app.config['YAGMAIL_PASSWORD'])
            yag.send(to=receiver, subject=subject, contents=body, attachments=attachments)

            
    
        except Exception as e:
            print('Error sending email:', e)
        
        else:
            print(f"monthly reminder sent for {user.username}")

        # Delete the PDF file from disk
        os.remove(filename)
    return "Monthly report's sent successfully..!"