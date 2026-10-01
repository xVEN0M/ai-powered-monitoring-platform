from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    device_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        unique=True,
        nullable=False
    )

    mac_address: Mapped[str] = mapped_column(
        String(17),
        unique=True,
        nullable=False
    )

    device_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    vendor: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="Offline"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )