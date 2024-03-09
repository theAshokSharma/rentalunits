from datetime import date
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


# Association Model
class AssociationManagementBase(SQLModel):
    company_name: str = Field(nullable=False)
    short_name: str = Field(nullable=False, index=True)
    contact_name: str = Field(nullable=True)
    contact_phone: str = Field(nullable=True)
    contact_email: str = Field(nullable=True)
    web_url: str = Field(nullable=True)
    web_username: str = Field(nullable=True)
    web_pwd: str = Field(nullable=True)
    notes:  str = Field(nullable=True)


class AssociationManagement(AssociationManagementBase, table=True):
    id: Optional[int] = Field(default=None,
                              primary_key=True,
                              nullable=False)


class AssociationManagementCreate(AssociationManagementBase):
    pass


class AssociationManagementRead(AssociationManagementBase):
    id: int


# Rental Property Model
class RentalPropertyBase(SQLModel):
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


class RentalProperty(RentalPropertyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)


class RentalPropertyCreate(RentalPropertyBase):
    pass


class RentalPropertyRead(RentalPropertyBase):
    id: int


class TenantLease(SQLModel, table=True):
    leaseagreement_id: Optional[int] = Field(default=None,
                                             foreign_key="leaseagreement.id",
                                             primary_key=True)
    tenant_id: Optional[int] = Field(default=None,
                                     foreign_key="tenant.id",
                                     primary_key=True)

class TenantBase(SQLModel):
    first_name: str = Field(index=True)
    middle_name: str = Field(nullable=True)
    last_name: str = Field(nullable=True)
    email: str = Field(nullable=True)
    mobile_phone: str = Field(nullable=True)
    contact_name: str = Field(nullable=True)
    contact_phone: str = Field(nullable=True)
    contact_email: str = Field(nullable=True)



class Tenant(TenantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    lease_agreements: List["LeaseAgreement"] = Relationship(back_populates="tenants",
                                                            link_model=TenantLease)

class TenantCreate(TenantBase):
    pass


class TenantRead(TenantBase):
    id: int


class LeaseAgreementBase(SQLModel):
    lease_title: str = Field(nullable=False, index=True)
    property_id: Optional[int] = Field(default=None, foreign_key="rentalproperty.id")
    from_date: str = Field(nullable=False)
    to_date: str = Field(nullable=False)
    rent_amount: float = Field(default=0.0, nullable=False)
    security_deposit: float = Field(default=0.0, nullable=False)
    management_fee: float = Field(default=0.0, nullable=False)
    pets: str = Field(nullable=True)
    pets_deposit: float = Field(default=0.00, nullable=True)
    signed_document_url: str = Field(nullable=True)
    notes: str = Field(nullable=True)




class LeaseAgreement(LeaseAgreementBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    tenants: List["Tenant"] = Relationship(back_populates="lease_agreements",
                                           link_model=TenantLease)

class LeaseAgreementRead(LeaseAgreementBase):
    id: int


class LeaseAgreementCreate(LeaseAgreementBase):
    pass
