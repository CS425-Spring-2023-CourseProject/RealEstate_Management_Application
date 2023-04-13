CREATE TABLE House (
    property_id SERIAL PRIMARY KEY,
    location VARCHAR(255),
    number_of_rooms INT,
    square_footage INT,
    neighborhood_id INT REFERENCES Neighborhood(neighborhood_id) ON DELETE SET NULL
);

CREATE TABLE Apartment (
    property_id SERIAL PRIMARY KEY,
    location VARCHAR(255),
    number_of_rooms INT,
    square_footage INT,
    building_type VARCHAR(255)
);

CREATE TABLE Commercial_Building (
    property_id SERIAL PRIMARY KEY,
    location VARCHAR(255),
    square_footage INT,
    business_type VARCHAR(255),
    neighborhood_id INT REFERENCES Neighborhood(neighborhood_id) ON DELETE SET NULL
);

CREATE TABLE Vacation_Home (
    property_id SERIAL PRIMARY KEY,
    location VARCHAR(255)
);

CREATE TABLE Land (
    property_id SERIAL PRIMARY KEY,
    location VARCHAR(255)
);

CREATE TABLE Property (
    property_id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    description TEXT,
    city VARCHAR(255),
    credit_card_id INT REFERENCES Credit_Card(card_id) ON DELETE SET NULL,
    state VARCHAR(255),
    address_id INT REFERENCES Address(address_id) ON DELETE SET NULL,
    availability DATE
);

CREATE TABLE Price (
    property_id INT PRIMARY KEY REFERENCES Property(property_id) ON DELETE CASCADE,
    rental_price DECIMAL(10, 2)
);

CREATE TABLE Booking (
    booking_id SERIAL PRIMARY KEY,
    email VARCHAR(255) REFERENCES User(email) ON DELETE CASCADE,
    property_id INT REFERENCES Property(property_id) ON DELETE CASCADE,
    start_date DATE,
    end_date DATE
);

CREATE TABLE Neighborhood (
    neighborhood_id SERIAL PRIMARY KEY,
    crime_rate DECIMAL(5, 2),
    nearby_schools INT
);

CREATE TABLE Address (
    address_id SERIAL PRIMARY KEY,
    line_1 VARCHAR(255),
    line_2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(255)
);

CREATE TABLE User (
    email VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    preferred_Location_id INT REFERENCES Neighborhood(neighborhood_id) ON DELETE SET NULL
);

CREATE TABLE RenterAddress (
    property_id INT REFERENCES Property(property_id) ON DELETE CASCADE,
    email VARCHAR(255) REFERENCES User(email) ON DELETE CASCADE,
    address_id INT REFERENCES Address(address_id) ON DELETE SET NULL
);

CREATE TABLE Agent (
    email VARCHAR(255) PRIMARY KEY REFERENCES User(email) ON DELETE CASCADE,
    job_title VARCHAR(255),
    agency_name VARCHAR(255),
    contact_info VARCHAR(255)
);

CREATE TABLE PerspectiveRenter (
    email VARCHAR(255) PRIMARY KEY REFERENCES User(email) ON DELETE CASCADE,
    move_in_date DATE,
    budget DECIMAL(10, 2),
    preferred_location_id INT REFERENCES Neighborhood(neighborhood_id) ON DELETE SET NULL,
    reward_points INT
);

CREATE TABLE Credit_Card (
    card_id SERIAL PRIMARY KEY,
    email VARCHAR(255) REFERENCES User(email) ON DELETE CASCADE,
    payment_address_id INT REFERENCES Address(address_id) ON DELETE SET NULL
);

CREATE TABLE CreditCardUserAddress (
    card_id INT REFERENCES Credit_Card(card_id) ON DELETE CASCADE,
    address_id INT REFERENCES Address(address_id) ON DELETE CASCADE,
    payment_address BOOLEAN
);

CREATE TABLE Reward_Program (
    email VARCHAR(255) REFERENCES User(email) ON DELETE CASCADE,
    rental_price DECIMAL(10, 2) REFERENCES Price(rental_price)
);

CREATE TABLE Payment (
    payment_id SERIAL PRIMARY KEY,
    property_id INT REFERENCES Property(property_id) ON DELETE CASCADE,
    card_id INT REFERENCES Credit_Card(card_id) ON DELETE CASCADE,
    address_id INT REFERENCES Address(address_id) ON DELETE CASCADE,
    amount NUMERIC(10, 2) NOT NULL,
    payment_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE Booking (
    booking_id SERIAL PRIMARY KEY,
    email VARCHAR(320) REFERENCES PerspectiveRenter(email) ON DELETE CASCADE,
    property_id INT REFERENCES Property(property_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    payment_id INT REFERENCES Payment(payment_id) ON DELETE CASCADE
);

CREATE TABLE Reward_Program (
    email VARCHAR(320) PRIMARY KEY REFERENCES PerspectiveRenter(email) ON DELETE CASCADE,
    rental_price INT NOT NULL REFERENCES Price(price_id) ON DELETE CASCADE
);

CREATE TABLE CreditCardUserAddress (
    card_id INT REFERENCES Credit_Card(card_id) ON DELETE CASCADE,
    address_id INT REFERENCES Address(address_id) ON DELETE CASCADE,
    payment_address BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (card_id, address_id)
);
