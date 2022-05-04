from User import User
from Course import Course
from Review import Review

#Class inherited from User Class
class Instructor(User):
    # Constructor method
    def __init__(
        self, 
        id_=-1,
        username="",
        password="",
        display_name="",
        job_title="",
        image_100x100="",
        course_id_list=[]
        ):
        self.display_name = display_name
        self.job_title = job_title
        self.image_100x100 = image_100x100
        self.course_id_list = course_id_list
        
        super().__init__(id_, username, password)

    # Function to find and view courses by instructor.
    def view_courses(self,args=[]):
        result = Course().find_course_by_instructor_id(self.id) 
        for course in result[:11]:
            print(course)

    # Function to find and view reviews by instructor
    def view_reviews(self,args=[]):
        courses_teached = Course().find_course_by_instructor_id(self.id) 
        result = []
        for course in courses_teached:
            result += Review().find_review_by_course_id(course.course_id)
        for review in result[:11]:
            print(review)
        print("Total Reviews: ",len(result))
                   
    def __str__(self) -> str:
        parent_attrs = super().__str__()
        return f"{parent_attrs};;;{self.display_name};;;{self.job_title};;;{self.image_100x100};;;123123–323–32–3123–3123"


