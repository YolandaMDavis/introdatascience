import sys
import json
import re

def count_words(tweet_file):
    tweet_word = {}
    lines = tweet_file.readlines()    
    for line in lines:        
        tweet = json.loads(line)                        
        if "text" in tweet:               
            words = tweet["text"].split()            
            for word in words:  
                ascii_word = re.sub(r"[^A-Za-z',\.]",'',word.encode('utf-8','ignore'))                                
                if ascii_word in tweet_word: 
                    tweet_word[ascii_word]+=1
                else:
                    if ascii_word != '':
                        tweet_word[ascii_word]=1
                            
    return tweet_word

def sum_words(tweet_word):
    total = 0;
    for key in tweet_word:
        total += tweet_word[key]    
    return total

def print_words(tweet_word, total_words):
    for key in tweet_word:
        i = float(tweet_word[key]) / total_words
        print key + " %0.5f" % i
    
    
def main():    
    tweet_file = open(sys.argv[1])
    tweet_word_count = count_words(tweet_file)    
    print_words(tweet_word_count,sum_words(tweet_word_count))


if __name__ == '__main__':
    main()
