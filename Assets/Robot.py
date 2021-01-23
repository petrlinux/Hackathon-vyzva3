# -*- coding: utf-8 -*-

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid                                 #https://pypi.org/project/pathfinding/
from pathfinding.finder.bi_a_star import BiAStarFinder

def Pole(cil, sloupcu, Array, robot):
    podlaha=[]
    array = Array[:-1].split(',')
    for bunka in array:
        podlaha.append(int(bunka))
    return(str(Path(cil, sloupcu, podlaha, robot)).replace("(","").replace(")",""))
    
def Path(cil, sloupcu, podlaha, robot):
    matrix = []
    mezi = []
    for pole in podlaha:
        pole = int(pole)
        if(pole == int(robot)):
            matrix.append(1)
        elif(pole == 0):
            matrix.append(1)
        elif(pole >> 0):
            if (pole >> 1000):
                matrix.append(1)
            elif (pole >> 800):
                matrix.append(pole)
            else:
                matrix.append(0)
        else:
            matrix.append(0)       
    if 800 in matrix:
        mezi_b = []
        mezi_a = []
        matrix_a = []
        matrix_b = []
        i = 0
        for pole in matrix:
            i += 1
            if(pole == 800):
                mezi_b.append(0)
                mezi_a.append(1)
            else:
                mezi_a.append(pole)
                mezi_b.append(pole)
            if(i == sloupcu):
                matrix_a.append(mezi_a)
                matrix_b.append(mezi_b)
                mezi_a = []
                mezi_b = []
                i = 0
        path_a,lenght_a = Trasa(cil, podlaha, matrix_a, sloupcu, robot)
        path_b,lenght_b = Trasa(cil, podlaha, matrix_b, sloupcu, robot)
        if (path_b == []):
            path = path_a
            Wait = 1
        elif (lenght_b-2 <= lenght_a):
            path = path_b
            Wait = 0
        else:
            path = path_a
            Wait = 1
    else:
        i=0
        matrix_ = []
        for pole in matrix:
            i += 1
            if(i == sloupcu):
                matrix_.append(mezi)
                mezi = []
                i = 0
            else:
                mezi.append(pole)
        matrix = matrix_   
        path,lenght = Trasa(cil, podlaha, matrix, sloupcu, robot)
        Wait = 0
    if(Wait == 0):
        path=(path[0])[1]
    else:
        path=(path[0])[0]
    return(path,lenght)
        
def Trasa(cil, pole, matrix, sloupcu, robot):                                             #Výpočet trasy
    Sx,Sy = Prevod_xy(pole.index(robot), sloupcu)             #Poloha Start
    Cx,Cy = Prevod_xy(pole.index(cil), sloupcu)             #Poloha cíl
    grid = Grid(matrix=matrix)
    start = grid.node(Sx, Sy)
    end = grid.node(Cx, Cy)
    finder = BiAStarFinder(diagonal_movement=DiagonalMovement.never)
    path = finder.find_path(start, end, grid)
    lenght=len(path[0])
    return(path,lenght)

def Prevod_xy(poloha,sloupcu):          #Převod polohy v poli na souřadnice
    x=int(poloha%sloupcu)
    y=int(poloha/sloupcu)
    return(x,y)

#print(Pole(cil, sloupcu, pole))
