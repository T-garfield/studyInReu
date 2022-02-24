def username_generator(first_name, last_name):
    username = first_name[0:3] + last_name[0:4]
    return username         
print(username_generator('Matthew', 'McConaughey'))


def password_generator(username):
    username = username_generator('Matthew', 'McConaughey')
    password= username[-1] + username[:-1] 
    return password
print(password_generator(username_generator('Matthew', 'McConaughey')))