import MapReduce
import sys

mr = MapReduce.MapReduce()
 
def mapper(data):          
    mr.emit_intermediate(data[0],data[1])

def reducer(key, list_of_values):
    length = len(list_of_values)
    mr.emit((key,length))

def main():     
    file = open(sys.argv[1])
    mr.execute(file, mapper, reducer)

if __name__ == '__main__':
    main()