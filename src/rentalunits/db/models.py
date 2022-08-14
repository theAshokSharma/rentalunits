from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel


class RentalProperty(SQLModel, table=True):
    # Optional because if we use this field as auto id increment
    # the value would be None before it gets to the database
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    property_shortname: str = Field(index=True)
    address_line1: str = Field(nullable=False)
    address_line2: str = Field()
    city: str = Field(nullable=False)
    state: str = Field(nullable=False)
    zipcode: str = Field(nullable=False)
    county: str = Field(nullable=False)
    property_id: str = Field()
    purchase_date: str = Field(nullable=False)
    purchase_amount: float = Field(nullable=False)


class Association(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    association_name: str = Field(index=True)
    association_address: str = Field()
    contact_name: str = Field()
    contact_phone: str = Field()
    contact_email: str = Field()
    association_weburl: str = Field()

