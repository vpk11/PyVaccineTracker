from dataclasses import dataclass
from models.session import Session
from typing import List

@dataclass
class Center():
    """A class holding ceter details"""

    center_id: int
    name: str
    address: str
    state_name: str
    district_name: str
    block_name: str
    pincode: int
    from_time: str
    to_time: str
    lat: int
    long: int
    fee_type: str
    sessions: List[Session]
