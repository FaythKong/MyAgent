"""Depth-first search (DFS) for graphs represented by adjacency lists."""

from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

Node = TypeVar("Node", bound=Hashable)


def depth_first_search(
    graph: Mapping[Node, Iterable[Node]], start: Node
) -> list[Node]:
    """Return nodes reachable from ``start`` in depth-first order.

    Neighbors are visited in the order supplied by ``graph``. Nodes missing
    from the mapping are treated as having no outgoing edges.
    """
    visited: set[Node] = set()
    order: list[Node] = []

    def visit(node: Node) -> None:
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, ()):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


if __name__ == "__main__":
    # An undirected graph represented by adjacency lists.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print("DFS traversal:", " -> ".join(depth_first_search(graph, "A")))
