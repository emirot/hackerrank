__author__ = 'nolanemirot'



def findMaxNumberTopicPerson(arr):
    maxTopics = 0
    maxTeamsMates = 0
    for i, teamate in enumerate(arr):
        j = i + 1
        while j < len(arr) :
            p1 =  int(teamate,2)
            p2 =  int(arr[j],2)
            rest = bin(p1|p2)
            maxval = rest.count("1");
            if maxval > maxTopics:
                maxTopics = maxval
                maxTeamsMates = 1
            elif maxval == maxTopics:
                maxTeamsMates += 1
            #print("p1",teamate)
            #print("p2",arr[j])
            j += 1
    return maxTopics, maxTeamsMates



if __name__ == '__main__':
    firstLine = input()
    arr = list(map(int,firstLine.split()))
    numberOfPeople = arr[0]
    nbTopics = arr[1]
    #print("nb people",numberOfPeople)
    #print("nb topics",nbTopics)
    i = 0
    arr = []
    while i < numberOfPeople:
        arr.append(input())
        i += 1
    arr = findMaxNumberTopicPerson(arr)
    print(arr[0])
    print(arr[1])