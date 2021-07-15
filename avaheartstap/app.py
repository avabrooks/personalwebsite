from flask import Blueprint, render_template



groups_bp = Blueprint('groups', __name__,
                      template_folder='templates',
                      static_folder='static')

@groups_bp.route('/')
def groups():
    return render_template("/groups/groups.html")


