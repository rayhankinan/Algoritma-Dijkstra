'''
Dijkstra's Algorithm untuk mencari shortest path antara dua node
Sumber Pseudocode : Pemrograman Kompetitif Dasar
1. Pilih sebuah node yang belum dikunjungi dan memiliki dist terkecil. Sebut saja node
ini sebagai u.
2. Apabila tidak ada lagi node yang belum dikunjungi, atau dist[u] bernilai ∞, artinya
tidak ada lagi node yang dapat dikunjungi. Algoritma Dijkstra berakhir.
3. Karena u dikunjungi, maka set visited[u] = true. Kini dipastikan shortest path dari
s menuju u adalah dist[u]. Diketahui pula edge <pred[u],u> merupakan edge yang
perlu digunakan pada shortest path ke u.
4. Untuk setiap node v yang merupakan tetangga dari u, lakukan sebuah proses
yang disebut "relax". Proses relax untuk node u dan v adalah proses untuk
memperbaharui jarak terpendek mencapai v, apabila ternyata mencapai v melalui u
membutuhkan jarak yang lebih kecil. Dengan kata lain, dilakukan:
dist[v] = min(dist[v], dist[u] + w[u][v])
Setiap kali dist[v] mengalami perubahan, ubah nilai pred[v] menjadi u. Sebab sejauh
ini diketahui bahwa untuk mencapai v pada shortest path , node sebelumnya adalah
u.
5. Kembali ke langkah 1.
'''
import random
import tkinter
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from tkinter import BooleanVar

def start():
    global canvas1
    global label1
    global entry1
    global button1

    label1 = tkinter.Label(root, text='Masukkan jumlah node: ')
    label1.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label1)
    entry1 = tkinter.Entry(root)
    canvas1.create_window(200, 140, window=entry1)
    button1 = tkinter.Button(text='Input jumlah node', command=getJumlahNode, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

def getJumlahNode():
    global n
    global adjMatrix
    global temp
    global canvas1
    global label1
    global entry1
    global button1

    n = int(entry1.get())
    for i in range(n):
        for j in range(n):
            temp.append(float("Inf"))
        adjMatrix.append(temp)
        temp = []
    button1.destroy()
    label1.destroy()
    entry1.delete(0, 'end')
    entry1.insert(0, "")

    label1 = tkinter.Label(root, text='Masukkan jumlah edge: ')
    label1.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label1)
    entry1 = tkinter.Entry(root)
    canvas1.create_window(200, 140, window=entry1)
    button1 = tkinter.Button(text='Input jumlah edge', command=getJumlahEdge, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)


