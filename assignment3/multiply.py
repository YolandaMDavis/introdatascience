import MapReduce
import sys
import json

mr = MapReduce.MapReduce()
 
def mapper(data):
    default_size = [0,1,2,3,4]
    if data[0] == "a":
        for x in default_size:
            mr.emit_intermediate((data[1],x),data)
            
    if data[0] == "b":    
        for x in default_size:
            mr.emit_intermediate((x,data[2]),data)
    
def reducer(key, list_of_values):     
    matrixA = []
    matrixB = []
    
    for tuple in list_of_values:
        if tuple[0] == "a":
            matrixA.append(tuple)
        else:
            matrixB.append(tuple)
    sum = 0
    
    for tupleA in matrixA:
        for tupleB in matrixB:
           if tupleA[2] == tupleB[1]:
                sum+= tupleA[3] * tupleB[3]
    
    mr.emit((key[0],key[1],sum))
    
def main():     
    file = open(sys.argv[1])
    mr.execute(file, mapper, reducer)

if __name__ == '__main__':
    main()