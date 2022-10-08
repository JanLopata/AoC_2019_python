import os


def part1(data: str, x_size=25, y_size=6):
    full_ints = [int(x) for x in data]
    layers = read_layers(full_ints, x_size, y_size)

    zeros_count = [count_given_number(layer, 0) for layer in layers]
    arg_min_zeros = zeros_count.index(min(zeros_count))
    least_zeros_layer = layers[arg_min_zeros]

    return count_given_number(least_zeros_layer, 1) * count_given_number(least_zeros_layer, 2)


def read_layers(full_ints, x_size, y_size):
    layers = []
    layer_number = 0
    y_number = 0
    x_number = -1
    for i in range(len(full_ints)):
        x_number += 1
        if x_number >= x_size:
            x_number = 0
            y_number += 1

        if y_number >= y_size:
            y_number = 0
            layer_number += 1

        if len(layers) <= layer_number:
            layers.append(init_layer(x_size, y_size))
        # print("{}, {}, {}, num={}".format(layer_number, y_number, x_number, full_ints[i]))

        layers[layer_number][y_number][x_number] = full_ints[i]
    return layers


def count_given_number(layer, target):
    result = 0
    for row in layer:
        for val in row:
            result += val == target
    return result


def init_layer(x_size, y_size):
    layer = []
    for y in range(y_size):
        layer.append([-1 for x in range(x_size)])
    return layer


def render_layers(layers, x_size, y_size):
    layer = layers[0]
    for c in range(1, len(layers)):
        layer_com = layers[c]
        for x in range(x_size):
            for y in range(y_size):
                if (layer[y][x] == 2):
                    layer[y][x] = layer_com[y][x]

    return layer


def part2(data: str, x_size=25, y_size=6):
    full_ints = [int(x) for x in data]
    layers = read_layers(full_ints, x_size, y_size)

    result_layer = render_layers(layers, x_size, y_size)
    result_text = ""
    for row in result_layer:
        for val in row:
            if val == 1:
                result_text += "*"
            else:
                result_text += " "
        result_text += "\n"

    return result_text


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
