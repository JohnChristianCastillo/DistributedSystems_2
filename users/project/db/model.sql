CREATE TABLE users(
    user_name VARCHAR,
    user_password VARCHAR,
    PRIMARY KEY (user_name)
);
CREATE TABLE friends(
    user_name VARCHAR,
    friend_name VARCHAR,
    FOREIGN KEY (user_name) REFERENCES users(user_name),
    FOREIGN KEY (friend_name) REFERENCES users(user_name)


);
INSERT INTO users values ('1', '1');