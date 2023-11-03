-- CREATE TABLE MeasurementUnit (
--     unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name VARCHAR(50) NOT NULL,
--     abbreviation VARCHAR(10)
-- );

CREATE TABLE GalaxyType (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE Galaxy (
    galaxy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age NUMERIC,
    -- age_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    type_id INTEGER REFERENCES GalaxyType(type_id),
    size NUMERIC
    -- size_unit_id INTEGER REFERENCES MeasurementUnit(unit_id)
);

CREATE TABLE StarSystem (
    system_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age NUMERIC,
    -- age_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    radius INT,
    -- radius_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    galaxy_id INTEGER REFERENCES Galaxy(galaxy_id) ON DELETE CASCADE
);

CREATE TABLE Planet (
    planet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age NUMERIC,
    -- age_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    radius INT,
    -- radius_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    mass NUMERIC,
    -- mass_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    habitable BOOLEAN,
    system_id INTEGER REFERENCES StarSystem(system_id) ON DELETE CASCADE
);

CREATE TABLE Star (
    star_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    temperature NUMERIC,
    -- temperature_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    age NUMERIC,
    -- age_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    radius INT,
    -- radius_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    mass NUMERIC,
    -- mass_unit_id INTEGER REFERENCES MeasurementUnit(unit_id),
    system_id INTEGER REFERENCES StarSystem(system_id) ON DELETE CASCADE
);


-- INSERT INTO MeasurementUnit (name, abbreviation) VALUES
--     ('Meters', 'm'),
--     ('Years', 'y'),
--     ('Kilograms', 'kg'),
--     ('Kelvin', 'K'),
--     ('Light-years', 'ly');

INSERT INTO GalaxyType (name) VALUES
    ('Elliptical'),
    ('Spiral'),
    ('Irregular');

INSERT INTO Galaxy (name, age, type_id, size) VALUES
    ('Milky Way', 13.6, 2, 100000),
    ('Andromeda', 13.2, 2, 110000),
    ('Triangulum', 1.2, 2, 7000);

INSERT INTO StarSystem (name, age, radius, galaxy_id) VALUES
    ('Solar System', 4.6, 1, 1),
    ('Alpha Centauri', 4.85, 1, 1),
    ('Proxima Centauri', 4.85, 1, 1);

INSERT INTO Planet (name, age, radius, mass, habitable, system_id) VALUES
    ('Earth', 4.6, 6371, 5.97219, 1, 1),
    ('Mars', 4.6, 3389, 0.64171, 0, 1),
    ('Venus', 4.6, 6052, 4.8675, 0, 1);

INSERT INTO Star (name, temperature, age, radius, mass, system_id) VALUES
    ('Sun', 5778, 4.6, 696340, 1989000, 1),
    ('Proxima Centauri', 3050, 4.85, 196500, 0.123, 3);
