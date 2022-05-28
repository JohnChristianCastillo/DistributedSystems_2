CREATE TABLE groupsTable(
    group_name VARCHAR,
    owner_username VARCHAR,
    PRIMARY KEY (group_name)
);
CREATE TABLE members(
    group_name VARCHAR,
    member_name VARCHAR,
    FOREIGN KEY (group_name) REFERENCES groupsTable(group_name)
);
INSERT INTO groupsTable values ('TimmyG', 'TG');
INSERT INTO members values('TimmyG', 'John');