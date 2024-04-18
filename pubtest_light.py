#from geopy.geocoders import Nominatim
import time
import string
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException
import pyrebase
import os

pnChannel = "raspi-tracker";
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-305cae0d-0ae8-4bd5-af55-6caf4d309670"
pnconfig.publish_key = "pub-c-54cc73fe-ad96-4dad-8032-f8fe4b184336"
pnconfig.uuid = "909092e7-0586-4d21-82ad-f73d88a77cbc"
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)
pubnub.subscribe().channels(pnChannel).execute()

while True:
    time.sleep(2)
    try:
        url = "https://firebasestorage.googleapis.com/v0/b/aprtest1.appspot.com/o/pepe5.jpg?alt=media&token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImYyOThjZDA3NTlkOGNmN2JjZTZhZWNhODExNmU4ZjYzMDlhNDQwMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYXBydGVzdDEiLCJhdWQiOiJhcHJ0ZXN0MSIsImF1dGhfdGltZSI6MTcxMzA2NjQ0MCwidXNlcl9pZCI6IjRRak43QUhoS2NNQmI5Y3huZk4wbTRjVjVmbTEiLCJzdWIiOiI0UWpON0FIaEtjTUJiOWN4bmZOMG00Y1Y1Zm0xIiwiaWF0IjoxNzEzMDY2NDQwLCJleHAiOjE3MTMwNzAwNDAsImVtYWlsIjoiY2h1bi5tby5jQG55Y3UuZWR1LnR3IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiY2h1bi5tby5jQG55Y3UuZWR1LnR3Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.D_hFbOLJHk9TRTz9igAf6TVwb62Tlsi6n1FCDxdh5y9jD4ytJzh9kGdGwwHQvOusdcwg9LwCX6AGukxIIjRz55yNUx4GLBarViL-Jbjzw3EgCa36rIcLqv62Oul2b7KfamD7rnW23xjzvs-8kny-i148GJAU8ivYrgclZkn4RPvB7RMll5SXkbQ7X4JxxpF_2GW8GhdIGrs8U5fcaUSYcefTVo4tnIEmadDgxk3VfA89aH2r0kV6FO2WEhkW312vzCEPkwaVdqZOtXU2hJgtqFC5BmcBhEVglrYfkbIHoKRbEMpySv3Y4vQqYuxl8BvTJ6V-53fUDbYxL7pyyda3gQ"
        
        envelope = pubnub.publish().channel(pnChannel).message({
            "lat": 24.7941595,
            'lng': 120.9499721,
            'url': url
        }).sync()
        print("publish message timetoken: %d" % envelope.result.timetoken)

    except PubNubException as e:
        handle_exception(e)
