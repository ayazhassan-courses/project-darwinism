  
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
#print(fitness_score(my_map,[['A', 'C', 'D', 'B', 'H'], ['A', 'E', 'A', 'F', 'G', 'H']]))

#x = fitness_score(my_map,initial_pop)

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
#print(quicksort(x))
def selectparent(x):
    #print(x,"pop")
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
#print(selectparent(x),"parents")
#parents = (selectparent(x))
#print(parents)
#parentscopy = parents.copy()
#parent1 = parentscopy.pop()
#parent2 = parentscopy.pop()
def valid_child(path,my_map):  #helper funtion to check if a given path is valid  
    for p in range(len(path)-1):
        check = False
        pa = path[p]
        for x in my_map[path[p+1]]:
            if pa == x[0]:
                check = True            
    return check
#print(valid_child(["A","G","H"],my_map))
import random
def crossover(parent1,parent2,a = 0):
    if parent1 == parent2:
        if valid_path(parent1,my_map)== True:
            return parent1
        elif valid_path(parent2,my_map)==True:
            return parent2
    else:
        #print(parent1,parent2,"parameters to cross over")
        a+=1
        child = []
        #print("parents",parent1,",", parent2)
        
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
                #print("crossover resultt",child)
                return child
            else:
                return crossover(parent1,parent2,a)
        else:
            #print("crossover resultt",parent1)
            if valid_path(parent1,my_map)==True:
                return parent1
            else:
                return parent2
#print(crossover(["A","B","H"],["A","B","D","H"],a = 0))

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
#print(valid_path(['A', 'B', 'H'],my_map))
#member=crossover(parent1,parent2,a = 0)
def mutation(member,my_map):
    #print(member,"parmeter to mutation")
    probability = random.randint(0,4)
    if probability<=2:
        #print(probability, "p1")
        x=random.randint(1,len(member)-2)
        #print(x,"x")
        y=member.copy()
        z=member.copy()
        y.pop(x)
        path=y
        if valid_path(path,my_map)==True:
            #print(path,"mutation result1")
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
                                    #print(member,"mutation result2")
                                    return member
                            else:
                                member.insert(x+1,i[0])
                                member.pop(x)
                                if valid_path(member,my_map)==True:
                                    #print(member,"mutation result3")
                                    return member
                                return z
            #print(z,"mutation result4")
            return z
    else: 
        #print(member,"mutation result5")
        return member

#print(mutation(member,my_map),"mutated")

def new_member(my_map,source,destination):
    check=True
    member=[source]
    current=0
    while check:
        if member[current]!=destination:
            prospect=my_map[member[current]]
            #print(member[current])
            #print(prospect)
            i= random.randint(0,len(prospect)-1)
            #if prospect[i][0] not in member:
            member.append(prospect[i][0])
            current+=1
            #else:
                #while prospect[i][0] in member:
                #    print(prospect[i][0], member)
                #    i= random.randint(0,len(prospect)-1)
                #member.append(prospect[i][0])
                #current+=1
        else:
            check=False
    #print(member,"new member")
    return member
    
#print(new_member(my_map,"A","H"))

#current_pop=[['A', 'B', 'D', 'G', 'H'], ['A', 'C', 'D', 'G', 'D', 'H'], ['A', 'F', 'A', 'C', 'A', 'F', 'D', 'C', 'A', 'C', 'A', 'F', 'E', 'F', 'D', 'G', 'D', 'B', 'A', 'E', 'F', 'D', 'H']]

def new_population(current_copy, my_map, source, destination):
    currently= current_copy
    #print(currently,"NEW POP FUNCTION CURRENT_POP")
    children=[]
    pop_size=len(currently)
    x = fitness_score(my_map,current_copy)
    y = selectparent(quicksort(x))
    #print(x)
    #print(y,"parents")
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
    #print(children,"children")
    for some in range(pop_size//2):
        children.append(new_member(my_map,source,destination))
    #print(children,"some more children")
    #print(currently,"current_pop")
    m=quicksort(fitness_score(my_map,currently + children))
    
    #print(m,"m")
    new=[]
    while len(new)!=pop_size:
        temp=m.pop(0)
        new.append(temp[0])
             
    return new
#print(new_population(current_pop, my_map, "A", "H"))

def plot_gen(res,my_map,source,destination):
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
    plt.title("The fitness of the graph is "+str(fitness))
   
    plt.show()
#plot_gen((['A', 'E', 'A', 'B', 'H'], 56),my_map,"A","H")



def genetic_algo(gen_no, current_pop, my_map, source, destination):
    max_gen=10
    pop_size=3

    if gen_no==0:
        #current_pop = initial_population (my_map, pop_size, source, destination)
        current_pop=[]
        for i in range(pop_size):
            current_pop.append((new_member(my_map,source,destination)))
        fitness = quicksort(fitness_score(my_map,current_pop))
        fittest = fitness[0]
        gen_no+= 1
        print(plot_gen(fittest,my_map,source,destination))
        print("Genaration",gen_no,":",fittest)
        print("pop : ",fitness)
        genetic_algo(gen_no, current_pop, my_map, source, destination)

    elif gen_no < max_gen:
        current_copy= current_pop.copy()
        #print(current_copy,"MAIN FUNCTION CURRENT_POP")
        current_pop=[]
        neww = new_population(current_copy ,my_map, source, destination)

        fitness = quicksort(fitness_score(my_map,neww))
        fittest = fitness[0]
        gen_no+= 1
        print(plot_gen(fittest,my_map,source,destination))
        print("Genaration",gen_no,":",fittest)
        print("pop : ",fitness)
        genetic_algo(gen_no, neww, my_map, source, destination)

    else:  
        return 
print(genetic_algo(0, [], my_map, "A", "H"))





