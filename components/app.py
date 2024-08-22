from models import Ocean, Rock, River, Session

# Create a database session
session = Session()

# Create Oceans
atlantic_ocean = Ocean(name="Atlantic Ocean")
pacific_ocean = Ocean(name="Pacific Ocean")

# Create Rocks
granite = Rock(name="Granite", ocean=atlantic_ocean)
basalt = Rock(name="Basalt", ocean=pacific_ocean)

# Create Rivers
nile_river = River(name="Nile River")
amazon_river = River(name="Amazon River")

# Add Many-to-Many relationships
atlantic_ocean.rivers.append(nile_river)
pacific_ocean.rivers.append(amazon_river)

nile_river.oceans.append(atlantic_ocean)
amazon_river.oceans.append(pacific_ocean)

nile_river.rocks.append(granite)
amazon_river.rocks.append(basalt)


session.add_all([atlantic_ocean, pacific_ocean, granite, basalt, nile_river, amazon_river])

session.commit()


session.close()

print("Successfully created relationships between Oceans, Rocks, and Rivers!")