CREATE TABLE Releases (
    id SERIAL PRIMARY KEY,
    name TEXT,
    genre TEXT,
    performer TEXT,
    release_year INTEGER
);

CREATE TABLE Tracks (
    id SERIAL PRIMARY KEY,
    name TEXT,
    release_id INTEGER REFERENCES Releases
);

CREATE TABLE Personnel (
    id INTEGER,
    name TEXT,
    role TEXT,
    release_id INTEGER REFERENCES Releases
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

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name TEXT
    password TEXT
);
