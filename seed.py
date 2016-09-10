"""Utility file to seed database with parks data in seed_data/"""

from sqlalchemy import func
import pdb
from model import Park

from model import connect_to_db, db
from server import app


def load_parks():
    """Load parks from u.park into database."""

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Park.query.delete()

    # Read u.park file and insert data
    for row in open("park_data/u.park.csv"):

        park_name, latitude, longitude = row.split(",")
        latitude = float(latitude)
        longitude = float(longitude)

        park = Park(park_name=park_name,
                    latitude=latitude,
                    longitude=longitude)

        db.session.add(park)

    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()
    load_parks()