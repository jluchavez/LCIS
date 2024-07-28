BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"email"	VARCHAR(150),
	"password"	VARCHAR(150),
	"first_name"	VARCHAR(150),
	PRIMARY KEY("id"),
	UNIQUE("email")
);
CREATE TABLE IF NOT EXISTS "records" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(150),
	"disease"	VARCHAR(150),
	"doctor"	VARCHAR(150),
	"attendance"	VARCHAR(150),
	"date"	DATETIME,
	"status"	VARCHAR(150),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "patients" (
	"id"	INTEGER NOT NULL,
	"lname"	VARCHAR(150),
	"fname"	VARCHAR(150),
	"mname"	VARCHAR(150),
	"gender"	VARCHAR(150),
	"age"	VARCHAR(150),
	"contact"	VARCHAR(150),
	"date"	DATETIME,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "views" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(150),
	"note"	VARCHAR(150),
	"doctor"	VARCHAR(150),
	"confidential"	VARCHAR(150),
	"date"	DATETIME,
	"patient_id"	INTEGER,
	FOREIGN KEY("patient_id") REFERENCES "patients"("id"),
	PRIMARY KEY("id")
);
INSERT INTO "user" VALUES (1,'luchavezjohnlouie@gmail.com','sha256$AkgI4JozvTTRtYcW$e615942cf8b0125c4a1e65fa4c72be2dd31e8604d81bccc7f94534f774855bd0','John Louie ');
INSERT INTO "user" VALUES (2,'jaysean@gmail.com','sha256$BsJZO8zs2MgDhml6$892468cab6b28466a0cd8af35bfaf5862edd4f02b7881a7066572057914da405','Jay');
INSERT INTO "user" VALUES (3,'joenardamaro@gmail.com','sha256$6tgOjAO0sZoYY4qS$3471867b6db03d346db33e8a0b7f1711a16c8f60abc3db3274c8fcb4bfeb72ff','Joenard');
INSERT INTO "records" VALUES (0,'John Louie Luchavez','Asthma','Dra. Baskinas',NULL,'2022-12-13 00:00:00.000000',NULL);
INSERT INTO "records" VALUES (7,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (8,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (9,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (10,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (11,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (12,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (13,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (14,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-06 00:00:00.000000','Pending');
INSERT INTO "records" VALUES (15,'John Louie Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-02 00:00:00.000000','Active');
INSERT INTO "records" VALUES (16,'John Louie Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-02 00:00:00.000000','Active');
INSERT INTO "records" VALUES (17,'John Louie Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-02 00:00:00.000000','Active');
INSERT INTO "records" VALUES (18,'John Louie Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-02 00:00:00.000000','Active');
INSERT INTO "records" VALUES (19,'John Louie Luchavez','Asthma','Dra. Baskinas','Attended','2022-12-02 00:00:00.000000','Active');
INSERT INTO "records" VALUES (20,'Jay sean','Asthma','Dra. Baskinas','Missed','2022-12-09 00:00:00.000000','Inactive');
INSERT INTO "records" VALUES (21,'Lucila Rodriguez Luchavez','Asthma','Dra. Baskinas','Missed','2022-11-30 00:00:00.000000','Inactive');
INSERT INTO "patients" VALUES (1,'Luchavez','John Louie','Rodriguez','Male','20','09057173552','2022-11-27 00:00:00.000000');
INSERT INTO "patients" VALUES (2,'Smith','Julie','Foster','Female','19','09123452313','2022-11-28 00:00:00.000000');
INSERT INTO "patients" VALUES (3,'Sean','Jay','Odin','Male','21','09123452312','2022-11-12 00:00:00.000000');
INSERT INTO "views" VALUES (1,'Prolactin','History and Physical','Dr. Branch','No','2022-12-01 00:00:00.000000',1);
INSERT INTO "views" VALUES (2,'Alcohol','History and Physical','Dra. Baskinas','No','2022-10-12 00:00:00.000000',1);
COMMIT;
