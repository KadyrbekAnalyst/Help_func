from shapely.geometry import LineString, Polygon, Point


def is_object_inside_shape(object_coords, shape_coords, object_type='line'):
    # convert line and shape coordinates to shapely objects
    if object_type == 'point':
        object = Point(object_coords[0], object_coords[1])
    elif object_type == 'line':
        object = LineString([(object_coords[0], object_coords[1]), (object_coords[2], object_coords[3])])
    elif object_type == 'polygon':
        object = Polygon([(object_coords[i], object_coords[i+1]) for i in range(0, len(object_coords), 2)])
    else:
        raise ValueError("Invalid line_type: must be 'point', 'line', or 'polygon'")

    shape = Polygon([(shape_coords[i], shape_coords[i+1]) for i in range(0, len(shape_coords), 2)])

    # check if line intersects shape
    if object.intersects(shape):
        return True
    
    return False


a = is_object_inside_shape((200,150,200,300,300,200,300,70), (50,50,50,300,100,300,100,50),object_type = 'polygon')
print(a)


# В функцию полигон можно запихивать треугольник и так далее увеличивать кол-во углов
# Пока думаю над реализацией на прием многоугольника