import chorecore


def test_fraction_to_symbol():
	assert chorecore.symbols.fraction_to_symbol("1/2") == chorecore.fraction.Fraction.ONE_HALF
	assert chorecore.symbols.fraction_to_symbol("1/8") == chorecore.fraction.Fraction.ONE_EIGHTH
	assert chorecore.symbols.fraction_to_symbol("1/10") == chorecore.fraction.Fraction.ONE_TENTH
	assert chorecore.symbols.fraction_to_symbol("0.5") == chorecore.fraction.Fraction.ONE_HALF
	assert chorecore.symbols.fraction_to_symbol("0.75") == chorecore.fraction.Fraction.THREE_QUARTERS
	assert chorecore.symbols.fraction_to_symbol("0.875") == chorecore.fraction.Fraction.SEVEN_EIGHTHS
	assert chorecore.symbols.fraction_to_symbol(1/2) == chorecore.fraction.Fraction.ONE_HALF
	assert chorecore.symbols.fraction_to_symbol(1/8) == chorecore.fraction.Fraction.ONE_EIGHTH
	assert chorecore.symbols.fraction_to_symbol(1/10) == chorecore.fraction.Fraction.ONE_TENTH
	assert chorecore.symbols.fraction_to_symbol(0.5) == chorecore.fraction.Fraction.ONE_HALF
	assert chorecore.symbols.fraction_to_symbol(0.75) == chorecore.fraction.Fraction.THREE_QUARTERS
	assert chorecore.symbols.fraction_to_symbol(0.875) == chorecore.fraction.Fraction.SEVEN_EIGHTHS
