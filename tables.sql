CREATE TABLE IF NOT EXISTS USER_POINTS (
    user_id PRIMARY KEY,
    message_points, seniority_points, activity_points,
    contribution_points,
    bias_points);