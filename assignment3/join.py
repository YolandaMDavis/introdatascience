import MapReduce
import sys

mr = MapReduce.MapReduce()
 
def mapper(data):          
        mr.emit_intermediate(data[1],data)

def reducer(key, list_of_values):
    orders = []
    line_items = []
    
    for values in list_of_values:
        if values[0] == "order":
            orders.append(values)        
        else:
            line_items.append(values)
            
    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)

def main():     
    file = open(sys.argv[1])
    mr.execute(file, mapper, reducer)

if __name__ == '__main__':
    main()