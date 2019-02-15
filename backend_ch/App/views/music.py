# from ..extensions import db
import os
import hashlib
from flask import Blueprint, request, send_file, send_from_directory


music = Blueprint("music", __name__)


@music.route("/get/<user>/<filename>", methods=["GET","POST"])
def get_mp3(user,filename):
    directory = os.getcwd()
    path = os.path.join(directory,"data",user)

    return send_from_directory(path, filename, as_attachment=True)
