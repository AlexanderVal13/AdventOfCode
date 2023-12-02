import re

"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


# Splits a text. Returning strings of lines into an array.
def splitLinesIntoArray(text):
    return re.split("\n", text)


# Finds all string name digits in a line of string and returns the array of found string name digits oneight
def allstringNameDigitsInline(line):
    ar = []
    reversedLine = line[::-1]
    firstInLine = re.findall(
        "(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)", line
    )
    lastInLine = re.findall(
        "(enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|1|2|3|4|5|6|7|8|9)", reversedLine
    )
    if len(firstInLine) == 0 or len(lastInLine) == 0:
        return "zero"
    else:
        ar.append(firstInLine[0])
        ar.append(lastInLine[0][::-1])
        return ar


# Input a string name and returns the digit of that name
def stringNameToDigit(digitStringName):
    digit = 0
    match digitStringName:
        case "one":
            digit = 1
        case "two":
            digit = 2
        case "three":
            digit = 3
        case "four":
            digit = 4
        case "five":
            digit = 5
        case "six":
            digit = 6
        case "seven":
            digit = 7
        case "eight":
            digit = 8
        case "nine":
            digit = 9
        case "1":
            digit = 1
        case "2":
            digit = 2
        case "3":
            digit = 3
        case "4":
            digit = 4
        case "5":
            digit = 5
        case "6":
            digit = 6
        case "7":
            digit = 7
        case "8":
            digit = 8
        case "9":
            digit = 9
        case _:
            digit = 0
    return digit


f = open("input.txt", "r")
text = f.read()
sumOfAll = 0
arrayOflines = splitLinesIntoArray(text)

for line in arrayOflines:
    if len(line) > 0:
        arrayOfDigits = allstringNameDigitsInline(line)
        firstNum = stringNameToDigit(arrayOfDigits[0])
        lastNum = stringNameToDigit(arrayOfDigits[-1])

        numberCreated = str(firstNum) + str(lastNum)
        num = int(numberCreated)
        sumOfAll += num

print(str(sumOfAll))
# answer is
