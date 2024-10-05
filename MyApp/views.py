from flask import Blueprint, render_template, request, redirect, url_for ,jsonify , flash
from flask_login import login_required, current_user
from .models import Users,Orders
from . import db
from datetime import datetime, timedelta

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return render_template('landingpage.html')

@views.route("/userhome", methods=['GET', 'POST'])
@login_required
def userhome():
    if current_user.is_authenticated:
        return render_template("userHome.html", user=current_user)
    else:
        return redirect(url_for('auth.login'))


@views.route("/order", methods=['GET', 'POST'])
@login_required
def orders():
    # Fetch orders for the currently logged-in user
    orders_list = Orders.query.filter_by(user_id=current_user.id).all()
    
    return render_template("order.html", orders=orders_list)



@views.route("/userdata", methods=['GET', 'POST'])
def userdata():
    return "UserData"

@views.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    top_users = Users.query.order_by(Users.score.desc()).limit(5).all()  # Fetch top 5 users by score
    your_rank = Users.query.filter_by(id=current_user.id).first()  # Get current user's score
    user_score = your_rank.score if your_rank else 0  # Default to 0 if user not found

    # Determine the user's rank among all users
    user_rank = Users.query.filter(Users.score > user_score).count() + 1  # Rank is 1-based

    return render_template("leaderboard.html", top_users=top_users, your_rank=user_rank)


@views.route("/leaderboardAll", methods=['GET', 'POST'])
def leaderboardall():
    show_all = request.args.get('show_all', default='0', type=int)  # Check if show_all is set
    if show_all:
        top_users = Users.query.order_by(Users.score.desc()).all()  # Fetch all users by score
    else:
        top_users = Users.query.order_by(Users.score.desc()).limit(5).all()  # Fetch top 5 users by score

    your_rank = Users.query.filter_by(id=current_user.id).first()  # Get current user's score
    user_score = your_rank.score if your_rank else 0  # Default to 0 if user not found

    # Determine the user's rank among all users
    user_rank = Users.query.filter(Users.score > user_score).count() + 1  # Rank is 1-based

    return render_template("completeleader.html", top_users=top_users, your_rank=user_rank, show_all=show_all)

@views.route("/score", methods=['GET'])
@login_required
def score_page():
    # Assuming current_user is authenticated and holds the necessary data
    user_score = current_user.score
    username = current_user.username
    
    # Calculate user's rank based on their score
    your_rank = Users.query.order_by(Users.score.desc()).filter(Users.score >= user_score).count()

    return render_template("score.html", username=username, score=user_score, rank=your_rank)

# Route for delivery challenges
@views.route('/challenge', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in to access this page
def delivery_challenge():
    return render_template('challenge.html', current_user=current_user)

@views.route('/complete_challenge/<challenge_type>', methods=['POST'])
@login_required
def complete_challenge(challenge_type):
    # Get current date
    today = datetime.utcnow().date()
    user_id = current_user.id
    
    # Initialize completed order counts
    completed_orders_count = 0

    if challenge_type == 'daily':
        # Count completed orders for today
        completed_orders_count = Orders.query.filter(
            Orders.user_id == user_id,
            Orders.order_status == 'Completed',
            Orders.order_time >= today
        ).count()
        
        if completed_orders_count >= 5:
            current_user.score += 100
            flash("Daily challenge completed! You earned 100 points.")
        else:
            flash("Insufficient completed orders for daily challenge.")

    elif challenge_type == 'weekly':
        # Count completed orders for the past week
        week_start = today - timedelta(days=7)
        completed_orders_count = Orders.query.filter(
            Orders.user_id == user_id,
            Orders.order_status == 'Completed',
            Orders.order_time >= week_start
        ).count()

        if completed_orders_count >= 25:
            current_user.score += 250
            flash("Weekly challenge completed! You earned 250 points.")
        else:
            flash("Insufficient completed orders for weekly challenge.")

    elif challenge_type == 'monthly':
        # Count completed orders for the past month
        month_start = today - timedelta(days=30)
        completed_orders_count = Orders.query.filter(
            Orders.user_id == user_id,
            Orders.order_status == 'Completed',
            Orders.order_time >= month_start
        ).count()

        if completed_orders_count >= 120:
            current_user.score += 500
            flash("Monthly challenge completed! You earned 500 points.")
        else:
            flash("Insufficient completed orders for monthly challenge.")

    # Update the user's score in the database
    db.session.commit()
    return redirect(url_for('views.delivery_challenge'))


@views.route('/reward')
def reward():
    return render_template('reward.html')



import matplotlib.pyplot as plt
import io
import base64
from flask import render_template, url_for

@views.route('/graph')
@login_required
def graph_page():
    # Get the current user
    user = current_user

    # Get the completed orders count for the current user
    completed_orders_count = Orders.query.filter_by(user_id=user.id, order_status='Completed').count()

    # Prepare data for the pie chart
    labels = ['Completed Orders', 'Score']
    sizes = [completed_orders_count, user.score]
    colors = ['blue', 'orange']
    
    # Create a pie chart
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'{user.username}\'s Completed Orders vs Score')

    # Save the pie chart to a buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    # Pass the graph URL to the template
    return render_template('graph.html', graph_url=f'data:image/png;base64,{graph_url}')

@views.route("/map")
def maps():
    return render_template("mapp.html")