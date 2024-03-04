def nodecover():
    minlen = n+1
    # stepcounter=0
    
    for i in range(n):
        stack = [(int(i), [])]

        while stack:
            i, current_nodes = stack.pop()
            
            if promising(current_nodes):
                current_nodes.append(i)
                
                if checkcover(current_nodes):
                    answer.append(current_nodes.copy())
                    
                    if(len(current_nodes) < minlen):
                        minlen = len(current_nodes)
                        
                else:
                    for j in range(i + 1, n):
                        stack.append((j, current_nodes.copy()))
                        
            # stepcounter = stepcounter + 1        
    
    # print(stepcounter)
    
    return minlen

def checkcover(ls):
    nodecovered = []  

    for i in ls: 
        for j in range(0, n):
            if W[i][j] == 1:
                nodecovered.append(j)
    
    for j in range(0, n):
        if j not in nodecovered:
            return False
    
    nodecovered.clear()
    
    return True

def promising(temp):
    flag = True
    k = 0
    
    while k < n:
        temp.append(k)
        
        if temp in Not_promising: 
            return False
        
        temp.pop()
        k += 1

    return True

def print_result():
    print("\nAll possible answers : ")
    for item in answer:
        print(item)
            
    # find all answers with minlen 
    minanswers=[]
    for index in range(0,len(answer)):
        if(len(answer[index]) == minlen):
            minanswers.append(answer[index])
    
    print("\nBest answer/answers : ")  
    for item in minanswers:
        print(item)
        
# main
answer = []
Not_promising = []

W = [[0, 1, 1, 0, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [1, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 0]]

temp = []
n = len(W)

minlen = nodecover()
print_result()