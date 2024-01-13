class courseInfo:
    def __init__(self):
        self.roomNumbers = {
            'CSC101': '3004',
            'CSC102': '4501',
            'CSC103': '6755',
            'NET110': '1244',
            'COM241': '1411'
        }
        self.instructors = {
            'CSC101': 'Haynes',
            'CSC102': 'Alvarado',
            'CSC103': 'Rich',
            'NET110': 'Burke',
            'COM241': 'Lee'
        }
        self.meeting_times = {
            'CSC101': '8:00 a.m.',
            'CSC102': '9:00 a.m.',
            'CSC103': '10:00 a.m.',
            'NET110': '11:00 a.m.',
            'COM241': '1:00 p.m.'
        }
    
    def getCourseInfo(self,courseId):
        if courseId in self.roomNumbers and courseId in self.instructors and courseId in self.meeting_times:
            room_no = self.roomNumbers[courseId]
            instructor = self.instructors[courseId]
            meeting_time = self.meeting_times[courseId]

            return{
                'Course': courseId,
                'Room Number':room_no,
                'Instructor' : instructor,
                'Meeting Time' : meeting_time
            }
        else:
            return None

course_information = courseInfo()

result = course_information.getCourseInfo(input("Enter Course Number: "))
if result:
    for k,v in result.items():
        print(f"{k}:{v}")
else:
    print("Please enter a valid Course Number")