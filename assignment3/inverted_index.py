import MapReduce
import sys

mr = MapReduce.MapReduce()
 
def mapper(data):
    words = data[1].split()            
    for word in words: 
        mr.emit_intermediate(word,data[0])

def reducer(key, list_of_values):
    setArrayString = ",".join(set(list_of_values))
    mr.emit((key,setArrayString.split(",")))

def main():     
    file = open(sys.argv[1])
    mr.execute(file, mapper, reducer)

if __name__ == '__main__':
    main()