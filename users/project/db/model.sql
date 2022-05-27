CREATE TABLE users(
    user_name VARCHAR,
    user_password VARCHAR,
    PRIMARY KEY (user_name)
);
CREATE TABLE friends(
    user_name VARCHAR references users(user_name),
    friend_name VARCHAR references users(user_name),
    PRIMARY KEY (user_name)
);
INSERT INTO users values ('1', '1');