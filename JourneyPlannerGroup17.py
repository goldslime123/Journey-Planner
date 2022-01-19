import turtle
import pygame
from math import *

# Set title to the window
from pip._vendor.msgpack.fallback import xrange

pygame.init()
pygame.display.set_caption("Journey Planner")

# Open a window
window_width = 800
window_height = 730
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# MRT LINES
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)

# BUS LINES
ROSY_BROWN = (188, 143, 143)

# Node colors
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)

# Default font size
font_obj = pygame.font.Font('freesansbold.ttf', 22)
font_color = BLACK

# 21 mrt stns x,y coord
HarbourFront = [245, 685]
BuonaVista = [70, 410]
BotanicGarden = [130, 230]
Caldecott = [220, 150]
Bishan = [355, 105]
Serangoon = [515, 140]
MacPherson = [650, 280]
PayaLebar = [675, 345]
Promenade = [620, 590]
BayFront = [560, 650]
MarinaBay = [445, 680]
RafflesPlace = [445, 615]
CityHall = [446, 565]
Bugis = [530, 485]
LittleIndia = [400, 360]
Newton = [305, 260]
Steven = [220, 230]
Orchard = [245, 345]
DhobyGhaut = [360, 475]
ChinaTown = [310, 525]
OutramPark = [260, 580]

# bus stns near the area x,y coord
AndrewRd = [250, 190]
TyersallAve = [200, 400]
OppBlk177 = [340, 380]
BraddelFlyover = [400, 200]
Bendemeer_Road = [550, 300]
Esplanade = [600, 500]
PSA_KEPPEL = [350, 680]
Middle_Road = [485, 490]

# to get the node that the user clicked include both bus and mrt stn
lis_of_xcoord = [
    245, 70, 130, 220, 355, 515, 650, 675, 620, 560, 445, 445, 446, 530, 400,
    305, 220, 245, 360, 310, 260, 250, 200, 340, 400, 550, 600, 350, 485
]
lis_of_ycoord = [
    685, 410, 230, 150, 105, 140, 280, 345, 590, 650, 680, 615, 565, 485, 360,
    260, 230, 345, 475, 525, 580, 190, 400, 380, 200, 300, 500, 680, 490
]

# name of all location
location = [
    "HarbourFront", "BuonaVista", "BotanicGarden", "Caldecott", "Bishan",
    "Serangoon", "MacPherson", "PayaLebar", "Promenade", "BayFront",
    "MarinaBay", "RafflesPlace", "CityHall", "Bugis", "LittleIndia", "Newton",
    "Steven", "Orchard", "DhobyGhaut", "ChinaTown", "OutramPark", "AndrewRd",
    "TyersallAve", "OppBlk177", "BraddelFlyover", "Bendemeer_Road",
    "Esplanade", "PSA_KEPPEL", "Middle_Road"
]

# contain list of list of xy coord for all location
location_coord = [
    HarbourFront, BuonaVista, BotanicGarden, Caldecott, Bishan, Serangoon,
    MacPherson, PayaLebar, Promenade, BayFront, MarinaBay, RafflesPlace,
    CityHall, Bugis, LittleIndia, Newton, Steven, Orchard, DhobyGhaut,
    ChinaTown, OutramPark, AndrewRd, TyersallAve, OppBlk177, BraddelFlyover,
    Bendemeer_Road, Esplanade, PSA_KEPPEL, Middle_Road
]

# global var to pass to background() function
mrt_graph = {}
mrt_bus_graph = {}

