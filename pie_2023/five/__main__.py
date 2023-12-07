from utils.file_utils import read_input

if __name__ == "__main__":
    seeds, *puzzle = read_input().split("\n\n")
    seeds = seeds.split(": ")[1].split()

    mappings = [[rule.split() for rule in rules.split("\n")[1:]] for rules in puzzle]

    distances = []
    for seed in seeds:
        curr = seed
        for mapping in mappings:
            for dest_start, source_start, range_length in mapping:
                if int(curr) in range(int(source_start), int(source_start) + int(range_length)):
                    curr = int(dest_start) + int(curr) - int(source_start)
                    break

        distances.append(curr)

    lower_bound = min(distances)
    print(lower_bound)

    reversed_mappings = mappings[::-1]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i + 1]))

    # Map backwards to find first location
    found = False
    for i in range(69040623, 75040623):
        if found:
            break

        curr = i
        for mapping in reversed_mappings:
            for dest_start, source_start, range_length in mapping:
                if int(curr) in range(int(dest_start), int(dest_start) + int(range_length)):
                    curr = int(source_start) + int(curr) - int(dest_start)
                    break

        for lower_bound, range_length in seed_ranges:
            if int(lower_bound) <= curr < int(lower_bound) + int(range_length):
                print(f"found seed {curr} at position {i}")
                found = True
                break
