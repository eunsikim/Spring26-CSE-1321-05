class comment:
    pass

class media_post:
    # Constructor Function
    def __init__(self, media, description, tags=[]):
        # Defining Attributes/Member Attribute/Member Values
        self.media = media
        self.description = description
        self.comments = [] 
        self.like_counter = 1
        self.views = 1
        self.tags = tags

    # Defining Behavior/Member Functions
    def comment(self, comment):
        self.comments.append(comment)
    
    def like(self):
        self.like_counter += 1
    
    def view(self):
        self.views += 1
    
    def share(self):
        print("Sending this post to...")

    def repost(self):
        print("Reposting...")

    def save(self):
        print("Saving...")

    def print_info(self):    
        print(f"Post: {self.description}, Likes: {self.like_counter}, Views: {self.views}")
    
    def print_comments(self):
        for comment in self.comments:
            print(f"- {comment}")

def main():
    posts = []

    while True:
        print("1. Add a new post")
        print("2. Comment")
        print("3. Give like")
        print("4. See Posts")
        print("5. Exit")
        choice = int(input("> "))

        if choice == 1:
            media = input("Enter media: ")
            desc = input("Enter description: ")
            tag = input("Enter tags (comma separated ,): ").split(",")

            media_post_obj = media_post(media, desc, tag)

            posts.append(media_post_obj)
        elif choice == 2:
            pass
        elif choice == 3:
            for i in range(len(posts)):
                print(i, end =" ")
                posts[i].print_info()
            index = int(input("Select a post: "))

            posts[index].like()
        elif choice == 4:
            for post in posts:
                post.print_info()
        elif choice == 5:
            print("Terminating Program")
            break


if __name__=="__main__":
    main()