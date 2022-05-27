CREATE TABLE groups(
    group_name VARCHAR,
    owner_username VARCHAR,
    PRIMARY KEY (group_name)
);
CREATE TABLE members(
    group_name VARCHAR references groups(group_name),
    member_name VARCHAR,
    PRIMARY KEY (group_name)
);
INSERT INTO groups values ('TimmyG', 'TG');
INSERT INTO members values('TimmyG', 'John');