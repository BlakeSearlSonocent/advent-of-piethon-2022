import re

from pie.file_utils import read_lines


def geodes_opened(
    t_remaining: int,
    ore_cost_ore: int,
    clay_cost_ore: int,
    obsidian_cost_ore: int,
    obsidian_cost_clay: int,
    geode_cost_ore: int,
    geode_cost_obsidian: int,
    ore: int,
    clay: int,
    obsidian: int,
    geodes: int,
    ore_robots: int,
    clay_robots: int,
    obsidian_robots: int,
    geode_robots: int,
    geode_cache,
):
    # print(clay)
    if t_remaining == 0:
        # print(geodes)
        return geodes

    max_required_ore = max(ore_cost_ore, clay_cost_ore, obsidian_cost_ore, geode_cost_ore) * (t_remaining - 1)
    next_ore = max_required_ore if ore > max_required_ore else ore

    max_required_clay = obsidian_cost_clay * (t_remaining - 1)
    next_clay = max_required_clay if clay > max_required_clay else clay

    max_required_obsidian = geode_cost_obsidian * (t_remaining - 1)
    next_obsidian = max_required_obsidian if obsidian > max_required_obsidian else obsidian

    if (
        t_remaining,
        ore_cost_ore,
        clay_cost_ore,
        obsidian_cost_ore,
        obsidian_cost_clay,
        geode_cost_ore,
        geode_cost_obsidian,
        next_ore,
        next_clay,
        next_obsidian,
        geodes,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ) in geode_cache:
        # print("cache hit")
        return geode_cache[
            t_remaining,
            ore_cost_ore,
            clay_cost_ore,
            obsidian_cost_ore,
            obsidian_cost_clay,
            geode_cost_ore,
            geode_cost_obsidian,
            next_ore,
            next_clay,
            next_obsidian,
            geodes,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
        ]

    best = geodes_opened(
        t_remaining - 1,
        ore_cost_ore,
        clay_cost_ore,
        obsidian_cost_ore,
        obsidian_cost_clay,
        geode_cost_ore,
        geode_cost_obsidian,
        ore + ore_robots,
        clay + clay_robots,
        obsidian + obsidian_robots,
        geodes + geode_robots,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
        geode_cache,
    )

    # only make an ore robot if we don't already have surplus of ore. i.e. (23 - t) * greatest_ore_cost > ore
    greatest_ore_cost = max(ore_cost_ore, clay_cost_ore, obsidian_cost_ore, geode_cost_ore)
    worth_making_ore_robot = (t_remaining - 1) * greatest_ore_cost > ore
    if ore_cost_ore <= ore and worth_making_ore_robot:
        # print("made ore robot")
        best = max(
            best,
            geodes_opened(
                t_remaining - 1,
                ore_cost_ore,
                clay_cost_ore,
                obsidian_cost_ore,
                obsidian_cost_clay,
                geode_cost_ore,
                geode_cost_obsidian,
                next_ore + ore_robots - ore_cost_ore,
                next_clay + clay_robots,
                next_obsidian + obsidian_robots,
                geodes + geode_robots,
                ore_robots + 1,
                clay_robots,
                obsidian_robots,
                geode_robots,
                geode_cache,
            ),
        )

    # only make a clay robot if we don't already have enough clay to make clay greediest robot every round
    worth_making_clay_robot = ((t_remaining - 1) * obsidian_cost_clay) > clay
    if ore >= clay_cost_ore and worth_making_clay_robot:
        # print("made clay robot")
        best = max(
            best,
            geodes_opened(
                t_remaining - 1,
                ore_cost_ore,
                clay_cost_ore,
                obsidian_cost_ore,
                obsidian_cost_clay,
                geode_cost_ore,
                geode_cost_obsidian,
                next_ore + ore_robots - clay_cost_ore,
                next_clay + clay_robots,
                next_obsidian + obsidian_robots,
                geodes + geode_robots,
                ore_robots,
                clay_robots + 1,
                obsidian_robots,
                geode_robots,
                geode_cache,
            ),
        )

    # only make an obsidian robot if we don't already have enough obsidian to make obsidian greediest robot every round
    worth_making_obsidian_robot = ((t_remaining - 1) * geode_cost_obsidian) > obsidian
    if ore >= obsidian_cost_ore and clay >= obsidian_cost_clay and worth_making_obsidian_robot:
        best = max(
            best,
            geodes_opened(
                t_remaining - 1,
                ore_cost_ore,
                clay_cost_ore,
                obsidian_cost_ore,
                obsidian_cost_clay,
                geode_cost_ore,
                geode_cost_obsidian,
                next_ore + ore_robots - obsidian_cost_ore,
                next_clay + clay_robots - obsidian_cost_clay,
                next_obsidian + obsidian_robots,
                geodes + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots + 1,
                geode_robots,
                geode_cache,
            ),
        )

    if ore >= geode_cost_ore and obsidian >= geode_cost_obsidian:
        best = max(
            best,
            geodes_opened(
                t_remaining - 1,
                ore_cost_ore,
                clay_cost_ore,
                obsidian_cost_ore,
                obsidian_cost_clay,
                geode_cost_ore,
                geode_cost_obsidian,
                next_ore + ore_robots - geode_cost_ore,
                next_clay + clay_robots,
                next_obsidian + obsidian_robots - geode_cost_obsidian,
                geodes + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots + 1,
                geode_cache,
            ),
        )

    geode_cache[
        t_remaining,
        ore_cost_ore,
        clay_cost_ore,
        obsidian_cost_ore,
        obsidian_cost_clay,
        geode_cost_ore,
        geode_cost_obsidian,
        next_ore,
        next_clay,
        next_obsidian,
        geodes,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ] = best
    return best


if __name__ == "__main__":
    blueprints = [map(int, re.findall("[0-9]+", line)) for line in read_lines("nineteen/input.txt")]

    # scores = [] for i, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore,
    # geode_cost_obsidian in blueprints: scores.append(geodes_opened(24, ore_cost, clay_cost, obsidian_cost_ore,
    # obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian, 0, 0, 0, 0, 1, 0, 0, 0, {}) * i) print(sum(scores))
    scores = []
    for (
        i,
        ore_cost,
        clay_cost,
        obsidian_cost_ore,
        obsidian_cost_clay,
        geode_cost_ore,
        geode_cost_obsidian,
    ) in blueprints[:3]:
        scores.append(
            geodes_opened(
                32,
                ore_cost,
                clay_cost,
                obsidian_cost_ore,
                obsidian_cost_clay,
                geode_cost_ore,
                geode_cost_obsidian,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                {},
            )
        )
    print(scores)
