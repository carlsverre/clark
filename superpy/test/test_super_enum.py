from superpy import SuperEnum

def test_basic():
    class Colors(SuperEnum):
        red = SuperEnum.Element
        blue = SuperEnum.E
        green = SuperEnum.E

    class OtherColors(SuperEnum):
        yellow = SuperEnum.Element
        red = SuperEnum.Element

    red = Colors['red']
    red = Colors.red

    assert red in Colors

    assert str(red) == 'red'
    assert red == Colors.red

    assert Colors.red != OtherColors.red

    class Foo(object):
        class Colors(SuperEnum):
            blue = SuperEnum.Element

    assert Foo.Colors.blue != Colors.blue
