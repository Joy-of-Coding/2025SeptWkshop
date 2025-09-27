from Sept import match


def test_01():
    assert match("tap", "apt") == True

def test_02():
    assert match("live","") == False