def getJumlahEdge():
    global m
    global index
    global adjMatrix
    global startPoint
    global endPoint
    global distance
    global DG
    global edge
    global weight
    global canvas1
    global label1
    global entry1
    global button1
    global pos
    global canvas

    m = int(entry1.get())
    index = 0
    block = BooleanVar(root, False)
    while index < m:
        def getStartPoint():
            global startPoint
            global index
            global canvas1
            global label1
            global entry1
            global button1

            startPoint = int(entry1.get())
            button1.destroy()
            label1.destroy()
            entry1.delete(0, 'end')
            entry1.insert(0, "")

            label1 = tkinter.Label(root, text=f'Masukkan titik akhir edge ke-{index + 1}: ')
            label1.config(font=('helvetica', 10))
            canvas1.create_window(200, 100, window=label1)
            button1 = tkinter.Button(text=f'Input titik akhir edge ke-{index + 1}', command=getEndPoint, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(200, 180, window=button1)
        
        def getEndPoint():
            global endPoint
            global index
            global canvas1
            global label1
            global entry1
            global button1

            endPoint = int(entry1.get())
            button1.destroy()
            label1.destroy()
            entry1.delete(0, 'end')
            entry1.insert(0, "")

            label1 = tkinter.Label(root, text=f'Masukkan waktu yang ditempuh dari node {startPoint} ke node {endPoint}: ')
            label1.config(font=('helvetica', 10))
            canvas1.create_window(200, 100, window=label1)
            button1 = tkinter.Button(text=f'Input waktu yang ditempuh dari node {startPoint} ke node {endPoint}', command=getDistance, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(200, 180, window=button1)
        
        def getDistance():
            global distance
            global adjMatrix
            global startPoint
            global endPoint
            global DG
            global edge
            global weight
            global canvas1
            global label1
            global entry1
            global button1

            distance = int(entry1.get())
            button1.destroy()
            label1.destroy()
            entry1.delete(0, 'end')
            entry1.insert(0, "")
            block.set(False)

            adjMatrix[startPoint][endPoint] = distance
            DG.add_edge(startPoint, endPoint, weight=distance)
            edge.append((startPoint, endPoint))
            weight[(startPoint, endPoint)] = distance
            
        entry1.delete(0, 'end')
        entry1.insert(0, "")

        label1 = tkinter.Label(root, text=f'Masukkan titik awal edge ke-{index + 1}: ')
        label1.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label1)
        button1 = tkinter.Button(text=f'Input titik awal edge ke-{index + 1}', command=getStartPoint, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 180, window=button1)

        block.set(True)
        root.wait_variable(block)
        index += 1

    button1.destroy()
    label1.destroy()
    entry1.delete(0, 'end')
    entry1.insert(0, "")

    pos = nx.spring_layout(DG, seed=seed)
    nx.draw_networkx_nodes(DG, pos)
    nx.draw_networkx_labels(DG, pos)
    nx.draw_networkx_edges(DG, pos, edgelist=edge, edge_color="k", style="dashed")
    nx.draw_networkx_edge_labels(DG, pos, edge_labels=weight)

    canvas.draw()

    getInput()

def getInput():
    global canvas1
    global label1
    global entry1
    global button1
    global DG
    global pos

    block = BooleanVar(root, False)
    while True:
        def getStartNode():
            global startNode
            global canvas1
            global label1
            global entry1
            global button1
            global DG
            global pos

            startNode = int(entry1.get())
            button1.destroy()
            label1.destroy()
            entry1.delete(0, 'end')
            entry1.insert(0, "")

            plt.clf()
            pos = nx.spring_layout(DG, seed=seed)
            nx.draw_networkx_nodes(DG, pos)
            nx.draw_networkx_labels(DG, pos)
            nx.draw_networkx_edges(DG, pos, edgelist=edge, edge_color="k", style="dashed")
            nx.draw_networkx_edge_labels(DG, pos, edge_labels=weight)

            canvas.draw()

            label1 = tkinter.Label(root, text='Masukkan titik tujuan node: ')
            label1.config(font=('helvetica', 10))
            canvas1.create_window(200, 100, window=label1)
            entry1 = tkinter.Entry(root)
            canvas1.create_window(200, 140, window=entry1)
            button1 = tkinter.Button(text='Input titik tujuan node', command=getEndNode, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(200, 180, window=button1)

        def getEndNode():
            global adjMatrix
            global startNode
            global endNode
            global answer
            global canvas1
            global label1
            global entry1
            global button1
            global pos
            global canvas

            endNode = int(entry1.get())
            answer = Dijkstra(adjMatrix, startNode, endNode)
            finalDistance = answer[0]
            pathTravelled = ""
            answer.remove(answer[0])
            for i in range(0, len(answer)):
                pathTravelled = pathTravelled + str(answer[i]) + " "
            not_answer = [edge[i] for i in range(len(edge)) if edge[i] not in answer]

            nx.draw_networkx_edges(DG, pos, edgelist=answer, edge_color="r")
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            plt.text(0, 1.1, f"Waktu tercepat yang dapat ditempuh dari node {startNode} ke node {endNode} adalah {finalDistance} menit dengan arah {pathTravelled}", 
                    transform=ax.transAxes, verticalalignment='top', bbox=props)
            red_line = mlines.Line2D([], [], color='red', label='Jalan yang dilewati')
            black_line = mlines.Line2D([],[], color='black', linestyle='dashed', label='Jalan yang tidak dilewati')
            plt.legend(handles=[red_line, black_line])
            button1.destroy()
            label1.destroy()
            entry1.delete(0, 'end')
            entry1.insert(0, "")

            block.set(False)

            canvas.draw()

        button1.destroy()
        label1.destroy()
        entry1.delete(0, 'end')
        entry1.insert(0, "")

        label1 = tkinter.Label(root, text='Masukkan titik asal node: ')
        label1.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label1)
        entry1 = tkinter.Entry(root)
        canvas1.create_window(200, 140, window=entry1)
        button1 = tkinter.Button(text='Input titik asal node', command=getStartNode, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 180, window=button1)
        
        block.set(True)
        root.wait_variable(block)

    button1.destroy()
    label1.destroy()
    entry1.delete(0, 'end')
    entry1.insert(0, "")

    start()

def _quit():
    root.quit()
    root.destroy()

def printDistance(dist, startNode, endNode):
    if dist[endNode] == float("Inf"):
        return None
    else:
        return dist[endNode]

def printPath(pred, startNode, endNode):
    result = []
    while pred[endNode] != -1:
        result.append((pred[endNode], endNode))
        endNode = pred[endNode]
    result.reverse()
    return result

def Dijkstra(adjMatrix, startNode, endNode):
    dist = [float("Inf") for i in range(len(adjMatrix))]
    visited = [False for i in range(len(adjMatrix))]
    pred = [-1 for i in range(len(adjMatrix))]

    dist[startNode] = 0
    while True: # Perulangan ini akan diakhiri dengan break
        u = -1
        minDist = float("Inf")
        for i in range(len(adjMatrix)): # Cari node yang belum dikunjungi dan memiliki dist terkecil
            if not visited[i] and dist[i] < minDist:
                u = i
                minDist = dist[i]
        if u == -1 or dist[u] == float("Inf"):
            break # Akhiri perulangan while

        visited[u] = True
        for v in range(len(adjMatrix)): # Lakukan relax untuk semua tetangga u
            if dist[v] > dist[u] + adjMatrix[u][v]:
                dist[v] = dist[u] + adjMatrix[u][v]
                pred[v] = u

    return [printDistance(dist, startNode, endNode)] + printPath(pred, startNode, endNode)

if __name__ == "__main__":

    root = tkinter.Tk()
    root.wm_title("Dijkstra's Algorithm")

    adjMatrix = []
    temp = []
    edge = []
    weight = {}
    index = 0
    n = 0
    m = 0
    startPoint = 0
    endPoint = 0
    distance = 0
    startNode = 0
    endNode = 0
    answer = []
    pathTravelled = ""
    not_answer = []
    seed = random.randint(0, 100)

    DG = nx.DiGraph()
    fig = plt.figure()
    ax = fig.add_subplot(111)

    quit_button = tkinter.Button(master=root, text="Quit", command=_quit)
    quit_button.pack(side=tkinter.BOTTOM)

    canvas1 = tkinter.Canvas(root, width = 400, height = 300,  relief = 'raised')
    canvas1.pack(side=tkinter.BOTTOM)

    label0 = tkinter.Label(root, text='Simulasi Google Maps / Waze')
    label0.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label0)

    canvas = FigureCanvasTkAgg(fig, master=root)
    plt.gca().axes.xaxis.set_ticks([])
    plt.gca().axes.yaxis.set_ticks([])
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    start()

    tkinter.mainloop()
