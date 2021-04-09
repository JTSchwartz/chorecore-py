import chorecore


def test_lowercase_at():
	assert chorecore.alpha.lowercase_at(0) == "a"
	assert chorecore.alpha.lowercase_at(26) == "a"


def test_uppercase_at():
	assert chorecore.alpha.uppercase_at(0) == "A"
	assert chorecore.alpha.uppercase_at(26) == "A"


def test_lowercase_vowel_at():
	assert chorecore.alpha.lowercase_vowel_at(0) == "a"
	assert chorecore.alpha.lowercase_vowel_at(26) == "a"


def test_uppercase_vowel_at():
	assert chorecore.alpha.uppercase_vowel_at(0) == "A"
	assert chorecore.alpha.uppercase_vowel_at(26) == "A"


def test_lowercase_non_vowel_at():
	assert chorecore.alpha.lowercase_non_vowel_at(0) == "b"
	assert chorecore.alpha.lowercase_non_vowel_at(26) == "b"


def test_uppercase_non_vowel_at():
	assert chorecore.alpha.uppercase_non_vowel_at(0) == "B"
	assert chorecore.alpha.uppercase_non_vowel_at(26) == "B"
