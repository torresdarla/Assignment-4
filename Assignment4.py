#Programmed by Darla Torres
#July 25, 2017

import Short


#This function reads a specific file (filename) and returns a dictionary whose keys are bird names and whose values are the number of times the bird has been seen
def countBirds(filename):
    d={}
    for line in open(filename):
        temp = line.split(', ')
        if temp[0] in d.keys():
            count=int(temp[1])
            d[temp[0]]=d[temp[0]] + count
        else:
            name = temp[0]
            count= int(temp[1])
            d[name] = count
    return d
    
#This function asks the user to enter a bird name and then looks up the sighting count for that bird in the specified dictionary (d).
def askUser(d):
    bird = Short.userString("Enter a bird name:")
    if bird in d:
        print "I have seen that bird %s times(s)" %d[bird]
    else: 
        print "I have seen that bird 0 time(s)"

#The main function nests one function into the other to ask the user what bird count they specifically want       
def main():
    askUser(countBirds('Birds.txt'))


main()

            




