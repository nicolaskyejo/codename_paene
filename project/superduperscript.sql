CREATE TABLE Character
(
  Character_id INT NOT NULL,
  PRIMARY KEY (Character_id)
);

CREATE TABLE Room
(
  Room_id INT NOT NULL,
  PRIMARY KEY (Room_id)
);

CREATE TABLE NPC
(
  Enemy_Id INT NOT NULL,
  Name INT NOT NULL,
  Room_id INT,
  PRIMARY KEY (Enemy_Id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);

CREATE TABLE Text
(
  Text_id INT NOT NULL,
  ActualText INT NOT NULL,
  PRIMARY KEY (Text_id)
);

CREATE TABLE Relationship
(
  Text_id INT NOT NULL,
  Room_id INT NOT NULL,
  PRIMARY KEY (Text_id, Room_id),
  FOREIGN KEY (Text_id) REFERENCES Text(Text_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);

CREATE TABLE Lista
(
  Description INT NOT NULL,
  RoomStart_id INT NOT NULL,
  RoomEnd_id INT NOT NULL,
  PRIMARY KEY (RoomStart_id, RoomEnd_id),
  FOREIGN KEY (RoomStart_id) REFERENCES Room(Room_id),
  FOREIGN KEY (RoomEnd_id) REFERENCES Room(Room_id)
);

CREATE TABLE Item
(
  Item_id INT NOT NULL,
  Name INT NOT NULL,
  Character_id INT,
  Room_id INT,
  PRIMARY KEY (Item_id),
  FOREIGN KEY (Character_id) REFERENCES Character(Character_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);


############################################################################
###################                    #####################################
