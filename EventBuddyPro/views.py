from flask import Blueprint, render_template , redirect, url_for
from .forms import EventForm

main_bp = Blueprint('main', __name__)
from . import db
# Import your models and other necessary dependencies
from .models import Event, Comment  # Import your models here

@main_bp.route('/')
def index():
    # Fetch a list of events (you should implement this query)
    events = Event.query.all()  # Replace with your actual query
    return render_template('index.html', events=events)

@main_bp.route('/event_detail', defaults={'event_id': None})
@main_bp.route('/event_detail/<int:event_id>')
def event_detail(event_id):
    if event_id is not None:
        # Fetch the event data from your database using the event_id
        event = Event.query.get(event_id)  # Replace with your actual query

        if event is not None:
            # Fetch comments for the event
            comments = Comment.query.filter_by(event_id=event_id).all()  # Replace with your actual query
            return render_template('event_detail.html', event=event, comments=comments)

    # Handle the case where there is no event ID or the event does not exist
    return render_template('event_detail.html', event=None, comments=None)

@main_bp.route('/event_create_update', methods=['GET', 'POST'])
def create_event():
    form = EventForm()  

    if form.validate_on_submit():
        print("Form has been submitted successfully")
        title = form.title.data
        description = form.description.data
        date = form.date.data
        status = form.status.data

        event = Event(title=title, description=description, date=date, status=status)

        db.session.add(event)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('create_event_update.html', form=form)

@main_bp.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')

@main_bp.route('/user')
def user():
    return render_template('user.html')

