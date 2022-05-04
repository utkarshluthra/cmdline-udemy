from User import User
 
# Class inherited from User class
class Student(User):

    # Constructor method
    def __init__(
        self, 
        id_=-1,
        username="",
        password="",
        user_title="",
        user_image_50x50="",
        user_initials="",
        review_id=-1
        ):
        self.user_title = user_title
        self.user_image_50x50 = user_image_50x50
        self.user_initials = user_initials
        self.review_id = review_id
        print(review_id)
        super().__init__(id_, username, password)

    # Method to search and view course information
    def view_courses(self,args=[]):
        course_id=None
        with open('data/result/review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        for review in reviews:
            review_data = review.split(";;;")
            __review_id__ = review_data[0]
            if __review_id__==self.review_id:
                course_id = review_data[-1]
                break
        if not course_id: print("no courses found")

        with open('data/review/courses.txt','r',encoding='utf-8') as f:
            courses = f.readlines()

        for course in courses:
            course_data = course.split(";;;")
            __course_id__ = course_data[0]

            if __course_id__==course_id:
                print(course)

    # Method to search and view reviews
    def view_reviews(self,args=[]):
        with open('data/result/review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        for review in reviews:
            review_data = review.split(";;;")
            review_id = review_data[0]
            if review_id==self.review_id:
                review_content = review_data[1]
                print(review_content)
                return
        print("no reviews found")

    def __str__(self) -> str:
        parent_attrs = super().__str__()
        return f"{parent_attrs};;;{self.user_title};;;{self.user_image_50x50};;;{self.user_initials};;;{self.review_id}"