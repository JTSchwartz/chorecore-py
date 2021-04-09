import chorecore


def test_days():
	assert chorecore.time.days(2) == chorecore.time.Time.DAY * 2
	assert chorecore.time.days(.5) == chorecore.time.Time.DAY * .5


def test_hours():
	assert chorecore.time.hours(2) == chorecore.time.Time.HOUR * 2
	assert chorecore.time.hours(.5) == chorecore.time.Time.HOUR * .5


def test_minutes():
	assert chorecore.time.minutes(2) == chorecore.time.Time.MINUTE * 2
	assert chorecore.time.minutes(.5) == chorecore.time.Time.MINUTE * .5


def test_milliseconds():
	assert chorecore.time.milliseconds(2) == chorecore.time.Time.MILLISECOND * 2
	assert chorecore.time.milliseconds(.5) == chorecore.time.Time.MILLISECOND * .5


def test_seconds():
	assert chorecore.time.seconds(2) == chorecore.time.Time.SECOND * 2
	assert chorecore.time.seconds(.5) == chorecore.time.Time.SECOND * .5


def test_weeks():
	assert chorecore.time.weeks(2) == chorecore.time.Time.WEEK * 2
	assert chorecore.time.weeks(.5) == chorecore.time.Time.WEEK * .5
