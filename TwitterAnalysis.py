#ASSIGMENT OBJECTIVES:

#QUESTION 1: find how many retweets (retweet_count)
#QUESTION 2: find average # of retweets per tweet
             #total retweets / total tweet amount - use len()
#QUESTION 3: find how many status = quote status 
             #"is_quote_status": true 
            #conditonal if statement inside loop 

#BONUS: find an interesting metric / explain why its good or useful
    #how many tweets have been favorited / "favourites_count":
    #"user_mentions:" = "screen_name": "RuPaulsDragRace" 

import json

trixiefile = open("/Users/jaycolosi/Desktop/Python/trixie/twitter_summarytrixiemattel.json","r") 
trixie = json.load(trixiefile) 

taylorfile = open("/Users/jaycolosi/Desktop/Python/assignment_starter/assignment_data/twitter_summarytaylorswift13.json","r") 
taylor = json.load(taylorfile) #opened additonal file for testing myAnalysis functionality

gretafile = open("/Users/jaycolosi/Desktop/Python/assignment_starter/assignment_data/twitter_summaryGretaThunberg.json","r") 
greta = json.load(gretafile) #opened additional file for testing myAnalysis functionality

def avg(x,y):
    div = round((x/y),2)
    return div

def myAnalysis(data,who):
    print(f"===== {who} Analysis =====") #change name in print out
    #QUESTION 1: Retweet Totals
    t_rtwt = 0 #counter - total retweets 
    for rtwt in data: 
        rtwt_count = rtwt["retweet_count"] 
        t_rtwt += rtwt_count
    print("Total Retweets:", t_rtwt)

    #QUESTION 2: Avg # of retwts / twts
    t_twts = len(data) #total tweets 
    avg_rtwts = avg(t_rtwt,t_twts) #both counters divide using function
    print("Total Average Retweets:", avg_rtwts)

    #QUESTION 3: Quote Status = True 
    t_sq = 0 #counter - total quote statuses
    for sqs in data: 
        statusTweet = sqs["is_quote_status"] 
        if statusTweet == True: 
            t_sq += 1 
    print("Total Status Count:", t_sq)

#FAVOURITES "favorite_count":
#how many people have favorited the tweets overall
favCounter = 0
for fav in trixie:
    favCount = fav["favorite_count"]
    favCounter += favCount

#Average favs
t_twts = len(trixie) #find total tweets 
avg_favs = avg(favCounter, t_twts) #total retweets / total tweets 

#USER_MENTIONS
#Trixie is a famous drag queen known for winning the show RPDR
#how many times is RuPaul's Drag Race mention
rpdr_count = 0 
for tweet in trixie: 
    usermentions = tweet["entities"]["user_mentions"]
    for rdpr in usermentions:
        if rdpr["screen_name"] == "RuPaulsDragRace": 
            rpdr_count += 1 

#use myAnalysis function to complete these 
myAnalysis(trixie, "Trixie Mattel")
print ("===== * BONUS ROUND: Trixie * =====")
print("Total Favourites:", favCounter)
print("Average Favs per Tweets Overall:", avg_favs)
print("Total Mentions of 'RuPaul's Drag Race':", rpdr_count)

myAnalysis(taylor, "Taylor Swift") #wanted to test myanalysis function on additional files
myAnalysis(greta, "Greta Thunberg") #wanted to test myanalysis function on additional files
































