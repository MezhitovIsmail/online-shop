from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from flask_migrate import Migrate
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from models import db, Game, User
from auth import bp as auth_bp, init_login_manager, check_perm

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')
PER_PAGE = 10

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)

init_login_manager(app)

@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(err):
    error_msg = ('Возникла ошибка при подключении к базе данных. '
                 'Повторите попытку позже.')
    return f'{error_msg} (Подробнее: {err})', 500

@app.route('/')
def index():
    games = db.session.query(Game).all()
    return render_template('index.html', games=games)

@app.route('/buy/<int:game_id>', methods=['POST'])
@login_required
def buy_game(game_id):
    game = db.session.query(Game).get(game_id)
    if not game:
        flash("Игра не найдена.", "danger")
        return redirect(url_for('index'))

    if game.id in [g.id for g in current_user.purchased_games]:
        flash("Игра уже куплена.", "warning")
        return redirect(url_for('index'))

    current_user.purchased_games.append(game)
    db.session.commit()
    flash(f'Вы успешно приобрели игру "{game.name}".', 'success')
    return redirect(url_for('index'))

@app.route('/purchased_games')
@login_required
def purchased_games():
    return render_template('purchased_games.html', games=current_user.purchased_games)