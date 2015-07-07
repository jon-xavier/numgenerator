import sys
import argparse
import random
import simplejson

def generate(count):
    '''Returns a list of (count) pseudorandom numbers, using system time as a seed'''
    current_count= 0
    random.seed
    number_list = []
    while current_count < count:
        number_list.append(random.randint(1, 1000))
        current_count = current_count+1
    return number_list    
    

def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument("count", help="Count is the number of random numbers that numgenerator should generate.", type=int)
    args = parser.parse_args()
    
    #Convert the args to a dictionary and pull out the count value
    args= vars(args)
    count=args.pop("count")
    
    #Run generate on count, save this to a list, then write the list to a text file using json
    final_list= generate(count)
    f = open('output.txt', 'w')
    simplejson.dump(final_list, f)
    f.close()
    
if __name__ == "__main__":
    main()