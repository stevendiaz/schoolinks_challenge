# This is an in-memory representation of what a noSQL datastore
# would look like for this application
db = {
        'texas': {
			'classes': {
            'science': [(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            'math': [(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            'english':[(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            'history': [(9,'9AM'), (10,'10AM'), (13, '1PM'), (14,'2PM')],
            'elective': [(9,'9AM'), (10,'10AM'), (11, '11AM'), (12,'12PM')],
            },
			'students': []
		}
	}

class MasterSchedule:
    
    def __init__(self, school_system):
        # DB is stubbed
        self.science = db.get(school_system).get('classes').get('science')
        self.math = db.get(school_system).get('classes').get('math')
        self.english = db.get(school_system).get('classes').get('english')
        self.history = db.get(school_system).get('classes').get('history')
        self.elective = db.get(school_system).get('classes').get('elective')

class Student:
	
	def __init__(self, classes, school):
		self.school = school
		self.science = classes.get('science')
		self.math = classes.get('math')
		self.history = classes.get('history')
		self.elective = classes.get('electives')
		self.english = classes.get('english')
		if db.get(school)['students'] == []:
			db.get(school)['students'] = [self]
		else:
			db.get(school)['students'].append(self)

class ClassTimes:

    def __init__(self, args):
        self.science = self._time(args.get('science'))
        self.math = self._time(args.get('math'))
        self.electives = self._time(args.get('electives'))
        self.english = self._time(args.get('english'))
        self.history = self._time(args.get('history'))

    def _time(self, hour):
        hour = int(hour)
        if hour > 12:
            return str(hour % 12) + 'PM'
        else:
            return str(hour) + 'AM'
