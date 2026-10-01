from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.device import Device
from schemas.device_schema import DeviceCreate


def create_device(device: DeviceCreate, db: Session):
    existing_ip = (
        db.query(Device)
        .filter(Device.ip_address == device.ip_address)
        .first()
    )

    if existing_ip:
        raise HTTPException(
            status_code=400,
            detail="IP address already exists."
        )

    existing_mac = (
        db.query(Device)
        .filter(Device.mac_address == device.mac_address)
        .first()
    )

    if existing_mac:
        raise HTTPException(
            status_code=400,
            detail="MAC address already exists."
        )

    new_device = Device(
        device_name=device.device_name,
        ip_address=device.ip_address,
        mac_address=device.mac_address,
        device_type=device.device_type,
        vendor=device.vendor,
        location=device.location,
    )

    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return new_device


def get_all_devices(db: Session):
    return db.query(Device).all()
from schemas.device_schema import DeviceUpdate


def get_device_by_id(device_id: int, db: Session):
    device = db.query(Device).filter(Device.id == device_id).first()

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found."
        )

    return device


def update_device(
    device_id: int,
    updated_device: DeviceUpdate,
    db: Session,
):
    device = get_device_by_id(device_id, db)

    device.device_name = updated_device.device_name
    device.ip_address = updated_device.ip_address
    device.mac_address = updated_device.mac_address
    device.device_type = updated_device.device_type
    device.vendor = updated_device.vendor
    device.location = updated_device.location
    device.status = updated_device.status

    db.commit()
    db.refresh(device)

    return device


def delete_device(device_id: int, db: Session):
    device = get_device_by_id(device_id, db)

    db.delete(device)
    db.commit()

    return {
        "message": "Device deleted successfully."
    }