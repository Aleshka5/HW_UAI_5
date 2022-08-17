import math
def test_filter():
    assert list(filter(lambda x: x > 0, [-1,0,1])) == [1]
    assert list(filter(lambda x: x < 0, [-1,0,1])) == [-1]
    assert list(filter(lambda x: x == 0, [-1, 0, 1])) == [0]
    assert list(filter(lambda x: x != 0, [-1, 0, 1])) == [-1,1]

def test_map():
    assert list(map(int,['1','2','3'])) == [1, 2, 3]
    assert list(map(float, ['1.2', '2.3', '3.4'])) == [1.2, 2.3, 3.4]
    assert list(map(str, [1, 2, 3])) == ['1', '2', '3']

def test_sorted():
    assert sorted([1,2,3],reverse=True) == [3, 2, 1]
    assert sorted([3,2,1]) == [1, 2, 3]
    assert sorted([1,2,3]) == [1, 2, 3]
    assert sorted([3,2,1], reverse=True) == [3, 2, 1]

def test_math_pi():
    assert math.pi > 3.1415926
    assert math.pi < 3.1415927

def test_math_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(16) == 4
    assert math.sqrt(64) == 8
    assert math.sqrt(1) == 1

def test_math_pow():
    for i in range(5):
        assert math.pow(1, i) == 1
        if i == 0:
            assert math.pow(0, i) == 1
        else:
            assert math.pow(0, i) == 0
    assert math.pow(5, 2) == 25
    assert math.pow(3, 3) == 27

def test_math_hypot():
    assert math.hypot(4,3) == 5
    assert math.hypot(3,4) == 5
    assert abs(math.sqrt(2) - math.hypot(1,1)) < 0.0001
    assert abs(math.sqrt(5) - math.hypot(1, 2)) < 0.0001