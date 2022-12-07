from math import sin


def f1(x):
    return x ** (1 / 3)


def f2(x):
    return sin(x)


def f3(x):
    return 4 * x * ((1 - x) ** 3)


def f4(x, y):
    return ((x - 1) ** 2) + ((y - 1) ** 2) <= 1


DATA_SET = [
    {
        "type": "integral",
        "data":
            {
                "a": 0,
                "b": 8,
                "M": 2,
                "formula": f1,
                "real_value": 12
            }
    },
    {
        "type": "integral",
        "data":
            {
                "a": 0,
                "b": 3.141592653589793,
                "M": 1,
                "formula": f2,
                "real_value": 2
            }
    },
    {
        "type": "integral",
        "data":
            {
                "a": 0,
                "b": 1,
                "M": 0.421875,
                "formula": f3,
                "real_value": 0.2
            }
    },
    {
        "type": "circle",
        "data":
            {
                "a": 0,
                "b": 2,
                "M": 2,
                "formula": f4,
                "real_value": 3.141592653589793
            }
    }
]