# 2 dict one for mrt and mrt with bus
# actual time used for the cost
def initialization():
    global mrt_graph, mrt_bus_graph
    mrt_bus_graph = {
        'HarbourFront': {
            'OutramPark': [3, 'NorthEast Line'],
            'BuonaVista': [15, 'Circle Line'],
            'PSA_KEPPEL': [5, '100']
        },
        'BuonaVista': {
            'BotanicGarden': [7, 'Circle Line'],
            'HarbourFront': [12, 'Circle Line'],
            'OutramPark': [15, 'NorthEast Line'],
            'TyersallAve': [11, '106']
        },
        'BotanicGarden': {
            'Steven': [2, 'Downtown Line'],
            'Caldecott': [5, 'Circle Line'],
            'BuonaVista': [7, 'EastWest Line'],
            'AndrewRd': [9, '54']
        },
        'Caldecott': {
            'BotanicGarden': [5, 'Downtown Line'],
            'Bishan': [5, 'Circle Line'],
            'AndrewRd': [2, '162']
        },
        'Bishan': {
            'Serangoon': [4, 'Circle Line'],
            'Caldecott': [5, 'Circle Line'],
            'Newton': [9, 'NorthSouth Line'],
            'AndrewRd': [9, '54']
        },
        'Serangoon': {
            'Bishan': [4, 'Circle Line'],
            'MacPherson': [7, 'Circle Line'],
            'LittleIndia': [10, 'NorthEast Line'],
            'OppBlk177': [18, '105'],
            'BraddelFlyover': [6, '153'],
            'Bendemeer_Road': [14, '147']
        },
        'MacPherson': {
            'PayaLebar': [2, 'Circle Line'],
            'Serangoon': [7, 'Circle Line'],
            'ChinaTown': [13, 'NorthEast Line'],
            'Bendemeer_Road': [17, '65']
        },
        'PayaLebar': {
            'MacPherson': [2, 'Circle Line'],
            'Promenade': [10, 'Circle Line'],
            'Bugis': [9, 'EastWest Line']
        },
        'Promenade': {
            'BayFront': [2, 'Circle Line'],
            'DhobyGhaut': [2, 'Circle Line'],
            'Bugis': [2, 'Downtown Line'],
            'PayaLebar': [10, 'Circle Line']
        },
        'BayFront': {
            'Promenade': [2, 'Downtown Line'],
            'MarinaBay': [2, 'Circle Line'],
            'ChinaTown': [5, 'Downtown Line'],
            'Esplanade': [7, '57']
        },
        'MarinaBay': {
            'RafflesPlace': [2, 'NorthSouth Line'],
            'BayFront': [2, 'Circle Line'],
            'PSA_KEPPEL': [11, '100'],
            'MarinaBay': [7, '57']
        },
        'Steven': {
            'BotanicGarden': [2, 'Downtown Line'],
            'Newton': [3, 'Downtown Line'],
            'BraddelFlyover': [19, '153']
        },
        'Newton': {
            'LittleIndia': [1, 'Downtown Line'],
            'Steven': [3, 'Downtown Line'],
            'Orchard': [3, 'NorthSouth Line'],
            'Bishan': [9, 'NorthSouth Line']
        },
        'Orchard': {
            'Newton': [3, 'NorthSouth Line'],
            'DhobyGhaut': [4, 'NorthSouth Line'],
            'OppBlk177': [19, '105']
        },
        'LittleIndia': {
            'Newton': [1, 'Downtown Line'],
            'DhobyGhaut': [2, 'NorthEast Line'],
            'Bugis': [4, 'Downtown Line'],
            'Serangoon': [10, 'NorthSouth Line']
        },
        'DhobyGhaut': {
            'LittleIndia': [2, 'NorthSouth Line'],
            'CityHall': [3, 'NorthSouth Line'],
            'Orchard': [4, 'NorthSouth Line'],
            'ChinaTown': [4, 'NorthEast Line'],
            'Promenade': [6, 'Circle Line'],
            'AndrewRd': [21, '162'],
            'TyersallAve': [13, '106']
        },
        'Bugis': {
            'Promenade': [2, 'Downtown Line'],
            'CityHall': [3, 'EastWest Line'],
            'LittleIndia': [4, 'Downtown Line'],
            'PayaLebar': [9, 'EastWest Line'],
            'Esplanade': [4, '56'],
            'Middle_Road': [6, '123']
        },
        'ChinaTown': {
            'OutramPark': [2, 'NorthEast Line'],
            'DhobyGhaut': [4, 'NorthEast Line'],
            'BayFront': [5, 'Circle Line'],
            'MacPherson': [13, 'Downtown Line']
        },
        'CityHall': {
            'RafflesPlace': [2, 'NorthSouth Line'],
            'DhobyGhaut': [3, 'NorthSouth Line'],
            'PayaLebar': [12, 'EastWest Line'],
            'TyersallAve': [21, '174']
        },
        'RafflesPlace': {
            'CityHall': [2, 'NorthSouth Line'],
            'MarinaBay': [2, 'NorthSouth Line'],
            'OutramPark': [5, 'EastWest Line']
        },
        'OutramPark': {
            'ChinaTown': [2, 'NorthEast Line'],
            'HarbourFront': [3, 'NorthEast Line'],
            'RafflesPlace': [5, 'EastWest Line'],
            'BuonaVista': [12, 'EastWest Line']
        },
        'AndrewRd': {
            'Caldecott': [2, '162'],
            'DhobyGhaut': [21, '162'],
            'Bishan': [8, '54'],
            'BotanicGarden': [9, '54'],
            'BraddelFlyover': [8, '93']
        },
        'TyersallAve': {
            'BuonaVista': [11, '106'],
            'DhobyGhaut': [13, '106'],
            'CityHall': [21, '174']
        },
        'OppBlk177': {
            'Serangoon': [18, '105'],
            'Orchard': [19, '105'],
            'BraddelFlyover': [10, '153'],
            'LittleIndia': [21, '56']
        },
        'BraddelFlyover': {
            'Serangoon': [6, '153'],
            'Steven': [19, '153'],
            'OppBlk177': [10, '153'],
            'AndrewRd': [8, '93']
        },
        'Bendemeer_Road': {
            'Serangoon': [14, '147'],
            'Middle_Road': [18, '147'],
            'MacPherson': [17, '65']
        },
        'Esplanade': {
            'Bugis': [4, '56'],
            'MarinaBay': [7, '57']
        },
        'PSA_KEPPEL': {
            'HarbourFront': [5, '100'],
            'MarinaBay': [11, '100']
        },
        'Middle_Road': {
            'Bendemeer_Road': [18, '147'],
            'Bugis': [6, '123']
        }
    }

    mrt_graph = {
        'HarbourFront': {
            'OutramPark': [3, 'NorthEast Line'],
            'BuonaVista': [15, 'Circle Line']
        },
        'BuonaVista': {
            'BotanicGarden': [7, 'Circle Line'],
            'HarbourFront': [12, 'Circle Line'],
            'OutramPark': [15, 'NorthEast Line']
        },
        'BotanicGarden': {
            'Steven': [2, 'Downtown Line'],
            'Caldecott': [5, 'Circle Line'],
            'BuonaVista': [7, 'EastWest Line']
        },
        'Caldecott': {
            'BotanicGarden': [5, 'Downtown Line'],
            'Bishan': [5, 'Circle Line']
        },
        'Bishan': {
            'Serangoon': [4, 'Circle Line'],
            'Caldecott': [5, 'Circle Line'],
            'Newton': [9, 'NorthSouth Line']
        },
        'Serangoon': {
            'Bishan': [4, 'Circle Line'],
            'MacPherson': [7, 'Circle Line'],
            'LittleIndia': [10, 'NorthEast Line']
        },
        'MacPherson': {
            'PayaLebar': [2, 'Circle Line'],
            'Serangoon': [7, 'Circle Line'],
            'ChinaTown': [13, 'NorthEast Line']
        },
        'PayaLebar': {
            'MacPherson': [2, 'Circle Line'],
            'Promenade': [10, 'Circle Line'],
            'Bugis': [9, 'EastWest Line']
        },
        'Promenade': {
            'BayFront': [2, 'Circle Line'],
            'DhobyGhaut': [2, 'Circle Line'],
            'Bugis': [2, 'Downtown Line'],
            'PayaLebar': [10, 'Circle Line']
        },
        'BayFront': {
            'Promenade': [2, 'Downtown Line'],
            'MarinaBay': [2, 'Circle Line'],
            'ChinaTown': [5, 'Downtown Line']
        },
        'MarinaBay': {
            'RafflesPlace': [2, 'NorthSouth Line'],
            'BayFront': [2, 'Circle Line']
        },
        'Steven': {
            'BotanicGarden': [2, 'Downtown Line'],
            'Newton': [3, 'Downtown Line']
        },
        'Newton': {
            'LittleIndia': [1, 'Downtown Line'],
            'Steven': [3, 'Downtown Line'],
            'Orchard': [3, 'NorthSouth Line'],
            'Bishan': [9, 'NorthSouth Line']
        },
        'Orchard': {
            'Newton': [3, 'NorthSouth Line'],
            'DhobyGhaut': [4, 'NorthSouth Line']
        },
        'LittleIndia': {
            'Newton': [1, 'Downtown Line'],
            'DhobyGhaut': [2, 'NorthEast Line'],
            'Bugis': [4, 'Downtown Line'],
            'Serangoon': [10, 'NorthSouth Line']
        },
        'DhobyGhaut': {
            'LittleIndia': [2, 'NorthSouth Line'],
            'CityHall': [3, 'NorthSouth Line'],
            'Orchard': [4, 'NorthSouth Line'],
            'ChinaTown': [4, 'NorthEast Line'],
            'Promenade': [6, 'Circle Line']
        },
        'Bugis': {
            'Promenade': [2, 'Downtown Line'],
            'CityHall': [3, 'EastWest Line'],
            'LittleIndia': [4, 'Downtown Line'],
            'PayaLebar': [9, 'EastWest Line']
        },
        'ChinaTown': {
            'OutramPark': [2, 'NorthEast Line'],
            'DhobyGhaut': [4, 'NorthEast Line'],
            'BayFront': [5, 'Circle Line'],
            'MacPherson': [13, 'Downtown Line']
        },
        'CityHall': {
            'RafflesPlace': [2, 'NorthSouth Line'],
            'DhobyGhaut': [3, 'NorthSouth Line'],
            'PayaLebar': [12, 'EastWest Line']
        },
        'RafflesPlace': {
            'CityHall': [2, 'NorthSouth Line'],
            'MarinaBay': [2, 'NorthSouth Line'],
            'OutramPark': [5, 'EastWest Line']
        },
        'OutramPark': {
            'ChinaTown': [2, 'NorthEast Line'],
            'HarbourFront': [3, 'NorthEast Line'],
            'RafflesPlace': [5, 'EastWest Line'],
            'BuonaVista': [12, 'EastWest Line']
        }
    }


