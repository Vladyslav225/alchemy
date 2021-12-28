from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import String, Column, Boolean, Integer, Date, JSON, ForeignKey, engine_from_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class user(Base):
    __tablename__ = 'user_primary'
    id = Column(Integer, primary_key=True)
    name = Column(String,)
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    def __str__(self):
        return f"{self.name}"

CONN = "localhost:5432/test_db"
USER = "postgres"
PASS = "kmixas"
engine = create_engine(f'postgresql+psycopg2://{USER}:{PASS}@{CONN}')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

a = session.query(user).filter(user.id==1, user.name=='name').first()
print(a)