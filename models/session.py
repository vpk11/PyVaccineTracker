from dataclasses import dataclass

@dataclass
class Session():
    """A class holding session content"""

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
    session_id: str
    date: str
    available_capacity: int
    available_capacity_dose1: int
    available_capacity_dose2: int
    fee: str
    min_age_limit: int
    allow_all_age: bool
    vaccine: str
    slots: list
