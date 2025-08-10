CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

CREATE TABLE IF NOT EXISTS telemetry (
  id SERIAL PRIMARY KEY,
  device_id TEXT NOT NULL,
  ts TIMESTAMP WITH TIME ZONE NOT NULL,
  metrics JSONB
);

SELECT create_hypertable('telemetry', 'ts', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS anomalies (
  id SERIAL PRIMARY KEY,
  device_id TEXT,
  ts TIMESTAMP WITH TIME ZONE,
  metric TEXT,
  value NUMERIC,
  details JSONB
);