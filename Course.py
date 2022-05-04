class Course:
    
    # Constructor Method
    def __init__(
        self,
        course_id=-1,
        course_title="",
        course_image_100x100="",
        course_headline="",
        course_num_subscribers=-1,
        course_avg_rating=-1.0,
        course_content_length=-1        
        ) -> None:

        self.course_id = course_id 
        self.course_title = course_title 
        self.course_image_100x100 = course_image_100x100
        self.course_headline = course_headline
        self.course_num_subscribers = course_num_subscribers
        self.course_avg_rating = course_avg_rating
        self.course_content_length = course_content_length

    # Method to search and view course information by title keyword
    @classmethod
    def find_course_by_title_keyword(cls,keyword):
        result = []
        with open('data/result/courses.txt','r',encoding='utf-8') as f:
            courses = f.readlines()

        for course in courses:
            course_data = course.split(";;;")
            course_title = course_data[1].lower()
            if keyword in course_title:
                print(course)
    # Method to search and view course information by Course ID
    @classmethod
    def find_course_by_id(cls,course_id):

        course_id = str(course_id)
        with open('data/result/courses.txt','r',encoding='utf-8') as f:
            courses = f.readlines()
        
        for course in courses:
            course_data = course.split(";;;")
            __course_id__ = course_data[0]
            if course_id == __course_id__:
                cs = Course(*course_data)
                print(cs)
                return cs
        print("no items found")

    # Method to search and view course information by instructor ID         
    @classmethod
    def find_course_by_instructor_id(cls,instructor_id):
        course_ids = []
        result = []
        instructor_id = str(instructor_id)
        with open('data/result/user_instructor.txt','r',encoding='utf-8') as f:
            instructors = f.readlines()
        
        for instructor in instructors:
            instructor_data = instructor.split(";;;")
            __instructor_id__ = instructor_data[0]
            if __instructor_id__==instructor_id:
                course_ids = instructor_data[-1].split("-")
        if len(course_ids)==0: return result
        
        with open('data/result/courses.txt','r') as f:
            courses = f.readlines()

        for course in courses:
            course_data = course.split(";;;")
            course_id = course_data[0]
            if course_id in course_ids:
                result.append(Course(*course_data))

        print(result)
        return result

    # Method to view the overview of the course
    @classmethod
    def courses_overview(cls):
        with open('data/result/courses.txt','r',encoding='utf-8') as f:
            courses = f.readlines()
            print(courses)
            return len(courses)      

    def __str__(self):
        return f"{self.course_id};;;{self.course_title};;;{self.course_image_100x100};;;{self.course_headline};;;{self.course_num_subscribers};;;{self.course_avg_rating};;;{self.course_content_length}"
