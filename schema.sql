DROP TABLE IF EXISTS userlist;
DROP TABLE IF EXISTS studentprofile;
DROP TABLE IF EXISTS adminprofile;
DROP TABLE IF EXISTS student_contact;
DROP TABLE IF EXISTS "Hall Ticket";
DROP TABLE IF EXISTS "Subjects";


CREATE TABLE userlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    _name TEXT NOT NULL,
    _password TEXT NOT NULL,
    isAdmin INTEGER NOT NULL
);

CREATE TABLE studentprofile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    s_fname TEXT NOT NULL,
    s_mname TEXT NOT NULL,
    s_lname TEXT NOT NULL,
    gender TEXT NOT NULL,
    birthdate TEXT NOT NULL,
    cast_catagory TEXT NOT NULL,
    '10thpr' TEXT NOT NULL,
    '10thpercentage' TEXT NOT NULL,
    past_school_name TEXT NOT NULL,
    enrollment_year INTEGER,
    'standard' TEXT NOT NULL,
    permenent_id TEXT NOT NULL
);

CREATE TABLE student_contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    s_fname TEXT,
    home_address TEXT,
    city TEXT,
    pin_code INTEGER,
    home_state TEXT,
    mobile_no TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE adminprofile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    a_fname TEXT NOT NULL,
    a_mname TEXT NOT NULL,
    a_lname TEXT NOT NULL,
    gender TEXT NOT NULL,
    birthdate TEXT NOT NULL,
    permenent_id TEXT NOT NULL,
    cast_catagory TEXT
);

CREATE TABLE "Hall Ticket"(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "Exam No" INTEGER,
    "Exam Code" TEXT NOT NULL,
    "Exam Type" TEXT,
    "Date" TEXT,
    "Exam Time" TEXT
    "Semester" INTEGER,
);

CREATE TABLE "Subjects" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "Subject Name" TEXT NOT NULL,
    "Standard" TEXT,
    "Semester" TEXT,
    "Subject Credit" TEXT
);