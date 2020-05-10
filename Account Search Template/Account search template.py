#!/usr/bin/python
import praw
import time

reddit = praw.Reddit('bot1')

while True:
    comments = reddit.inbox.unread()
    
    for item in reddit.inbox.unread(limit=None):
        print(repr(item))
    
    for comment in comments:
        i=0
        text = comment.body
        parent = comment.parent()
        splittedc = text.split(' ')
        
        #Targeted (Using Specified User As Target)
        if 'u/[BOTNAME] ' in text.lower() and 'u/' in splittedc[1]:
            try:
                target = (splittedc[1].split('u/'))[1]
                print('Target: ' + target)
            except:
                print('Not a true username, using parent commenter')
                target = parent.author.name
                print('Target: ' + target)
            if target == '[BOTNAME]':
                pass
            
            #Searching Their Submissions
            for submission in reddit.redditor(target).comments.new():
                #print(submission.body)
                if '[SEARCHINGFOR]' in submission.body.lower():
                    i = i+submission.body.lower().count('[SEARCHINGFOR]')
                    i = i-submission.body.lower().count('[BOTNAME]')
                    print(submission.body)
            print('[SEARCHINGFOR] Count:' + str(i) + '\n')
            
            #Replying
            try:
                comment.reply(str(i)) #Put reply in the brackets (ex: comment.reply('Target said _____ ' + str(i) + ' times')
                print('replied\n')
                comment.mark_read()
            except:
                print('Exception Occured (Probably a comment cooldown)')
                time.sleep(30)
                print('ready to go\n')
            
        #Targetless (Using Parent Commenter As Target)
        elif 'u/[BOTNAME] in text.lower():
            target = parent.author.name
            print('Target: ' + target)
            if target == '[BOTNAME]':
                pass
            
            #Searching Their Submissions
            for submission in reddit.redditor(target).comments.new():
                #print(submission.body)
                if '[SEARCHINGFOR]' in submission.body.lower():
                    i = i+submission.body.lower().count('[SEARCHINGFOR]')
                    i = i-submission.body.lower().count('[BOTNAME]')
                    print(submission.body)
            print('[SEARCHINGFOR] Count:' + str(i) + '\n')
                
            #Replying
            try:
                comment.reply(str(i)) #Put reply in the brackets (ex: comment.reply('Target said _____ ' + str(i) + ' times'))
                print('replied\n')
                comment.mark_read()
            except:
                print('Exception Occured (Probably a comment cooldown)')
                time.sleep(30)
                print('ready to go\n')
                
        time.sleep(1)
    
            
