import os

from aoc_tools import get_data

debug_mode = False


class Piece:

    def __init__(self, indices_set: set[tuple[int, int]], number=0):
        self.source_indices = indices_set
        dim_i, dim_j = self.compute_dimensions()
        self.dim_i = dim_i
        self.dim_j = dim_j
        self.number = number

    def compute_dimensions(self):
        max_i = max([x[0] for x in self.source_indices])
        max_j = max([x[1] for x in self.source_indices])
        return max_i, max_j

    def get_indices(self):
        return self.source_indices

    def rotate_right(self):
        rotated = set()
        for i, j in self.source_indices:
            rotated.add((j, self.dim_i - i))
        return Piece(rotated)

    def flip_top_down(self):
        flipped = set()
        for i, j in self.source_indices:
            flipped.add((self.dim_i - i, j))
        return Piece(flipped)

    def hash_repr(self):
        result = 0
        for i in range(self.dim_i + 1):
            for j in range(self.dim_j + 1):
                result = result << 1
                if (i, j) in self.source_indices:
                    result += 1
        return result

    # debug method
    def str_multiline(self):
        lines = []
        for i in range(self.dim_i + 1):
            line = "".join(['#' if (i, j) in self.source_indices else '.' for j in range(self.dim_j + 1)])
            lines.append(line)
        return "\n".join(lines)

    # debug method
    def print(self):
        print(self.str_multiline())


class PreparedPiece:

    def __init__(self, piece: Piece):
        self.original_piece = piece
        self.unique_variants = []
        self.generate_variants()

    def generate_variants(self):
        all_variants = []
        current_piece = self.original_piece
        for i in range(4):
            all_variants.append(current_piece)
            all_variants.append(current_piece.flip_top_down())
            current_piece = current_piece.rotate_right()

        unique_variants = self.get_unique_variants(all_variants)

        self.unique_variants = unique_variants

    @staticmethod
    def get_unique_variants(variants_full):
        known_hashed = set()
        unique_variants = []
        for variant in variants_full:
            hash_repr = variant.hash_repr()
            if hash_repr in known_hashed:
                continue
            unique_variants.append(variant)
            known_hashed.add(hash_repr)
        return unique_variants


def parse_piece(part: str) -> tuple[int, PreparedPiece]:
    line_idx = -1
    num = None
    raw_set = set()
    for line in part.splitlines():
        if len(line) == 0:
            continue
        if ":" in line:
            num = int(line[:-1])
        else:
            for i in range(len(line)):
                if line[i] == "#":
                    raw_set.add((line_idx, i))

        line_idx += 1

    return num, PreparedPiece(Piece(raw_set, num))


def parse_requirements(part: str):
    requirements = []
    for line in part.splitlines():
        sp = line.split(": ")
        dimensions = parse_dimensions(sp[0])
        parts = parse_parts(sp[1])
        requirements.append((dimensions, parts))
    return requirements


def parse_dimensions(line: str):
    sp = line.split("x")
    return int(sp[0]), int(sp[1])


def parse_parts(line: str):
    sp = line.split()
    result = []
    for idx in range(len(sp)):
        count = int(sp[idx])
        if count > 0:
            result.append((idx, count))
    return result


def parse_data(data):
    pieces = []
    requirements = None
    for part in data.split("\n\n"):
        if "x" in part:
            requirements = parse_requirements(part)
        else:
            n, p_set = parse_piece(part)
            pieces.append((n, p_set))

    print(pieces)
    print(requirements)

    return pieces, requirements


def check_fit(r, pieces):
    return False


def part1(data: str):
    pieces, requirements = parse_data(data)
    fit_count = 0
    for r in requirements:
        if check_fit(r, pieces):
            fit_count += 1

    return 0


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
