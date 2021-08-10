
import re #the Regular expression operations
#https://docs.python.org/3/library/re.html

def validate_brackets(input):
    conditin=False
    if input.count('{')==input.count('}') and input.count('(')==input.count(')') and input.count('[')==input.count(']'):
        conditin=True
    try :
       if re.findall("\(.?}", input) or re.findall("\[.?}", input) or re.findall("\[.?)", input) or re.findall("\(.?]", input) or re.findall("\{.?)", input) or re.findall("\{.?]", input):
            conditin=False
    except:
        return conditin

    return conditin

print(validate_brackets('{}'))
print(validate_brackets('{}(){}'))
print(validate_brackets('()[[Extra Characters]]'))
print(validate_brackets('(){}[[]]'))
print(validate_brackets('{}{Code}[Fellows](())'))
print(validate_brackets('[({}]'))
print(validate_brackets('(]('))
print(validate_brackets('{(})'))

