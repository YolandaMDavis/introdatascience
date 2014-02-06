import MapReduce
import sys

mr = MapReduce.MapReduce()
 
def mapper(data):
    val1 = hash(data[0])
    val2 = hash(data[1])
    mr.emit_intermediate(val1 + val2,(data[0],data[1]))
    
def reducer(key, list_of_values): 
   
    for tuple in list_of_values:
        if len(list_of_values) == 1:
            mr.emit(tuple)
            mr.emit((tuple[1],tuple[0]))

def main():     
    file = open(sys.argv[1])
    mr.execute(file, mapper, reducer)

if __name__ == '__main__':
    main()