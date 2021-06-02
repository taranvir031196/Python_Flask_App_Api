from typing import Literal
from cowin_api.api import CoWinAPI
from flask import Flask
from flask import request
import getStates
import getdistricts


app = Flask(__name__)

@app.route("/")
def WelcomeToCowinAPI():
    return "Welcome to Cowin API";

@app.route("/states")
def getIndianStates():
    return getStates.getAllStates()

@app.route("/districts")
def getIndianDistricts():
    stateid = request.args.get('state_id')
    print(stateid)
    dist_obj = getdistricts.getspecificdistrict(stateid)
    return dist_obj

@app.route("/calendarByDistrict")
def getCenterInDistricts():
        cowin = CoWinAPI()

        districtId:str = request.args.get('district_id')
        print(districtId)
        date: str = request.args.get('date')
        print(date)
     #   min_age_limit = request.args.get('min_age_limt')

        availability = cowin.get_availability_by_district(districtId, date)
        assert isinstance(availability, dict)
        assert isinstance(availability.get('centers'), list)
        return availability
           

@app.route("/calendarByPin")
def getCenterByPinCode():
    # districtPin:str = request.args.get('district')
    # print(type(districtPin), districtPin)
    # date:str = '02-06-2021'
    # min_age_limit:int = 18

    cowin = CoWinAPI()
    pin_code:str = request.args.get('pincode')
    print(pin_code)
    date:str  = request.args.get('date')
    print(date)
    availability = cowin.get_availability_by_pincode(pin_code, date)
    
    assert isinstance(availability, dict)
    assert isinstance(availability.get('centers'), list)
    return availability

if __name__ == "__main__":
    app.run(port=4000)