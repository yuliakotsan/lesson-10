class MyLazyError(Exception):
  def __init__(self, *args):
    self.message = args and args[0]
    
  def __str__(self):
    if self.message:
      return 'My custom error: {0}'.format(self.message)
    else:
      return 'My first Custom Error'


raise MyLazyError('Custom raise')