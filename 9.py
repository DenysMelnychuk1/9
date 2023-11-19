name_phone_dict = {}

class NameAlreadySavedError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'Contact not found'
        except ValueError:
            return 'Command not real'
        except IndexError:
            return 'Please enter name and phone'
        except NameAlreadySavedError:
            return 'Name already saved'
        except Exception as e:
            return f'Error: {str(e)}'
    return inner

def write_to_file():
    with open('C:/Users/User/Desktop/9/phone.txt', 'w') as file:
        for key, value in name_phone_dict.items():
            file.write(f'{key} {value}\n')

def read_file():
    try:
        with open('C:/Users/User/Desktop/9/phone.txt', 'r') as file:
            for line in file.readlines():
                values = line.split(' ')
                name = values[0]
                phone = values[1].replace('\n', '')
                name_phone_dict.update({name: phone})
    except FileNotFoundError:
        print("File not found. Creating a new one.")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

@input_error
def handle_add(name, phone):
    if name.title() in name_phone_dict:
        raise NameAlreadySavedError
    name_phone_dict[name.title()] = phone
    return 'Name saved successfully'

@input_error
def handle_change(name, phone):
    if name.title() in name_phone_dict:
        name_phone_dict[name.title()] = phone
        return 'Contact updated'
    else:
        raise KeyError

@input_error
def handle_phone(name):
    if name.title() in name_phone_dict:
        return f'Number: {name_phone_dict[name.title()]}'
    else:
        raise KeyError

@input_error
def handle_show_all():
    result = ''
    for key, value in name_phone_dict.items():
        result += f'For name {key} phone is: {value}\n'
    if result == '':
        return None
    return result

def parser(user_input):
    commands = user_input.split(' ')
    if commands[0] == 'add':
        return handle_add(commands[1], commands[2])
    elif commands[0] == 'change':
        return handle_change(commands[1], commands[2])
    elif commands[0] == 'phone':
        return handle_phone(commands[1])
    elif user_input.startswith('show all'):
        return handle_show_all()

def main():
    read_file()
    while True:
        user_input = input("Enter command >>> ")
        if user_input == 'exit':
            print("Bye")
            break
        result = parser(user_input)
        if result is not None:
            print(result)
    write_to_file()

if __name__ == '__main__':
    main()