# contain final path for both dijsktra and bellman
dijkstra_path = []
dijkstra_color_path = []
bellman_path = []


def bellman_ford(graph, source, endpt):
    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0
    # Step 2: Relax the edges
    for x in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than
                # the current, store it
                if (distance[neighbour]
                    ) > distance[node] + (graph[node][neighbour])[0]:
                    (distance[neighbour]
                     ), predecessor[neighbour] = distance[node] + (
                         graph[node][neighbour])[0], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert (distance[neighbour]) <= distance[node] + (
                graph[node][neighbour])[0], "Negative weight cycle."

    for k, v in distance.items():
        if k == endpt:
            print("Shortest Time needed to " + endpt + " is " + str(v) +
                  " minutes")

    # trace back path
    route = []
    route.insert(0, endpt)
    for k, v in predecessor.items():
        # trace from end to start by using predecessor
        if endpt == k:
            route.append(v)
            prev = v
            # will repeat 10 times by passing previous value as key
            for x in range(0, 10):
                for k, v in predecessor.items():
                    if prev == k:
                        route.append(v)
                        prev = v
                    if prev == start_pt:
                        break
    print("Route")
    route.reverse()
    global bellman_path
    bellman_path = route.copy()
    temp = []
    temp.append('Begin Journey at {}'.format(route[0]))
    for i in range(1, len(route)):
        prv = route[i - 1]
        nxt = route[i]
        temp.append('{} via {}'.format(route[i], (mrt_bus_graph[prv][nxt])[1]))
    print(temp)


