import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

def msh_reader_2D(filename):
    filepath = os.path.join(os.getcwd(),filename)
    assert os.path.exists(filepath), "Wrong filename!"

    mshFile = open(filepath)
    mshData = mshFile.readlines()

    entityStartIndex = mshData.index("$Entities\n")

    #The first line below the word $Entities will have the number of entities of each dimension
    numPoints = int(mshData[entityStartIndex+1].split()[0])
    numCurves = int(mshData[entityStartIndex+1].split()[1])
    
    #Storing points information
    pointStartIndex = entityStartIndex + 2
    points = {}
    numPointFlags = {}
    pointFlags = {}
    for i in range(pointStartIndex, pointStartIndex+numPoints):
        id = int(mshData[i].split()[0]) - 1
        points[id] = (float(mshData[i].split()[1]), float(mshData[i].split()[2]), float(mshData[i].split()[3]))
        numPointFlags[id] = int(mshData[i].split()[4])
        if(numPointFlags[id] != 0):
            pointFlags[id] = int(mshData[i].split()[5])
        
    
    #Curves
    curveStartIndex = pointStartIndex + numPoints
    numCurveFlags = {}
    curveFlags = {}
    for i in range(curveStartIndex, curveStartIndex + numCurves):
        id = int(mshData[i].split()[0]) + numPoints - 1
        numCurveFlags[id] = int(mshData[i].split()[7])
        curveFlags[id] = int(mshData[i].split()[8])

    nodeStartIndex = mshData.index("$Nodes\n")

    #First line below the word $Nodes.
    numNodeBlocks = int(mshData[nodeStartIndex + 1].split()[0])

    currentLine = nodeStartIndex + 2

    nodes = []
    nodeFlag = []
    for i in range(numNodeBlocks):
        parentDim = int(mshData[currentLine].split()[0])
        parentEntityID = int(mshData[currentLine].split()[1]) - 1
        numNodesInBlock = int(mshData[currentLine].split()[3])

        if(parentDim == 0):
            parentEntityGlobalID = parentEntityID
            flag = pointFlags[parentEntityGlobalID]
        elif(parentDim == 1):
            parentEntityGlobalID = parentEntityID + numPoints
            flag = curveFlags[parentEntityGlobalID]
        else:
            parentEntityGlobalID = parentEntityID + numPoints + numCurves
            flag = 0
        
        currentLine += 1

        for j in range(currentLine, currentLine + numNodesInBlock):
            id = int(mshData[j].split()[0]) - 1
            xcoord = float(mshData[j+numNodesInBlock].split()[0])
            ycoord = float(mshData[j+numNodesInBlock].split()[1])
            zcoord = float(mshData[j+numNodesInBlock].split()[2])

            nodes.append([xcoord, ycoord])
            nodeFlag.append(flag)
        
        currentLine = currentLine + 2*numNodesInBlock

    #Read in the elements.
    elementStartIndex = mshData.index("$Elements\n")
    numElementBlocks = int(mshData[elementStartIndex + 1].split()[0])

    currentLine = elementStartIndex + 2

    elements = []
    elemFlag = []
    for i in range(0, numElementBlocks):
        elParentEntityDim = int(mshData[currentLine].split()[0])
        numElInBlock = int(mshData[currentLine].split()[3])

        if(elParentEntityDim != 2):
            currentLine += 1 + numElInBlock
        else:
            currentLine = currentLine + 1

            for j in range(currentLine, currentLine + numElInBlock):
                id = int(mshData[j].split()[0])
                nodelist = []
                for k in range(1, 4):
                    nodelist.append(int(mshData[j].split()[k]))
                elements.append(nodelist)
                elemFlag.append(5)
            currentLine = currentLine + numElInBlock

    p = np.asarray(nodes)
    LM = np.asarray(elements).T
    nodeFlag = np.asarray(nodeFlag)
    elemFlag = np.asarray(elemFlag)
    
    return p, LM, nodeFlag

def plot_mesh(numel, p, LM):
    # Loop on elements and plot each
    for n in range(numel):
        # Element nodal coordinates
        x = p[LM[:,n]-1, 0]
        y = p[LM[:,n]-1, 1]
        # Add to plot
        plt.fill(x, y, edgecolor='black', fill=False)

def plot_solution_contour(numel, p, LM, u):
    triang = mtri.Triangulation(p[:,0], p[:,1], LM.T-1)
    plt.figure(1)
    levels = np.linspace(min(u), max(u), 11)
    plt.tricontourf(triang, u, levels=levels, cmap='rainbow')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('u', rotation=90)
    plot_mesh(numel, p, LM)
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'$u(x,y)$ over the domain')
    plt.show()