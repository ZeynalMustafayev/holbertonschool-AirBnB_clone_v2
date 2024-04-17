#!/usr/bin/python3
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    __engine = None
    __session = None
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]

    def __init__(self):
        self.user = getenv("HBNB_MYSQL_USER")
        self.password = getenv("HBNB_MYSQL_PWD")
        self.host = getenv("HBNB_MYSQL_HOST", 'localhost')
        self.database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(self.user, self.password, self.host, self.database),
            pool_pre_ping=True,
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objs = dict()

        if cls is None:
            for class_name in self.classes:
                type_of_class = eval(class_name)
                values = self.__session.query(type_of_class).all()
                objs = {"{}.{}".format(
                    type_of_class.__name__, value.id
                    ): value for value in values}
        else:
            values = self.__session.query(cls).all()
            objs = {"{}.{}".format(
                cls.__name__, value.id
                ): value for value in values}

        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        self.__session.close()
