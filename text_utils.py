
def capitalize_string(string):
    if type(string) == str:
        print(string.capitalize())
    else:
        return "Invalid string"

def reverse_string(string):
    if type(string) == str:
        print(string[::-1])
    else:
        return "Invalid string"
