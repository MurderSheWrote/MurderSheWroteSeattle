from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    Text,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    """Create New Crime Entry for crimedb database. Mimic Socrata Table."""
    __tablename__ = 'crimedb'
    id = Column(Integer, primary_key=True)
    rms_cdw_id = Column(Integer)
    general_offense_number = Column(Integer)
    offense_code = Column(Integer)
    offense_code_extension = Column(Integer)
    offense_type = Column(Text)
    summary_offense_code = Column(Integer)
    summarized_offense_description = Column(Text)
    date_reported = Column(DateTime)#TODO is DateTime correct format?
    occured_data_or_data_range_start = Column(DateTime)#TODO is DateTime correct format?
    occured = Column(DateTime)#TODO is DateTime correct format?
    hundred_block_location = Column(Text)
    district = Column(Text)
    zone = Column(Text)
    census_tract_2000 = Column(Text)
    longitude = Column(Numeric)
    latitude = Column(Numeric)
    location = Column(Text)

# Index('my_index', MyModel.name, unique=True, mysql_length=255)
