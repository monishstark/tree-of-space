class Node:
    def __init__(self,val):
        self.val=val
        self.c=[]
        self.parent=None
        self.id=None
        self.locked=None
        self.anslocked=0
        self.deslocked=0

def lock(node,id):
    if node.locked:
        return False
    if node.anslocked>0  or node.deslocked>0:
        return False
    
    temp=node.parent
    while temp:
        temp.deslocked+=1
        temp=temp.parent
    
    ascend(node,1)
    
    node.locked=True
    node.id=id
    return True

def unlock(node,id):
    if node.locked==False or node.id!=id:
        return False
    
    temp=node.parent
    while temp:
        temp.deslocked-=1
        temp=temp.parent
    
    ascend(node,-1)
    node.locked=False
    node.id=None
    return True
    

def upgrade(node,id):
    if node.locked or node.anslocked>0 or node.deslocked==0:
        return False
    sub=set()
    if not func(node,sub,id):
        return False
    
    ascend(node, 1)
    
    for i in sub:
        unlock(i,id)
    
    node.locked=True
    node.id=id
    return True
    
    

def func(node,sub,id):
    if node is None:
        return True
    if node.locked:
        if node.id!=id:
            return False
        else:
            sub.add(node)
    
    for i in node.c:
        if not func(i,sub,id):
            return False
    return True

    
    

def ascend(node,val):
    if node is None:
        return
    node.anslocked+=val
    for i in node.c:
        ascend(i, val)
    

n = 7
m = 2

nodes = ['World', 'Asia','Africa', 'China','India', 'SouthAfrica', 'Egypt']
queries = ['1 China 9', '1 India 9','3 Asia 9', '2 India 9', '2 Asia 9']

dic={}
root=Node(nodes[0])
dic[nodes[0]]=root
q=nodes[1:]
n=[root]

while q:
    parent=n.pop(0)
    for i in range(m):
        if q:
            ele=q.pop(0)
            nele=Node(ele)
            dic[ele]=nele
            nele.parent=parent
            n.append(nele)
            parent.c.append(nele)
        
for i in queries:
    x,y,z=i.split()
    if x=="1":
        print(lock(dic[y],z))
    elif x=="2":
        print(unlock(dic[y],z))
    elif x=="3":
        print(upgrade(dic[y],z))