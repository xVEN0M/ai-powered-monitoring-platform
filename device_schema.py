from datetime import datetime
from ipaddress import ip_address
from pydantic import BaseModel, field_validator
class DeviceBase(BaseModel):
    device_name: str
    ip_address: str
    mac_address: str
    device_type: str
    vendor: str
    location: str

    @field_validator("ip_address")
    @classmethod
    def validate_ip(cls, value: str) -> str:
        ip_address(value)
        return value

    @field_validator("mac_address")
    @classmethod
    def validate_mac(cls, value: str) -> str:
        parts = value.split(":")

        if len(parts) != 6:
            raise ValueError(
                "MAC address must contain 6 octets."
            )

        for part in parts:
            if len(part) != 2:
                raise ValueError(
                    "Each MAC octet must contain exactly 2 characters."
                )

            int(part, 16)

        return value.upper()


class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(DeviceBase):
    status: str

class DeviceResponse(DeviceBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True