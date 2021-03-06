#!/usr/bin/env python3
# HW07_ch10_ex02

# Instructions:
# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################################
# Imports


# Body
def capitalize_nested(lst):
    capitalized_lst = []
    for item in lst:
        if isinstance(item, list):
            capitalized_lst.append(capitalize_nested(item))
        else:
            capitalized_lst.append(item.capitalize())
    return capitalized_lst


##############################################################################
def main():
    list_1 = ['apple', ['bear'], 'cat', 'doggy', ['elbow', 'fin', 'garage']]
    list_2 = [[[['apple']], 'bear', 'cat', 'doggy',
              ['elbow', 'fin', 'garage', 'house', 'indigo']], 'jump']
    list_3 = []
    list_4 = ["doggy"]
    list_5 = [[[[[[["this"]]]]]]]
    print(capitalize_nested(list_1))
    print(capitalize_nested(list_2))
    print(capitalize_nested(list_3))
    print(capitalize_nested(list_4))
    print(capitalize_nested(list_5))
if __name__ == "__main__":
    main()
