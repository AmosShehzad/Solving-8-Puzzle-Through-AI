import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, x):
        heapq.heappush(self.elements, x)

    def dequeue(self):        
        return heapq.heappop(self.elements)
    
    def is_empty(self):
        return len(self.elements) == 0

class Node:
    def __init__(self, state, parent=None):
        self.state = state 
        self.parent = parent
        self.g = 0 if parent is None else parent.g + 1
        self.h = self.heuristic(state)
        self.f = self.g + self.h

    def __lt__ (self, other):
        return self.f < other.f
    
    def heuristic(self, state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        man_dis = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile == 0:
                    continue
                if tile == 1:
                    goal_x, goal_y = 0, 0
                elif tile == 2:
                    goal_x, goal_y = 0, 1
                elif tile == 3:
                    goal_x, goal_y = 0, 2
                elif tile == 4:
                    goal_x, goal_y = 1, 0
                elif tile == 5:
                    goal_x, goal_y = 1, 1
                elif tile == 6:
                    goal_x, goal_y = 1, 2
                elif tile == 7:
                    goal_x, goal_y = 2, 0
                elif tile == 8:
                    goal_x, goal_y = 2, 1
                man_dis += abs(i - goal_x) + abs(j - goal_y)
        return man_dis 
            
    
    def __str__ (self):
        res = ""
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    res += "  " 
                else:
                    res += str(self.state[i][j]) + " "
            res += "\n"  
        return res
    
class PuzzleSolver:
    def __init__(self, start,goal):
        self.start = Node(start)
        self.goal = Node(goal)
    def find_space(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return None
    
    def find_moves(self, pos):
        x, y = pos
        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_moves = []
        for i, j in moves:
            if 0 <= i < 3 and 0 <= j < 3:
                valid_moves.append((i, j))
        return valid_moves
    
    def is_valid(self, move):
        x, y = move
        return 0 <= x < 3 and 0 <= y < 3  
    
    def play_move(self, state, move, space):
        move_x, move_y = move
        space_x, space_y = space
        new_state = [row[:] for row in state]  
        new_state[space_x][space_y] = new_state[move_x][move_y]
        new_state[move_x][move_y] = 0
        return new_state
     
    def find_children(self, state):
        children = []
        space = self.find_space(state)  
        moves = self.find_moves(space)          
        for move in moves:
            new_state = self.play_move(state, move, space)  
            children.append(new_state)       
        return children
        
    def solve_puzzle(self):
        pq = PriorityQueue()
        pq.enqueue(self.start)
        explored = set()
        while not pq.is_empty():
            node = pq.dequeue()
            if node.state == self.goal.state:
                return self.print_solution(node)
            explored.add(str(node.state))
            space = self.find_space(node.state)
            for move in self.find_moves(space):
                new_state = self.play_move(node.state, move, space)
                if str(new_state) not in explored:
                    pq.enqueue(Node(new_state, node))
        return None
    
    def print_solution(self, node):        
        if not node:
            print("No solution found")
            return
        path = []
        while node:
            path.append(node.state)  
            node = node.parent  
        path.reverse()  
        print("\nSolution Path:")
        for state in path:
            for row in state:
                print(" ".join(str(x) if x!= 0 else " " for x in row))  
            print("\n") 

def main():
    start = [[4, 7, 8], [3, 6, 5], [1, 2, 0]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    ps = PuzzleSolver(start,goal)
    ps.solve_puzzle()
main()