def dijkstra(graph, start, goal):
    shortestDist = {}
    trackPredecessor = {}
    unseenNodes = graph
    infinity = 99999999

    # final path after combining from track predecessor
    for node in unseenNodes:
        shortestDist[node] = infinity
    shortestDist[start] = 0

    while unseenNodes:
        minDistNode = None
        for node in unseenNodes:
            if minDistNode is None:
                # starting node
                minDistNode = node
            #determine lowest cost
            elif shortestDist[node] < shortestDist[minDistNode]:
                minDistNode = node

        # all the possible path for min dist node
        pathOptions = graph[minDistNode].items()

        # update cost of node
        for child_node, weight in pathOptions:
            if type(weight) == list:
                if weight[0] + shortestDist[minDistNode] < shortestDist[
                        child_node]:
                    shortestDist[
                        child_node] = weight[0] + shortestDist[minDistNode]
                    trackPredecessor[child_node] = minDistNode
            else:
                if weight + shortestDist[minDistNode] < shortestDist[
                        child_node]:
                    shortestDist[
                        child_node] = weight + shortestDist[minDistNode]

                    trackPredecessor[child_node] = minDistNode
        # pop out nodes after marked them
        unseenNodes.pop(minDistNode)

    currNode = goal
    # trace back until start node
    initialization()

    while currNode != start:
        if 'Line' not in ((
                mrt_bus_graph[currNode])[trackPredecessor[currNode]])[1]:
            try:
                dijkstra_color_path.insert(0, currNode)
                dijkstra_path.insert(
                    0, '{} Via BusNo.{}'.format(
                        currNode, ((mrt_bus_graph[currNode]
                                    )[trackPredecessor[currNode]])[1]))
                currNode = trackPredecessor[currNode]

            # if no path
            except KeyError:
                print("Path is not reachable")
                break
        else:
            try:
                dijkstra_color_path.insert(0, currNode)
                dijkstra_path.insert(
                    0, '{} Via {}'.format(currNode,
                                          ((mrt_bus_graph[currNode]
                                            )[trackPredecessor[currNode]])[1]))
                currNode = trackPredecessor[currNode]

            #     if no path
            except KeyError:
                print("Path is not reachable")
                break

    dijkstra_path.insert(0, "Begin Journey at {}".format(start))
    dijkstra_color_path.insert(0, start)

    if shortestDist[goal] != infinity:
        print("Shortest Time needed " + str(shortestDist[goal]) + " minutes")
        print("Optimal path is " + str(dijkstra_path))
        shortestDist.clear()
        trackPredecessor.clear()
        unseenNodes.clear()


def post_set():
    global dijkstra_path
    global dijkstra_color_path
    dijkstra_path = []
    dijkstra_color_path = []


def updatePathColor(path, string):
    allIndex = []
    nodeColor = RED
    nodeRadius = 10
    lineThickness = 4

    # draw circle
    for x in path:
        # get index based on matched string
        index = [
            index for index in range(len(location)) if location[index] == x
        ]
        # convert list to index
        strings = [str(x) for x in index]
        a_string = "".join(strings)
        an_integer = int(a_string)
        allIndex.append(an_integer)
        pygame.draw.circle(screen, nodeColor, location_coord[an_integer],
                           nodeRadius)

    # draw lines
    for i, curr in enumerate(allIndex):
        if i > 0:
            prev = allIndex[i - 1]
            pygame.draw.line(screen, TURQUOISE, location_coord[prev],
                             location_coord[curr], lineThickness)
            # different style
            if string == 'dash':
                DashedLine(screen, [0, 0, 0], BLACK, location_coord[prev],
                           location_coord[curr], 10)
            else:
                Arrow(screen, TURQUOISE, location_coord[prev],
                      location_coord[curr])


# global var to store start and end points
start_pt = ""
end_pt = ""


def calculate_distance_start(x, y, nodeRadius=10):
    eud_dis = []
    for xy in range(len(lis_of_xcoord)):
        eud_dis.append(
            sqrt(((x - lis_of_xcoord[xy])**2) + ((y - lis_of_ycoord[xy])**2)))
    # once calculate the eud distance the variance should be less than 10
    # because of node radius
    for ed in range(len(eud_dis)):
        if eud_dis[ed] <= nodeRadius:
            global start_pt
            start_pt = location[ed]
            print("From: ", start_pt)
            return location_coord[ed]


def calculate_distance_end(x, y, nodeRadius=10):
    eud_dis = []
    for xy in range(len(lis_of_xcoord)):
        eud_dis.append(
            sqrt(((x - lis_of_xcoord[xy])**2) + ((y - lis_of_ycoord[xy])**2)))
    # once calculate the eud distance the variance should be less than 10
    # because of node radius
    for ed in range(len(eud_dis)):
        if eud_dis[ed] <= nodeRadius:
            global end_pt
            end_pt = location[ed]
            print("To: ", end_pt)
            return location_coord[ed]


