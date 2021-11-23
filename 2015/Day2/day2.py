def calculate_area(box_dimensions_list):
    l = box_dimensions_list[0]
    w = box_dimensions_list[1]
    h = box_dimensions_list[2]

    side_sizes = [l * w, w * h, h * l]
    smallest_side = min(side_sizes)
    square_feet_area = smallest_side
    for side in side_sizes:
        square_feet_area = square_feet_area + side * 2
    return square_feet_area


def calculate_ribbon(box_dimensions_list):
    l = box_dimensions_list[0]
    w = box_dimensions_list[1]
    h = box_dimensions_list[2]

    box_dimensions_list.remove(max(box_dimensions_list))
    return ( (sum(box_dimensions_list)*2) + (l*w*h) )


def split_boxes(box_dimension):
    split_list = box_dimension.split('x')
    return [int(item) for item in split_list]


with open("input.txt", 'r') as box_file:
    boxes = box_file.readlines()
    total_square_feet = 0
    for box in boxes:
        total_square_feet += calculate_area(split_boxes(box))
    print(f"Part 1: total square feet is {total_square_feet}")

    total_feet_ribbon = 0
    for box in boxes:
        total_feet_ribbon += calculate_ribbon(split_boxes(box))

    print(f"Part 2: total feet of ribbon is {total_feet_ribbon}")
