CREATE TABLE GalaxyType (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE Galaxy (
    galaxy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age NUMERIC,
    type_id INTEGER REFERENCES GalaxyType(type_id) ON DELETE CASCADE,
    size NUMERIC
);

CREATE TABLE StarSystem (
    system_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age NUMERIC,
    radius INT,
    galaxy_id INTEGER REFERENCES Galaxy(galaxy_id) ON DELETE CASCADE
);

CREATE TABLE Planet (
    planet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age NUMERIC,
    radius INT,
    mass NUMERIC,
    habitable BOOLEAN,
    system_id INTEGER REFERENCES StarSystem(system_id) ON DELETE CASCADE
);

CREATE TABLE Star (
    star_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    temperature NUMERIC,
    age NUMERIC,
    radius INT,
    mass NUMERIC,
    system_id INTEGER REFERENCES StarSystem(system_id) ON DELETE CASCADE
);




INSERT INTO GalaxyType (name) VALUES
    ('Elliptical'),
    ('Spiral'),
    ('Irregular');

INSERT INTO Galaxy (name, age, type_id, size) VALUES
    ('Milky Way', 1.36E10, 2, 1.0E5),
    ('Andromeda', 1.32E10, 2, 1.1E5),
    ('Triangulum', 1.2E9, 2, 7.0E3);

INSERT INTO StarSystem (name, age, radius, galaxy_id) VALUES
    ('Solar System', 4.6E9, 4.5E12, 1),
    ('Alpha Centauri', 4.85E9, 1.711E8, 1),
    ('Proxima Centauri', 4.85E9, 1.965E8, 1),
    ('Sirius System', 2.37E8, 1.711E8, 1),
    ('Alpha Centauri B', 4.85E9, 2.187E8, 1),
    ('Kepler-186', 3.92E9, 2.12E8, 2);

INSERT INTO Planet (name, age, radius, mass, habitable, system_id) VALUES
    ('Earth', 4.543E9, 6.371E6, 5.97219E24, 1, 1),
    ('Mars', 4.603E9, 3.3895E6, 6.4171E23, 0, 1),
    ('Venus', 4.503E9, 6.0518E6, 4.8675E24, 0, 1),
    ('Mars 2', 4.603E9, 3.3895E6, 6.4171E23, 0, 2),
    ('Gliese 581c', 2.37E9, 7.210E6, 5.92E24, 1, 4),
    ('Kepler-186f', 3.92E9, 8.75E6, 2.89E24, 1, 6);

INSERT INTO Star (name, temperature, age, radius, mass, system_id) VALUES
    ('Sun', 5778, 4.603E9, 6.9634E8, 1.989E30, 1),
    ('Proxima Centauri', 3050, 4.85E9, 1.965E8, 1.23E28, 3),
    ('Sirius A', 9940, 2.37E8, 1.711E8, 2.02E30, 5),
    ('Alpha Centauri A', 5790, 4.85E9, 1.223E9, 1.1E30, 6),
    ('Kepler-186 K', 3686, 3.92E9, 3.66E8, 0.5E30, 7);

