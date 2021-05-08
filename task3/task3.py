import unittest

"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def parentheses_validator(input):
    answer = 0
    try:
        for character in input:
            if character == '(':
                answer += 1
            elif character == ')':
                answer -= 1
            else:
                print("Entered string contains not available symbols")
            if answer < 0:
                return answer >= 0
    except:
        print ("Oops, some error occured...")
    else:
        return answer == 0
        
parentheses_validator("()")


class Test(unittest.TestCase):
    def test_positive_parentheses_validator(self):
        assert parentheses_validator("()")
        assert not parentheses_validator(")(()))")
        assert parentheses_validator("(") is False
        assert parentheses_validator("(())((()())())")


if __name__ == '__main__':
    unittest.main()
