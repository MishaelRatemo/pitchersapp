class User:
    
    def __init__(self,email,username,password,pitchees):
        self.email = email
        self.username = username
        self.password=password
        self.pitchees = pitchees


class Piches:
    def __ini__(self,pitch_id,owner,title,description,category,upvotes,downvotes,comments):
        self.pitch_id = pitch_id
        self.owner = owner
        self.title = title
        self.description = description
        self.category = category
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.comments = comments