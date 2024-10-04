from MyApp import createapp, db

app = createapp()

# with app.app_context():
#     # Create all database tables
#     db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
