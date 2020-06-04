# A volume / area / perimeter calculation tool


# Declaring global definitions
def side(n_sides):
    sides_array = []
    num = ['first', 'second', 'third', 'fourth']

    def add(string):
        sides_array.append(int(input(string)))

    try:
        if n_sides == 1:
            add('Please enter one dimension or radius: ')
        else:
            for i in range(n_sides):
                add('Please enter the ' + num[i] + ' significant side: ')

    except ValueError:
        print('Please input positive numerals')
        sides_array = side(n_sides)

    return sides_array


def result(volume, area, perimeter, dimensions):

    if dimensions == 1:
        print('''
        The perimeter for this shape is ''' + str(perimeter) + '''
        As it is one dimensional, it has no area.
        ''')
    elif dimensions == 2:
        print('''
        The perimeter for this shape is ''' + str(perimeter) + '''
        The area for this shape is ''' + str(area) + '''
        ''')
    elif dimensions == 3:
        print('''
        The surface area for this shape is ''' + str(area) + '''
        The volume for this shape is ''' + str(volume) + '''
        ''')


# Declaring the purpose of the tool, as well as the operating instructions
print('''
This is a perimeter, area and volume calculation tool.
Please enter the shape and then the dimensions at the respective prompt.
The volume, area and perimeter will be outputted if all is without error.
If negatives are inputted, then the tool will act as if the shape is an imaginary one.

Note:
Pi will be rounded to 3.14 in calculations.
For shapes with radius, it should be inputted first.
Otherwise, height should be inputted first if there is no radius, and second if there is.

The calculations performed will be saved.
If the program is to end, please press "ENTER" with no other input at shape selection.
''')


# Defining all the 0D shapes to be calculated
def point():
    print('''
    A point has no area or perimeter.
    ''')


# Defining all the 1D shapes to be calculated
def line():
    perimeter = side(0)[0]
    result(0, 0, perimeter, 1)


# Defining all the 2D shapes to be calculated
def triangle():
    sides = side(2)
    area = 0.5 * sides[0] * sides[1]
    sides = side(3)
    perimeter = sum(sides)
    result(0, area, perimeter, 2)


def square():
    s1 = side(1)[0]
    area = s1 ** 2
    perimeter = s1 * 4
    result(0, area, perimeter, 2)


def rectangle():
    sides = side(2)
    area = sides[0] * sides[1]
    perimeter = sides[0] * 2 + sides[1] * 2
    result(0, area, perimeter, 2)


def parallelogram():
    sides = side(2)
    area = sides[0] * sides[1]
    sides = side(2.5)
    perimeter = sides[0] + sides[1]
    result(0, area, perimeter, 2)


def trapezium():
    sides = side(2)
    area = sides[0] * sides[1]
    sides = side(4)
    perimeter = sides[0] * 2 + sides[1] + sides[2] + sides[3]
    result(0, area, perimeter, 2)


def circle():
    r = side(1)[0]
    area = 3.14 * r ** 2
    perimeter = 3.14 * r * 2
    result(0, area, perimeter, 2)


# Defining all the 3D shapes to be calculated
def cube():
    s1 = side(1)[0]
    volume = s1 ** 3
    surface_area = s1 ** 2 * 6
    result(volume, surface_area, 0, 3)


def cuboid():
    sides = side(3)
    volume = sides[0] * sides[1] * sides[2]
    surface_area = sides[0] * sides[1] * 2 + sides[0] * sides[2] * 2 + sides[1] * sides[2] * 2
    result(volume, surface_area, 0, 3)


def regular_tetrahedron():
    s1 = side(1)[0]
    volume = 2 ** 0.5 / 12 * s1 ** 3
    surface_area = (s1 ** 2 - (s1 / 2) ** 2) ** 0.5 * s1 * 2
    result(volume, surface_area, 0, 3)


def circular_cylinder():
    sides = side(2)
    volume = 3.14 * sides[0] ** 2 * sides[1]
    surface_area = 2 * 3.14 * sides[0] * sum(sides)
    result(volume, surface_area, 0, 3)


def cone():
    sides = side(2)
    volume = 1 / 3 * 3.14 * sides[0] ** 2 * sides[1]
    surface_area = 3.14 * sides[0] * (sides[0] + (sides[0] ** 2 + sides[1] ** 2) ** 0.5)
    result(volume, surface_area, 0, 3)


def sphere():
    s1 = side(1)[0]
    volume = 4 / 3 * 3.14 * s1 ** 3
    surface_area = 4 * 3.14 * s1 ** 2
    result(volume, surface_area, 0, 3)


# Shape function dictionary
shapes = {
    'point': point,
    'line': line,
    'triangle': triangle,
    'square': square,
    'rectangle': rectangle,
    'parallelogram': parallelogram,
    'trapezium': trapezium,
    'circle': circle,
    'cube': cube,
    'cuboid': cuboid,
    'regular tetrahedron': regular_tetrahedron,
    'circular cylinder': circular_cylinder,
    'cone': cone,
    'sphere': sphere
}

# Students choose the shape, then the known dimensions, the program should calculate the area and perimeter
while True:
    shape = input('What shape is to be chosen: ').lower()

    if shape in shapes:
        shapes[shape]()

# The break and error codes
    elif shape == '':
        print('''
        This tool is thankful for having purpose.
        ''')
        break
    else:
        print('''
        Sorry, but that input was not available for calculation,
        Please enter a different shape,
        Or press "ENTER" to stop.
        ''')

# Saving the calculation history
