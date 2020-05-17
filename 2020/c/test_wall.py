import numpy as np
import pytest
import os
import wall


def get_tests(file_name):
    """ Get tests from file """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name), "r") as f_obj:
        t = int(f_obj.readline().rstrip("\n"))  # read number of tests
        tests = []
        for t_i in range(1, t + 1):
            sr, sc = f_obj.readline().rstrip("\n").split()
            r = int(sr)
            c = int(sc)
            wall = [f_obj.readline().rstrip("\n") for _ in range(r)]
            tests.append((r, c, wall))

    return tests


@pytest.mark.parametrize(("r", "c", "wall_inp"), get_tests("wall_unstable.in"))
def test_unstable(r, c, wall_inp):
    assert wall.solve(r, c, wall_inp) == -1


@pytest.mark.parametrize(("r", "c", "wall_inp"), get_tests("wall_stable.in"))
def test_stable(r, c, wall_inp):
    sol = wall.solve(r, c, wall_inp)
    assert is_stable(sol, wall_inp, r, c)


def is_stable(sol, wall, r, c):
    mat = np.zeros((r, c))
    for s in sol:
        for i in range(r):
            for j in range(c):
                if wall[i][j] == s:
                    mat[i, j] = 1
        if not _is_stable(mat, r, c):
            return False

    assert np.count_nonzero(mat) == r * c
    return True


def _is_stable(mat, r, c):
    for i in range(1, r):
        for j in range(c):
            if mat[i-1, j] and not mat[i, j]:
                return False
    return True


@pytest.mark.parametrize(
    ("a", "b", "r"), [
        ("A", "A", "A"),
        ("A", "AB", "AB"),
        ("ABC", "CD", "ABCD"),
        ("OZ", "AOZ", "AOZ"),
        ("AOZ", "OZ", "AOZ"),
        ("ABCD", "BC", "ABCD"),
        ("A", "B", "AB"),
        ("ABC", "B", "ABC"),
        ("ABCDE", "BD", "ABCDE"),
    ]
)
def test_merge(a, b, r):
    assert wall.merge(a, b) == r
