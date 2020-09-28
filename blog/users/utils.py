import os
import secrets
from PIL import Image
from flask import current_app


def save_pic(form_picture):
  """
  function that saves the picture uploaded, gives it a rondom hex number and also resizes it
  """
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_fn = random_hex + f_ext
  pic_path = os.path.join(current_app.root_path, 'static/images', picture_fn)

  output_size = (125, 125)
  form_picture.save(pic_path)
  i = Image.open(form_picture)
  i.thumbnail(output_size)
  i.save(pic_path)

  return picture_fn
