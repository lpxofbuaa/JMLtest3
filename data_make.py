import random
import sys

pnodesmin = 70
pnodesmax = 80

randommode = False

nodescountmax = 100

intlen = 100
intlist = []
for i in range(intlen):
    r = (random.randint(-2147483648,2147483647))
    while (r in intlist):
        r = (random.randint(-2147483648,2147483647))
    intlist.append(r)

container = {}
idlist = []
nodeList = []
nodecounter = {}
counter = 0

fout = None

#########################50 max#####################################

def add(path = []):
    global nodeList
    global container
    global idlist
    global nodecounter
    addop = 'PATH_ADD'
    if (path == []):
        total = random.randint(pnodesmin,pnodesmax)
        datas = []
        for i in range(total):
            if (len(nodeList) < nodescountmax):
                data = str(intlist[random.randint(0,intlen - 1)])
                if (int(data) in nodecounter):
                    nodecounter[int(data)] += 1
                else:
                    nodeList.append(int(data))
                    nodecounter[int(data)] = 1
            else:
                data = nodeList[random.randint(0,len(nodeList) - 1)]
                nodecounter[data] += 1
            datas.append(int(data))
            addop = addop + ' ' + str(data)
        fout.write(addop)
        return datas
    else:
        for i in path:
            addop = addop + ' ' + str(i)
        fout.write(addop)
        return path
    
def remove(path = []):
    global nodeList
    global container
    global idlist
    global nodecounter
    removeop = 'PATH_REMOVE'
    if (path == []):
        total = random.randint(pnodesmin,pnodesmax)
        diffcount = random.randint(5,1200)
        datas = ''
        for i in range(total):
            data = str(intlist[random.randint(0,intlen - 1)])
            path.append(int(data))
            datas = datas + ' ' + data
        for i in container:
            if (len(container[i]) == len(path)):
                t = True
                for j in range(len(path)):
                    if (path[j] != container[i][j]):
                        t = False
                        break
                if (t):
                    for j in path:
                        nodecounter[j] -= 1
                        if (nodecounter[j] == 0):
                            del nodecounter[j]
                            nodeList.remove(j)
                    del container[i]
                    idlist.remove(i)
        removeop = removeop + datas
        fout.write(removeop)
    else:
        for i in path:
            removeop = removeop + ' ' + str(i)
        fout.write(removeop)
        fout.write('\n')
        r = random.randint(1,7)
        if (r == 1):
            r = random.randint(0,len(path) - 1)
            containsnode(path[r])
        elif (r == 2):
            r = random.randint(0,len(path) - 2)
            containsedge(path[r],path[r+1])
        elif (r == 3):
            connectblockscoount()
        elif (r == 4):
            r1 = random.randint(0,len(path) - 1)
            r2 = random.randint(0,len(path) - 1)
            shortroadlen(path[r1],path[r2])
        elif (r == 5):
            r1 = random.randint(0,len(path) - 1)
            r2 = random.randint(0,len(path) - 1)
            leastticketprice(path[r1],path[r2])
        elif (r == 6):
            r1 = random.randint(0,len(path) - 1)
            r2 = random.randint(0,len(path) - 1)
            leasttransfer(path[r1],path[r2])
        else:
            r1 = random.randint(0,len(path) - 1)
            r2 = random.randint(0,len(path) - 1)
            leastunpleasant(path[r1],path[r2])

        
def removeid(id = -1):
    global nodeList
    global container
    global idlist
    global nodecounter
    removeidop = 'PATH_REMOVE_BY_ID'
    if (id == -1):
        id = random.randint(-2147483648,2147483647)
        if id in container:
            for i in container[id]:
                nodecounter[i] -= 1
                if (nodecounter[i] == 0):
                    del nodecounter[i]
                    nodeList.remove(i)
            del container[id]
            idlist.remove(id)
        removeidop = removeidop + ' ' + str(id)
        fout.write(removeidop)
    else:
        removeidop = removeidop + ' ' + str(id)
        fout.write(removeidop)


###############################1000 max include add remove####################################################

