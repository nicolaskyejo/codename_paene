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
  Name VARCHAR(40) NOT NULL,
  Hidden BOOLEAN,
  Inventory BOOLEAN,
  Room_id INT,
  Description VARCHAR(500), #added manually
  # We perhaps might add a new text field which contains the text which we update to after a room state has changed
  Pickable BOOLEAN,		#added manually
  Used BOOLEAN, 	#added manually
  PRIMARY KEY (Item_id),
  FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);



############################################################################
###################  INPUT BELOW  ##########################################

# [Protagonist] #

# [Room] # 33 rooms
INSERT INTO Room VALUES(100,"Clinic/West wing",FALSE);	#_00 and _10 are reserved for corridors
INSERT INTO Room VALUES(110,"Clinic/Lobby",FALSE);
INSERT INTO Room VALUES(666,"Hospital Yard",TRUE);  # Locked , can be opened by key or you know what.

INSERT INTO Room VALUES(101,"Operating room",FALSE);	#rooms are numbered clockwise starting from bottom
INSERT INTO Room VALUES(102,"Dispensary",FALSE);
INSERT INTO Room VALUES(103,"...eria, the starting letters are missing",FALSE);
INSERT INTO Room VALUES(104,"Storage",FALSE);
INSERT INTO Room VALUES(105,"Private room",TRUE);	#LOCK
INSERT INTO Room VALUES(106,"Private room",TRUE);	#LOCK
INSERT INTO Room VALUES(107,"Operating room",FALSE);
INSERT INTO Room VALUES(108,"Administration Services",TRUE); #LOCK

INSERT INTO Room VALUES(200,"Physiotherapy",FALSE);
INSERT INTO Room VALUES(210,"Cardiology",FALSE);
INSERT INTO Room VALUES(201,"Operating room",FALSE);
INSERT INTO Room VALUES(202,"Patient room",FALSE);
INSERT INTO Room VALUES(203,"Patient room",TRUE);
INSERT INTO Room VALUES(204,"Can't make out the letters",FALSE);
INSERT INTO Room VALUES(205,"Laboratory",TRUE);
INSERT INTO Room VALUES(206,"Cardiac care unit",FALSE);
INSERT INTO Room VALUES(207,"Cardiac care unit",TRUE);

INSERT INTO Room VALUES(300,"Oncology",FALSE);
INSERT INTO Room VALUES(310,"Radiology",FALSE);
INSERT INTO Room VALUES(301,"Chemotherapy",TRUE);
INSERT INTO Room VALUES(302,"Storage room",FALSE);
INSERT INTO Room VALUES(303,"Bone Marrow Transplant",TRUE);
INSERT INTO Room VALUES(304,"Radiotherapy",FALSE);
INSERT INTO Room VALUES(305,"Operating room",FALSE);   # has 1 npc and 1 enemy
INSERT INTO Room VALUES(306,"Medical Imaging",FALSE);	 # has two enemies
INSERT INTO Room VALUES(307,"Medical Imaging",FALSE);

INSERT INTO Room VALUES(400,"Neurology",FALSE);
INSERT INTO Room VALUES(410,"Orthopaedics",FALSE);
INSERT INTO Room VALUES(401,"Brain Scans",FALSE);			
INSERT INTO Room VALUES(402,"Operating room",TRUE);
INSERT INTO Room VALUES(403,"Trauma room",FALSE);


# [Npc] # 13 npcs
INSERT INTO Npc VALUES(1,"Crackmaster",100,NULL,NULL);
INSERT INTO Npc VALUES(2,"drugsarebad",202,NULL,NULL);
INSERT INTO Npc VALUES(3,"Coffeisadrug",210,NULL,NULL);
INSERT INTO Npc VALUES(4,"Sleepislikedeath",306,NULL,NULL);
INSERT INTO Npc VALUES(5,"im12whatisthis",306,NULL,NULL);
INSERT INTO Npc VALUES(6,"follower",305,NULL,NULL);
INSERT INTO Npc VALUES(7,"Doctor Ingolf Buchwald",401,"A balding man with big spectactles","Thank you for sparing me");

INSERT INTO Npc VALUES(8,"Jake",107,"A hunch-backed man with bloodshot eyes is incessantly staring at the wall. He doesn't look very well..","Th-the w-w-walls are spying on me.. T-THOSE BASTARDS ARE UP TO SOMETHING BAD I KNOW IT! I-i-i got to keep on eye on them..");   
INSERT INTO Npc VALUES(9,"Lawrence",201,"A wretched looking man is sitting in a rusted wheelchair","I'm bored! Do you want to play a game of hangman? If you win I'll give you a reward"); #hangman game and lighter from him
INSERT INTO Npc VALUES(10,"Oliver Cromwell",403,"A ghostly-looking pale man is lying on a hospital bed. His face is filled with sweat","Hey, are you the doctor? You don't look like one. Can you find the doctor for me? I feel sick after taking the pills he gave me");
INSERT INTO Npc VALUES(11,"Doctor Reinhold Eisenberg",305,"An old man in his twilight years, gaunt and serious looking","Leave me alone for now");       #in room with npc(Paul & follower)
INSERT INTO Npc VALUES(12,"Paul",305,"A lean naked man is spread on the operating table","");
INSERT INTO Npc VALUES(13,"Jonathan Gebhard",200,"A confused looking man is walking in circles muttering to himself","uh ah... I know oh yes I know... It is the Aliens!");


