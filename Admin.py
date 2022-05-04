from User import User
from Review import Review
from Course import Course
import json 
import glob

#Class inheriting from User class
class Admin(User):
    
    #Constructor function
    def __init__(self, id_=-1, username="", password=""):
        super().__init__(id_, username, password)

    #Function to register a user as admin
    def register_admin(self):
        
        with open('data/result/user_admin.txt','r',encoding='utf-8') as f:
            admins = f.readlines()

        for admin in admins:
            admin_data = admin.split(";;;")
            username = admin_data[1]
            password = admin_data[2]
            if username==self.username and password==self.password:
                print("Admin already exist")
                return 
        
        with open('data/result/user_admin.txt','a',encoding='utf-8') as f:
            f.write(f"{self.id};;;{self.username};;;{self.password}\n")
        
    # Function to extract information of courses
    def extract_course_info(self):
        filename = "data/course_data/raw_data2.txt"
        with open(filename,'r',encoding='utf-8') as f:
            raw_data = f.read()
        course_data = json.loads(raw_data)["unit"]["items"]

        with open('data/result/courses.txt','a',encoding='utf-8') as f:
            
            for course in course_data:
                course_id = course.get("id")
                course_title = course.get("title")
                image_100x100 = course.get("image_100x100")
                headline = course.get("headline").replace("\n"," ")
                num_of_subscribers = course.get("num_subscribers")
                avg_rating = course.get("avg_rating")
                course_content_length = course.get("content_info").replace("total hours","")

                f.writelines(f"{course_id};;;{course_title};;;{image_100x100};;;{headline};;;{num_of_subscribers};;;{avg_rating};;;{course_content_length}\n")
         
    # Function to extract information of reviews
    def extract_review_info(self):
        filenames = glob.glob("data/review_data/*.json")

        for filename in filenames: 
            with open(filename,'r',encoding='utf-8') as f:
                raw_data = f.read()

            review_data = json.loads(raw_data)
            reviews = review_data['results']

            with open('data/result/review.txt','a',encoding='utf-8') as f:
                
                for review in reviews:
                    course_id = review.get('id')
                    review_content = review.get('content').replace("\n"," ")
                    review_rating = review.get('rating')
                    review_id = review.get('user').get('id')

                    f.write(f"{review_id};;;{review_content};;;{review_rating};;;{course_id}\n")
    
    # Function to extract student information      
    def extract_students_info(self):
        filenames = glob.glob("data/review_data/*.json")
        for filename in filenames:
            with open(filename,'r',encoding='utf-8') as f:
                raw_data = f.read()      
            
            review_data = json.loads(raw_data)
            reviews = review_data['results']

            with open('data/result/user_student.txt','a',encoding='utf-8') as f:
                for review in reviews:
                    user_id = review.get('user').get('id')
                    username = review.get('user').get('name').lower().replace(" ","_")
                    user_title = review.get('user').get('title')
                    user_image = review.get('user').get('image_50x50')
                    user_initials = review.get('user').get('initials')
                    review_id = review.get('id')
                    password = self.encryption(f"{user_initials}{user_id}{user_initials}")

                    f.write(f"{user_id};;;{username};;;{password};;;{user_title};;;{user_image};;;{user_initials};;;{review_id}\n")
                 
    # Function to extract instructor informaation 
    def extract_instructor_info(self):
        filename = "data/course_data/raw_data2.txt"
        with open(filename,'r',encoding='utf-8') as f:
            raw_data = f.read()
        course_data = json.loads(raw_data)["unit"]["items"]

        with open('data/result/user_instructor.txt','a',encoding='utf-8') as f:
            
            for course in course_data:
                instrustors = course.get("visible_instructors",[])
                course_id = course.get('id')
                
                for instrustor in instrustors:
                    instrustor_id = instrustor.get("id")
                    username = instrustor.get("display_name","").replace(" ","_")
                    password = self.encryption(str(instrustor_id))
                    display_name = instrustor.get("display_name")
                    job_title = instrustor.get("job_title").replace("\n"," ")
                    image_100x100 = instrustor.get("image_100x100")

                    f.writelines(f"{instrustor_id};;;{username};;;{password};;;{display_name};;;{job_title};;;{image_100x100};;;{course_id}\n")

    # Function to extract all the information together
    def extract_info(self):
        self.extract_course_info()
        self.extract_instructor_info()
        self.extract_review_info()
        self.extract_students_info()

    # Function to remove all existing data from the all files
    def remove_data(self):
        core_data_files = ['data/result/courses.txt','data/result/review.txt','data/result/user_student.txt','data/result/user_instructor.txt']
        for core_file in core_data_files:
            with open(core_file,'w',encoding='utf-8') as f:
                f.write("")
        
    #Function to view courses according to args
    def view_courses(self,args=[]):
        if len(args)==0:
            print(Course.courses_overview())
        elif len(args)==2:
            command = args[0]
            value = args[1]
            course_driver = Course()

            if command=='TITLE_KEYWORD':
                course_driver.find_course_by_title_keyword(value)
            elif command=='ID':
                course_driver.find_course_by_id(value)
            elif command=='INSTRUCTOR_ID':
                course_driver.find_course_by_instructor_id(value)
            else:
                print("invalid command")
            
        else:
            print("invalid no if args passed")

    # Function to view user informations
    def view_users(self):

        admins = sum(1 for line in open('data/result/user_admin.txt','r',encoding='utf-8'))
        instructors = sum(1 for line in open('data/result/user_instructor.txt','r',encoding='utf-8'))
        students = sum(1 for line in open('data/result/user_student.txt','r',encoding='utf-8'))

        print(f"admins:{admins}, instructors:{instructors}, students:{students}")

    # Function to view reviews and information regarding reviews
    def view_reviews(self,args=[]):
        if len(args)==0:
            print(Review.reviews_overview())
        elif len(args)==2:
            command = args[0]
            value = args[1]
            review_driver = Review()

            if command=='KEYWORD':
                review_driver.find_review_by_keywords(value)
            elif command=='ID':
                review_driver.find_review_by_id(value)
            elif command=='COURSE_ID':
                review_driver.find_review_by_course_id(value)
            else:
                print("invalid command")
            
        else:
            print("invalid no if args passed")

    # Decorator function.
    def __str__(self) -> str:
        return super().__str__()
        

