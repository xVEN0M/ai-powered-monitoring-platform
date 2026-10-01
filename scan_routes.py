from fastapi import APIRouter

from network.scanner import scan_network

router = APIRouter(
    prefix="/scan",
    tags=["Network Scanner"]
)


@router.get("")
def scan():
    """
    Scan the local network.
    """

    devices = scan_network("192.168.1.0/24")

    return {
        "devices": devices
    }
    