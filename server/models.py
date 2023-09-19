from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Owner(db.model):
    __tablename__ = "owners"

    id = db.column (db.Integer, primary_key=True)
    name = db.column (db.String, unique=True)

    pets = db.relationship ('pet' , backref='owner')

    def __repr__(self) :
        return f'<Pet Owner {self.name}>'
    

class Pets(db.model):
    __tablename__="pets"

    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String)
    species = db.column (db.String)

    owner_id = db.column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__ (self):
        return f'<Pet {self.name}, {self.species}>'    