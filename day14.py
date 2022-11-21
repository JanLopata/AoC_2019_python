import math
import os

from aoc_tools import get_data

debug_mode = True


def parse_recipe(line):
    input_and_product = line.split(" => ")
    product = Chem(input_and_product[1])

    inputs = [Chem(x) for x in input_and_product[0].split(", ")]

    return Recipe(inputs, product)


def recipe_applied(recipe, chem):
    if recipe.product_is_matching(chem.name):
        multiplier = math.ceil(chem.amount / recipe.output.amount)

        return multiplier, [x.times(multiplier) for x in recipe.inputs]

    return None, None


def process_requirements(recipes, requirements):
    for req in requirements.values():
        if req.is_ore():
            continue

        if req.amount < 1:
            continue

        for recipe in recipes:
            multiplier, new_requirements = recipe_applied(recipe, req)
            if new_requirements is not None:
                if debug_mode:
                    print("Recipe {} applied on requirement {} with result {}"
                          .format(recipe, req, new_requirements))
                requirements[req.name].add_amount(- multiplier * recipe.output.amount)
                return new_requirements


def positive_requirements_present(requirements):
    for req in requirements.values():
        if req.is_ore():
            continue
        if req.amount <= 0:
            continue

        return True

    return False


def part1(data: str):
    recipes = []
    requirements = {"FUEL": Chem("1 FUEL"), "ORE": Chem("0 ORE")}

    for line in data.split("\n"):
        if line == "":
            continue
        recipes.append(parse_recipe(line))

    while positive_requirements_present(requirements):
        if debug_mode:
            print("Requirements: {}".format(requirements))
        new_requirements = process_requirements(recipes, requirements)

        for nr in new_requirements:
            if nr.name in requirements:
                requirements.get(nr.name).add(nr)
            else:
                requirements[nr.name] = nr

    return requirements["ORE"].amount


def part2(data: str):
    pass


class Chem:

    def __init__(self, description: str):
        amount_and_name = description.split(" ")
        self.amount = int(amount_and_name[0])
        self.name = amount_and_name[1]

    def __str__(self):
        return "{} {}".format(self.amount, self.name)

    def __repr__(self):
        return "{} {}".format(self.amount, self.name)

    def is_ore(self):
        return self.name == "ORE"

    def is_fuel(self):
        return self.name == "FUEL"

    def can_sum(self, other):
        return other.name == self.name

    def add(self, other):
        if not self.can_sum(other):
            raise AssertionError
        self.amount += other.amount

    def add_amount(self, amount):
        self.amount += amount

    def copy(self):
        return Chem(str(self))

    def times(self, multiplier):
        copy = self.copy()
        copy.amount *= multiplier
        return copy


class Recipe:
    def __init__(self, inputs: list, output: Chem):
        self.inputs = inputs
        self.output = output

    def __str__(self):
        return ", ".join([str(x) for x in self.inputs]) + " => " + str(self.output)

    def product_is_matching(self, given_product):
        return self.output.name == given_product


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
