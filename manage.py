
from app import create_app
from app import db
from app.models import User

# from flask_migrate import Migrate #MigrateCommand

from flask.cli import FlaskGroup


# Creating app instance
app = create_app('production')
cli = FlaskGroup(app)

# migrate = Migrate(app,db)


@cli.command('test')
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@cli.command('shell')
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ == '_main_':
    cli()




# from app import create_app,db
# from flask_script import Manager,Server
# from app.models import User
# from flask_migrate import Migrate,MigrateCommand
# #app instance
# app = create_app('development')
# app= create_app('production')

# manager= Manager(app)
# manager.add_command('server', Server)

# migrate = Migrate(app,db)
# manager.add_command('db', MigrateCommand)

# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
# @manager.shell
# def make_shell_context():
#     return dict(app=app,db=db,User=User)
    
# if __name__ == '__main__':
#     manager.run()
