from src.db.database import get_connection

def save_prediction(data, score, is_fraud):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions (user_id, amount, fraud_score, is_fraud)
        VALUES (%s, %s, %s, %s)
        """,
        (data.user_id, data.amount, score, is_fraud)
    )

    conn.commit()
    cursor.close()
    conn.close()
    