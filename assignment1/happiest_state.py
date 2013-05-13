import sys
import json
import re
import operator

def get_state_dict():    
    map = {'AL':0,'AK':0,'AZ':0,'AR':0,'CA':0,'CO':0,'CT':0,'DE':0,'DC':0,'FL':0,'GA':0,'HI':0,'ID':0,'IL':0,'IN':0,'IA':0,'KS':0,'KY':0,'LA':0,'ME':0,'MD':0,'MA':0,'MI':0,'MN':0,'MS':0,'MO':0,'MT':0,'NE':0,'NV':0,'NH':0,'NJ':0,'NM':0,'NY':0,'NC':0,'ND':0,'OH':0,'OK':0,'OR':0,'PA':0,'RI':0,'SC':0,'SD':0,'TN':0,'TX':0,'UT':0,'VT':0,'VA':0,'WA':0,'WV':0,'WI':0,'WY':0}
    return map
    
def convert_to_dict(sent_file):    
    map = {}
    lines = sent_file.readlines()
    for line in lines:        
        string_array = line.rstrip().split('\t')
        map[string_array[0]] = string_array[1]         
    return map

def get_tweet_state(tweet,map):         
    
        location_array = tweet["place"]["full_name"].split(',')
        if len(location_array) == 2:
            state = location_array[1]            
            state = re.sub(r' ','',state.encode('utf-8','ignore')).upper()            
            if state in map:
                return state
            else: 
                return None

def calculate_tweet_sent(tweet_text,state_sent,sent_dict):                              
        sent_sum = state_sent
        words = tweet_text.split()            
        for word in words:  
            utf_word =  word.encode('utf-8','ignore').lower()
            if utf_word in sent_dict: 
                sent_sum += int(sent_dict[utf_word])            
        return sent_sum     
                

def calculate_state_sent(tweet_file,sent_file):
    map = get_state_dict()
    sent_dict = convert_to_dict(sent_file)
    lines = tweet_file.readlines()
    for line in lines:        
        tweet = json.loads(line)                        
        if ('place' in tweet and tweet['place'] and tweet['place']['country_code'] == 'US'):                    
            state = get_tweet_state(tweet,map)
            if state and "text" in tweet:
                map[state] = calculate_tweet_sent(tweet['text'],map[state],sent_dict)                
    return map            

def sort_state_sent(state_sent):
    return sorted(state_sent.iteritems(), key=operator.itemgetter(1), reverse=True)
    
                
def main():
    sent_file = open(sys.argv[1])    
    tweet_file = open(sys.argv[2])        
    states = sort_state_sent(calculate_state_sent(tweet_file,sent_file))    
    print states[0][0]
    
    
if __name__ == '__main__':
    main()
