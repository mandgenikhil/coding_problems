
def load_dict_data():
    ascii_to_integers = {}
    counter = 0
    for i in range(48,58):
        ascii_to_integers[i] = counter
        counter = counter + 1
    return ascii_to_integers

ascii_to_integers = load_dict_data()

def check_valid_integer(value):
    try:
        if value in ascii_to_integers.keys():
            return True
        else:
            return False                
    except:
        return False

def str_to_int_formula(value,string_value):
    ord_value = (ord(string_value) - 48)
    value = value * 10
    value  = value + ord_value    
    return value
    

def string_to_number(s):
    number_data = 0      
    for i in s:    
        if check_valid_integer(ord(i)):    
            number_data = str_to_int_formula(number_data,i)
        else:
            return number_data
    return number_data


print('Please put your input string here')
input_data = input()
result = string_to_number(input_data)
print(result)
  

    
