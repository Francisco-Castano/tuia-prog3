from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        # TODO Complete the rest!!

        #Ejecutamos el test objetivo
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Creamos la cola y encolamos el nodo raiz.
        frontera = QueueFrontier()
        frontera.add(root)

        # Verificamos que la frontera no este vacia
        while not frontera.is_empty():

            #Desencolamos el primer nodo de la queue
            nodo_desc = frontera.remove()

            for accion in grid.actions(nodo_desc.state):

                #Calculamos el nuevo estado al aplicar la acción
                estado_alcanzado = grid.result(nodo_desc.state, accion)

                if estado_alcanzado not in reached:
                    nodo_hijo = Node("",
                                     state=estado_alcanzado,
                                     cost=nodo_desc.cost + grid.individual_cost(nodo_desc.state, accion),
                                     parent=nodo_desc,
                                     action=accion)

                    if grid.objective_test(nodo_hijo.state):
                        return Solution(nodo_hijo, reached)

                    #Marcamos el estado como visitado y lo agregamos a la frontera
                    reached[nodo_hijo.state] = True
                    frontera.add(nodo_hijo)
       
        #Si la frontera esta vacia, no hay solucion
        return NoSolution(reached)

