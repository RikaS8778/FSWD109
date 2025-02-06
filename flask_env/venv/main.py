from flask import Flask, jsonify, request, render_template

#Flask App
template_folder = "templates"
app = Flask(__name__, template_folder=template_folder)

# print(isinstance(app, Flask))  # Output: True

#define our routes -- GET Route
@app.route('/')
def home():
    print(request)
    print(request.method, request.path, request.query_string)
    return "Welcome to the home page!"

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        print(request.method, request.path, request.query_string)
    elif request.method == 'POST':
        print(request.method, request.path, request.query_string, request.json)
    return "This is the about page!"

@app.route('/contact')
def contact():
    print(request.method, request.path, request.query_string)
    # print(request.query_string[1])
    # print(request.query_string[0])
    id = request.args.id
    
    
    query = request.query_string.decode().split('&')
    dict = {}
    for i in query:
        key, value = i.split('=')
        dict[key] = value
    print(dict)
    return '++Contact Page++'

@app.route('/post/<id>')
def post(id):
    return id


#assignment-class6

posts = [
        {
            'id': 1,
            'title': 'Post 1',
            'content': 'This is the content of post 1'
        },
        {
            'id': 2,
            'title': 'Post 2',
            'content': 'This is the content of post 2'
        },
        {
            'id': 3,
            'title': 'Post 3',
            'content': 'This is the content of post 3'
        },
        {
             'id': 4,
            'title': 'Post 4',
            'content': 'This is the content of post 4'
        },
        {
            'id': 5,
            'title': 'Post 5',
            'content': 'This is the content of post 5'
        }
]

comments = [
    {
        'id': 1,
        'post_id': 1,
        'content': 'This is the comment of post 1-1'
    },
    {
        'id': 2,
        'post_id': 1,
        'content': 'This is the comment of post 1-2'
    },
    {
        'id': 3,
        'post_id': 2,
        'content': 'This is the comment of post 2-1'
    },
    {
        'id': 4,
        'post_id': 3,
        'content': 'This is the comment of post 3-1'
    },
    {
        'id': 5,
        'post_id': 3,
        'content': 'This is the comment of post 3-2'
    },
    {
        'id': 6,
        'post_id': 3,
        'content': 'This is the comment of post 3-3'
    },
    {
        'id': 7,
        'post_id': 4,
        'content': 'This is the comment of post 4-1'
    },
    {
        'id': 8,
        'post_id': 5,
        'content': 'This is the comment of post 5-1'
    },
    {
        'id': 9,
        'post_id': 5,
        'content': 'This is the comment of post 5-2'
    }
]
# GET posts/
@app.route('/posts')
def get_posts():
    return jsonify(posts)
        
# GET posts/pid
@app.route('/posts/<int:pid>')
def get_post(pid):
    data = []
    for i in posts:
        if i['id'] == pid:
            data = i
    if data :
        return f'Post title is "{data['title']}", post content is "{data["content"]}"'
    else:
        return 'Post not found'

# POST posts
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    title = data['title']
    content = data['content']
    # length = len(posts)
    reverseList = posts[::-1]['id']
    # maxId = posts[reverseList-1]['id']
    new_post = {
        'id': reverseList + 1,
        'title': title,
        'content': content
    }
    # posts.append(new_post)
    print(new_post)

    return 'success'
    # return posts[maxId]

# GET posts/pid/comments
@app.route('/posts/<pid>/comments')
def get_comments(pid):
    int_pid = int(pid)
    data = []
    for i in posts:
        if i['id'] == int_pid:
            print(i)
            for j in comments:
                if j['post_id'] == int_pid:
                    data.append(j)
                    print(j)
    print(data)
    return jsonify(data)
    

# GET posts/pid/comments/cid
@app.route('/posts/<pid>/comments/<cid>')
def getSpecificCommentOfSpecificPost(pid, cid):
    int_pid = int(pid)
    int_cid = int(cid)
    data = []
    for i in posts:
        if i['id'] == int_pid:
            for j in comments:
                if j['id'] == int_cid and j['post_id'] == int_pid:
                    data.append(j)
    return jsonify(data)


# POST posts/pid/comments
@app.route('/posts/<pid>/comments', methods=['POST'])
def create_comment(pid):
    int_pid = int(pid)
    data = request.json
    content = data['content']
    count_before = len(comments)
    for i in posts:
        if int_pid == i['id']:
            print('in logic')
            new_comment = {
                'id': comments[count_before-1]['id'] + 1,
                'post_id': int_pid,
                'content': content
            }
            comments.append(new_comment)
            print(comments)
    if(count_before == len(comments)):
        return ["Posts not found", 404]

    return f'Comment created with id {comments[len(comments)-1]['id']} and content saved as "{comments[len(comments)-1]['content']}"'




if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
    
