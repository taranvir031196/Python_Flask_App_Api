from cowin_api import CoWinAPI

def getspecificdistrict(state_id:str):
    cowin = CoWinAPI()
    districts = cowin.get_districts(state_id)
    return districts