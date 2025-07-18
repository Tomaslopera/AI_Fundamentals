# -*- coding: utf-8 -*-

import heapq
import math

locations = {
    'A': (0, 0),
    'B': (2, 4),
    'C': (5, 1),
    'D': (6, 5),
    'E': (8, 0),
    'F': (10, 2)
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

def heuristic(city, goal='F'):
    x1, y1 = locations[city]
    x2, y2 = locations[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def best_first_search(start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start), [start]))  

    while priority_queue:
        _, path = heapq.heappop(priority_queue)
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            print(current, "->", graph[current])
            for neighbor in graph[current]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (heuristic(neighbor), new_path))
    
    return None

# Ejecutar búsqueda
ruta = best_first_search('A', 'F')
print("Ruta encontrada:", ruta)
