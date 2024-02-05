from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel


class AssociationManagement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    company_name: str = Field(nullable=False)
    short_name: str = Field(nullable=False, Index=True)
    contact_name: str = Field(nullable=True)
    contact_phone: str = Field(nullable=True)
    contact_email: str = Field(nullable=True)
    web_url: str = Field(nullable=True)
    web_username: str = Field(nullable=True)
    web_pwd: str = Field(nullable=True)
    notes:  str = Field(nullable=True)


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
    tax_amount: float = Field(default=0.0, nullable=True)
    association_name: str = Field(nullable=True)
    association_fee: float = Field(default=0.0, nullable=True)
    association_url: str = Field(nullable=True)
    association_username: str = Field(nullable=True)
    association_pwd: str = Field(nullable=True)
    lock_master_key: str = Field(nullable=True)
    garage_key_code: str = Field(nullable=True)
    mail_box_number: str = Field(nullable=True)
    property_info: str = Field(nullable=True)
    notes: str = Field(nullable=True)
    association_mgmt_id: Optional[int] = Field(default=None,
                                               foreign_key="associationmanagement.id")


class Tenant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    first_name: str = Field(index=True)
    last_name: str = Field(nullable=True)
    email: str = Field(nullable=True)
    mobile_phone: str = Field(nullable=True)
    contact_name: str = Field(nullable=True)
    contact_phone: str = Field(nullable=True)
    contact_email: str = Field(nullable=True)


class LeaseAgreement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    lease_id: str = Field(nullable=False, index=True)
    property_id: Optional[int] = Field(default=None, foreign_key="rentalproperty.id")
    tenant_id1: Optional[int] = Field(default=None, foreign_key="tenant.id")
    tenant_id2: Optional[int] = Field(default=None, foreign_key="tenant.id")
    from_date: str = Field(nullable=False)
    to_date: str = Field(nullable=False)
    rent_amount: float = Field(default=0.0, nullable=False)
    security_deposit: float = Field(default=0.0, nullable=False)
    management_fee: float = Field(default=0.0, nullable=False)
    pets: str = Field(nullable=True)
    pets_deposit: float = Field(default=0.00, nullable=True)
    signed_document_url: str = Field(nullable=True)
    notes: str = Field(nullable=True)
