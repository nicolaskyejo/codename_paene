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
  Description VARCHAR(100),  #added manually  #Npcs outward appearance
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
INSERT INTO Room VALUES(100);  #100 and 110 are reserved for corridors
INSERT INTO Room VALUES(110);
INSERT INTO Room VALUES(101);	#rooms are numbered clockwise starting from bottom
INSERT INTO Room VALUES(102);
INSERT INTO Room VALUES(103);
INSERT INTO Room VALUES(104);
INSERT INTO Room VALUES(105);
INSERT INTO Room VALUES(106);
INSERT INTO Room VALUES(107);
INSERT INTO Room VALUES(108);

INSERT INTO Room VALUES(200);
INSERT INTO Room VALUES(210);
INSERT INTO Room VALUES(201);
INSERT INTO Room VALUES(202);
INSERT INTO Room VALUES(203);
INSERT INTO Room VALUES(204);
INSERT INTO Room VALUES(205);
INSERT INTO Room VALUES(206);
INSERT INTO Room VALUES(207);

INSERT INTO Room VALUES(300);
INSERT INTO Room VALUES(310);
INSERT INTO Room VALUES(301);
INSERT INTO Room VALUES(302);
INSERT INTO Room VALUES(303);
INSERT INTO Room VALUES(304);
INSERT INTO Room VALUES(305);   # has 1 npc and 1 enemy
INSERT INTO Room VALUES(306);	# has two enemies
INSERT INTO Room VALUES(307);

INSERT INTO Room VALUES(400);
INSERT INTO Room VALUES(410);
INSERT INTO Room VALUES(401);
INSERT INTO Room VALUES(402);
INSERT INTO Room VALUES(403);

# [Npc] # 13 npcs
INSERT INTO Npc VALUES(1,"Crackmaster",100,NULL,NULL);
INSERT INTO Npc VALUES(2,"drugsarebad",202,NULL,NULL);
INSERT INTO Npc VALUES(3,"Coffeisadrug",210,NULL,NULL);
INSERT INTO Npc VALUES(4,"Sleepislikedeath",306,NULL,NULL);
INSERT INTO Npc VALUES(5,"im12whatisthis",306,NULL,NULL);
INSERT INTO Npc VALUES(6,"follower",305,NULL,NULL);
INSERT INTO Npc VALUES(7,"Doctor Ingolf Buchwald",401,"A balding man with big spectactles","Thank you for sparing me");

INSERT INTO Npc VALUES(8,"Jake",107,"desc","conv");   #hangman game and key from him
INSERT INTO Npc VALUES(9,"Lawrence",201,"desc","conv");
INSERT INTO Npc VALUES(10,"Oliver Cromwell",403,"desc","conv");
INSERT INTO Npc VALUES(11,"Doctor Reinhold Eisenberg",305,"An old man in his sixties, gaunt and serious looking","Leave me alone for now");       #in room with npc(Paul & follower)
INSERT INTO Npc VALUES(12,"Paul",305,"A thin man is spread on the operating table","conv");

# [Texti] # Room text  #33 rooms therefore 33 texts
INSERT INTO Texti VALUES(1, "Looks like some kind of corridor", 100);

# [Room_List] # Each room has a list of room it is connected to
INSERT INTO Room_List VALUES (100,101);
INSERT INTO Room_List VALUES (100,102);
INSERT INTO Room_List VALUES (100,103);
INSERT INTO Room_List VALUES (100,104);
INSERT INTO Room_List VALUES (100,105);
INSERT INTO Room_List VALUES (100,106);
INSERT INTO Room_List VALUES (110,107);
INSERT INTO Room_List VALUES (110,108);

INSERT INTO Room_List VALUES (101,100);
INSERT INTO Room_List VALUES (102,100);
INSERT INTO Room_List VALUES (103,100);
INSERT INTO Room_List VALUES (104,100);
INSERT INTO Room_List VALUES (105,100);
INSERT INTO Room_List VALUES (106,100);

INSERT INTO Room_List VALUES (107,110);
INSERT INTO Room_List VALUES (108,110);

# [Item] # 9 items
INSERT INTO Item VALUES (6, "Scalpel", 0, NULL, 101, "sharp, a tool used in surgery");
