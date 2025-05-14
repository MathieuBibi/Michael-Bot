CREATE TABLE IF NOT EXISTS USER_POINTS (
    user_id PRIMARY KEY,
    message_points DEFAULT 0 NOT NULL, seniority_points DEFAULT 0 NOT NULL, activity_points DEFAULT 0 NOT NULL,
    date_joined NOT NULL, 
    contribution_points DEFAULT 0 NOT NULL,
    bias_points DEFAULT 0 NOT NULL);