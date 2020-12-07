from utils import get_lines_from_file
from collections import defaultdict


class Node:
    def __init__(self, color):
        self.total_bags = 0
        self.color = color
        self.children = []
        self.weighted_children = []
        self.parents = []

    def add_parent(self, parent_node):
        self.parents.append(parent_node)

    def add_child(self, child_node, weight):
        self.children.append(child_node)
        self.total_bags += weight
        self.weighted_children.append((weight, child_node))

    def __repr__(self):
        return f"Color: {self.color} with {self.total_bags} bags"


def parse_rule(rule):
    parent_color, rest = rule.split(' bags contain')
    if 'no other bags' in rule:
        return parent_color, []

    children_parts = [txt.replace('.', '') for txt in rest.split(',')]
    children = [" ".join(child.split(' ')[1:-1]) for child in children_parts]
    # ['4 clear indigo', '1 mirrored bronze', '1 mirrored magenta', '5 posh beige']
    final_children = []
    for child in children:
        num = child[0]
        color = child[2:]
        final_children.append((num, color))

    return parent_color, final_children


if __name__ == '__main__':
    rules = get_lines_from_file('inputs/day7_debug.txt')
    print(f"Found a total of {len(rules)} bag colors")

    nodes_index = {}
    reversed_index = defaultdict(list)

    # Go over once and create all nodes
    for rule in rules:
        parent_color, children_colors = parse_rule(rule)
        nodes_index[parent_color] = Node(parent_color)

    # Connect them together now by iterating a second time
    for rule in rules:
        parent_color, children_tuples = parse_rule(rule)
        parent_node = nodes_index[parent_color]
        for child_tuple in children_tuples:
            child_node = nodes_index[child_tuple[1]]
            parent_node.add_child(child_node, int(child_tuple[0]))
            child_node.add_parent(parent_node)

    # Now traverse the tree starting at shiny gold to get all parents
    parents_visited = set()

    def traverse_parents_from(node):
        if node.color in parents_visited:
            return
        parents_visited.add(node.color)

        for parent_node in node.parents:
            traverse_parents_from(parent_node)

    children_visited = set()

    outer = {'total': 0}

    def traverse_children_from(node, num_parent_bags):
        for (weight, child_node) in node.weighted_children:
            outer['total'] += (1 + weight) * num_parent_bags
            traverse_children_from(child_node, weight * num_parent_bags)

        outer['total'] += 1


    traverse_parents_from(nodes_index['shiny gold'])
    result = traverse_children_from(nodes_index['shiny gold'], 1)

    print(f"Total bags in shiny gold is {nodes_index['shiny gold'].total_bags}")
    print(f"Found {len(parents_visited) - 1} sources that lead to containing a shiny gold bag")
    print(f" Found {result} total bags necessary within a shiny gold")
