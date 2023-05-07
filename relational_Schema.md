-- Users
CREATE TABLE users (
  email VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  phone_number VARCHAR(50),
  address_id INTEGER
);

-- Addresses
CREATE TABLE addresses (
  address_id SERIAL PRIMARY KEY,
  email VARCHAR(255) REFERENCES users(email),
  line_1 VARCHAR(255) NOT NULL,
  line_2 VARCHAR(255),
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255),
  zip_code VARCHAR(50),
  neighborhood_id INTEGER
);

-- Neighborhoods
CREATE TABLE neighborhoods (
  neighborhood_id SERIAL PRIMARY KEY,
  crime_rate FLOAT,
  nearby_schools TEXT
);

-- Agents
CREATE TABLE agents (
  email VARCHAR(255) PRIMARY KEY REFERENCES users(email),
  job_title VARCHAR(255) NOT NULL,
  agency VARCHAR(255) NOT NULL
);

-- Perspective Renters
CREATE TABLE perspective_renters (
  email VARCHAR(255) PRIMARY KEY REFERENCES users(email),
  move_in_date DATE,
  budget DECIMAL(10,2),
  pref_neighborhood_id INTEGER REFERENCES neighborhoods(neighborhood_id)
);

-- Reward Program
CREATE TABLE reward_program (
  email VARCHAR(255) PRIMARY KEY REFERENCES users(email),
  reward_points INTEGER
);

-- Credit Cards
CREATE TABLE credit_cards (
  card_id SERIAL PRIMARY KEY,
  email VARCHAR(255) REFERENCES users(email),
  payment_address INTEGER REFERENCES addresses(address_id)
);

-- Properties
CREATE TABLE properties (
  property_id SERIAL PRIMARY KEY,
  type VARCHAR(255) NOT NULL,
  description TEXT,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255),
  address_id INTEGER REFERENCES addresses(address_id),
  availability BOOLEAN NOT NULL,
  neighborhood_id INTEGER REFERENCES neighborhoods(neighborhood_id),
  agent_email VARCHAR(255) REFERENCES agents(email),
  square_footage INTEGER
);

-- Prices
CREATE TABLE prices (
  property_id INTEGER PRIMARY KEY REFERENCES properties(property_id),
  rental_price DECIMAL(10,2) NOT NULL
);

-- Bookings
CREATE TABLE bookings (
  booking_id SERIAL PRIMARY KEY,
  email VARCHAR(255) REFERENCES users(email),
  property_id INTEGER REFERENCES properties(property_id),
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  card_id INTEGER REFERENCES credit_cards(card_id)
);

-- Houses
CREATE TABLE houses (
  property_id INTEGER PRIMARY KEY REFERENCES properties(property_id),
  num_of_rooms INTEGER NOT NULL
);

-- Apartments
CREATE TABLE apartments (
  property_id INTEGER PRIMARY KEY REFERENCES properties(property_id),
  num_of_rooms INTEGER NOT NULL,
  building_type VARCHAR(255) NOT NULL
);

-- Commercial Buildings
CREATE TABLE commercial_buildings (
  property_id INTEGER PRIMARY KEY REFERENCES properties(property_id),
  business_type VARCHAR(255) NOT NULL
);

-- Vacation Homes
CREATE TABLE vacation_homes (
  property_id INTEGER PRIMARY KEY REFERENCES properties(property_id),
  neighborhood_id INTEGER REFERENCES neighborhoods(neighborhood_id)
);

-- Land
CREATE TABLE land (
  property_id INTEGER PRIMARY KEY REFERENCES properties(property_id),
  neighborhood_id INTEGER REFERENCES neighborhoods(neighborhood_id)
);

-- Indexes
CREATE INDEX idx_users_address ON users(address_id);
CREATE INDEX idx_addresses_neighborhood ON addresses(neighborhood_id);
CREATE INDEX idx_pr_neighborhood ON perspective_renters(pref_neighborhood_id);
CREATE INDEX idx_properties_neighborhood ON properties(neighborhood_id);
CREATE INDEX idx_properties_agent ON properties(agent_email);
CREATE INDEX idx_prices_property ON prices(property_id);
CREATE INDEX idx_bookings_email ON bookings(email);
CREATE INDEX idx_bookings_property ON bookings(property_id);
CREATE INDEX idx_bookings_card ON bookings(card_id);
