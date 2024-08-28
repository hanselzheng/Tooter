from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.database import Toot
from . import db

views = Blueprint('views', __name__)


# Home Page
@views.route('/', methods=['GET','POST'])
@login_required
def home():
    posts = Toot.query.all()
    return render_template('home.html', user=current_user, posts=posts)


# Create Toots
@views.route('/toot', methods=['GET', 'POST'])
@login_required
def create_toot():
    if request.method == 'POST':
        toot = request.form.get('toot')

        if len(toot) < 1:
            flash('Toot cannot be empty', category='error')
        else:
            post = Toot(data=toot, user_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Toot!', category='success')
            return redirect(url_for('views.home'))

    return render_template('toot.html', user=current_user)


# Delete Toots
@views.route('/delete-post/<id>')
@login_required
def delete_post(id):
    post = Toot.query.get_or_404(id)

    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()
            flash('Toot deleted!', category='success')
        else:
            flash("You are not the owner of the toot", category="error")
    else: 
        flash("Toot does not exist.", category='error')

    return redirect(url_for('views.home'))
