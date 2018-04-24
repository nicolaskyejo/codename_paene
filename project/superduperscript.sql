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
  Npc_id INT NOT NULL,
  Name VARCHAR(40) NOT NULL,
  Room_id INT NOT NULL,
  Description VARCHAR(40),  #added manually  #Npcs outward appearance
  Conversation VARCHAR(200),   #added manually  #Text that comes when you interact with a NPC
  PRIMARY KEY (Npc_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);

CREATE TABLE Texti
(
  Text_id INT NOT NULL,
  ActualText VARCHAR(1000) NOT NULL,
  Room_id INT,
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
  Name VARCHAR(40) NOT NULL,
  Use_item INT NOT NULL,
  Character_id INT,
  Room_id INT,
  Description VARCHAR(100), #added manually
  PRIMARY KEY (Item_id),
  FOREIGN KEY (Character_id) REFERENCES Protagonist(Character_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);



############################################################################
###################  INPUT BELOW       #####################################

# [Protagonist] #
INSERT INTO Protagonist VALUES (1);

# [Room] # 33 rooms
INSERT INTO Room VALUES(101);
INSERT INTO Room VALUES(100);  #100 and 109 are reserved for corridors
INSERT INTO Room VALUES(102);
INSERT INTO Room VALUES(103);
INSERT INTO Room VALUES(104);
INSERT INTO Room VALUES(105);
INSERT INTO Room VALUES(106);
INSERT INTO Room VALUES(107);
INSERT INTO Room VALUES(108);
INSERT INTO Room VALUES(109);


# [Npc] # 13 npcs
INSERT INTO Npc VALUES(1,"Crackmaster",100,NULL,NULL);

# [Texti] # Room text
INSERT INTO Texti VALUES(1, "Looks like some kind of corridor", 100);

# [Room_List] # Each room has a list of room it is connected to
INSERT INTO Room_List VALUES (100,107);

# [Item] # 9 items
#INSERT INTO VALUES ()
INSERT INTO Item VALUES (6, "scalpel", 0, NULL, 101, "sharp, a tool used in surgery");

 