def background():
    # load bg
    clock_tick_rate = 20
    a = True
    clock = pygame.time.Clock()
    background_image = pygame.image.load(
        "/Users/kenjileong/VisualStudioProjects/Python/CSC1008/Assignment/mrt.png")
    # xy coord of mrt stn
    user_start_xy = None
    user_end_xy = None
    print("Choose to take 1.MRT 2.MRT/BUS ")
    user_input1 = input()
    print("Choose Algorithm 1.Dijkstra 2.Bellman-Ford ")
    user_input2 = input()

    while a is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # use for close window button
                a = False
            if event.type == pygame.KEYDOWN:  # if user press "enter"
                # press q to quit program
                if event.key == pygame.K_q:
                    a = False
                # press c to reset program
                if event.key == pygame.K_c:
                    user_start_xy = None
                    user_end_xy = None

            if event.type == pygame.MOUSEBUTTONUP:  # user mouse click event
                if pygame.mouse.get_pressed():  # if user click the mouse

                    # if both start and end is not clicked
                    if user_start_xy is None:
                        user_start_xy = calculate_distance_start(
                            pygame.mouse.get_pos()[0],
                            pygame.mouse.get_pos()[1])

                    else:
                        # mrt with dijkstra
                        if user_input1 == '1' and user_input2 == '1':
                            user_end_xy = calculate_distance_end(
                                pygame.mouse.get_pos()[0],
                                pygame.mouse.get_pos()[1])

                            initialization()
                            post_set()
                            dijkstra(mrt_graph, start_pt, end_pt)
                            initialization()

                        # mrt and bus with dijkstra
                        if user_input1 == '2' and user_input2 == '1':
                            user_end_xy = calculate_distance_end(
                                pygame.mouse.get_pos()[0],
                                pygame.mouse.get_pos()[1])

                            initialization()
                            post_set()
                            dijkstra(mrt_bus_graph, start_pt, end_pt)
                            initialization()

                        # mrt only with bellman
                        if user_input1 == '1' and user_input2 == '2':
                            user_end_xy = calculate_distance_end(
                                pygame.mouse.get_pos()[0],
                                pygame.mouse.get_pos()[1])

                            initialization()
                            bellman_ford(mrt_graph, start_pt, end_pt)
                            initialization()

                        # mrt and bus with bellman
                        if user_input1 == '2' and user_input2 == '2':
                            user_end_xy = calculate_distance_end(
                                pygame.mouse.get_pos()[0],
                                pygame.mouse.get_pos()[1])

                            initialization()
                            bellman_ford(mrt_bus_graph, start_pt, end_pt)
                            initialization()

        screen.blit(background_image, [0, 0])
        drawLine()
        drawCircle()
        addText()
        if user_start_xy is not None:
            pygame.draw.circle(screen, ORANGE, user_start_xy, 10)
        if user_end_xy is not None:
            pygame.draw.circle(screen, TURQUOISE, user_end_xy, 10)
            if user_input2 == "1":
                updatePathColor(dijkstra_color_path, 'dash')
            if user_input2 == "2":
                updatePathColor(bellman_path, 'arrow')

        pygame.display.flip()
        clock.tick(clock_tick_rate)


# different styling of line
# for dijkstra
def DashedLine(surface, color1, color2, pos1, pos2, increment):
    YDiff = float(pos2[1] - pos1[1])
    XDiff = float(pos2[0] - pos1[0])
    Length = sqrt((XDiff**2) + (YDiff**2))
    colornumber = 0
    Color = color1
    for pos in xrange(int(round(Length))):
        Position = (int(round(((pos / Length) * XDiff) + pos1[0])),
                    int(round(((pos / Length) * YDiff) + pos1[1])))
        surface.set_at(Position, Color)
        colornumber += 1
        if colornumber == increment:
            colornumber = 0
            if Color == color1:
                Color = color2
            else:
                Color = color1


# for bellman
def Arrow(screen, colour, start, end):
    radius = 15
    pygame.draw.line(screen, colour, start, end, 2)
    rotation = degrees(atan2(start[1] - end[1], end[0] - start[0])) + 90
    pygame.draw.polygon(screen, (255, 0, 0),
                        ((end[0] + radius * sin(radians(rotation)),
                          end[1] + radius * cos(radians(rotation))),
                         (end[0] + radius * sin(radians(rotation - 120)),
                          end[1] + radius * cos(radians(rotation - 120))),
                         (end[0] + radius * sin(radians(rotation + 120)),
                          end[1] + radius * cos(radians(rotation + 120)))))


def drawCircle():
    # note properties
    nodeColorMrt = BLACK
    nodeColorBus = GREY
    nodeRadius = 10

    # mrt stns
    pygame.draw.circle(screen, nodeColorMrt, HarbourFront, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, BuonaVista, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, BotanicGarden, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Caldecott, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Bishan, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Serangoon, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, MacPherson, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, PayaLebar, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Promenade, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, BayFront, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, MarinaBay, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, RafflesPlace, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, CityHall, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Bugis, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, LittleIndia, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Newton, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Steven, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, Orchard, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, DhobyGhaut, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, ChinaTown, nodeRadius)
    pygame.draw.circle(screen, nodeColorMrt, OutramPark, nodeRadius)

    # bus stns
    pygame.draw.circle(screen, nodeColorBus, AndrewRd, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, TyersallAve, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, OppBlk177, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, BraddelFlyover, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, Bendemeer_Road, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, Esplanade, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, PSA_KEPPEL, nodeRadius)
    pygame.draw.circle(screen, nodeColorBus, Middle_Road, nodeRadius)


