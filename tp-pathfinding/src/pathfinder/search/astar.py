from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:

    @staticmethod
    def heuristica(grid_end: tuple[int,int], grid_pos: tuple[int,int]):
        """Retorna el valor heuristico usando la distancia Manhattan."""
        x1, x2 = grid_pos
        y1, y2 = grid_end
        return abs(x1 - y1) + abs(x2 - y2)

    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        #Inicializamos la front con el costo heuristico
        frontera = PriorityQueueFrontier()
        frontera.add(node=root, priority=root.cost + AStarSearch.heuristica(grid.end, root.state))

        #Si la front no esta vacia, expandimos
        while not frontera.is_empty():

            nodo_desc = frontera.pop()

            #Hacemos el test objetivo del nodo desencolado
            if grid.objective_test(nodo_desc.state):
                return Solution(node=nodo_desc,
                                reached=reached)

            #Si no es una solucion, evaluamos mas acciones
            for accion in grid.actions(nodo_desc.state):
                estado_alcanzado = grid.result(pos=nodo_desc.state,
                                               action=accion)

                costo_accion = nodo_desc.cost + grid.individual_cost(pos=nodo_desc.state,
                                                                     action=accion)

                #Verificacion de si no alcanzamos el estado o si llegamos al mismo estado con un costo menor
                if estado_alcanzado not in reached or costo_accion < reached[estado_alcanzado]:
                    nodo_hijo = Node("",
                                     state=estado_alcanzado,
                                     cost=costo_accion,
                                     parent=nodo_desc,
                                     action=accion)

                    #Agregamos el estado alcanzado y el nodo a la frontera con su costo heuristico
                    reached[estado_alcanzado] = costo_accion
                    frontera.add(node=nodo_hijo,
                                 priority=nodo_hijo.cost + AStarSearch.heuristica(grid_end=grid.end,
                                                                                  grid_pos=nodo_hijo.state))
        return NoSolution(reached)
