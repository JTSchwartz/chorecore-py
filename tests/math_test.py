import chorecore


def test_closest():
	assert chorecore.math.closest(8, [1, 2, 5, 7, 10]) == 7
	assert chorecore.math.closest(8, [10, 5, 2, 7, 1]) == 7
	assert chorecore.math.closest(1, [-1, 0, 12, 8, 1]) == 1
	assert chorecore.math.closest(1, [-1, 0, 12, 8]) == 0
	assert chorecore.math.closest(-1, [0, 12, 8]) == 0


def test_parse_fraction_string():
	assert chorecore.math.parse_fraction_string("1/2") == 0.5
	assert chorecore.math.parse_fraction_string("1/1") == 1
	assert chorecore.math.parse_fraction_string("-3/1") == -3
	assert chorecore.math.parse_fraction_string("7/4") == 1.75
