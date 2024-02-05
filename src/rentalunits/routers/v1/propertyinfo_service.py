from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select
from typing import List

from rentalunits import log, config
from rentalunits.db.database import get_session, engine
from rentalunits.db.models import RentalProperty

router = APIRouter(
    prefix="/v1/rentalunit",
    tags=["RentalPropertyService"],
    responses={404: {"Property Information": "Not Found"}},
)


@router.get("/list",
            response_model=List[RentalProperty],
            status_code=status.HTTP_200_OK)
def get_rental_property_list(*,
                             session: Session = Depends(get_session)):
    stmt = select(RentalProperty)
    rental_properties = session.exec(stmt).all()
    # rental_properties = getAllRentalProperty()
    return rental_properties


@router.get("/{shortname}",
            description="get rental unit by using rental shortname",
            response_model=RentalProperty,
            status_code=status.HTTP_200_OK)
def get_rental_unit_by_shortname(*,
                                 session: Session = Depends(get_session),
                                 shortname: str):
    stmt = select(RentalProperty).\
           where(RentalProperty.property_shortname == shortname)
    result = session.exec(stmt)
    rec = result.one_or_none()
    if rec is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Shortname {shortname} not found")
    return rec


def getAllRentalProperty() -> List[RentalProperty]:
    with Session(engine) as session:
        stmt = select(RentalProperty)
        rental_properties = session.exec(stmt).all()
    return rental_properties


def main():
    rentals = getAllRentalProperty()
    for data in rentals:
        print(data.property_shortname)


if __name__ == "__main__":
    main()
