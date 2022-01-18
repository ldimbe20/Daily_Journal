DROP TABLE ENTRY

CREATE TABLE `Entry` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entries` TEXT NOT NULL,
	`concepts` TEXT NOT NULL,	
	`mood_id`	INTEGER NOT NULL,
	`date` TEXT NOT NULL,
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)

);



CREATE TABLE `Mood` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);


INSERT INTO `Entry` VALUES (null, "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake","Python",1,"Wed Sep 15 2021 10:10:47");
INSERT INTO `Entry` VALUES (null, "Don't like it", "Javescript!!",4,"Wed Sep 19 2021 10:10:47");



INSERT INTO `Mood` VALUES (null, "Happy");
INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Angry");
INSERT INTO `Mood` VALUES (null, "Ok");



SELECT

    a.id,
	a.entries,
    a.concepts,
    a.mood_id,
	a.date
FROM entry a
-- WHERE a.id = 1