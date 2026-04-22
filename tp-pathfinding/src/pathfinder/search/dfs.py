from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize frontier with the root node
        # TODO Complete the rest!!
       
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        frontera = StackFrontier()
        frontera.add(node=root)

        #Comprobamos que la front no este vacia
        while not frontera.is_empty():

            #Desapilamos el nodo
            nodo_desp = frontera.remove()

            for accion in grid.actions(pos=nodo_desp.state):
                estado_alcanzado = grid.result(pos=nodo_desp.state,
                                               action=accion)

                if estado_alcanzado not in expanded:
                    nodo_hijo = Node("",
                                     estado_alcanzado,
                                     nodo_desp.cost + grid.individual_cost(nodo_desp.state, accion),
                                     parent=nodo_desp,
                                     action=accion)

                    if grid.objective_test(pos=nodo_hijo.state):
                        return Solution(node=nodo_hijo,
                                        reached=expanded)

                    expanded[nodo_hijo.state] = True
                    frontera.add(node=nodo_hijo)

        return NoSolution(reached=expanded)       
