class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []
        
    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    
    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post
    

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
            

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
            

    def find_posts_by_author(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)

        return found_posts    



forum = Forum()
foo1 = forum.register_user('alex', 'leito1101@gmail.com')
foo2 = forum.register_user('asdfasd', 'leitoxxx16@gmail.com')
print(forum.users)

forum.create_post("My first post", "Post content", foo1)

print(forum.posts)
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)


print(forum.find_user_by_username('dsf'))
print(forum.find_user_by_username('asdfasd'))
print(forum.find_user_by_email('dasf'))
print(forum.find_user_by_email('leito1101@gmail.com'))
        

forum.create_post("Prostate", "some advices", 'leito')
forum.create_post("Foo", "some advices", 'leito')

found_posts = forum.find_posts_by_author('leito')

print([post.title for post in found_posts])


user_email = 'leito1101@gmail.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"User with email {user_email} doesn't exist")


# forum.find_posts_by_author()