def getid(path = []):
    getidop = 'PATH_GET_ID'
    if (path == []):
        total = random.randint(pnodesmin,pnodesmax)
        datas = ''
        diffcount = random.randint(5,1200)
        for i in range(total):
            data = str(intlist[random.randint(0,intlen - 1)])
            datas = datas + ' ' + data
    else:
        datas = ''
        for i in path:
            datas = datas + ' ' + str(i)
    getidop = getidop + datas
    fout.write(getidop)

def get(id = -1):
    getop = 'PATH_GET_BY_ID'
    if (id == -1):
        id = random.randint(1,300)
    getop = getop + ' ' + str(id)
    fout.write(getop)

def contains(path = []):
    containsop = 'CONTAINS_PATH'
    if (path == []):
        total = random.randint(pnodesmin,pnodesmax)
        datas = ''
        diffcount = random.randint(5,1200)
        for i in range(total):
            data = str(intlist[random.randint(0,intlen - 1)])
            datas = datas + ' ' + data
    else:
        datas = ''
        for i in path:
            datas = datas + ' ' + str(i)
    containsop = containsop + datas
    fout.write(containsop)

def compare(id1 = -1,id2 = -1):
    compareop = 'COMPARE_PATHS'
    if (id1 == -1):
        id1 = random.randint(1,300)
    if (id2 == -1):
        id2 = random.randint(1,300)
    compareop = compareop + ' ' + str(id1) + ' ' + str(id2)
    fout.write(compareop)

##############################any ok#####################################################

def count():
    countop = 'PATH_COUNT'
    fout.write(countop)

def size(id = -1):
    sizeop = 'PATH_SIZE'
    if (id == -1):
        id = random.randint(1,300)
    sizeop = sizeop + ' ' + str(id)
    fout.write(sizeop)

def pdiffnode(id = -1):
    pdiffnodeop = 'PATH_DISTINCT_NODE_COUNT'
    if (id == -1):
        id = random.randint(1,300)
    pdiffnodeop = pdiffnodeop + ' ' + str(id)
    fout.write(pdiffnodeop)

def containsid(id = -1):
    containsidop = 'CONTAINS_PATH_ID'
    if (id == -1):
        id = random.randint(1,300)
    containsidop = containsidop + ' ' + str(id)
    fout.write(containsidop)

def diffnodes():
    diffnodesop = 'DISTINCT_NODE_COUNT'
    fout.write(diffnodesop)

def pcontainnode(id = -1,node = None):
    pcontainnodeop = 'PATH_CONTAINS_NODE'
    if (id == -1):
        id = random.randint(1,300)
    if (node == None):
        node = intlist[random.randint(0,intlen - 1)]
    pcontainnodeop = pcontainnodeop + ' ' + str(id) + ' ' + str(node)
    fout.write(pcontainnodeop)

#14
def containsnode(node = None):
    if (node == None):
        node = intlist[random.randint(0,intlen - 1)]
    containsnodeop = 'CONTAINS_NODE ' + str(node)
    fout.write(containsnodeop)

#15
def containsedge(a = None, b = None):
    if (a == None):
        a = intlist[random.randint(0,intlen - 1)]
    if (b == None):
        b = intlist[random.randint(0,intlen - 1)]
    containsedgeop = 'CONTAINS_EDGE ' + str(a) + ' ' + str(b)    
    fout.write(containsedgeop)

#16
def isnodeconnected(a = None, b = None):
    if (a == None):
        a = intlist[random.randint(0,intlen - 1)]
    if (b == None):
        b = intlist[random.randint(0,intlen - 1)]
    isnodeconnectedop = 'IS_NODE_CONNECTED ' + str(a) + ' ' + str(b)
    fout.write(isnodeconnectedop)

#17
def shortroadlen(a = None, b = None):
    if (a == None):
        a = intlist[random.randint(0,intlen - 1)]
    if (b == None):
        b = intlist[random.randint(0,intlen - 1)]
    shortroadlenop = 'SHORTEST_PATH_LENGTH ' + str(a) + ' ' + str(b)
    fout.write(shortroadlenop)

##########################################jml 3#############################################################

#18
def connectblockscoount():
    fout.write('CONNECTED_BLOCK_COUNT')

