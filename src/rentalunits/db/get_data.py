
import json
import pathlib
from typing import List
from sqlmodel import Session, select

from rentalunits.db.database import engine
from rentalunits.db.models import RentalProperty
from rentalunits.db.database import create_db_and_tables

from rentalunits.db.models import RentalProperty

DATA_FILE =  pathlib.Path(__file__).parent.parent.parent.parent / "data/rentalproperty.json"

def get_renatlproperty_data() -> List:
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        rental_data = data["rental_data"]
        rental: List[RentalProperty] = [RentalProperty(**item) for item in rental_data]
        for item in rental:
            print(item.property_shortname,
                  item.address_line1,
                  item.city,
                  item.state,
                  item.zipcode,
                  item.county,
                  item.property_id,
                  item.purchase_date,
                  item.purchase_amount)
        return rental

def add_rentalproperty():

    rental = get_renatlproperty_data()
    

    # with Session(engine) as session:
    #     for item in rental:
    #         session.add(item)
    #     session.commit()

if __name__ == "__main__":
#    create_db_and_tables()
    add_rentalproperty()
