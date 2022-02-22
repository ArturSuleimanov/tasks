def files_parse():
    file1_route = input()
    file2_route = input()
    with open(file1_route, 'r', encoding='utf-8') as circle_specification:
        circle_specification = circle_specification.readlines()
        circle_center_coords = [int(i) for i in circle_specification[0].split()]
        radius = int(circle_specification[1])

    with open(file2_route, 'r', encoding='utf-8') as dot_coords:
        dot_coords = dot_coords.readlines()
        dot_coords = [list(map(int, i.split())) for i in dot_coords]
    
    return circle_center_coords, radius, dot_coords





def belongs_or_not():
    circle_center_coords, radius, dot_coords  = files_parse()
    for i in dot_coords:
        if (i[0] - circle_center_coords[0]) ** 2 + (i[1] - circle_center_coords[1]) ** 2 == radius ** 2:
            print(0)
        elif (i[0] - circle_center_coords[0]) ** 2 + (i[1] - circle_center_coords[1]) ** 2 > radius ** 2:
            print(2)
        else:
            print(1)

belongs_or_not()