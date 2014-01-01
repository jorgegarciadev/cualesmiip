import os

def loadVariable(variable1, variable2):
    try:
        return os.environ[variable1]
    except:
        return variable2
        

CSRF_ENABLED = True
SECRET_KEY = loadVariable("CSFR_KEY", "tonto-el-que-lo-lea")
