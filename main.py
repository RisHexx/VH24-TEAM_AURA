from MyApp import createapp , db
app = createapp();
# app.app_context().push()
# db.create_all()
if __name__ == "__main__":
    app.run(debug=True)