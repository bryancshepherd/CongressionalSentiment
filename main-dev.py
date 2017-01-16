
# coding: utf-8

# In[61]:

# Purpose: Keep congress members informed
# of what is being said about them on Twitter.

import twitter


# In[62]:

results = []
with open('./user_info.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))

cons_key = results[0][0]
cons_secret = results[1][0]
acc_tok = results[2][0]
acc_tok_sec = results[3][0]

# Log in
api = twitter.Api(consumer_key=cons_key,
                  consumer_secret=cons_secret,
                  access_token_key=acc_tok,
                  access_token_secret=acc_tok_sec, 
                  sleep_on_rate_limit=True)


# In[66]:

# Get the relevant tweets.
# Get geocoded tweets as 
# we can filter based on likely 
# constituents. 
# This sets a point in the 
# middle of the state based on
# this:
# http://www.latlong.net/
results = api.GetSearch(term='-RT @thomtillis', lang='en', 
                        since='2016-12-27',
                        result_type='recent', 
                        count='100',
                        # geocode="35.511828,-78.804932,250mi"
                       )


# In[67]:

len(results)


# In[79]:

corpus = ''.join([result.text for result in results])


# In[80]:

from collections import Counter

word_list = corpus.split()
counts = Counter(word_list)
print(counts)


# In[78]:

corpus.split()


# In[ ]:



