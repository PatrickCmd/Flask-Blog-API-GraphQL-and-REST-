from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from blog import create_app
from blog.users import models
from blog.articles import models
from blog.database import Base, engine, db_session

app = create_app()
manager = Manager(app)
migrate = Migrate(app)


def make_shell_context():
    return dict(app=app)

manager.add_command(
    "shell", Shell(make_context=make_shell_context)
)

# migrations
manager.add_command("db", MigrateCommand)


@manager.command
def create_db():
    Base.metadata.create_all(bind=engine)
    return ("All tables created")


@manager.command
def drop_db():
    db_session.remove()
    Base.metadata.drop_all(bind=engine)
    return ("All tables droppped")

if __name__ == "__main__":
    manager.run()
