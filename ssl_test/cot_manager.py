import random
import uuid
from datetime import datetime as dt
import datetime
import xml.etree.ElementTree as ET

DEVICES = ["GOOGLE PIXEL 6", "GOOGLE PIXEL 5", "GOOGLE PIXEL 4", "SAMSUNG S8", "SAMSUNG S7", "SAMSUNG S6"]

TEAMS = ["red", "yellow", "cyan"]

ROLES = ["Team Leader", "Team Member", "Sniper"]

class CoTManager:

    def __init__(self, callsign, uid, timeout=10):
        self.callsign = str(callsign)
        self.uid = str(uid)
        self.timeout = int(timeout)

    def get_fmt_time(self, delta=None):
        if delta == None:
            delta = self.timeout

        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        now = dt.utcnow()
        zulu = now.strftime(DATETIME_FMT)
        td = datetime.timedelta(seconds=delta)
        stale_part = dt.strptime(zulu, DATETIME_FMT) + td
        return stale_part.strftime(DATETIME_FMT)

    def get_con_message(self):
        event = ET.Element("event", {
            'version': "2.0",
            'type': "a-f-G-U-C",
            'uid': str(uuid.uuid4()),
            'how': "m-g",
            'time': self.get_fmt_time(),
            'start': self.get_fmt_time(),
            'stale': self.get_fmt_time(100),
        })

        ET.SubElement(event, "point", {
            'lat': str(random.randint(-89, 89)),
            'lon': str(random.randint(-179, 179)),
            'hae': "9999999.0",
            'ce': "9999999.0",
            'le': "9999999.0",
        })

        detail = ET.SubElement(event, "detail", {})

        ET.SubElement(detail, "__group", {
            "name": random.choice(TEAMS),
            "role": random.choice(ROLES)
        })

        ET.SubElement(detail, "status", {
            'battery': str(random.randint(1, 100))
        })

        ET.SubElement(detail, "takv", {
            'version': f'{random.randint(1,4)}.{random.randint(0,9)}.{random.randint(0,9)}.{random.randint(0,9)} (79017e13)[playstore].1675714487-CIV',
            'platform': 'ATAK-CIV',
            'device': random.choice(DEVICES),
            'os': str(random.randint(1,33))
        })

        ET.SubElement(detail, "track", {
            'course': str(random.randint(1,359)),
            'speed': str(random.randint(0, 100))
        })

        ET.SubElement(detail, "contact",{
            'callsign': self.callsign,
            'endpoint': '*:-1:stcp',
        })

        ET.SubElement(detail, "uid", {
            'Droid': self.callsign
        })

        ET.SubElement(detail, "precisionlocation", {
            'altsrc': "???"
        })
        return event

    def get_message(self, message_name = str(uuid.uuid1())):
        event = ET.Element("event", {
            'version': "2.0",
            'type': "a-u-G",
            'uid': str(uuid.uuid4()),
            'how': "m-g",
            'time': self.get_fmt_time(),
            'start': self.get_fmt_time(),
            'stale': self.get_fmt_time(),
        })

        ET.SubElement(event, "point", {
            'lat': str(random.randint(-89, 89)),
            'lon': str(random.randint(-179, 179)),
            'hae': "9999999.0",
            'ce': "9999999.0",
            'le': "9999999.0",
        })
        
        detail = ET.SubElement(event, "detail", {})

        ET.SubElement(detail, "status", {
            'readiness': "true"
        })

        ET.SubElement(detail, "archive")

        ET.SubElement(detail, "link", {
            'uid': str(self.callsign),
            'production_time': self.get_fmt_time(),
            'type': "a-f-G-U-C",
            'parent_callsign': self.uid,
            'relation': "p-p",
        })

        ET.SubElement(detail, "contact", {
            'callsign': str(self.callsign)
        })
        
        ET.SubElement(detail, "remarks")

        ET.SubElement(detail, "color", {
            'argb': "-1"
        })

        ET.SubElement(detail, "precisionlocation", {
            'altsrc': "???"
        })

        ET.SubElement(detail, "usericon", {
            'iconsetpath': "COT_MAPPING_2525B/a-u/a-u-G"
        })

        return event