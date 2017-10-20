#recursive backtracking algorithm

import random



class Maze:

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
                    self.grid.append(Cell(i,j))

    def index(self, i, j):
        """This method calculates the index of the current cell"""
        index = i + j * self.cols
        return self.grid[index]

    def checkNeighbors(self,current_cell):
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

        if len(neighbors)>0: #if there are neighbors wich have not been visited
            r = random.randint(0, len(neighbors)-1) #chooses a neighbor randomly
            print('r',str(r))
            return neighbors[r]
        else:
            return None

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

    def create_path(self):
        """
            Makes a path through the grid
        :return:nothing
        """
        # TODO: il faut itérer tant qu'il reste des Cells non visitées
       # on prend le premier objet Cell dans la liste grid
        current = self.grid[0]
       # on initialise la pile par une liste vide
        stack = []
        # on récupère la cellule voisine de la cellule courante
        chosen_cell = self.checkNeighbors(current)
        chosen_cell.visited = True
        stack.append(current) #adds the current_cell to the stack
        self.remove_walls(current, chosen_cell)
        # Step 3 ok reste step 4
        chosen_cell = current_cell


class Cell:
    """
    class
    """

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]  #each cell has 4 walls
        self.visited = False


    def highlight(self):
        x = self.i * self.width
        y = self.j * self.width



# pour tester les classes et méthodes
maze = Maze(15, 15, 2)
maze.generate_grid()
print('longueur de grid {}'.format(len(maze.grid)))
current_cell = maze.grid[0]
print('current cell -> i :{} , j :{}'.format(current_cell.i, current_cell.j))
current_cell2 = maze.grid[125]
print('current cell2 -> i :{} , j :{}'.format(current_cell2.i, current_cell2.j))
current3 = maze.index(5, 8)
print('current -> i :{} , j :{}'.format(current3.i, current3.j))
chosen_cell = maze.checkNeighbors(current3)
print('chosen_cell -> i :{} , j :{}'.format(chosen_cell.i, chosen_cell.j))






