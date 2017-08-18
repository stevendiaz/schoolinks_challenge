
db = {
        'texas': {
            'science': [(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            'math': [(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            'english':[(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            'history': [(9,'9AM'), (10,'10AM'), (13, '1PM'), (14,'2PM')],
            'elective': [(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            }
        }


class MasterSchedule:
    
    def __init__(self, school_system):
        # DB is stubbed
        self.science = db.get(school_system).get('science')
        self.math = db.get(school_system).get('math')
        self.english = db.get(school_system).get('english')
        self.history = db.get(school_system).get('history')
        self.elective = db.get(school_system).get('elective')

