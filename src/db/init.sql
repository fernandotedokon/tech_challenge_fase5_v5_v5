CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    amount FLOAT,
    fraud_score FLOAT,
    is_fraud BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
