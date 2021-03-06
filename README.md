# ChoreCore

![PyPi Version](https://img.shields.io/pypi/v/chorecore)
![Downloads](https://img.shields.io/pypi/dm/chorecore)
![Code Size](https://img.shields.io/github/languages/code-size/jtschwartz/chorecore-py)
![GitHub Issues](https://img.shields.io/github/issues/jtschwartz/chorecore-py)

ChoreCore is a multi-language utility library built to make every developer's life easier.

It is made up of a plethora of modules and this documentation will assume that you import all definitions from each
module
<details>
  <summary>Import Explanation</summary>


Obviously this method of importing is not required, but is simply used in this documentation to save time and space.

```python
from chorecore.alphabet import *
from chorecore.conditionals import *
from chorecore.fraction import *
from chorecore.math import *
from chorecore.strings import *
from chorecore.symbols import *
from chorecore.time import *
```
</details>

<hr/>

## Alphabet

### Class

#### `Alphabet`
Contains the alphabet in an abundance of variants in Array form.

| Name                 | Value                                                                                                                              |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------|
| LOWERCASE            | ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] |
| UPPERCASE            | ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] |
| LOWERCASE_VOWELS     | ["a", "e", "i", "o", "u", "y"]                                                                                                     | 
| UPPERCASE_VOWELS     | ["A", "E", "I", "O", "U", "Y"]                                                                                                     |
| LOWERCASE_NON_VOWELS | ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]                               |
| UPPERCASE_NON_VOWELS | ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]                               |

#### `Alphabet.Strings`
Contains the alphabet in an abundance of variants in String form.

| Name                 | Value                        |
|----------------------|------------------------------|
| LOWERCASE            | "abcdefghijklmnopqrstuvwxyz" |
| UPPERCASE            | "ABCDEFGHIJKLMNOPQRSTUVWXYZ" |
| LOWERCASE_VOWELS     | "aeiouy"                     | 
| UPPERCASE_VOWELS     | "AEIOUY"                     |
| LOWERCASE_NON_VOWELS | "bcdfghjklmnpqrstvwxz"       |
| UPPERCASE_NON_VOWELS | "BCDFGHJKLMNPQRSTVWXZ"       |

### Methods
All constants have an accompanying method that will simply return the character at the index passed to it

- #### `lowercase_at(i: int): str`
- #### `uppercase_at(i: int): str`
- #### `lowercase_vowel_at(i: int): str`
- #### `uppercase_vowel_at(i: int): str`
- #### `lowercase_non_vowel_at(i: int): str`
- #### `uppercase_non_vowel_at(i: int): str`

<hr/>

## Conditionals
Conditional functions were mainly made to simplify ternary operations and provide one-sided cases.

They are specialized for string interpolation, but are certainly not limited to this.

It should be noted that `Conditionals` extensively leverages the <a href="#internal">`Internal`</a> module.

