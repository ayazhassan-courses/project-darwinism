my_map={'A':[('B',15),('C',10),('E',13),('F',8)],'B':[('A',15),('D',12),('H',15)],'C':[('A',10),('D',12)],'D':[('B',12),('C',12),('F',10),('G',9),('H',9)],'E':[('A',13),('F',12)],'F':[('A',8),('D',10),('E',12),('G',10)],'G':[('D',9),('F',10),('H',12)],'H':[('B',15),('D',9),('G',12)]}

def enqueue(lst,i):    
    lst.append(i)
    return lst
def dequeue(lst):
    return lst.pop(0)
def is_empty(lst):
    if len(lst)==0:
        return True 
    else: return False

def initial_population (my_map, pop_size, source, destination):
### it creates a list of possible solution i.e. possible paths from source to destination  
    q=[[source]]
    r=[]
    while is_empty(q) == False:     #using bfs approach to find all paths b/w source and destination
        temp_path=dequeue(q)
        l=len(temp_path)-1
        vertex = temp_path[l]
        if vertex!= destination:
            for i in my_map[vertex]:
                if i[0] not in temp_path:
                    temp_path.append(i[0])
                    a=temp_path.copy()
                    enqueue(q,a)
                    temp_path.remove(i[0])
        else:
            r.append(temp_path)
            if len(r)==pop_size:
                return r        
    if len(r)!= pop_size:       #repeating initially created paths until pop_size is acheived 
        n= pop_size-len(r)
        for x in range(n):
            r.append(r[x])
    #print(len(r))
    return r
initial_pop=(initial_population (my_map, 50,"A", "H"))

def fitness_score(my_map,initial_pop):
    r=[]
    for member in initial_pop:
        score=0
        for i in range(len(member)-1,0,-1):
            for j in my_map[member[i-1]]:
                if j[0]==member[i]:
                    score+=j[1]
        r.append((member,score))
    return r
        
print(fitness_score(my_map,initial_pop))
def partition(x,low,high):
    i = low - 1
    pivot = x[high][1]
    for j in range(low,high):
        if x[j][1]<pivot:
            i = i+1 
            x[i],x[j] = x[j],x[i]
    x[i+1],x[high] = x[high],x[i+1] 
    return ( i+1 )
def sort(x,low,high):
        if low<high:
            u = partition(x,low,high)
            sort(x, low, u-1) 
            sort(x, u+1, high)
    
def quicksort(x):
    low=0 
    high= len(x) - 1
    sort(x,low,high)
    return x
(quicksort(x))
def selectparents(x):
    parents= []
    parents.append(x[0][0])
    a = 1
    for i in range(len(x)):
        if x[i][0] not in parents:
            parents.append(x[i][0])
            a +=1
        if a == 2:
            break 
    return parents
parents = (selectparents(x))
print(parents)
parentscopy = parents.copy()
parent1 = parentscopy.pop()
parent2 = parentscopy.pop()
import random
def crossover(parent1,parent2):
    child = []
    if len(parent1)>len(parent2):
        h = len(parent2)
        g = len(parent1)
        r = random.randint(0,h)
        u = parent2
    else:
        h = len(parent1)
        g = len(parent2)
        r = random.randint(0,h)
        u = parent1
    for i in range(0,r):
        child.append(u[i])
    for j in range(r,g):
        child.append(u[j])
    return child
print(crossover(parent1,parent2))

member=(crossover(parent1,parent2))

def valid_path(path,my_map):       #helper funtion to check if a given path is valid
    start=0
    end=len(path)-2
    while start!=end:
        check=False
        for i in my_map[path[start]]:
            if i[0] in my_map[path[start+1]]:
                check=True
        if check==False:
            return False
        else:
            start+=1
    return True

def mutation(member,my_map):
    x=len(member)-2
    y=member.copy()
    y.pop(x)
    path=y
    if valid_path(path,my_map)==True:
        return path
    else:
        return member 
print(mutation(member,my_map))
