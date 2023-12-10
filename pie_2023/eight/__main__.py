import re
from math import lcm

from utils.file_utils import read_input

if __name__ == "__main__":
    directions, nodes_input = read_input().split("\n\n")
    nodes = {}
    for line in nodes_input.split("\n"):
        node, options_string = line.split(" = ")
        options = re.findall(r"\d*[A-Z]+", options_string)
        nodes[node] = (options[0], options[1])

    index = 0
    curr_node = "AAA"
    count = 0
    while curr_node != "ZZZ":
        direction = directions[index % len(directions)]
        curr_node = nodes[curr_node][direction == "R"]
        count += 1
        index += 1
    print(count)

    count_pt2 = 0
    start_nodes = [node for node, (left, right) in nodes.items() if node.endswith("A")]
    counts = []
    for start_node in start_nodes:
        curr_node = start_node
        count = 0
        index_pt_2 = 0
        while not curr_node.endswith("Z"):
            direction = directions[index_pt_2 % len(directions)]
            curr_node = nodes[curr_node][direction == "R"]
            count += 1
            index_pt_2 += 1
        counts.append(count)
    print(lcm(*counts))
