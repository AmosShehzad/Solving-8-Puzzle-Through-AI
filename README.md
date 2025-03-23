# **8-Puzzle Solver Using A* Algorithm**  

## **Overview**  
This project implements an **AI-based solution** for solving the **8-puzzle problem** using the **A* search algorithm with the Manhattan Distance heuristic**. The 8-puzzle is a sliding tile game where tiles must be arranged in a specific order by moving them within a **3×3 grid**.  

## **Features**  
✅ **A* Search Algorithm** for optimal pathfinding  
✅ Uses **Manhattan Distance heuristic** for efficient searching  
✅ Displays **step-by-step solution** from the initial state to the goal state  
✅ Implements a **priority queue** for managing search nodes efficiently  

## **How It Works**  
The program starts with an **initial state** and uses the **A* algorithm** to find the shortest path to the **goal state** by expanding nodes with the lowest cost `(f = g + h)`.  
- **g**: Number of moves made from the start state  
- **h**: Manhattan Distance heuristic (sum of tile distances from their goal positions)  
- **f**: Total estimated cost (g + h)  

## **Requirements**  
Ensure you have **Python 3.x** installed. No additional dependencies are needed.  

## **Usage**  
1. Clone the repository or download the script.  
2. Run the program:  
   ```bash
   python solve_8_puzzle.py
