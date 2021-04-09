import chorecore
from constants import Constant


def test_is_even():
	assert chorecore.conditionals.is_even(2, else_val=Constant.INCORRECT) == 2
	assert chorecore.conditionals.is_even(1, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_even(2, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_even(1, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_equal():
	assert chorecore.conditionals.is_equal(1, 1, else_val=Constant.INCORRECT) == 1
	assert chorecore.conditionals.is_equal(1, 2, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_equal(1, 1, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_equal(1, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_equal("Equal", "Equal", Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_equal("Equal", "Not Equal", Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_false():
	assert chorecore.conditionals.is_false(False, else_val=Constant.INCORRECT) is False
	assert chorecore.conditionals.is_false(True, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_false(False, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_false(True, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_false("", Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_false("False", Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_gt():
	assert chorecore.conditionals.is_gt(2, 1, else_val=Constant.INCORRECT) == 2
	assert chorecore.conditionals.is_gt(2, 2, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_gt(1, 2, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_gt(2, 1, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_gt(2, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_gt(1, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_gte():
	assert chorecore.conditionals.is_gte(2, 1, else_val=Constant.INCORRECT) == 2
	assert chorecore.conditionals.is_gte(2, 2, else_val=Constant.INCORRECT) == 2
	assert chorecore.conditionals.is_gte(1, 2, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_gte(2, 1, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_gte(2, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_gte(1, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_lt():
	assert chorecore.conditionals.is_lt(1, 2, else_val=Constant.INCORRECT) == 1
	assert chorecore.conditionals.is_lt(2, 2, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_lt(2, 1, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_lt(1, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_lt(2, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_lt(2, 1, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_lte():
	assert chorecore.conditionals.is_lte(1, 2, else_val=Constant.INCORRECT) == 1
	assert chorecore.conditionals.is_lte(2, 2, else_val=Constant.INCORRECT) == 2
	assert chorecore.conditionals.is_lte(2, 1, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_lte(1, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_lte(2, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_lte(2, 1, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_none():
	assert chorecore.conditionals.is_none(None, else_val=Constant.INCORRECT) is None
	assert chorecore.conditionals.is_none(True, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_none(None, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_none(True, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_none(1, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_none("Not None", Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_none("", Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_not_equal():
	assert chorecore.conditionals.is_not_equal(1, 2, else_val=Constant.INCORRECT) == 1
	assert chorecore.conditionals.is_not_equal(1, 1, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_not_equal(1, 2, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_not_equal(1, 1, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_not_equal("Equal", "Not Equal", Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_not_equal("Equal", "Equal", Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	
	
def test_is_not_none():
	assert chorecore.conditionals.is_not_none(True, else_val=Constant.INCORRECT) is True
	assert chorecore.conditionals.is_not_none(None, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_not_none(True, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_not_none(1, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_not_none("Not None", Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_not_none("", Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_not_none(None, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_odd():
	assert chorecore.conditionals.is_odd(1, else_val=Constant.INCORRECT) == 1
	assert chorecore.conditionals.is_odd(2, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_odd(1, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_odd(2, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT


def test_is_true():
	assert chorecore.conditionals.is_true(True, else_val=Constant.INCORRECT) is True
	assert chorecore.conditionals.is_true(False, else_val=Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_true(True, Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_true(False, Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
	assert chorecore.conditionals.is_true("True", Constant.CORRECT, Constant.INCORRECT) is Constant.CORRECT
	assert chorecore.conditionals.is_true("", Constant.CORRECT, Constant.INCORRECT) is Constant.INCORRECT
