
def remove_invisible_tags_naive(string):
    new_string = ""
    for char in string:
        c_ord = ord(char)
        if ((c_ord < 0xE0000) or (c_ord > 0xE007F)):
            new_string += char
    return new_string


def is_invisible_tag(char):
    c_ord = ord(char)
    return ((c_ord >= 0xE0000) and (c_ord <= 0xE007F))

def remove_invisible_tags(string):
    new_string = ""
    in_flag = False
    flag_chars = []
    for char in string:
        c_ord = ord(char)
        if in_flag:
            flag_chars.append(char)
            if in_flag and c_ord == 0xE007F:
                new_string += "".join(flag_chars)
                in_flag = False
                flag_chars = []
            elif len(flag_chars) > 10:
                in_flag = False
                flag_chars = []
        elif c_ord == 0x1F3F4:
            in_flag = True
            flag_chars = [char]
        elif not is_invisible_tag(char):
            new_string += char
    return new_string


def run(string):
    print("Original string: " + string)
    print("Length: " + str(len(string)))
    new_string = remove_invisible_tags(string)
    print("New string: " + new_string)
    print("Length: " + str(len(new_string)))
    print("")

string = "hello world!"
invisible_string = "󠁔󠁨󠁥󠁳󠁥󠀠󠁣󠁨󠁡󠁲󠁡󠁣󠁴󠁥󠁲󠁳󠀠󠁳󠁨󠁯󠁵󠁬󠁤󠀠󠁮󠁯󠁴󠀠󠁢󠁥󠀠󠁶󠁩󠁳󠁩󠁢󠁬󠁥󠀠󠁢󠁵󠁴these characters should be visible󠁡󠁮󠁤󠀠󠁴󠁨󠁥󠁳󠁥󠀠󠁣󠁨󠁡󠁲󠁡󠁣󠁴󠁥󠁲󠁳󠀠󠁳󠁨󠁯󠁵󠁬󠁤󠀠󠁮󠁯󠁴"
flag = "🏴󠁧󠁢󠁥󠁮󠁧󠁿"
false_flag = "".join([chr(c) for c in [0x1F3F4, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE0061, 0xE007F]])

run(string)
run(invisible_string)
run(flag)
run(false_flag)

