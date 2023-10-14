#!/usr/bin/python3
"""A module that print text indentation"""


def text_indentation(text):
    """A function that print text indentation"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chr_list = [".", "?", ":"]
    space_post_chr = False

    for i in text:
        if i == " " and space_post_chr is True:
            continue
        space_post_chr = False
        print(i, end="")
        if i in chr_list:
            space_post_chr = True
            print("")
            print("")
