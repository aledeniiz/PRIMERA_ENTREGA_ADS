# PRIMERA_ENTREGA_ADS

Este código implementa un árbol genealógico en Python utilizando la biblioteca networkx para representar las relaciones familiares en forma de un grafo dirigido. En este contexto, cada persona en el árbol genealógico se representa como un nodo, y las relaciones de parentesco de padre a hijo se representan como aristas (o conexiones) dirigidas entre nodos.

Descripción de Funcionalidades
1. Agregar Personas y Relaciones:

Cada persona se agrega al árbol como un nodo único mediante el método add_person(nombre).
Las relaciones de parentesco de padre-hijo se agregan con el método add_relationship(padre, hijo), creando una arista dirigida que conecta al nodo del padre con el del hijo.
2. Buscar Relaciones:

El método find_relationship(person1, person2) permite identificar el tipo de parentesco entre dos personas (nodos). Busca la "distancia" entre ellos en el grafo:
Distancia 1: Padre-Hijo.
Distancia 2: Abuelo-Nieto.
Distancia 3: Bisabuelo-Bisnieto.
También identifica relaciones de hermanos y primos si las personas están conectadas indirectamente.
3. Detectar Endogamia:

La función detect_inbreeding() analiza si existen múltiples caminos hacia un mismo nodo, lo que sugiere posibles casos de endogamia (cuando hay lazos familiares entre ancestros de un mismo individuo).
Busca nodos con varios caminos de acceso y los muestra, indicando posibles conexiones redundantes o complejas en el árbol.
4. Guardar y Cargar el Árbol:

El árbol genealógico se puede guardar en un archivo JSON con el método save_tree(nombre_archivo) para su almacenamiento.
El método load_tree(nombre_archivo) permite recargar el árbol desde un archivo, recuperando los nodos y las conexiones previamente guardadas.
5. Visualizar el Árbol:

El método visualize_tree() genera una visualización del árbol genealógico. Utiliza matplotlib para dibujar el grafo, mostrando los nodos (personas) y las aristas (relaciones) con etiquetas y un diseño visual organizado.