def drawLine():
    lineThickness = 4
    # yellow
    pygame.draw.line(screen, YELLOW, HarbourFront, BuonaVista, lineThickness)
    pygame.draw.line(screen, YELLOW, BuonaVista, BotanicGarden, lineThickness)
    pygame.draw.line(screen, YELLOW, BotanicGarden, Caldecott, lineThickness)
    pygame.draw.line(screen, YELLOW, Caldecott, Bishan, lineThickness)
    pygame.draw.line(screen, YELLOW, Bishan, Serangoon, lineThickness)
    pygame.draw.line(screen, YELLOW, Serangoon, MacPherson, lineThickness)
    pygame.draw.line(screen, YELLOW, MacPherson, PayaLebar, lineThickness)
    pygame.draw.line(screen, YELLOW, PayaLebar, Promenade, lineThickness)
    pygame.draw.line(screen, YELLOW, Promenade, BayFront, lineThickness)
    pygame.draw.line(screen, YELLOW, BayFront, MarinaBay, lineThickness)
    pygame.draw.line(screen, YELLOW, DhobyGhaut, Promenade, lineThickness)

    # green
    pygame.draw.line(screen, GREEN, BuonaVista, OutramPark, lineThickness)
    pygame.draw.line(screen, GREEN, OutramPark, RafflesPlace, lineThickness)
    pygame.draw.line(screen, GREEN, RafflesPlace, CityHall, lineThickness)
    pygame.draw.line(screen, GREEN, CityHall, Bugis, lineThickness)
    pygame.draw.line(screen, GREEN, Bugis, PayaLebar, lineThickness)

    # RED
    pygame.draw.line(screen, RED, Bishan, Newton, lineThickness)
    pygame.draw.line(screen, RED, Newton, Orchard, lineThickness)
    pygame.draw.line(screen, RED, Orchard, DhobyGhaut, lineThickness)
    pygame.draw.line(screen, RED, DhobyGhaut, CityHall, lineThickness)
    pygame.draw.line(screen, RED, CityHall, RafflesPlace, lineThickness)
    pygame.draw.line(screen, RED, RafflesPlace, MarinaBay, lineThickness)

    # PURPLE
    pygame.draw.line(screen, PURPLE, Serangoon, LittleIndia, lineThickness)
    pygame.draw.line(screen, PURPLE, LittleIndia, DhobyGhaut, lineThickness)
    pygame.draw.line(screen, PURPLE, DhobyGhaut, ChinaTown, lineThickness)
    pygame.draw.line(screen, PURPLE, ChinaTown, OutramPark, lineThickness)
    pygame.draw.line(screen, PURPLE, OutramPark, HarbourFront, lineThickness)

    # BLUE
    pygame.draw.line(screen, BLUE, BotanicGarden, Steven, lineThickness)
    pygame.draw.line(screen, BLUE, Steven, Newton, lineThickness)
    pygame.draw.line(screen, BLUE, Newton, LittleIndia, lineThickness)
    pygame.draw.line(screen, BLUE, LittleIndia, Bugis, lineThickness)
    pygame.draw.line(screen, BLUE, Bugis, Promenade, lineThickness)
    pygame.draw.line(screen, BLUE, Promenade, BayFront, lineThickness)
    pygame.draw.line(screen, BLUE, BayFront, ChinaTown, lineThickness)
    pygame.draw.line(screen, BLUE, ChinaTown, MacPherson, lineThickness)

    # ROSY_BROWN
    pygame.draw.line(screen, ROSY_BROWN, AndrewRd, DhobyGhaut, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, AndrewRd, Caldecott, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, AndrewRd, Bishan, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, AndrewRd, BotanicGarden,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, AndrewRd, BraddelFlyover,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, TyersallAve, BuonaVista,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, TyersallAve, DhobyGhaut,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, TyersallAve, CityHall, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, OppBlk177, Serangoon, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, OppBlk177, Orchard, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, OppBlk177, LittleIndia, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, OppBlk177, BraddelFlyover,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, BraddelFlyover, Serangoon,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, BraddelFlyover, Steven, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, BraddelFlyover, OppBlk177,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, Serangoon, Bendemeer_Road,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, Bendemeer_Road, Middle_Road,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, HarbourFront, PSA_KEPPEL,
                     lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, MarinaBay, PSA_KEPPEL, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, MarinaBay, Esplanade, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, Bugis, Middle_Road, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, Bugis, Esplanade, lineThickness)
    pygame.draw.line(screen, ROSY_BROWN, Bendemeer_Road, MacPherson,
                     lineThickness)


