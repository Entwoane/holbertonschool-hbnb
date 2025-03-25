CREATE TABLE Users(
    id CHAR(36), PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE Places(
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    owner_id CHAR(36)
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE Reviews(
    id CHAR(36),
    text TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36),
    place_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (place_id) REFERENCES Places(id),
    UNIQUE (user_id, place_id)
);

CREATE TABLE Amenities(
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE Place_Amenity(
    place_id CHAR(36),
    amenity_id CHAR(36),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id),
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id)
);