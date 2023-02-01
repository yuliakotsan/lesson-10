
def is_unique_list(input_string):
  result = None
  input_string = input_string.strip()

  if len(input_string) == 0:
    raise Exception('Invalid entered data. Please try again')

  try:
    numbers = []
    unique = {}
    for n in input_string.split():
      number = int(n)
      numbers.append(number)
      unique[number] = number

    result = len(numbers) == len(unique)
    pass
  
  except TypeError as error:
    print(error)
    pass
  
  except UnboundLocalError as error:
    print(error)
    pass
  
  except Exception as error:
    print(error)
    pass
  
  finally:
    return result


print(is_unique_list(input('Enter list of numbers: ')))
