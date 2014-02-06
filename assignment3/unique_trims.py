import MapReduce
import sys

mr = MapReduce.MapReduce()
 
def mapper(data):    
    mr.emit_intermediate(data[1],data[1][0:(len(data[1]) - 10)])
    
def reducer(key, list_of_values):
    sequences = set(list_of_values)
    for sequence in sequences:
        mr.emit(sequence)
            
def main():     
    file = open(sys.argv[1])
    mr.execute(file, mapper, reducer)

if __name__ == '__main__':
    main()