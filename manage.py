from blog import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from blog.models import User, Post, Comments, Email


#creating app instance
app = create_app('production')

migrate = Migrate(app, db)
manager =  Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, Post = Post, Comments=Comments, Email=Email)

if __name__=='__main__':
  manager.run()