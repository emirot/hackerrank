__author__ = 'nolanemirot'




def greaterLower(g, l):
    if(g > l):
        return g,l
    return l,g



def findPairs():
  l = input()
  n,k = list(map(int,l.split()))
  line = input()
  arr = list(map(int, line.split()))
  i = 0
  nbTimes = 0
  while i < len(arr) -1:
      j = i
      while j < len(arr)-1:
          #print("i",arr[i],"::",arr[j+1])
          great , low = greaterLower(arr[i], arr[j+1])
          if(great-low == k):
              nbTimes+=1
          j+=1
      i+=1
  return nbTimes


if __name__ == '__main__':
    print(findPairs())