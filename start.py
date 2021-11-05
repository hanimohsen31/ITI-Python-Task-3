import Functions

enter = input('Choose Register or Login (r/l)')
if enter == 'r':
    Functions.register()

elif enter == 'l':
    Functions.login()

else:
    print('Not A valid Choice')
    exit()
