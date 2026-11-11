from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False)

  posts = relationship('Post', back_populates='author')


class Post(Base):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  content = Column(String)
  user_id = Column(Integer, ForeignKey('users.id'))

  author = relationship('User', back_populates='posts')


# Создаем базу данных project.db
engine = create_engine('sqlite:///project.db', echo=True)

if __name__ == '__main__':
  Base.metadata.create_all(engine)
  print ('Таблицы по твоей схеме успешно созданы в project.db!')