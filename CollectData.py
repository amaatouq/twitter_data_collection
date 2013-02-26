__author__ = 'amaatouq'

import numpy as np
from Streaming import Streaming
# my credentials for Twitter with amaatouq@gmail.com
credential= {'consumer_key': '4Yd3iUGaFHltlezXYBJhFA',
 'consumer_secret': 'oKeNDcOIWRfmpsWqgKntU1XCl0abZ1objWWiCGCo',
 'access_token': '243804207-dXlUBW293YNz806LG3RcLfc5eXRWEkNQgPIVDTGY',
 'access_token_secret': 'JcvyrAVgVwzpl6BXdNwRsOCUrhUt0M0hgLA3tGEVa1c'}

# connecting to the stream
streaming = Streaming(credential)

# Riyadh "location=[46.56,24.50,47.00,24.85]""

# Start listening with the filters


def listen_to_location(location):
	streaming.listen(location=location)

def listen_to_users(list_of_users):
	streaming.listen(follow=list_of_users)

#listen_to_location(location=[46.56,24.50,47.00,24.85])

#getting spam from spam accounts
spam = np.loadtxt('Helpers/spammers_id.csv',dtype='i16').tolist()


listen_to_users(spam)
