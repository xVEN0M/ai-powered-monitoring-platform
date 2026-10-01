from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from services.device_service import (
    create_device,
    get_all_devices,
    get_device_by_id,
    update_device,
    delete_device,
)

from schemas.device_schema import (
    DeviceCreate,
    DeviceUpdate,
    DeviceResponse,
)

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.post(
    "",
    response_model=DeviceResponse
)
def add_device(
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    return create_device(device, db)


@router.get(
    "",
    response_model=list[DeviceResponse]
)
def list_devices(
    db: Session = Depends(get_db)
):
    return get_all_devices(db)

@router.get(
    "/{device_id}",
    response_model=DeviceResponse
)
def get_device(
    device_id: int,
    db: Session = Depends(get_db),
):
    return get_device_by_id(device_id, db)


@router.put(
    "/{device_id}",
    response_model=DeviceResponse
)
def edit_device(
    device_id: int,
    device: DeviceUpdate,
    db: Session = Depends(get_db),
):
    return update_device(device_id, device, db)


@router.delete("/{device_id}")
def remove_device(
    device_id: int,
    db: Session = Depends(get_db),
):
    return delete_device(device_id, db)