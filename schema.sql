drop TABLE if exists Tracks;
drop TABLE if exists Personnel;
drop TABLE if exists Releases;

CREATE TABLE Releases (
    id SERIAL PRIMARY KEY,
    name TEXT,
    genre TEXT,
    performer TEXT,
    year INTEGER
);

CREATE TABLE Tracks (
    listing INTEGER,
    name TEXT,
    release_id INTEGER REFERENCES Releases
);

CREATE TABLE Personnel (
    name TEXT,
    role TEXT,
    release_id INTEGER REFERENCES Releases
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE Reviews (
    id SERIAL PRIMARY KEY,
    reviewer_id INTEGER REFERENCES Users,
    riviewee_id INTEGER REFERENCES Releases,
    score INTEGER
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    release_id INTEGER REFERENCES Releases,
    commenter_id INTEGER REFERENCES Users,
    timestamp TIMESTAMP);
