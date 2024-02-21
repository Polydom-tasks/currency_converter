CREATE TABLE IF NOT EXISTS currencies (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    code CHAR(3) NOT NULL UNIQUE,
    rate NUMERIC(10, 2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO currencies (name, code, rate) VALUES
    ('US Dollar', 'USD', 1.00),
    ('Euro', 'EUR', 0.89),
    ('British Pound', 'GBP', 0.77),
    ('Japanese Yen', 'JPY', 109.79),
    ('Canadian Dollar', 'CAD', 1.28);