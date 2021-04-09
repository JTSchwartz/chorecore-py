import chorecore


def test_replacement_map():
	assert chorecore.strings.replacement_map("/`code//`", {
		"//`": "</code>",
		"/`":  "<code>",
	}) == "<code>code</code>"
	assert chorecore.strings.replacement_map("/`code//`", {
		"/`":  "<code>",
		"//`": "</code>",
	}) == "<code>code/<code>"

