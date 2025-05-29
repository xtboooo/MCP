import pytest

def sum_squares(arr):
    """Sum the squares of the numbers in an array."""
    return sum(map(lambda x: x**2, arr))

# Your tests can also be benchmarks
@pytest.mark.benchmark
def test_sum_squares():
    assert sum_squares(range(1000)) == 332833500
