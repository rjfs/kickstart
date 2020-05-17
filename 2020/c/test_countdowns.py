import pytest
import countdowns


@pytest.mark.parametrize(
    ("k", "seq", "ans"), [
        (3, "1 2 3 7 9 3 2 1 8 3 2 1", 2),
        (2, "101 100 99 98", 0),
        (6, "100 7 6 5 4 3 2 1 100", 1),
        (6, "6 5 6 5 4 3 2 1 100", 1),
        (6, "6 5 5 4 3 2 1 100", 0),
        (6, "6 5 4 3 2 1", 1),
        (2, "1 2 1", 1),
        (3, "3 2 1 3 2 1", 2),
        (2, "2 1 2 1", 2),
        (3, "3 2 3 2", 0),
        (2, "2 1", 1),
        (3, "3 2 1", 1),
        (3, "3 1 1", 0),
    ]
)
def test_solve(k, seq, ans):
    n = len(seq.split())
    assert 2 <= k <= n
    assert countdowns.solve(n, k, seq) == ans