#19
def leastticketprice(a = None, b = None):
    if (a == None):
        a = intlist[random.randint(0,intlen - 1)]
    if (b == None):
        b = intlist[random.randint(0,intlen - 1)]
    leastop = 'LEAST_TICKET_PRICE ' + str(a) + ' ' + str(b)
    fout.write(leastop)

#20
def leasttransfer(a = None, b = None):
    if (a == None):
        a = intlist[random.randint(0,intlen - 1)]
    if (b == None):
        b = intlist[random.randint(0,intlen - 1)]
    leastop = 'LEAST_TRANSFER_COUNT ' + str(a) + ' ' + str(b)
    fout.write(leastop)

#21
def leastunpleasant(a = None, b = None):
    if (a == None):
        a = intlist[random.randint(0,intlen - 1)]
    if (b == None):
        b = intlist[random.randint(0,intlen - 1)]
    leastop = 'LEAST_UNPLEASANT_VALUE ' + str(a) + ' ' + str(b)
    fout.write(leastop)

def makeop(opnum):
    global counter
    global idlist
    global container
    global nodeList
    global nodecounter
    if (opnum == 1):
        path = add()
        counter+=1
        container[counter] = path
        idlist.append(counter)
    elif (opnum == 2):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            remove()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            path = container[idlist[i]]
            for j in path:
                nodecounter[j] -= 1
                if (nodecounter[j] == 0):
                    del nodecounter[j]
                    nodeList.remove(j)
            del container[idlist[i]]
            del idlist[i]
            remove(path)
    elif (opnum == 3):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            removeid()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            rid = idlist[i]
            path = container[idlist[i]]
            for j in container[idlist[i]]:
                nodecounter[j] -= 1
                if (nodecounter[j] == 0):
                    del nodecounter[j]
                    nodeList.remove(j)
            del container[idlist[i]]
            del idlist[i]
            removeid(rid)
            fout.write('\n')
            r = random.randint(1,7)
            if (r == 1):
                r = random.randint(0,len(path) - 1)
                containsnode(path[r])
            elif (r == 2):
                r = random.randint(0,len(path) - 2)
                containsedge(path[r],path[r+1])
            elif (r == 3):
                connectblockscoount()
            elif (r == 4):
                r1 = random.randint(0,len(path) - 1)
                r2 = random.randint(0,len(path) - 1)
                shortroadlen(path[r1],path[r2])
            elif (r == 5):
                r1 = random.randint(0,len(path) - 1)
                r2 = random.randint(0,len(path) - 1)
                leastticketprice(path[r1],path[r2])
            elif (r == 6):
                r1 = random.randint(0,len(path) - 1)
                r2 = random.randint(0,len(path) - 1)
                leasttransfer(path[r1],path[r2])
            else:
                r1 = random.randint(0,len(path) - 1)
                r2 = random.randint(0,len(path) - 1)
                leastunpleasant(path[r1],path[r2])

    elif (opnum == 4):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            getid()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            path = container[idlist[i]]
            getid(path)
    elif (opnum == 5):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            get()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            rid = idlist[i]
            get(rid)
    elif (opnum == 6):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            contains()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            path = container[idlist[i]]
            contains(path)
    elif (opnum == 7):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        if (r1 == 1)|(idlist==[]):
            r1 = -1
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            r1 = idlist[i]
        if (r2 == 1)|(idlist==[]):
            r2 = -1
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            r2 = idlist[i]
        compare(r1,r2)
    elif (opnum == 8):
        count()
    elif (opnum == 9):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            size()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            rid = idlist[i]
            size(rid)
    elif (opnum == 10):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            pdiffnode()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            rid = idlist[i]
            pdiffnode(rid)
    elif (opnum == 11):
        r = random.randint(1,6)
        if (r <= 2)|(idlist==[]):
            containsid()
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            rid = idlist[i]
            containsid(rid)
    elif (opnum == 12):
        diffnodes()
    elif (opnum == 13):
        rid = random.randint(1,6)
        rnode = random.randint(1,6)
        path = []
        if (rid == 1)|(idlist==[]):
            rid = -1
        else:
            i = random.randint(0,max(len(idlist) - 1,0))
            rid = idlist[i]
            path = container[rid]
        if (rnode == 1):
            rnode = None
        elif (rid != -1):
            rnode = path[random.randint(0,len(path) - 1)]
        else:
            rnode = None
        pcontainnode(rid,rnode)
    elif (opnum == 14):
        rid = random.randint(1,6)
        if ((rid <= 1)|(len(nodeList) == 0)):
            containsnode()
        else:
            rid = random.randint(0,len(nodeList) - 1)
            rid = nodeList[rid]
            containsnode(rid)
    elif (opnum == 15):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        if ((r1 == 1)|(len(nodeList) == 0)):
            r1 = None
        else:
            r1 = nodeList[random.randint(0,len(nodeList) - 1)]
        if ((r2 == 1)|(len(nodeList) == 0)):
            r2 = None
        else:
            r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        containsedge(r1,r2)
    elif (opnum == 16):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        if ((r1 == 1)|(len(nodeList) == 0)):
            r1 = None
        else:
            r1 = nodeList[random.randint(0,len(nodeList) - 1)]
        if ((r2 == 1)|(len(nodeList) == 0)):
            r2 = None
        else:
            r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        isnodeconnected(r1,r2)
    elif (opnum == 17):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        if (len(nodeList) == 0)|(r1 == 1):
            r1 = None
        else:
            r1 = nodeList[random.randint(0,len(nodeList) - 1)]
        if (len(nodeList) == 0)|(r2 == 1):
            r2 = None
        else:
            r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        shortroadlen(r1,r2)
    elif (opnum == 18):
        connectblockscoount()
    elif (opnum == 19):
        if (randommode):
            r1 = random.randint(1,6)
            r2 = random.randint(1,6)
            if (len(nodeList) == 0)|(r1 == 1):
                r1 = None
            else:
                r1 = nodeList[random.randint(0,len(nodeList) - 1)]
            if (len(nodeList) == 0)|(r2 == 1):
                r2 = None
            else:
                r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        else:
            if (len(nodeList) == 0):
                r1 = None
            else:
                r1 = nodeList[random.randint(0,len(nodeList) - 1)]
            if (len(nodeList) == 0):
                r2 = None
            else:
                r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        leastticketprice(r1,r2)
    elif (opnum == 20):
        if (randommode):
            r1 = random.randint(1,6)
            r2 = random.randint(1,6)
            if (len(nodeList) == 0)|(r1 == 1):
                r1 = None
            else:
                r1 = nodeList[random.randint(0,len(nodeList) - 1)]
            if (len(nodeList) == 0)|(r2 == 1):
                r2 = None
            else:
                r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        else:
            if (len(nodeList) == 0):
                r1 = None
            else:
                r1 = nodeList[random.randint(0,len(nodeList) - 1)]
            if (len(nodeList) == 0):
                r2 = None
            else:
                r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        leasttransfer(r1,r2)
    elif (opnum == 21):
        if (randommode):
            r1 = random.randint(1,6)
            r2 = random.randint(1,6)
            if (len(nodeList) == 0)|(r1 == 1):
                r1 = None
            else:
                r1 = nodeList[random.randint(0,len(nodeList) - 1)]
            if (len(nodeList) == 0)|(r2 == 1):
                r2 = None
            else:
                r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        else:
            if (len(nodeList) == 0):
                r1 = None
            else:
                r1 = nodeList[random.randint(0,len(nodeList) - 1)]
            if (len(nodeList) == 0):
                r2 = None
            else:
                r2 = nodeList[random.randint(0,len(nodeList) - 1)]
        leastunpleasant(r1,r2)