def addText():
    # set font
    font_bus_txt = pygame.font.Font('freesansbold.ttf', 15)
    font_color_bus_text = ROSY_BROWN
    # bus node name
    text_surface_bus1 = font_bus_txt.render('AndrewRd', True,
                                            font_color_bus_text)
    text_surface_bus2 = font_bus_txt.render('Tyersall Avenue', True,
                                            font_color_bus_text)
    text_surface_bus3 = font_bus_txt.render('Block 177', True,
                                            font_color_bus_text)
    text_surface_bus4 = font_bus_txt.render('Braddel Flyover', True,
                                            font_color_bus_text)
    text_surface_bus5 = font_bus_txt.render('Bendemeer_Road', True,
                                            font_color_bus_text)
    text_surface_bus6 = font_bus_txt.render('Esplanade', True,
                                            font_color_bus_text)
    text_surface_bus7 = font_bus_txt.render('PSA_KEPPEL', True,
                                            font_color_bus_text)
    text_surface_bus8 = font_bus_txt.render('Middle_Road', True,
                                            font_color_bus_text)

    text_rect_bus1 = text_surface_bus1.get_rect()
    text_rect_bus2 = text_surface_bus2.get_rect()
    text_rect_bus3 = text_surface_bus3.get_rect()
    text_rect_bus4 = text_surface_bus4.get_rect()
    text_rect_bus5 = text_surface_bus5.get_rect()
    text_rect_bus6 = text_surface_bus6.get_rect()
    text_rect_bus7 = text_surface_bus7.get_rect()
    text_rect_bus8 = text_surface_bus8.get_rect()

    text_rect_bus1.center = (AndrewRd)
    text_rect_bus2.center = (TyersallAve)
    text_rect_bus3.center = (OppBlk177)
    text_rect_bus4.center = (BraddelFlyover)
    text_rect_bus5.center = (Bendemeer_Road)
    text_rect_bus6.center = (Esplanade)
    text_rect_bus7.center = (PSA_KEPPEL)
    text_rect_bus8.center = (Middle_Road)

    screen.blit(text_surface_bus1, text_rect_bus1)
    screen.blit(text_surface_bus2, text_rect_bus2)
    screen.blit(text_surface_bus3, text_rect_bus3)
    screen.blit(text_surface_bus4, text_rect_bus4)
    screen.blit(text_surface_bus5, text_rect_bus5)
    screen.blit(text_surface_bus6, text_rect_bus6)
    screen.blit(text_surface_bus7, text_rect_bus7)
    screen.blit(text_surface_bus8, text_rect_bus8)

    # display dist between stns
    harbourFront_neighbor()
    buonoVista_neighbor()
    botanicGarden_neighbor()
    caldecott_neighbor()
    bishan_neighbor()
    serangoon_neighbor()
    macPherson_neighbor()
    payaLebar_neighbor()
    promenade_neighbor()
    bayFront_neighbor()
    marinaBay_neighbor()
    steven_neighbor()
    newton_neighbor()
    littleIndia_neighbor()
    dhobyGhaut_neighbor()
    bugis_neighbor()
    cityHall_neighbor()
    outramPark_neighbor()


