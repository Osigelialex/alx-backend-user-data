#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """adds user to database
        """
        if email is None or hashed_password is None:
            return None

        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, *args, **kwargs) -> User:
        """finds user by input arguments
        """
        user = None

        if len(kwargs) != 0:
            user = self._session.query(User).filter_by(**kwargs).first()
        else:
            email = args[0]
            password = args[1]
            params = {"email": email, "hashed_password": password}
            user = self._session.query(User).filter_by(**params).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """updates user details using provided input
        """
        if len(kwargs) == 0:
            return

        user = None

        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            return

        valid_keys = ['hashed_password', 'email']

        for key, value in kwargs.items():
            if key not in valid_keys:
                raise ValueError
            user.key = value
