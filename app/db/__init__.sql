-- This script will be executed when the MySQL container first starts.
-- It ensures the database and table exist.

-- Note: The database is created via environment variables in docker-compose.yml
-- CREATE DATABASE IF NOT EXISTS telemetry_db;
-- USE telemetry_db;

-- Create the main table for storing telemetry data
CREATE TABLE IF NOT EXISTS telemetry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    status VARCHAR(50),
    INDEX idx_device_id (device_id),
    INDEX idx_timestamp (timestamp)
);