# display dist by getting center xy between stations
def harbourFront_neighbor():
    x = (HarbourFront[0] + BuonaVista[0]) // 2
    y = (HarbourFront[1] + BuonaVista[1]) // 2
    text_surface_line = font_obj.render('15', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (HarbourFront[0] + OutramPark[0]) // 2
    y1 = (HarbourFront[1] + OutramPark[1]) // 2
    text_surface_line1 = font_obj.render('3', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def buonoVista_neighbor():
    x = (BuonaVista[0] + OutramPark[0]) // 2
    y = (BuonaVista[1] + OutramPark[1]) // 2
    text_surface_line = font_obj.render('12', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (BuonaVista[0] + BotanicGarden[0]) // 2
    y1 = (BuonaVista[1] + BotanicGarden[1]) // 2
    text_surface_line1 = font_obj.render('7', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def botanicGarden_neighbor():
    x = (BotanicGarden[0] + Steven[0]) // 2
    y = (BotanicGarden[1] + Steven[1]) // 2
    text_surface_line = font_obj.render('2', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (BotanicGarden[0] + Caldecott[0]) // 2
    y1 = (BotanicGarden[1] + Caldecott[1]) // 2
    text_surface_line1 = font_obj.render('5', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def caldecott_neighbor():
    x = (Caldecott[0] + Bishan[0]) // 2
    y = (Caldecott[1] + Bishan[1]) // 2
    text_surface_line = font_obj.render('5', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)


def bishan_neighbor():
    x = (Bishan[0] + Newton[0]) // 2
    y = (Bishan[1] + Newton[1]) // 2
    text_surface_line = font_obj.render('9', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (Bishan[0] + Serangoon[0]) // 2
    y1 = (Bishan[1] + Serangoon[1]) // 2
    text_surface_line1 = font_obj.render('4', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def serangoon_neighbor():
    x = (Serangoon[0] + LittleIndia[0]) // 2
    y = (Serangoon[1] + LittleIndia[1]) // 2
    text_surface_line = font_obj.render('10', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (Serangoon[0] + MacPherson[0]) // 2
    y1 = (Serangoon[1] + MacPherson[1]) // 2
    text_surface_line1 = font_obj.render('7', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def macPherson_neighbor():
    x = (MacPherson[0] + ChinaTown[0]) // 2
    y = (MacPherson[1] + ChinaTown[1]) // 2
    text_surface_line = font_obj.render('13', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (MacPherson[0] + PayaLebar[0]) // 2
    y1 = (MacPherson[1] + PayaLebar[1]) // 2
    text_surface_line1 = font_obj.render('2', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def payaLebar_neighbor():
    x = (PayaLebar[0] + Bugis[0]) // 2
    y = (PayaLebar[1] + Bugis[1]) // 2
    text_surface_line = font_obj.render('9', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (PayaLebar[0] + Promenade[0]) // 2
    y1 = (PayaLebar[1] + Promenade[1]) // 2
    text_surface_line1 = font_obj.render('10', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def promenade_neighbor():
    x = (Promenade[0] + Bugis[0]) // 2
    y = (Promenade[1] + Bugis[1]) // 2
    text_surface_line = font_obj.render('2', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (Promenade[0] + BayFront[0]) // 2
    y1 = (Promenade[1] + BayFront[1]) // 2
    text_surface_line1 = font_obj.render('2', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)

    x2 = (Promenade[0] + DhobyGhaut[0]) // 2
    y2 = (Promenade[1] + DhobyGhaut[1]) // 2
    text_surface_line2 = font_obj.render('6', True, font_color)
    text_rect_line2 = text_surface_line2.get_rect()
    text_rect_line2.center = (x2, y2)
    screen.blit(text_surface_line2, text_rect_line2)


def bayFront_neighbor():
    x = (BayFront[0] + ChinaTown[0]) // 2
    y = (BayFront[1] + ChinaTown[1]) // 2
    text_surface_line = font_obj.render('5', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (BayFront[0] + MarinaBay[0]) // 2
    y1 = (BayFront[1] + MarinaBay[1]) // 2
    text_surface_line1 = font_obj.render('2', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def marinaBay_neighbor():
    x = (MarinaBay[0] + RafflesPlace[0]) // 2
    y = (MarinaBay[1] + RafflesPlace[1]) // 2
    text_surface_line = font_obj.render('2', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)


def steven_neighbor():
    x = (Steven[0] + Newton[0]) // 2
    y = (Steven[1] + Newton[1]) // 2
    text_surface_line = font_obj.render('3', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)


def newton_neighbor():
    x = (Newton[0] + Orchard[0]) // 2
    y = (Newton[1] + Orchard[1]) // 2
    text_surface_line = font_obj.render('3', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (Newton[0] + LittleIndia[0]) // 2
    y1 = (Newton[1] + LittleIndia[1]) // 2
    text_surface_line1 = font_obj.render('1', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def littleIndia_neighbor():
    x = (LittleIndia[0] + DhobyGhaut[0]) // 2
    y = (LittleIndia[1] + DhobyGhaut[1]) // 2
    text_surface_line = font_obj.render('2', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (LittleIndia[0] + Bugis[0]) // 2
    y1 = (LittleIndia[1] + Bugis[1]) // 2
    text_surface_line1 = font_obj.render('4', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def dhobyGhaut_neighbor():
    x = (DhobyGhaut[0] + Orchard[0]) // 2
    y = (DhobyGhaut[1] + Orchard[1]) // 2
    text_surface_line = font_obj.render('4', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (DhobyGhaut[0] + ChinaTown[0]) // 2
    y1 = (DhobyGhaut[1] + ChinaTown[1]) // 2
    text_surface_line1 = font_obj.render('4', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)

    x2 = (DhobyGhaut[0] + CityHall[0]) // 2
    y2 = (DhobyGhaut[1] + CityHall[1]) // 2
    text_surface_line2 = font_obj.render('3', True, font_color)
    text_rect_line2 = text_surface_line2.get_rect()
    text_rect_line2.center = (x2, y2)
    screen.blit(text_surface_line2, text_rect_line2)

    x3 = (DhobyGhaut[0] + Promenade[0]) // 2
    y3 = (DhobyGhaut[1] + Promenade[1]) // 2
    text_surface_line3 = font_obj.render('6', True, font_color)
    text_rect_line3 = text_surface_line3.get_rect()
    text_rect_line3.center = (x3, y3)
    screen.blit(text_surface_line3, text_rect_line3)


def chinaTown_neighbor():
    x = (ChinaTown[0] + OutramPark[0]) // 2
    y = (ChinaTown[1] + OutramPark[1]) // 2
    text_surface_line = font_obj.render('2', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)


def bugis_neighbor():
    x = (Bugis[0] + CityHall[0]) // 2
    y = (Bugis[1] + CityHall[1]) // 2
    text_surface_line = font_obj.render('3', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)


def cityHall_neighbor():
    x = (CityHall[0] + RafflesPlace[0]) // 2
    y = (CityHall[1] + RafflesPlace[1]) // 2
    text_surface_line = font_obj.render('2', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)


def outramPark_neighbor():
    x = (OutramPark[0] + RafflesPlace[0]) // 2
    y = (OutramPark[1] + RafflesPlace[1]) // 2
    text_surface_line = font_obj.render('5', True, font_color)
    text_rect_line = text_surface_line.get_rect()
    text_rect_line.center = (x, y)
    screen.blit(text_surface_line, text_rect_line)

    x1 = (OutramPark[0] + ChinaTown[0]) // 2
    y1 = (OutramPark[1] + ChinaTown[1]) // 2
    text_surface_line1 = font_obj.render('2', True, font_color)
    text_rect_line1 = text_surface_line1.get_rect()
    text_rect_line1.center = (x1, y1)
    screen.blit(text_surface_line1, text_rect_line1)


def main():
    background()


if __name__ == '__main__':
    main()
