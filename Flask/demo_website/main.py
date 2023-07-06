from website import create_app

# intialize app
app = create_app()

if __name__ == '__app__': #run the webserver only through this file
    app.run(debug =True)  #re-run automatically