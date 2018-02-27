import os, random, string

def loadVariable(variable1, variable2):
    try:
        return os.environ[variable1]
    except:
        return variable2

def generateCSFRKEY(lenght):
  key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(lenght)])
  return key

CSRF_ENABLED = True
SECRET_KEY = loadVariable("CSFR_KEY", generateCSFRKEY(32))