# [Texti] # Room inside text  #33 rooms therefore 33 texts
INSERT INTO Texti VALUES("There is man in black patrolling. OH SHIT! He saw me and IS coming after ME! Gotta defend myself!", 100); #INSERT INTO Texti VALUES("Looks like some kind of corridor with rooms side by side", 100);
#INSERT INTO Texti VALUES("A normal corridor with five rooms and stairs leading up", 100);
INSERT INTO Texti VALUES("Seems like a hospital lounge with two rooms. On the east side, the building is damaged and thus innaccesible. On the middle there is an exit door outside bolted with chains and a huge lock.", 110);
INSERT INTO Texti VALUES("A basic operating room. It is miserable looking but the surgery instruments appear well maintained.",101); 
INSERT INTO Texti VALUES("A messy storage room with tables and chairs lazily stacked on top of each other. Whoever maintains this place is not very orderly...",102); 
INSERT INTO Texti VALUES("Oh what's that smell! The whole room is covered in mold. Doesn't seem like theres really anything useful in this room.",103); 
INSERT INTO Texti VALUES("This looks like something that used to be an office's break room. Some floor tiles are missing and parts of the interior decorations have been ripped off the walls...",104); 
INSERT INTO Texti VALUES("A small storage room. Theres a big drawer near the back of the room.",105); 
INSERT INTO Texti VALUES("Theres a window on the wall but it appears to be completely sealed with several metal bars. At least the little bit of natural light and fresh air makes me feel better.",106); 
INSERT INTO Texti VALUES("This room looks familier to the one I woke up in. Oh what's that! I hear something from the corner.",107);
INSERT INTO Texti VALUES("This must be an office of some sort. The floor is cluttered with old paperwork.",108);


INSERT INTO Texti VALUES("A normal corridor with five rooms and stairs leading up and down. There's someone in the distance", 200);
INSERT INTO Texti VALUES("A corridor with two rooms. On the east side, the building is damaged and broken.", 210);
INSERT INTO Texti VALUES("Goosebumps go through my spine, this room looks excatly the same as the one I woke up in. Theres a faint eerie creaking noise.",201); 
INSERT INTO Texti VALUES("Oh shit! There's someone inside and he doesn't look happy at all.",202); 
INSERT INTO Texti VALUES("Ough.. The door handle wont budge.",203); 
INSERT INTO Texti VALUES("This room is completely empty and fairly bright, the window is only sealed with barb wire. Maybe I could get through this with something.",204); 
INSERT INTO Texti VALUES("The door wont open! Feels like it has been sealed from the other side.",205); 
INSERT INTO Texti VALUES("Something horrible must have had happened here. The smell is horrendous and the entire room is filled with trash. \
Ough wtf! I stepped on something wet.",206); 
INSERT INTO Texti VALUES("I can hear a child speaking faintly. The handle wont move at all.. I hope whoever is inside is okay.",207);


INSERT INTO Texti VALUES("A darker looking corridor with some rooms. Looks like there is a light coming from room ... 305. There are stairs leading up and down.", 300);
INSERT INTO Texti VALUES("A Corridor with two rooms side by side. The room closest to the corridor entrance has lights on.. Noises are coming from the room, it sounds like two people are in a heated argument. The far side of the corridor is innaccesible.", 310);

INSERT INTO Texti VALUES("The door is locked",301); 
INSERT INTO Texti VALUES("This room is extremely small.. I can barely move. The entire room is filled with cardboard and all sorts of trash.",302); 
INSERT INTO Texti VALUES("The door is lockd. It doesn't budge even after ramming it..",303); 
INSERT INTO Texti VALUES("This room is huge! It has been cleared of furniture but there appears to be all sorts of junk on the floor.",304); 
INSERT INTO Texti VALUES("An operating room with two men standing over what looks like a person on the surgery table. \
								The other person is wearing different attire and appears to be some kind of doctor",305);   #this text will be updated when the guard dies 
INSERT INTO Texti VALUES("There are two men standing inside.. I really don't think I should take this on",306); # Funktio for leaving / fighting
INSERT INTO Texti VALUES("A room with an old MRI machine. On the corner, there is a stack of old magazines. Near the window there is a dingy looking",307);



INSERT INTO Texti VALUES("The top floor corridor, with one distinguished looking room and another corridor on the other side. Stairs from are leading down only.", 400);
INSERT INTO Texti VALUES("A corridor with two rooms. The far side is damaged and innaccesible.", 410);
INSERT INTO Texti VALUES("There he is, the man himself is sitting behind his desk. Time to end this! ",401); #Cutscenes?
INSERT INTO Texti VALUES("The door is firmly shut",402); 
INSERT INTO Texti VALUES("This room is really clean. Theres someone sleeping.",403); 

