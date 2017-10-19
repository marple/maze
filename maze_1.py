#recursive backtracking algorithm

import random
import pygame
from pygame.locals import *

pygame.init()

#screen = pygame.display.set_mode((500, 500))
title = pygame.display.set_caption("Mac Gyver VS the guard")


class Maze:  #faut-il ajouter une méthode pour calculer le nombre total de cases du labyrinthe??
    #ou un attribut nombre de cases dans le constructeur?
    """
    description
    """

    def __init__(self, cols, rows, width):
        self.cols = cols
        self.rows = rows
        self.width = width
        self.grid = []

    def generate_grid(self):
            for j in range(0, self.cols):
                 for i in range(0, self.rows):
                    self.grid.append(Cell(i,j)) #erreur car on fait appel à l'objet cell en dehors de la classe

    def index(self, i, j):
        """This method calculates the index of the current cell"""
        index = i + j * self.cols
        return self.grid[index]

    def checkNeighbors(self,current_cell):  #dans quelle classe je mets cette fonction?
        """
            Checks if the neighbors cells have been visited
        """
        i = current_cell.i
        j = current_cell.j
        neighbors = []
        top = self.index(i, j -1)
        right = self.index(i+1, j)
        bottom = self.index(i, j + 1)
        left = self.index(i-1, j)

        if top and not top.visited:
            neighbors.append(top)

        if right and not right.visited:
            neighbors.append(right)

        if bottom and not bottom.visited:
            neighbors.append(bottom)

        if left and not left.visited:
            neighbors.append(left)

        if len(neighbors)>0:
            r = random.randint(0, len(neighbors)-1)
            print('r',str(r))
            return neighbors[r]
        else:
            return None

    #def display(self, window):
    #    """This method displays the maze according to the grid"""
    def draw(self):
        """
            Draw across the grid the path for this maze (à corriger)
        :return:nothing
        """






class Cell:  #TODO:ajouter current, next?? current_cell = maze.grid[0]?
    """
    class
    """

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]  #each cell has 4 walls
        self.visited = False

    #def index(self):
        #if self.i < 0 or self.j < 0 or self.i > Grid.cols - 1 or self.j > Grid.rows - 1:
        #    return -1
        #else:
        #    return i + j * Grid.cols


    def highlight(self):
        x = self.i * self.width
        y = self.j * self.width

    def remove_walls(self, a, b):
        """Remove the wall between the current cell(a) and the next cell(b)"""
        x = a.self.i - b.self.i
        if x == 1:
            a.walls[3] = False #remove the left wall of the current cell
            b.walls[1] = False #remove the right wall of the next cell
        elif x == -1:
            a.walls[1] = False #remove the right wall of the current cell
            b.walls[3] = False #remove the left wall of the next cell

        y = a.self.j - b.self.j
        if y == 1:
            a.walls[0] = False #remove the top wall of the current cell
            b.walls[2] = False #remove the bottom wall of the next cell
        elif y == -1:
            a.walls[2] = False #remove the bottom wall of the current cell
            b.walls[0] = False #remove the top wall of the next cell

        #if self.visited:
            #TODO ajouter une fonction "graphique" pour effacer les murs

            #TODO : ajouter la notion de stack : dans quelle classe?

#class Dedale : classe qui génére l'application graphique du labyrinthe


# pour test des classes et methodes
maze = Maze(15, 15, 2)
maze.generate_grid()
print('longueur de grid {}'.format(len(maze.grid)))
current_cell = maze.grid[0]
print('current cell -> i :{} , j :{}'.format(current_cell.i, current_cell.j))
current_cell2 = maze.grid[125]
print('current cell2 -> i :{} , j :{}'.format(current_cell2.i, current_cell2.j))
current = maze.index(5, 8)
print('current -> i :{} , j :{}'.format(current.i, current.j))
chosen_cell = maze.checkNeighbors(current)
print('chosen_cell -> i :{} , j :{}'.format(chosen_cell.i, chosen_cell.j))






