#try:
 #  int('346ap')
#except ValueError as ex:
 #   print(f'error:{ex}')       


try:
    raise ValueError('value error raised')
    l=[5,4,6]
    print(l[2])
    print('this will not print')
#except ValueError as ex:
#    print(f'error:{ex}')
#except IndexError as ex:
#    print(f'error:{ex}') 
    
except ValueError as ex:
    print(f'error:{ex}')
finally:
    print('always')