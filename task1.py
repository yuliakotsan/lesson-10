
def month_number(number):
  month_name="Undefinide"
  try:   
    q = []
    number = int(number)
    x = {
        1: "january", 
        2: "february",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november",
        12: "december"
      }
    
    month_name = x[number]
    q[number]
    return month_name

    pass
  except KeyError as ex:
    print('KeyError', ex)
    pass
  
  except LookupError as ex:
    print('LookupError', ex)
    pass
  
  except Exception as ex:
    print('Exception', ex)
    pass
  finally:
    return month_name
    pass

print(month_number(input('vvedit chyslo ')))