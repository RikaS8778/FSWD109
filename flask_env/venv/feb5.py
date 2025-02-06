from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def showHomePage():
    return render_template('homePage.html')

@app.route('/test', methods=['GET'])
def showTestPage():
    # name = request.args.get('name')
    # if name == None:
    #     name = "Guest"
    user = {"name": 'Alice', "age": 25, "is_authenticated": True}
    products = ['Laptop', 'Phone', 'Tablet', 'Watch']
    return render_template('homePage.html', user = user, items = products)


# Assignment 5 - Feb5.py
#Write routes and view functions to render templates with jinja2. Submit by copy/pasting your main.py file

#mock-database -- start--
posts = [
    {'id': 0, "title": 'Think Python', "user_name": 'Allen B. Downey', "date": '2024/12/27', "content": 'this is a content of Think Python'},
    {'id': 1, "title": 'Python Crash Course', "user_name": 'Eric Matthes', "date": '2023/11/11', "content": 'this is a content of Python Crash Course'},
    {'id': 2, "title": "Automate the Boring Stuff with Python", "user_name": 'Al Sw artz', "date": '2025/1/12', "content": 'this is a content of Automate the Boring Stuff with Python'},
    {'id': 5, "title": "Flamework of python", "user_name": 'Mark Charleton ', "date": '2025/1/12', "content": 'this is a content of Flamework of python'},
    {'id': 6, "title": "Jinja2 v.s Django", "user_name": 'Lee Chang Woo', "date": '2025/2/3', "content": 'this is a content of Jinja2 v.s Django'}
]

comments = [
    {'id': 0, "content": 'This is a comment of Think Python', "post_id": 0, "user_name": 'Alice'},
    {'id': 1, "content": 'This is a comment of Python Crash Course', "post_id": 1, "user_name": 'Bob'},
    {'id': 2, "content": 'This is a comment of Automate the B oring Stuff with Python', "post_id": 2, "user_name": 'Charlie'},
    {'id': 3, "content": 'This is a comment of Flamework of python', "post_id": 5, "user_name": 'David'},
    {'id': 4, "content": 'This is a comment of Flamework of python ', "post_id": 5, "user_name": 'Eve'},
    {'id': 5, "content": 'This is a comment of Think Python ', "post_id": 0, "user_name": 'Frank'},
    {'id': 6, "content": 'This is a comment of Python Crash Course ', "post_id": 1, "user_name": 'George'},
    {'id': 7, "content": 'This is a comment of Automate the B oring Stuff with Python ', "post_id": 2, "user_name": 'Helen'},
    {'id': 8, "content": 'This is a comment of Flamework of python ', "post_id": 5, "user_name": 'Ivy'},
    {'id': 9, "content": 'This is a comment of Think Python', "post_id": 0, "user_name": 'Jack'},
    {'id': 10, "content": 'This is a comment of Python Crash Course', "post_id": 1, "user_name": 'Kate'}
]

#mock-database -- end--
    

# GET posts/
@app.route('/posts')
def showPosts():
    return render_template('posts.html', posts = posts, comments=[], commentsCount = None)

#GET posts/pid
@app.route('/posts/<pid>')
def getPost(pid):
    for post in posts:
        if post['id'] == int(pid):
            return render_template('posts.html', posts = [post], comments=[], commentsCount = None)
    
    return render_template('posts.html', posts = [])

#GET posts/pid/comments
@app.route('/posts/<pid>/comments')
def getSpicificPostAndComments(pid):
    relateComments = []
    for post in posts:
        if post['id'] == int(pid):
            for comment in comments:
                if comment['post_id'] == int(pid):
                    relateComments.append(comment)
            commentsCount = len(relateComments)
            return render_template('posts.html', posts = [post], comments = relateComments, commentsCount = commentsCount)
    
    return render_template('posts.html', posts = [])


#GET posts/pid/comments/cid
@app.route('/posts/<pid>/comments/<cid>')
def getSpecificPostAndSpecoficComment(pid, cid):
    relateComment = []
    for post in posts:
        if post['id'] == int(pid):
            for comment in comments:
                if comment['post_id'] == int(pid) and comment['id'] == int(cid):
                    relateComment.append(comment)
            commentsCount = len(relateComment)
            return render_template('posts.html', posts = [post], comments = relateComment, commentsCount = commentsCount)


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
    
