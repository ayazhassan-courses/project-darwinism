import matplotlib.pyplot as plt
import random
my_map={'A':[('B',15),('C',10),('E',13),('F',8)],'B':[('A',15),('D',12),('H',15)],'C':[('A',10),('D',12)],'D':[('B',12),('C',12),('F',10),('G',9),('H',9)],'E':[('A',13),('F',12)],'F':[('A',8),('D',10),('E',12),('G',10)],'G':[('D',9),('F',10),('H',12)],'H':[('B',15),('D',9),('G',12)]}

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

def selectparent(x):
    parent = []
    parent.append(x[0][0])
    a = 1
    for i in range(len(x)):
        if x[i][0] not in parent:
            parent.append(x[i][0])
            a +=1
        if a == 4:
            break 
    return parent 


def crossover(parent1,parent2,a = 0):
    if parent1 == parent2:
        if valid_path(parent1,my_map)== True:
            return parent1
        elif valid_path(parent2,my_map)==True:
            return parent2
    else:
        a+=1
        child = []
        if len(parent1)>len(parent2):
            h = len(parent2)
            g = len(parent1)
            r = random.randint(0,h)
            u = parent2
            x = parent1
            print(r)       
        else:
            h = len(parent1)
            g = len(parent2)
            r = random.randint(0,h)
            u = parent1
            x = parent2
        if a != h:
            for i in range(0,r):
                child.append(u[i])
            for j in range(r,g):
                child.append(x[j])

            if valid_path(child,my_map) == True:
                return child
            else:
                return crossover(parent1,parent2,a)
        else:
            if valid_path(parent1,my_map)==True:
                return parent1
            else:
                return parent2


def valid_path(path,my_map):       #helper funtion to check if a given path is valid
    start=0
    end=len(path)-2
    if start==end:
        check=False
        for x in my_map[path[start]]:
            if x[0]==path[end+1]:
                check=True
        if check==False:
                return False
        else: return True
    else:
        while start!=end+1:
            check=False
            for i in my_map[path[start]]:
                if i[0] == path[start+1]:
                    check=True
            if check==False:
                return False
            else:
                start+=1
        return True

def mutation(member,my_map):
    probability = random.randint(0,4)
    if probability<=2:
        x=random.randint(1,len(member)-2)
        y=member.copy()
        z=member.copy()
        y.pop(x)
        path=y
        if valid_path(path,my_map)==True:
            return path
        else: 
            for i in my_map[member[x]]:
                if i[0] not in member:
                    for j in my_map[i[0]]:
                        if j[0]==member[x+1]:
                            probability=random.randint(0,4)
                            if probability<2:
                                member.insert(x+1,i[0])
                                if valid_path(member,my_map)==True:
                                    return member
                            else:
                                member.insert(x+1,i[0])
                                member.pop(x)
                                if valid_path(member,my_map)==True:
                                    return member
                                return z
            return z
    else: 
        return member


def new_member(my_map,source,destination):
    check=True
    member=[source]
    current=0
    while check:
        if member[current]!=destination:
            prospect=my_map[member[current]]
            i= random.randint(0,len(prospect)-1)
            member.append(prospect[i][0])
            current+=1
        else:
            check=False
    return member
    
def new_population(current_copy, my_map, source, destination):
    currently= current_copy
    children=[]
    pop_size=len(currently)
    x = fitness_score(my_map,current_copy)
    y = selectparent(quicksort(x))
    parents= y.copy()
    n=len(parents)
    for i in range(n//2):
        parent1 = parents.pop()
        parent2 = parents.pop()
        member=(crossover(parent1,parent2))
        children.append(member)
        
    for child in range(len(children)):
        z = children.pop(0)
        mutated = mutation(z,my_map)
        children.append(mutated)
    
    for some in range(pop_size//2):
        children.append(new_member(my_map,source,destination))
    
    m=quicksort(fitness_score(my_map,currently + children))
    new=[]
    while len(new)!=pop_size:
        temp=m.pop(0)
        new.append(temp[0])
             
    return new


def plot_gen(gen_no,res,my_map,source,destination):
    path=res[0]
    fitness=res[1]
    n=ord(source)-1
    x=[]
    y=[0]
    for i in path:
        x.append(ord(i)-n)
    for j in range(len(path)-1):
        for k in my_map[path[j]]:
            if k[0]==path[j+1]:
                y.append(k[1])
                plt.scatter(x[j],y[j])
    plt.scatter(x[len(x)-1],y[len(y)-1])
    plt.plot(x,y)
    plt.title("Genaration no."+str(gen_no)+"   Distance : "+str(fitness))
   
    plt.show()


def genetic_algo(gen_no, current_pop, my_map, source, destination):
    max_gen=10
    pop_size=3

    if gen_no==0:
        current_pop=[]
        for i in range(pop_size):
            current_pop.append((new_member(my_map,source,destination)))
        fitness = quicksort(fitness_score(my_map,current_pop))
        fittest = fitness[0]
        gen_no+= 1
        print(plot_gen(gen_no,fittest,my_map,source,destination))
        print("Genaration",gen_no,":",fittest)
        print("pop : ",fitness)
        genetic_algo(gen_no, current_pop, my_map, source, destination)

    elif gen_no < max_gen:
        current_copy= current_pop.copy()
        current_pop=[]
        neww = new_population(current_copy ,my_map, source, destination)
        fitness = quicksort(fitness_score(my_map,neww))
        fittest = fitness[0]
        gen_no+= 1
        print(plot_gen(gen_no,fittest,my_map,source,destination))
        print("Genaration",gen_no,":",fittest)
        print("pop : ",fitness)
        genetic_algo(gen_no, neww, my_map, source, destination)

    else:  
        return 
print(genetic_algo(0, [], my_map, "A", "H"))



