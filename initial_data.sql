INSERT INTO Users (
    id,
    email,
    first_name,
    last_name,
    password,
    is_admin
)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'admin@hbnb.io',
    'Admin',
    'HBnB',
    '$2y$10$4OcyuUIeMRjh2cjF3ullvOQrrCUqvBVhaOOS81xkj6htGPwiM7qeW',
    TRUE
);

INSERT INTO Amenities (id, name)
VALUES 
('59fd8144-c77a-4c02-b988-8cbb7e9cbbf8', 'WiFi'),
('30397e84-5462-4bf8-bb00-f8475d2719af', 'Swimming Pool'),
('d73311c6-4735-4299-9f2d-ca5c7d87ebad', 'Air Conditioning');
