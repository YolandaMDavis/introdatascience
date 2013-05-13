import sys
import json
import re
import operator

def count_words(tweet_file):
    tweet_word = {}
    lines = tweet_file.readlines()    
    for line in lines:        
        tweet = json.loads(line)                        
        if "entities" in tweet:                           
            hashtags = tweet["entities"]["hashtags"]             
            for hash in hashtags:                  
                utf_word = hash["text"].encode('utf-8','ignore')                
                if utf_word in tweet_word: 
                    tweet_word[utf_word]+=1
                else:
                    if utf_word != '':
                        tweet_word[utf_word]=1
                            
    return tweet_word

def sort_words(tweet_word):
    return sorted(tweet_word.iteritems(), key=operator.itemgetter(1),reverse=True)

def print_words(tweet_word):
    i = 10    
    if i > len(tweet_word): i = len(tweet_word)            
    for key in range(i):        
        print tweet_word[key][0] + ' ' + str(float(tweet_word[key][1]))
    
    
def main():    
    tweet_file = open(sys.argv[1])
    tweet_word_count = count_words(tweet_file)          
    print_words(sort_words(tweet_word_count))    


if __name__ == '__main__':
    main()
