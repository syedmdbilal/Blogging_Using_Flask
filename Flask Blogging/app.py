from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data to simulate blog posts
blog_posts = [
    {
        "id": 1,
        "title": "My First Blog Post",
        "content": "This is my First blog post content.",
    },
    {
        "id": 2,
        "title": "My Self",
        "content": "Hi, This is Syed Mohammed Bilal From Chennai.",
    },
    {
        "id": 3,
        "title": "Syed Mohammed Bilal",
        "content": "Welcome to My blog post content.",
    },
    {
        "id": 4,
        "title": "Pinaca Technology",
        "content": "Welcome to our Company.",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=blog_posts)


@app.route("/post/<int:post_id>")
def view_post(post_id):
    post = next((post for post in blog_posts if post["id"] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template("post.html", post=post)


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_post = {
            "id": len(blog_posts) + 1,
            "title": title,
            "content": content,
        }
        blog_posts.append(new_post)
        return redirect(url_for("index"))

    return render_template("new_post.html")


@app.route("/delete_post/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    global blog_posts
    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