def createop(mode='random'):
    if (mode == 'random'):
        gengraph = random.randint(5,19)
        line = random.randint(1,500 - gengraph)
        total = random.randint(line + gengraph + 2500,7000)
        op = []
        for _ in range(gengraph):
            op.append(random.randint(1,30)%3 + 1)
        for _ in range(line):
            op.append(random.randint(1,40)%4 + 4)
        for _ in range(total - line - gengraph):
            op.append(random.randint(1,280)%14 + 8)
        random.shuffle(op)
        # makeop(1)
        # fout.write('\n')
        for i in range(len(op)):
            makeop(op[i])
            if (i < len(op) - 1):
                fout.write('\n')
        print('have ' + str(len(nodeList)) + ' distinct nodes!')
    elif (mode == 'jml2test'):
        gengraph = random.randint(5,19)
        make = random.randint(int(gengraph/2),gengraph - 1)
        removes = gengraph - make
        # make = make + removes
        # removes = 0
        line = random.randint(1,500 - gengraph)
        total = random.randint(line + gengraph + 3000,7000)
        op = []
        for _ in range(make):
            op.append(1)
        for _ in range(removes):
            op.append(random.randint(1,20)%2 + 2)
        for _ in range(line):
            op.append(random.randint(1,40)%4 + 4)
        for _ in range(total - line - gengraph):
            r = random.randint(1,550)%55
            if (r >= 10)&(r < 20):
                r = 14
            elif (r >= 20)&(r < 30):
                r = 15
            elif (r >= 30)&(r < 40):
                r = 16
            elif (r >= 40)&(r < 55):
                r = 17
            else:
                r += 8
            op.append(r)
        random.shuffle(op)
        makeop(1)
        fout.write('\n')
        for i in range(len(op)):
            makeop(op[i])
            if (i < len(op) - 1):
                fout.write('\n')
        print('have ' + str(len(nodeList)) + ' distinct nodes!')
    elif (mode == 'jml3test'):
        gengraph = random.randint(20,45)
        make = random.randint(gengraph//2,gengraph-1)
        removes = gengraph - make
        # make = make + removes
        # removes = 0
        line = random.randint(100,900 - gengraph)
        total = random.randint(4000,5500)
        op = []
        for _ in range(make):
            op.append(1)
        for _ in range(removes):
            op.append(random.randint(1,20)%2 + 2)
        for _ in range(line):
            op.append(random.randint(1,40)%4 + 4)
        for _ in range(total - line - gengraph):
            r = random.randint(1,1080)%154
            if (r >= 14)&(r < 34):
                r = 18
            elif (r >= 34)&(r < 54):
                r = 19
            elif (r >= 54)&(r < 74):
                r = 20
            elif (r >= 74)&(r < 94):
                r = 21
            elif (r >= 94)&(r < 114):
                r = 17
            elif (r >= 114)&(r < 134):
                r = 15
            elif (r >= 134)&(r < 154):
                r = 14
            else:
                r += 8
            op.append(r)
        random.shuffle(op)
        # op = op[0:98]
        makeop(1)
        fout.write('\n')
        for i in range(len(op)):
            makeop(op[i])
            if (i < len(op) - 1):
                fout.write('\n')
        print('have ' + str(len(nodeList)) + ' distinct nodes!')
    elif (mode == 'shortmain'):
        gengraph = random.randint(40,45)
        make = random.randint(int(gengraph/2),gengraph - 2)
        removes = gengraph - make
        # make = make + removes
        # removes = 0
        line = random.randint(500,800 - gengraph)
        total = random.randint(line + gengraph + 3000,6000)
        op = []
        for _ in range(make):
            op.append(1)
        for _ in range(removes):
            op.append(random.randint(1,20)%2 + 2)
        for _ in range(line):
            op.append(random.randint(1,40)%4 + 4)
        for _ in range(total - line - gengraph):
            r = random.randint(1,1280)%64
            if (r >= 14)&(r < 24):
                r = 17
            elif (r >= 24)&(r < 34):
                r = 19
            elif (r >= 34)&(r < 44):
                r = 20
            elif (r >= 44)&(r < 54):
                r = 21
            elif (r >= 54)&(r < 64):
                r = 18
            else:
                r += 8
            op.append(r)
        random.shuffle(op)
        makeop(1)
        fout.write('\n')
        for i in range(len(op)):
            makeop(op[i])
            if (i < len(op) - 1):
                fout.write('\n')
        print('have ' + str(len(nodeList)) + ' distinct nodes!')

if __name__ == "__main__":
    fout = open('data/' + 'data' + str(sys.argv[1]) + '.txt','w')
    if ((sys.argv[2] != 'jml2test')&(sys.argv[2] != 'random')&(sys.argv[2] != 'shortmain')&(sys.argv[2] != 'jml3test')):
        print('Something wrong about you data_make mode')
        print('Please check again')
        print('Now make random data:')
        createop()
    else:
        createop(sys.argv[2])
    print('data gen finish!')
    fout.close()
            
        
            

