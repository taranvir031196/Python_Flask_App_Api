from cowin_api import CoWinAPI

def getAllStates():
    cowin = CoWinAPI()
    states = cowin.get_states() 
    return states
