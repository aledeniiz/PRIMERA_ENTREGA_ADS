import networkx as nx
import json

class GenealogyTree:
    def __init__(self):
        # Crea un grafo dirigido
        self.tree = nx.DiGraph()

    def add_person(self, name):
        """Agrega una nueva persona al árbol."""
        self.tree.add_node(name)

    def add_relationship(self, parent, child):
        """Agrega una relación de padre-hijo al árbol."""
        self.tree.add_edge(parent, child)

    def remove_person(self, name):
        """Elimina a una persona del árbol genealógico."""
        self.tree.remove_node(name)

    def find_relationship(self, person1, person2):
        """Encuentra la relación entre dos personas."""
        try:
            # Encuentra el camino más corto en el grafo dirigido
            path = nx.shortest_path(self.tree, source=person1, target=person2)
            distance = len(path) - 1

            if distance == 1:
                return "Padre/Hijo"
            elif distance == 2:
                return "Abuelo/Abuela - Nieto/Nieta"
            elif distance == 3:
                return "Bisabuelo/Bisabuela - Bisnieto/Bisnieta"
            else:
                return f"Relacion de grado {distance - 1}"
        except nx.NetworkXNoPath:
            # Si no hay un camino dirigido, revisa si existe en el grafo no dirigido
            try:
                distance = nx.shortest_path_length(self.tree.to_undirected(), person1, person2)
                if distance == 2:
                    return "Hermano/Hermana"
                elif distance == 3:
                    return "Primo/Prima"
                elif distance == 4:
                    return "Primo segundo/Prima segunda"
                else:
                    return f"Parentesco lejano de grado {distance // 2 - 1}"
            except nx.NetworkXNoPath:
                return "Sin relación directa"

    def detect_inbreeding(self):
        """Detecta endogamia al buscar múltiples caminos hacia un mismo nodo."""
        inbreeding_cases = {}

        # Recorre cada nodo en el grafo
        for target_node in self.tree.nodes:
            paths_to_node = []

            # Recorre cada otro nodo como punto de partida
            for source_node in self.tree.nodes:
                if source_node != target_node:
                    # Encuentra todas las rutas simples del nodo origen al nodo objetivo
                    all_paths = list(nx.all_simple_paths(self.tree, source=source_node, target=target_node))
                    if len(all_paths) > 1:  # Si hay más de una ruta
                        paths_to_node.extend(all_paths)

            if paths_to_node:
                inbreeding_cases[target_node] = paths_to_node

        # Muestra los resultados
        if inbreeding_cases:
            print("Endogamia detectada en los siguientes nodos:")
            for node, paths in inbreeding_cases.items():
                print(f"Nodo '{node}' tiene múltiples caminos de acceso:")
                for idx, path in enumerate(paths, 1):
                    print(f"  Camino {idx}: {' -> '.join(path)}")
        else:
            print("No se detectó endogamia.")

    def save_tree(self, filename):
        """Guarda el árbol genealógico en un archivo JSON."""
        with open(filename, 'w') as f:
            json.dump(dict(nodes=list(self.tree.nodes), edges=list(self.tree.edges)), f)

    def load_tree(self, filename):
        """Carga un árbol genealógico de un archivo JSON."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.tree.clear()
            self.tree.add_nodes_from(data['nodes'])
            self.tree.add_edges_from(data['edges'])

    def visualize_tree(self):
        """Visualiza el árbol genealógico."""
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.tree)
        nx.draw(self.tree, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Inicializa el árbol genealógico
    genealogy = GenealogyTree()

    # Agrega personas
    genealogy.add_person("Alice")
    genealogy.add_person("Bob")
    genealogy.add_person("Charlie")
    genealogy.add_person("Daisy")
    genealogy.add_person("Edward")

    # Establece relaciones
    genealogy.add_relationship("Alice", "Bob")
    genealogy.add_relationship("Alice", "Charlie")
    genealogy.add_relationship("Charlie", "Daisy")
    genealogy.add_relationship("Bob", "Edward")

    # Visualiza el árbol
    genealogy.visualize_tree()

    # Ejemplo de relación
    print("Relación entre Bob y Daisy:", genealogy.find_relationship("Bob", "Daisy"))
    print("Relación entre Alice y Edward:", genealogy.find_relationship("Alice", "Edward"))
    print("Relación entre Alice y Daisy:", genealogy.find_relationship("Alice", "Daisy"))
    print("Relación entre Charlie y Edward:", genealogy.find_relationship("Charlie", "Edward"))

    # Detecta endogamia
    genealogy.detect_inbreeding()
