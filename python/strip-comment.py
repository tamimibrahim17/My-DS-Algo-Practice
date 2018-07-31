# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"


def solution(string,markers):
    ssp = string.split('\n')

    def strip_sentence(s):            
        ret = s
        for m in markers:
            if m in s and len(ret) > len(s[:s.find(m)].rstrip()):
                ret = s[:s.find(m)].rstrip()
        return ret
    return '\n'.join([strip_sentence(s) for s in ssp])