# ROOMS THAT CANNOT BE ENTERED: 203, 205, 207, 301, 303, 402
#LETS MAKE A FUNCTION FOR THE PLAYER TO DECIDE IF HE ENTERS ROOM 306.

# [Item] # 23+ items
INSERT INTO Item VALUES (6, "Scalpel", TRUE, TRUE, 101, "Sharp, a tool used in surgery.",TRUE, FALSE);
INSERT INTO Item VALUES (1, "Cigarette", TRUE, TRUE, 101, "Strange that they didn't take these cigarettes from me.",TRUE, NULL);
INSERT INTO Item VALUES (10, "Box", FALSE,  NULL, 101, "A cardboard box full of old medical books.",FALSE, FALSE);
INSERT INTO Item VALUES (100, "Vent", FALSE, NULL, 101, "A big air vent. It has a metal cover, held in place by screws in its four corners.", FALSE, NULL);
INSERT INTO Item VALUES (101, "Vent", TRUE, NULL, 101, "An opened air vent. It is big enough for a person to pass through.", FALSE, NULL);

INSERT INTO Item VALUES (4, "Metal Pipe", TRUE, NULL, 104, "Maybe I could crack something with this.",TRUE, NULL);
INSERT INTO Item VALUES (12, "Noticeboard", FALSE, NULL, 104, "A noticeboard. It is filled with post-it notes and pinned papers.",FALSE, NULL);
INSERT INTO Item VALUES (13, "Paper", TRUE,  NULL, 104, "A piece of worn out, crumbled paper.. there's something written on it.",FALSE, NULL);

INSERT INTO Item VALUES (2, "Lighter", TRUE,  NULL, 201, "It's an old zippo.",TRUE, NULL);
INSERT INTO Item VALUES (18, "Office chair", FALSE,NULL, 201, "A dirty navy blue office chair, looks uncomfortable to sit in.", FALSE, NULL);

INSERT INTO Item VALUES (7, "Gasoline Tank", FALSE, NULL, 401, "It seems to have at least half a gallon left.",TRUE, NULL);

INSERT INTO Item VALUES (8, "Radiophone", FALSE, NULL, 202, "I wonder if this thing still works.",TRUE, NULL);
INSERT INTO Item VALUES (23, "A dusty diary with a bookmarked page", FALSE,NULL, 202, "THIS is thy hour O Soul, thy free flight into the wordless,\
	Away from books, away from art, the day erased, the lesson done,\
	Thee fully forth emerging, silent, gazing, pondering the themes thou,\
	lovest best.\
	Night, sleep, death and the stars.\
	-Walt Whitman", FALSE, NULL);
	
INSERT INTO Item VALUES (9, "Ethanol", FALSE,  NULL, 304, "I’d love to drink this.. But I probably shouldn’t.",TRUE, NULL);

INSERT INTO Item VALUES (11, "Drawer", FALSE,  NULL, 102, "A dark lacquered wooden drawer.",FALSE, NULL);
INSERT INTO Item VALUES (3, "Painkillers", TRUE,  NULL, 102, "I should probably take these...",TRUE, NULL);

INSERT INTO Item VALUES (17, "Sink", FALSE,  NULL, 107, "A small stained sink with rusted pipes under it.",FALSE, NULL);
INSERT INTO Item VALUES (14, "Stretcher", FALSE,  NULL, 107, "An apparatus for moving patients.. or bodies.",FALSE, NULL);

INSERT INTO Item VALUES (15, "Window", FALSE,  NULL, 110, "A window with metal bars blocking anyone from going through.",FALSE, NULL);

INSERT INTO Item VALUES (16, "Water dispenser",FALSE, NULL, 210, "An empty water dispenser sits next to the stairway.",FALSE, NULL);

INSERT INTO Item VALUES (19, "An old looking magazine cutout", FALSE, NULL, 307, "River water turning frogs gay?\
		How governments are a haven for satanic cults!\
		Bilderberg group wants to turn you into a slave!", FALSE, NULL);
INSERT INTO Item VALUES (20, "Table", FALSE, NULL, 307, "A dingy table with what appears to be a knife on it.", FALSE, NULL);
INSERT INTO Item VALUES (21, "Table", FALSE, NULL, 307, "A dingy table that looks like it was damaged by fire.", FALSE, NULL);
INSERT INTO Item VALUES (22, "MRI", FALSE, NULL, 307, "This look like an old Magnetic Resonance machine", FALSE, NULL);
INSERT INTO Item VALUES (5, "Knife", TRUE,  NULL, 307, "It’s a bit dull, but it should still get the job done.",TRUE, NULL);


INSERT INTO Item VALUES (24, "Drawer", FALSE,  NULL, 105, "A dark lacquered wooden drawer.",FALSE, NULL);
INSERT INTO Item VALUES (25, "Bookshelf", FALSE,  NULL, 108, "A large bookshelf filled with different books and documents.",FALSE, NULL);
INSERT INTO Item VALUES (26, "A book", FALSE,  NULL, 108, "On the cover there's a picture of something that faintly resembles a snake.\
I can't open the book, the pages seem to be stuck together.",FALSE, NULL);

	
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

INSERT INTO Room_List VALUES (110,666);

	