#### `is_even(test_val, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is even, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_equal(original_val, test_val, return_val=Default.PARAMETER, else_val='')`
If the `original_val` and `test_val` are equal, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_false(test_val, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is `false`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_gt: (original_val, test_val, return_val=Default.PARAMETER, else_val='')`
If the `original_val` is greater than the `test_val`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_gte: (original_val, test_val, return_val=Default.PARAMETER, else_val='')`
If the `original_val` is greater than or equal to the `test_val`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_lt: (original_val, test_val, return_val=Default.PARAMETER, else_val='')`
If the `original_val` is less than the `test_val`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_lte: (original_val, test_val, return_val=Default.PARAMETER, else_val='')`
If the `original_val` is less than or equal to the `test_val`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_not_equal(original_val, test_val, return_val=Default.PARAMETER, else_val='')`
If the `original_val` and `test_val` are not equal, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_not_none(test_val, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is not `None`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_not_undefined(test_val, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is not `undefined`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_none(test_val, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is `None`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_odd(test_val: number, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is odd, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_true(test_val, return_val=Default.PARAMETER, else_val='')`
If the `test_val` is `true`, the `return_val` is returned, otherwise it will return `else_val`.
<br/><br/>
#### `is_undefined(test_val, return_val=Default.PARAMETER, else_val='')`
If the `testVal` is `undefined`, the `returnVal` is returned, otherwise it will return `elseVal`.

<hr/>

## Fraction

### Class

#### `Fraction`
Contains all Unicode fraction symbols

| Name           | Value |
|----------------|-------|
| ONE_HALF       | ??     |
| ONE_THIRD      | ???     |
| ONE_QUARTER    | ??     |
| ONE_FIFTH      | ???     |
| ONE_SIXTH      | ???     |
| ONE_SEVENTH    | ???     |
| ONE_EIGHTH     | ???     |
| ONE_NINTH      | ???     |
| ONE_TENTH      | ???    |
| TWO_THIRDS     | ???     |
| TWO_FIFTHS     | ???     |
| THREE_QUARTERS | ??     |
| THREE_FIFTHS   | ???     |
| THREE_EIGHTHS  | ???     |
| FOUR_FIFTHS    | ???     |
| FIVE_SIXTHS    | ???     |
| FIVE_EIGHTHS   | ???     |
| SEVEN_EIGHTHS  | ???     |

<hr/>

## Internal
This module was created for the sole purpose of expanding on Python's default parameter abilities.

As it stands, Python allows for default parameters of specified values, but does not allow you to set them to the value of another parameter.

Combining the class and method below allows us to replicate the following JavaScript code:
```javascript
function func(x, y=x) {
	// If y is not defined, y will default to the value of x
}
```

in Python by doing this:
```python
def func(x, y=Default.PARAMETER):
    y = is_default_parameter(y, x)
	# If y is not defined, y will default to the value of x
```

### Class

#### `Default`
Default is an Enum which contains only a single member value: PARAMETER. (It's value is `None`, but that's irrelevant)

### Method

#### `is_default_parameter(test_val, return_val)`
If the `test_val` is `Default.PARAMETER`, the method returns `return_val`. Otherwise, that means the `test_val` was defined and is therefore returned.

<hr/>

## Math

#### `closest(needle: number, arr: number[]): number`
This method will return the closest value in the array to the needle

Example:
```python
closest(8, [1, 7, 3, 10, 5]) 
# returns 7
```
&nbsp;
#### `parse_fraction_string(fraction: string): number`
This method parses a function written in out in a string and returns the number as a decimal

<hr/>

## Strings

### Methods

#### `replacement_map(alter: str, replacements: dict): str`
This method is used to shrink multiple `replace` calls in a row. By passing in the string, as well as a dictionary of key (string in the original) value (string to replace with) pairs, you will receive back a string with all occurrences of the keys, replaced with their corresponding partner.

It should be noted that the order of keys does matter when keys overlap. (FIFO)

<hr/>

## Time

### Class

#### `Time`

Contains all time constants in milliseconds (Units such as months and up are not included as they are not constant).

| Unit        | Value     |
|-------------|-----------|
| MILLISECOND | 1         |
| SECOND      | 1000      |
| MINUTE      | 60000     |
| HOUR        | 3600000   |
| DAY         | 86400000  |
| WEEK        | 604800000 |

### Methods

All constants have an accompanying method that will simply return that unit in milliseconds multiplied by the argument you pass in.

- #### `days(multiplier: number): number`
- #### `hours(multiplier: number): number`
- #### `milliseconds(multiplier: number): number`
- #### `minutes(multiplier: number): number`
- #### `seconds(multiplier: number): number`
- #### `weeks(multiplier: number): number`

<hr/>

## Symbols

### Method

#### `fraction_to_symbol(originalVal: number | string): string`
This method accepts a fraction (either as a number or a string) and returns the closest value from the list of symbols above

Throws an error if the provided value is less than or equal to  -1, or greater than or equal to 1
