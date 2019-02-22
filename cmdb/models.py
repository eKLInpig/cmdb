from sqlalchemy import Column, Integer, BigInteger, String, Text, Boolean
from sqlalchemy import ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import config


Base = declarative_base()

# 逻辑表
class Schema(Base):
    __tablename__ = "schema"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(48), nullable=False, unique=True)
    desc = Column(String(128), nullable=False)
    deleted = Column(Boolean, nullable=False, default=False)

    fields = relationship('Field')


class Field(Base):
    __tablename__ = "field"
    __table_args__ = (UniqueConstraint('schema_id', 'name'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(48), nullable=False)
    schema_id = Column(Integer, ForeignKey('schema.id'), nullable=False)
    meta = Column(Text, nullable=False)
    ref_id = Column(Integer, ForeignKey('field.id'), nullable=True)
    deleted = Column(Boolean, nullable=False, default=False)

    schema = relationship('Schema')
    ref = relationship('Field', uselist=False) # 1对1，被引用的id


# 逻辑表的记录表
class Entity(Base):
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(64), nullable=False, unique=True)
    schema_id = Column(Integer, ForeignKey('schema.id'), nullable=False)
    deleted = Column(Boolean, nullable=False, default=False)

    schema = relationship('Schema')


class Value(Base):
    __tablename__ = "value"
    __table_args__ = (UniqueConstraint('entity_id', 'field_id', name='uq_entity_field'),)

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    value = Column(Text, nullable=False)
    field_id = Column(Integer, ForeignKey('field.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('entity.id'), nullable=False)
    deleted = Column(Boolean, nullable=False, default=False)

    entity = relationship('Entity')
    field = relationship('Field')


# 引擎
engine = create_engine(config.URL, echo=config.DATABASE_DEBUG)

# 创建表
def create_all():
    Base.metadata.create_all(engine)

# 删除表
def drop_all():
    Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

