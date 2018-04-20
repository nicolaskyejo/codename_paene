DROP DATABASE IF EXISTS theverge;
CREATE DATABASE theverge;
USE theverge;

CREATE TABLE Protagonist
(
  Character_id INT NOT NULL,
  PRIMARY KEY (Character_id)
);

CREATE TABLE Room
(
  Room_id INT NOT NULL,
  PRIMARY KEY (Room_id)
);

CREATE TABLE Npc
(
  Enemy_Id INT NOT NULL,
  Name INT NOT NULL,
  Room_id INT,
  PRIMARY KEY (Enemy_Id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);

CREATE TABLE Texti
(
  Text_id INT NOT NULL,
  ActualText INT NOT NULL,
  Room_id INT NOT NULL,
  PRIMARY KEY (Text_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);

CREATE TABLE Room_List
(
  Room_id INT NOT NULL,
  Room_List INT NOT NULL,
  PRIMARY KEY (Room_id, Room_List),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id),
  FOREIGN KEY (Room_List) REFERENCES Room(Room_id)
);

CREATE TABLE Item
(
  Item_id INT NOT NULL,
  Name INT NOT NULL,
  Use_item INT NOT NULL,
  Character_id INT,
  Room_id INT,
  PRIMARY KEY (Item_id),
  FOREIGN KEY (Character_id) REFERENCES Protagonist(Character_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);



############################################################################
###################  INPUT BELOW       #####################################

# [Protagonist] #
#INSERT INTO Protagonist VALUES (1);

# [Room] #
#INSERT INTO VALUES ()

# [Npc] #
#INSERT INTO VALUES ()

# [Texti] #
#INSERT INTO VALUES ()

# [Lista] #
#INSERT INTO VALUES ()

# [Item] #
#INSERT INTO VALUES ()
