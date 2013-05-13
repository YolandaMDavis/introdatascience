import sys
import json

def convert_to_dict(sent_file):    
    map = {}
    lines = sent_file.readlines()
    for line in lines:
        string_array = line.rstrip().split('\t')
        map[string_array[0]] = string_array[1] 
        
    return map

def calculate_tweet_sent(sent_dict,tweet_file):
    lines = tweet_file.readlines()
    for line in lines:        
        tweet = json.loads(line)                        
        if "text" in tweet:   
            sent_sum = 0
            words = tweet["text"].split()            
            for word in words:  
                utf_word =  word.encode('utf-8','ignore').lower()
                if utf_word in sent_dict: 
                    sent_sum += int(sent_dict[utf_word])            
            print str(sent_sum)     
            
def main():
    sent_file = open(sys.argv[1])    
    tweet_file = open(sys.argv[2])    
    sent_dict = convert_to_dict(sent_file)
    calculate_tweet_sent(sent_dict,tweet_file)


if __name__ == '__main__':
    main()
