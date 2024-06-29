from flask import Blueprint, render_template, request, redirect, url_for, render_template, redirect, url_for, request, flash
from app.models.Cierre import Cierre
from app.models import Promotor
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app import db


bp = Blueprint('Cierre', __name__)

