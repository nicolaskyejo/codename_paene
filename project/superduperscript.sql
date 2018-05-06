CREATE USER IF NOT EXISTS 'dbuser'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT, UPDATE, DELETE, INSERT ON theverge.* TO dbuser@localhost;

DROP DATABASE IF EXISTS theverge;
CREATE DATABASE theverge;
USE theverge;

CREATE TABLE Room
(
  Room_id INT NOT NULL,
  Door_description VARCHAR(50),
  Locked BOOLEAN, 
  PRIMARY KEY (Room_id)
);

CREATE TABLE Npc
(
  Npc_id INT NOT NULL,
  Name VARCHAR(40) NOT NULL,
  Room_id INT NOT NULL,
  Description VARCHAR(200),  #added manually  #Npcs outward appearance
  Conversation VARCHAR(200),   #added manually  #Text that comes when you interact with a NPC
  Talked BOOLEAN,
  PRIMARY KEY (Npc_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);

CREATE TABLE Texti
(
  #Text_id INT NOT NULL,
  ActualText VARCHAR(1000) NOT NULL,
  Room_id INT,
  #PRIMARY KEY (Text_id),
  PRIMARY KEY (Room_id), 
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
  Name VARCHAR(70) NOT NULL,
  Hidden BOOLEAN,
  Inventory BOOLEAN,
  Room_id INT,
  Description VARCHAR(1000), #added manually
  # We perhaps might add a new text field which contains the text which we update to after a room state has changed
  Pickable BOOLEAN,		#added manually
  Used BOOLEAN, 	#added manually
  PRIMARY KEY (Item_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);



############################################################################
###################  INPUT BELOW  ##########################################


# [Room] # 33 rooms     #rooms are numbered clockwise starting from bottom
INSERT INTO Room VALUES(100,"1F Corridor/Clinic",TRUE);	#_00 and _10 are reserved for corridors
INSERT INTO Room VALUES(110,"1F Corridor/Lobby",FALSE);
INSERT INTO Room VALUES(666,"Hospital Yard",TRUE);  # Locked , can be opened by key or you know what.

INSERT INTO Room VALUES(101,"Operating room",TRUE);	
INSERT INTO Room VALUES(102,"Dispensary",TRUE); 
INSERT INTO Room VALUES(103,"...eria, the starting letters are missing",FALSE);
INSERT INTO Room VALUES(104,"Toilet",FALSE);
INSERT INTO Room VALUES(105,"Private room",TRUE);	#LOCK
INSERT INTO Room VALUES(106,"Private room",TRUE);	#LOCK
INSERT INTO Room VALUES(107,"Operating room",FALSE);
INSERT INTO Room VALUES(108,"Administration Services",FALSE); 

INSERT INTO Room VALUES(200,"2F Corridor/Physiotherapy",FALSE);
INSERT INTO Room VALUES(210,"2F Corridor/Cardiology",FALSE);
INSERT INTO Room VALUES(201,"Operating room",FALSE);
INSERT INTO Room VALUES(202,"Patient room",FALSE);
INSERT INTO Room VALUES(203,"Patient room",TRUE);
INSERT INTO Room VALUES(204,"(Can't make out the letters)",FALSE);
INSERT INTO Room VALUES(205,"Laboratory",TRUE);
INSERT INTO Room VALUES(206,"Cardiac care unit",FALSE);
INSERT INTO Room VALUES(207,"Cardiac care unit",TRUE);

INSERT INTO Room VALUES(300,"3F Corridor/Oncology",FALSE);
INSERT INTO Room VALUES(310,"3F Corridor/Radiology",FALSE);
INSERT INTO Room VALUES(301,"Chemotherapy",TRUE);
INSERT INTO Room VALUES(302,"Storage room",FALSE);
INSERT INTO Room VALUES(303,"Bone Marrow Transplant",TRUE);
INSERT INTO Room VALUES(304,"Radiotherapy",FALSE);
INSERT INTO Room VALUES(305,"Operating room",FALSE);   # has 1 npc and 1 enemy
INSERT INTO Room VALUES(306,"Medical Imaging",FALSE);	 # has two enemies
INSERT INTO Room VALUES(307,"Medical Imaging",FALSE);

INSERT INTO Room VALUES(400,"4F Corridor/Neurology",FALSE);
INSERT INTO Room VALUES(410,"4F Corridor/Orthopaedics",FALSE);
INSERT INTO Room VALUES(401,"Brain Scans",TRUE);			
INSERT INTO Room VALUES(402,"Operating room",TRUE);
INSERT INTO Room VALUES(403,"Trauma room",FALSE);


# [Npc] # 13 npcs
INSERT INTO Npc VALUES(1,"Crackmaster",100,NULL,NULL,FALSE);
INSERT INTO Npc VALUES(2,"drugsarebad",202,NULL,NULL,FALSE);
INSERT INTO Npc VALUES(3,"Coffeisadrug",210,NULL,NULL,FALSE);
INSERT INTO Npc VALUES(4,"Sleepislikedeath",306,NULL,NULL,FALSE);
INSERT INTO Npc VALUES(5,"im12whatisthis",306,NULL,NULL,FALSE);
INSERT INTO Npc VALUES(6,"follower",305,NULL,NULL,FALSE);

INSERT INTO Npc VALUES(7,"Buchwald",401,"A balding man with big spectactles and a face full of wrinkles","Thank you for sparing me.",FALSE);
INSERT INTO Npc VALUES(8,"Jake",107,"He looks crazy","Get away from me!",FALSE);   
INSERT INTO Npc VALUES(9,"Lawrence",201,"He looks happy","He he he!",FALSE); #hangman game and lighter from him
INSERT INTO Npc VALUES(10,"Cromwell",403,"He looks sick","You...",FALSE);
INSERT INTO Npc VALUES(11,"Eisenberg",305,"He seems busy","Leave me alone for now.",FALSE);       #in room with npc(Paul & follower)
INSERT INTO Npc VALUES(12,"Paul",305,"He looks dead","",FALSE);
INSERT INTO Npc VALUES(13,"Gebhard",200,"He looks confused","Aliens I tell you!",FALSE);


# [Texti] # Room inside text  #33 rooms therefore 33 texts

INSERT INTO Texti VALUES("A normal corridor with five rooms and stairs leading up.", 100);
INSERT INTO Texti VALUES("Seems like a hospital lounge with two rooms. On the east side, the building is damaged and thus innaccesible. On the middle there is an exit door to outside bolted with chains and a huge lock.", 110);
INSERT INTO Texti VALUES("A basic operating room. It is miserable looking but the surgery instruments appear well maintained.",101); 
INSERT INTO Texti VALUES("A messy storage room with tables and chairs lazily stacked on top of each other. Whoever maintains this place is not very orderly...",102); 
INSERT INTO Texti VALUES("Oh what's that smell! The whole room is covered in mold. Doesn't seem like there's really anything useful in this room.",103); 
INSERT INTO Texti VALUES("A toilet room. Everything seems broken down including the sink and the wall tiles.",104); 
#INSERT INTO Texti VALUES("This looks like something that used to be an office's break room. Some floor tiles are missing and parts of the interior decorations have been ripped off the walls...",104); 
INSERT INTO Texti VALUES("A small storage room. There's a big drawer near the back of the room.",105); 
INSERT INTO Texti VALUES("There's a window on the wall but it appears to be completely sealed with several metal bars. The little bit of natural light and fresh air coming inside makes me feel better.",106); 
INSERT INTO Texti VALUES("This room looks familiar to the one I woke up in. Oh what's that! I hear something from the corner. A man in a hospital gown is staring at the wall.",107);
INSERT INTO Texti VALUES("This must be an office of some sort. The floor is cluttered with old paperwork.",108);


INSERT INTO Texti VALUES("A normal corridor with five rooms and stairs leading up and down. There's someone in the distance.", 200);
INSERT INTO Texti VALUES("A corridor with two rooms. On the east side, the building is damaged and broken.", 210);
INSERT INTO Texti VALUES("A large well room kept in great condition. I can hear a faint creaking noise. There's someone in the corner!",201); 
INSERT INTO Texti VALUES("Oh shit! There's someone inside and he doesn't look happy at all.",202); 
INSERT INTO Texti VALUES("Ough... The door handle won't budge.",203); 
INSERT INTO Texti VALUES("This room is completely empty and fairly bright, the window is sealed with barb wire. Maybe I could get through this with something.",204); 
INSERT INTO Texti VALUES("The door won't open! Feels like it has been sealed from the other side.",205); 
INSERT INTO Texti VALUES("Something horrible must have had happened here. The smell is horrendous and the entire room is filled with trash. \
Ough wtf! I stepped on something wet.",206); 
INSERT INTO Texti VALUES("I can hear a child speaking faintly. The handle won't move at all... I hope whoever is inside is okay.",207);


INSERT INTO Texti VALUES("A darker looking corridor with some rooms. Looks like there is a light coming from room ... 305. There are stairs leading up and down.", 300);
INSERT INTO Texti VALUES("A Corridor with two rooms side by side. The room closest to the corridor entrance has lights on... Noises are coming from the room, it sounds like two people are in a heated argument. The far side of the corridor is innaccesible.", 310);

INSERT INTO Texti VALUES("The door is locked.",301); 
INSERT INTO Texti VALUES("This room is extremely small... I can barely move. The entire room is filled with cardboard and all sorts of trash.",302); 
INSERT INTO Texti VALUES("The door is locked. It doesn't budge even after ramming it...",303); 
INSERT INTO Texti VALUES("This room is huge! It has been cleared of furniture but there appears to be all sorts of junk on the floor.",304); 
INSERT INTO Texti VALUES("An operating room with two men standing over what looks like a person on the surgery table. \
						One is a guard and \
						the other person is wearing different attire and appears to be some kind of doctor.",305);   #this text will be updated when the guard dies 
INSERT INTO Texti VALUES("There are two men standing inside talking loudly. They appear to be guards.",306); # Funktio for leaving / fighting
INSERT INTO Texti VALUES("A room with an old MRI machine. On the corner, there is a stack of old magazines. Near the window there is a dingy looking table.",307);



INSERT INTO Texti VALUES("The top floor corridor, with one distinguished looking room and another corridor on the other side. Stairs from are leading down only.", 400);
INSERT INTO Texti VALUES("A corridor with two rooms. The far side is damaged and innaccesible.", 410);
INSERT INTO Texti VALUES("There he is, the man himself sitting behind a desk. Time to end this! ",401); #Cutscenes?
INSERT INTO Texti VALUES("The door is firmly shut.",402); 
INSERT INTO Texti VALUES("This room is really clean. There's someone sleeping on a hospital bed.",403); 





# [Item] # 23+ items   #(id,name,hidden,inventory,room_id,desc,pickable,used)
INSERT INTO Item VALUES (1, "Medical table", FALSE, FALSE, 101, "A medical table with sharp instruments.", FALSE, FALSE);
INSERT INTO Item VALUES (1+1, "Scalpel", TRUE, FALSE, 101, "Sharp, a tool used in surgery.",TRUE, FALSE);
INSERT INTO Item VALUES (5, "Cigarette", TRUE, TRUE, 101, "Strange that they didn't take these cigarettes from me.",TRUE, FALSE);
INSERT INTO Item VALUES (8, "Box", FALSE,  FALSE, 101, "A cardboard box full of old medical books. Perhaps I could push this to the vent.",FALSE, FALSE);
INSERT INTO Item VALUES (100, "Vent", FALSE, FALSE, 101, "A big air vent. It has a metal cover, held in place by screws in its four corners.", FALSE, FALSE);
INSERT INTO Item VALUES (103, "Vent", TRUE, FALSE, 101, "An opened air vent. It is big enough for a person to pass through.", FALSE, FALSE);

INSERT INTO Item VALUES (11, "Drawer", FALSE,  FALSE, 102, "A dark lacquered wooden drawer.",FALSE, FALSE);
INSERT INTO Item VALUES (11+1, "Painkillers", TRUE,  FALSE, 102, "I should probably take these...",TRUE, FALSE);

INSERT INTO Item VALUES (15, "Sink", FALSE,  FALSE, 104, "A small stained sink with rusted pipes under it.",FALSE, FALSE);
INSERT INTO Item VALUES (15+1, "Metal pipe", TRUE, FALSE, 104, "Maybe I could crack something with this.",TRUE, FALSE);
INSERT INTO Item VALUES (19, "Noticeboard", FALSE, FALSE, 104, "A noticeboard. It is filled with post-it notes and pinned papers.",FALSE, FALSE);
INSERT INTO Item VALUES (19+1, "Paper", TRUE,  FALSE, 104, "A piece of worn out, crumbled paper... there's something written on it.
This place is not what it seems.",FALSE, FALSE);

INSERT INTO Item VALUES (23, "Drawer", FALSE,  FALSE, 105, "A dark lacquered wooden drawer.",FALSE, FALSE);
INSERT INTO Item VALUES (23+1, "Torn magazine", TRUE, FALSE, 105, "Internet Memes evolving as a form of metalanguage.",FALSE, FALSE);

INSERT INTO Item VALUES (27, "Stretcher", FALSE,  FALSE, 107, "An apparatus for moving patients... or bodies.",FALSE, FALSE);

INSERT INTO Item VALUES (30, "Bookshelf", FALSE,  FALSE, 108, "A large bookshelf filled with different books and documents.",FALSE, FALSE);
INSERT INTO Item VALUES (30+1, "A book", TRUE,  FALSE, 108, "On the cover there's a picture of something that faintly resembles a snake.\
I can't open the book, the pages seem to be stuck together.",FALSE, FALSE);

INSERT INTO Item VALUES (33, "Window", FALSE,  FALSE, 110, "A window with metal bars blocking anyone from going through.",FALSE, FALSE);

INSERT INTO Item VALUES (36, "Lighter", TRUE,  FALSE, 201, "It's an old zippo.",TRUE, FALSE);
INSERT INTO Item VALUES (39, "Office chair", FALSE,FALSE, 201, "A dirty navy blue office chair, looks uncomfortable to sit in.", FALSE, FALSE);


INSERT INTO Item VALUES (42, "Briefcase", FALSE, FALSE, 202, "A dirty pre-war briefcase.",FALSE, FALSE);
INSERT INTO Item VALUES (42+1, "Radiophone", TRUE, FALSE, 202, "I wonder if this thing still works.",TRUE, FALSE);
INSERT INTO Item VALUES (42+2, "Dusty diary", TRUE,FALSE, 202, "The dusty diary has a bookmarked page which contains what seems like a poem;

THIS is thy hour O Soul, thy free flight into the wordless,
Away from books, away from art, the day erased, the lesson done,
Thee fully forth emerging, silent, gazing, pondering the themes thou,
lovest best.
Night, sleep, death and the stars.
	-Walt Whitman", FALSE, FALSE);
	
INSERT INTO Item VALUES (47, "Water dispenser",FALSE, FALSE, 210, "An empty water dispenser sits next to the stairway.",FALSE, FALSE);

INSERT INTO Item VALUES (50, "Trunk", FALSE,  FALSE, 304, "An open foot locker trunk.",TRUE, FALSE);
INSERT INTO Item VALUES (50+1, "Alcohol", TRUE,  FALSE, 304, "Reads 'ISOPROPYL ALCOHOL 95%', they probably use this to clean wounds.",TRUE, FALSE);
INSERT INTO Item VALUES (50+2, "Torn journal", TRUE, FALSE, 304, "An excerpt from the magazine 'Voner' volume 36 issue 5 article 'What we take for granted' 
Euthanasia is the act of ending a life with the intention of relieving pain. In the 21st century it was a heatedly 
debated subject. Should people suffering in extreme pain be granted a request to end their life?

It is interesting to note that it is never was a crime to commit suicide. Everyone
has a right to that, but when it came to other people helping you die it meant
that they were complicit in your death.

Doctor Keller who is an Anthropologist at the University of Maine explained that what prevented 
them in their time to grant people this right were the following values:
Life is precious
It is a sin to end one's life (and therefore a sin to help someone else do it)
Giving up is a sign of weakness

Nowadays ofcourse the right to assisted-suicide is a universal right that we take for granted but in the 
21st century it was an issue of contention.",FALSE, FALSE);

INSERT INTO Item VALUES (55, "Table", FALSE, FALSE, 307, "A dingy table that looks like it was damaged by fire.", FALSE, FALSE);
INSERT INTO Item VALUES (55+1, "Magazine cutout", TRUE, FALSE, 307, "River water turning frogs gay?
How governments are a haven for satanic cults. Read feature on page 4 
Bilderberg group wants to turn you into a slave. Resist now!", FALSE, FALSE);
INSERT INTO Item VALUES (55+2, "Knife", TRUE,  FALSE, 307, "It’s a bit dull, but it should still get the job done.",TRUE, FALSE);
INSERT INTO Item VALUES (60, "MRI", FALSE, FALSE, 307, "This look like an old Magnetic Resonance Machine.", FALSE, FALSE);

INSERT INTO Item VALUES (61, "Storage box", FALSE, FALSE, 401, "An old storage box from before the war. It is slightly open.",TRUE, FALSE);
INSERT INTO Item VALUES (61+1, "Gasoline tank", TRUE, FALSE, 401, "It seems to have at least half a gallon left.",TRUE, FALSE);
INSERT INTO Item VALUES (61+2, "Medical book", TRUE, FALSE, 401, "Grays Anatomy the Anatomical Basis of Clinical Practice 41st Edition.",FALSE, FALSE);

INSERT INTO Item VALUES (66, "Shelf", FALSE, FALSE, 306, "Looks like there is something on it.",FALSE, FALSE);
INSERT INTO Item VALUES (66+1, "Robotics book", TRUE, FALSE, 306, "Robotic Surgery Guide 1st Edition.",FALSE, FALSE);
INSERT INTO Item VALUES (66+2, "Old journal", TRUE, FALSE, 306, "'Sugar: The white devil' reads on the cover.",FALSE, FALSE);


#KEYS#

INSERT INTO Item VALUES (70,"Simple key",TRUE,FALSE,305,"The doctor told me this opens one of the top floor doors.",TRUE,FALSE);
INSERT INTO Item VALUES (75,"Rusty key",TRUE,FALSE,401,"Opens the lobby door on the first floor.",TRUE,FALSE);

#TERMINAL#
#INSERT INTO Item VALUES (80, "Terminal", FALSE, FALSE, 110, "An old terminal, the power seems to be on.",FALSE, FALSE);



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
INSERT INTO Room_List VALUES (101,102);     #Vent from starting room to adjacent room

INSERT INTO Room_List VALUES (100,110);     #corridors
INSERT INTO Room_List VALUES (110,100);

INSERT INTO Room_List VALUES (200,201);
INSERT INTO Room_List VALUES (200,202);
INSERT INTO Room_List VALUES (200,203);
INSERT INTO Room_List VALUES (200,204);
INSERT INTO Room_List VALUES (200,205);

INSERT INTO Room_List VALUES (210,206);
INSERT INTO Room_List VALUES (210,207);

INSERT INTO Room_List VALUES (201,200);
INSERT INTO Room_List VALUES (202,200);
INSERT INTO Room_List VALUES (203,200);
INSERT INTO Room_List VALUES (204,200);
INSERT INTO Room_List VALUES (205,200);

INSERT INTO Room_List VALUES (206,210);
INSERT INTO Room_List VALUES (207,210);

INSERT INTO Room_List VALUES (200,210);		#corridors
INSERT INTO Room_List VALUES (210,200);

INSERT INTO Room_List VALUES (300,301);
INSERT INTO Room_List VALUES (300,302);
INSERT INTO Room_List VALUES (300,303);
INSERT INTO Room_List VALUES (300,304);
INSERT INTO Room_List VALUES (300,305);

INSERT INTO Room_List VALUES (310,306);
INSERT INTO Room_List VALUES (310,307);

INSERT INTO Room_List VALUES (301,300);
INSERT INTO Room_List VALUES (302,300);
INSERT INTO Room_List VALUES (303,300);
INSERT INTO Room_List VALUES (304,300);
INSERT INTO Room_List VALUES (305,300);

INSERT INTO Room_List VALUES (306,310);
INSERT INTO Room_List VALUES (307,310);

INSERT INTO Room_List VALUES (300,310);		#corridors
INSERT INTO Room_List VALUES (310,300);

INSERT INTO Room_List VALUES (400,401);

INSERT INTO Room_List VALUES (410,402);
INSERT INTO Room_List VALUES (410,403);

INSERT INTO Room_List VALUES (401,400);
INSERT INTO Room_List VALUES (402,410);
INSERT INTO Room_List VALUES (403,410);

INSERT INTO Room_List VALUES (400,410);		#corridors
INSERT INTO Room_List VALUES (410,400);

INSERT INTO Room_List VALUES (100,200);		#Lower corridor to upper corridor
INSERT INTO Room_List VALUES (200,100);
INSERT INTO Room_List VALUES (200,300);
INSERT INTO Room_List VALUES (300,200);
INSERT INTO Room_List VALUES (300,400);
INSERT INTO Room_List VALUES (400,300);

INSERT INTO Room_List VALUES (110,666);		#From lobby to outside # Game finishes when this is achieved

	
