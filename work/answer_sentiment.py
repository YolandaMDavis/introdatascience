import sys
import json

def convert_to_dict(sent_file):    
    map = {}
    lines = sent_file.readlines()
    for line in lines:
        string_array = line.rstrip().split('\t')
        map[string_array[0]] = string_array[1] 
        
    return map

def calculate_answer_sent(sent_dict,answer_file):
    lines = answer_file.readlines()
    lines = lines[0].split('\r')
    question_sent = {}
    for line in lines:                
        sent_sum = 0
        words = line.split('\t');
        wordArray = words[2].split();           
        for word in wordArray:  
            utf_word =  word.encode('utf-8','ignore').lower()
            if utf_word in sent_dict: 
                sent_sum += int(sent_dict[utf_word])    
        if words[1] in question_sent:        
            question_sent[str(words[1])] += sent_sum     
        else:
            question_sent[str(words[1])] = sent_sum     
    return question_sent
    
def main():
    sent_file = open(sys.argv[1])    
    answer_file = open(sys.argv[2])    
    sent_dict = convert_to_dict(sent_file)
    question_sent = calculate_answer_sent(sent_dict,answer_file)
    print question_sent

if __name__ == '__main__':
    main()
