import urllib2
import json

response = urllib2.urlopen("http://search.twitter.com/search.json?q=microsoft&page=10")

tweetResponse = json.load(response)

for tweet in tweetResponse["results"]:
    print tweet["text"]

