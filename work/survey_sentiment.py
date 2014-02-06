import sys
import json
import re

def convert_to_dict(sent_file):    
    map = {}
    lines = sent_file.readlines()
    for line in lines:
        string_array = line.rstrip().split('\t')
        map[string_array[0]] = string_array[1] 
        
    return map

def calculate_tweet_sent(sent_dict,tweet_file):
    sent_word = {}
    lines = tweet_file.readlines()
    lines = lines[0].split('\r')
    for line in lines:              
        sent_sum = 0        
        words = line.split('\t');
        wordArray = words[2].split();
        for word in wordArray:  
            utf_word = re.sub(r"[^A-Za-z@']",'',word.encode('utf-8','ignore'))  
            if utf_word in sent_dict: 
                sent_sum += int(sent_dict[utf_word])                           
        for word in wordArray:                
            utf_word = re.sub(r"[^A-Za-z@']",'',word.encode('utf-8','ignore'))                
            if utf_word in sent_word: 
                sent_word[utf_word] += sent_sum
            else: 
                if utf_word != '':
                    sent_word[utf_word] = sent_sum
            
    return sent_word
    
def print_sent_word(sent_word):
    for key in sent_word:
        print key + ' ' + str(sent_word[key])
    
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = convert_to_dict(sent_file)
    sent_word = calculate_tweet_sent(sent_dict,tweet_file)
    print_sent_word(sent_word)


if __name__ == '__main__':
    main()
