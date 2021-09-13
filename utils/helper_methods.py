from models.session import Session
from models.center import Center

def response_parser(response):
    sessions = []
    if not response.get('sessions'): return { 'sessions': sessions }

    for s in response.get('sessions'):
        session = Session(
            center_id=s.get('center_id'),
            name=s.get('name'),
            address=s.get('address'),
            state_name=s.get('state_name'),
            district_name=s.get('district_name'),
            block_name=s.get('block_name'),
            pincode=s.get('pincode'),
            from_time=s.get('from_time'),
            to_time=s.get('to_time'),
            lat=s.get('lat'),
            long=s.get('long'),
            fee_type=s.get('fee_type'),
            session_id=s.get('session_id'),
            date=s.get('date'),
            available_capacity=s.get('available_capacity'),
            available_capacity_dose1=s.get('available_capacity_dose1'),
            available_capacity_dose2=s.get('available_capacity_dose2'),
            fee=s.get('fee'),
            min_age_limit=s.get('min_age_limit'),
            allow_all_age=s.get('allow_all_age'),
            vaccine=s.get('vaccine'),
            slots=s.get('slots'),
        )
        sessions.append(session)
    return { 'sessions': sessions, 'error': None }

def calendar_by_district_response_parser(response):
    centers = []
    if not response.get('centers'): return { 'centers': centers }

    for c in response.get('centers'):
        center = Center(
            center_id=c.get('center_id'),
            name=c.get('name'),
            address=c.get('address'),
            state_name=c.get('state_name'),
            district_name=c.get('district_name'),
            block_name=c.get('block_name'),
            pincode=c.get('pincode'),
            from_time=c.get('from_time'),
            to_time=c.get('to_time'),
            lat=c.get('lat'),
            long=c.get('long'),
            fee_type=c.get('fee_type')
        )
        for s in c.get('sessions'):
            session = Session(
                session_id=s.session_id,
                date=s.get('date'),
                available_capacity=s.get('available_capacity'),
                available_capacity_dose1=s.get('available_capacity_dose1'),
                available_capacity_dose2=s.get('available_capacity_dose2'),
                fee=s.get('fee'),
                min_age_limit=s.get('min_age_limit'),
                allow_all_age=s.get('allow_all_age'),
                vaccine=s.get('vaccine'),
                slots=s.get('slots'),
            )


def resolve_find_by_pin_tg_messages(data):
    messages = []
    if data.get('error'):
        return messages

    message_format = "*{0}*\n*Date*: {1}\n*Vaccine*: {2}\n*Dose 1*:   {3}\n*Dose 2*:   {4}\n*Address*:   {5}\n*Pincode*:   {6}\n*Fee*:   {7}\n*Min Age Limit*: {8}"
    for session in data.get('sessions'):
        message = message_format.format(
            session.name, session.date, session.vaccine, session.available_capacity_dose1,
            session.available_capacity_dose2, " ".join(session.address.split()[:3]),
            session.pincode, session.fee, session.min_age_limit
        )
        messages.append(message)

    return messages
