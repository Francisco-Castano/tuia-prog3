from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
        #Inicializamos la frontera y encolamos la raiz
        frontera = PriorityQueueFrontier()
        frontera.add(node=root, priority=root.cost)

        #Si la cola no esta vacia, expandimos.
        while not frontera.is_empty():

            nodo_desc = frontera.pop()

            if grid.objective_test(nodo_desc.state):
                return Solution(node=nodo_desc,
                                reached=reached)

            for accion in grid.actions(nodo_desc.state):
                estado_alcanzado = grid.result(pos=nodo_desc.state,
                                               action=accion)
                costo_accion = nodo_desc.cost + grid.individual_cost(pos=nodo_desc.state,
                                                                     action=accion)

                if estado_alcanzado not in reached or costo_accion < reached[estado_alcanzado]:
                    nodo_hijo = Node("", state=estado_alcanzado,
                                     cost=costo_accion,
                                     parent=nodo_desc,
                                     action=accion)

                    reached[estado_alcanzado] = costo_accion
                    frontera.add(node=nodo_hijo,
                                 priority=costo_accion)

        return NoSolution(reached)
