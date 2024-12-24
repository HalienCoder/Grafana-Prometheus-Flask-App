from website import create_app


app = create_app()

#Only if we run this file it will execute it, not if we import the file , we want this to happen because, when we import the file into another file, then python will run the file being imported, and that will cause the webserver to be started but we dont want that to happen.

if __name__ == '__main__':
    app.run(debug=True) # every time we make a change to our python code, it will automatically re run the webserver. we will turn that off during production, but we dont want to manually re run the web server.