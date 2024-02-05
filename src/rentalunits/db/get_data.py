
import json
import pathlib
from typing import List
from sqlmodel import Session, select

from rentalunits.db.database import engine
from rentalunits.db.models import RentalProperty
from rentalunits.db.models import AssociationManagement
from rentalunits.db.database import create_db_and_tables

from rentalunits.db.models import RentalProperty

RENTAL_DATA_FILE = pathlib.Path(__file__).parent.parent.parent.parent / "data/rentalproperty.json"
MGMT_DATA_FILE = pathlib.Path(__file__).parent.parent.parent.parent / "data/association_mgmt.json"


def get_renatlproperty_data() -> List:
    with open(RENTAL_DATA_FILE, 'r') as f:
        data = json.load(f)
        rental_data = data["rental_data"]
        rental: List[RentalProperty] = [RentalProperty(**item) for item in rental_data]
        for item in rental:
            print(item.id,
                  item.property_shortname,
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

    with Session(engine) as session:
        for item in rental:
            statement = select(RentalProperty).\
                where(RentalProperty.property_shortname == item.property_shortname)
            results = session.exec(statement)
            rec = results.one_or_none()
            if rec is None:
                session.add(item)
        session.commit()


def get_mgmt_data() -> List:
    with open(MGMT_DATA_FILE, 'r') as f:
        data = json.load(f)
        mgmt_data = data["association_mgmt_data"]
        mgmt: List[AssociationManagement] = [AssociationManagement(**item) for item in mgmt_data]
        for item in mgmt:
            print(item.id,
                  item.company_name)
        return mgmt


def add_mgmt_data():

    data = get_mgmt_data()

    with Session(engine) as session:
        for item in data:
            statement = select(AssociationManagement).\
                where(AssociationManagement.company_name == item.company_name)
            results = session.exec(statement)
            rec = results.one_or_none()
            if rec is None:
                session.add(item)
        session.commit()


if __name__ == "__main__":
    create_db_and_tables()
    add_mgmt_data()
    add_rentalproperty()
