class Review:
    
    # Constructor method
    def __init__(
        self,
        id_=-1,
        content="",
        rating=-1.0,
        course_id=-1
        ) -> None:
        
        self.id = id_
        self.content = content
        self.rating = rating
        self.course_id = course_id

    # Method to search and print review by review ID
    @classmethod
    def find_review_by_id(cls,review_id):
        
        with open('data/result/review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        
        for review in reviews:
            review_data = review.split(";;;")
            __review_id__ = review_data[0]

            if __review_id__==review_id:
                r = Review(*review_data)
                print(r)
                return r
        print("no items found")
        
    # Method to search and print review by Keyword
    @classmethod
    def find_review_by_keywords(cls,keyword):
        if keyword=="": 
            print("keyword cannot be empty") 
            return []
        result = []
        with open('data/result/review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        
        for review in reviews:
            review_data = review.split(";;;")
            review_content = review_data[1]

            if keyword==review_content:
                print(review)
        return

    # Method to search and print review by course ID
    @classmethod
    def find_review_by_course_id(cls,course_id):
        course_id = str(course_id)
        result = []
        with open('data/result/review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        
        for review in reviews:
            review_data = review.split(";;;")
            course_id_check = review_data[-1]

            if course_id_check==course_id:
                print(review)

    # Function to print review
    @classmethod
    def reviews_overview(cls):
        with open('data/result/review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
            l = len(reviews)
            print(l)
            return l

    def __str__(self) -> str:
        return f"{self.id};;;{self.content};;;{self.rating};;;{self.course_id}"