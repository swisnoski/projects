"""
Code to test a graph's planarity
"""

import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import math

# Set the plotting backend to Agg for non-interactive mode (useful for saving images in scripts)
matplotlib.use("Agg")

ADJACENCY_MATRIX = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 0],
]

# ADJACENCY_MATRIX = [
#     [0, 1, 1, 1, 1, 1, 1, 0],
#     [1, 0, 1, 0, 0, 0, 1, 1],
#     [1, 1, 0, 1, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 0, 1, 0, 1],
#     [0, 1, 1, 1, 1, 1, 1, 0],
# ]

# ADJACENCY_MATRIX = [
#     [0, 0, 0, 1, 1, 0, 1, 0],
#     [0, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 0, 1, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [1, 1, 0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 0, 1, 1],
#     [1, 1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 1, 0, 0, 1, 1, 0],
# ]

# ADJACENCY_MATRIX = [
#     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
# ]


NUM_VERTICES = 8


class Hamilton:
    """Class to find Hamiltonian cycle in a given graph"""

    def __init__(self, vertices_num) -> None:
        self.graph = None
        self.V = vertices_num

    def is_safe(self, v, pos, path):
        """
        Check if vertex v can be added at index pos in the Hamiltonian path.

        Parameters:
        - v (int): Vertex to check
        - pos (int): Position in path to place vertex
        - path (list): Current Hamiltonian path

        Returns:
        - bool: True if vertex can be added, False otherwise
        """
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def hamilton_cycle(self, path, pos):
        """
        Recursive utility to solve the Hamiltonian cycle problem.

        Parameters:
        - path (list): Current Hamiltonian path
        - pos (int): Position in path to place next vertex

        Returns:
        - bool: True if Hamiltonian cycle is found, False otherwise
        """
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamilton_cycle(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def solution(self):
        """
        Find a Hamiltonian cycle if it exists.

        Returns:
        - list or None: Hamiltonian cycle path if exists, None otherwise
        """
        path = [-1] * self.V
        path[0] = 0

        if not self.hamilton_cycle(path, 1):
            print(
                "There is no Hamiltonian Circuit. We cannot assess the planarity of the Graph."
            )
            return None
        else:
            print(
                f"There is a Hamiltonian Circuit; following {path + [path[0]]} is one Hamiltonian Cycle."
            )
            return path + [path[0]]


def adjacency_to_edges(adj_matrix, ordered_nodes):
    """
    Convert adjacency matrix to a list of edges.

    Parameters:
    - adj_matrix (list): Adjacency matrix representing the graph
    - ordered_nodes (list): List of node identifiers in order

    Returns:
    - list: Edge list representing graph edges
    """
    edge_list = []
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adj_matrix[i][j] == 1:
                edge_list.append((ordered_nodes[i], ordered_nodes[j]))
    return edge_list


def ham_list_to_nodes(ham_list):
    """
    Convert Hamiltonian cycle list to an edge list for visualization.

    Parameters:
    - ham_list (list): List representing Hamiltonian cycle

    Returns:
    - list: Edge list representing the Hamiltonian cycle
    """
    hamiltonian_points = [
        (ham_list[i], ham_list[i + 1]) for i in range(len(ham_list) - 1)
    ]
    hamiltonian_points.append((ham_list[-1], ham_list[0]))  # Complete the cycle
    return hamiltonian_points


h = Hamilton(NUM_VERTICES)
h.graph = ADJACENCY_MATRIX
h_sol = h.solution()
if h_sol is not None:
    hamiltonian_list = h_sol[:-1]

    graph_g = adjacency_to_edges(ADJACENCY_MATRIX, sorted(hamiltonian_list))
    hamiltonian_cycle = ham_list_to_nodes(hamiltonian_list)

    vertices = [node for node, _ in hamiltonian_cycle]
    angle_increment = 2 * math.pi / len(vertices)
    locations = [
        (math.cos(i * angle_increment), math.sin(i * angle_increment))
        for i in range(len(vertices))
    ]
    VERTEX_LOCATIONS = {vertices[i]: locations[i] for i in range(len(vertices))}


def is_planar(edge_list, hamiltonian_nodes):
    """
    Check if the graph is planar and categorize edges.

    Parameters:
    - edge_list (list): List of edges in the graph
    - hamiltonian_nodes (list): Edge list of the Hamiltonian cycle

    Returns:
    - bool: True if graph is planar, False otherwise
    - dict: Edge labels where Hamiltonian cycle edges are not labeled, interior edges are "I", and exterior edges are "O"
    """
    ordered_edge_list = order_points(edge_list)
    ordered_hamiltonian_cycle = order_points(hamiltonian_nodes)

    non_ham_edges = [
        edge for edge in ordered_edge_list if edge not in ordered_hamiltonian_cycle
    ]
    edge_labels = {edge: None for edge in non_ham_edges}

    for edge in edge_labels:
        if edge_labels[edge] is None:
            edge_labels[edge] = "I"
            intersections = []
            for other_edge in edge_labels:
                if edge_labels[other_edge] is None and edges_intersect(
                    edge, other_edge
                ):
                    edge_labels[other_edge] = "O" if edge_labels[edge] == "I" else "I"
                    intersections.append(other_edge)
            for intersecting_edge in intersections:
                for intersecting_other_edge in intersections:
                    if (
                        intersecting_edge != intersecting_other_edge
                        and edges_intersect(intersecting_edge, intersecting_other_edge)
                    ):
                        return (
                            False,
                            edge_labels,
                        )  # Returns edge labels even if non-planar

    exterior_edges = [edge for edge, label in edge_labels.items() if label == "O"]
    for i, edge1 in enumerate(exterior_edges):
        for edge2 in exterior_edges[i + 1 :]:
            if edges_intersect(edge1, edge2):
                return False, edge_labels  # Returns edge labels even if non-planar

    return True, edge_labels  # Returns edge labels if planar


def edges_intersect(edge1, edge2):
    """
    Check if two edges intersect using combinatorial geometry.

    Parameters:
    - edge1 (tuple): First edge as a tuple of nodes
    - edge2 (tuple): Second edge as a tuple of nodes

    Returns:
    - bool: True if edges intersect, False otherwise
    """
    p1 = VERTEX_LOCATIONS[edge1[0]]
    p2 = VERTEX_LOCATIONS[edge1[1]]
    p3 = VERTEX_LOCATIONS[edge2[0]]
    p4 = VERTEX_LOCATIONS[edge2[1]]
    d1 = cross_product(p1, p2, p3)
    d2 = cross_product(p1, p2, p4)
    d3 = cross_product(p3, p4, p1)
    d4 = cross_product(p3, p4, p2)
    return d1 * d2 < 0 and d3 * d4 < 0


def cross_product(p1, p2, p):
    """
    Calculate the cross product to determine relative orientation.

    Parameters:
    - p1, p2, p (tuple): Points as (x, y) coordinates

    Returns:
    - float: Cross product result
    """
    x1, y1 = p1
    x2, y2 = p2
    px, py = p
    return (y2 - y1) * (px - x1) - (x2 - x1) * (py - y1)


def order_points(tuple_list):
    """
    Sort edges consistently for comparison.

    Parameters:
    - tuple_list (list): List of edges (tuples)

    Returns:
    - list: Sorted list of edges
    """
    sorted_tuple_list = [tuple_list[0]]
    for tuples in tuple_list[1:]:
        thislist = list(tuples)
        thislist.sort()
        sorted_tuple_list.append(tuple(thislist))
    return sorted_tuple_list


def draw_colored_graph(
    graph_edges, hamiltonian_cycle, interior_edges, exterior_edges, hamiltonian_list
):
    """
    Draw a graph with different colors for Hamiltonian cycle, interior edges, and exterior edges,
    ensuring the Hamiltonian cycle appears on the exterior in the specified circular node order.

    Parameters:
    - graph_edges (list): List of all edges in the graph.
    - hamiltonian_cycle (list): Edges in the Hamiltonian cycle.
    - interior_edges (list): Edges inside the Hamiltonian cycle.
    - exterior_edges (list): Edges outside the Hamiltonian cycle.
    - hamiltonian_list (list): Ordered list of nodes in the Hamiltonian cycle.
    """
    # Create the graph using NetworkX
    G = nx.Graph()
    G.add_edges_from(graph_edges)

    # Define colors for each type of edge
    edge_colors = []
    for edge in G.edges():
        if edge in hamiltonian_cycle or (edge[1], edge[0]) in hamiltonian_cycle:
            edge_colors.append("blue")  # Hamiltonian cycle in blue
        elif edge in interior_edges or (edge[1], edge[0]) in interior_edges:
            edge_colors.append("green")  # Interior edges in green
        elif edge in exterior_edges or (edge[1], edge[0]) in exterior_edges:
            edge_colors.append("red")  # Exterior edges in red
        else:
            edge_colors.append("black")  # Any other edges in black

    # Ensure nodes are positioned in the specified Hamiltonian cycle order
    pos = nx.shell_layout(G, nlist=[hamiltonian_list])

    # Draw the graph with colored edges
    nx.draw(
        G,
        pos,
        with_labels=True,
        edge_color=edge_colors,
        node_color="lightgrey",
        node_size=500,
    )

    # Add legend for edge types
    edge_legend = [
        plt.Line2D([0], [0], color="blue", lw=2, label="Hamiltonian Cycle"),
        plt.Line2D([0], [0], color="green", lw=2, label='"Interior"" Edges'),
        plt.Line2D([0], [0], color="red", lw=2, label='"Exterior" Edges'),
    ]

    plt.legend(
        handles=edge_legend,
        bbox_to_anchor=(1.05, 1),  # Adjust position to avoid clipping
    )

    # Show or save the figure
    plt.savefig("colored_graph.png", format="png", bbox_inches="tight")
    plt.clf()  # Clear the plot after saving to avoid overlap


if h_sol is not None:

    planar, edge_labels = is_planar(graph_g, hamiltonian_cycle)

    # Separate edges based on labels
    interior_edges = [edge for edge, label in edge_labels.items() if label == "I"]
    exterior_edges = [edge for edge, label in edge_labels.items() if label == "O"]

    g = nx.Graph()
    g.add_edges_from(graph_g)
    h_cycle = nx.Graph()
    h_cycle.add_edges_from(hamiltonian_cycle)
    # Save images of the graphs
    nx.draw(
        g, with_labels=True, edge_color="black", node_color="lightgrey", node_size=500
    )
    plt.savefig("graph.png")
    plt.clf()

    nx.draw(
        h_cycle,
        with_labels=True,
        edge_color="blue",
        node_color="lightgrey",
        node_size=500,
    )
    plt.savefig("h_cycle.png")
    plt.clf()

    # Draw the graph
    draw_colored_graph(
        graph_g, hamiltonian_cycle, interior_edges, exterior_edges, hamiltonian_list
    )

    # Test planarity of the graph
    print(f"The planarity of this graph is {is_planar(graph_g, hamiltonian_cycle)[0]}.")
    print(f"Test planarity is: {nx.check_planarity(g)[0]}.")
