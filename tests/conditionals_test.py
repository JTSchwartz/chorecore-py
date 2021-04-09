import chorecore
from constants import Constant


def test_is_even():
	assert chorecore.conditionals.is_equal(1, 1, else_val=Constant.INCORRECT) == 1
	assert chorecore.conditionals.is_equal(1, 1, Constant.CORRECT, Constant.INCORRECT) == Constant.CORRECT
	assert chorecore.conditionals.is_equal(1, 2, Constant.CORRECT, Constant.INCORRECT) == Constant.INCORRECT

# is_equal
# is_false
# is_gt
# is_gte
# is_lt
# is_lte
# is_none
# is_not_equal
# is_not_none
# is_odd
# is_true
