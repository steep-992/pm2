CREATE DATABASE IF NOT EXISTS flask_app;
USE flask_app;




CREATE TABLE IF NOT EXISTS roles (
                                     id INT PRIMARY KEY AUTO_INCREMENT,
                                     name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS permissions (
                                           id INT PRIMARY KEY AUTO_INCREMENT,
                                           name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS roles_permissions (
                                                 role_id INT,
                                                 permission_id INT,
                                                 PRIMARY KEY (role_id, permission_id),
                                                 FOREIGN KEY (role_id) REFERENCES roles(id),
                                                 FOREIGN KEY (permission_id) REFERENCES permissions(id)
);


CREATE TABLE IF NOT EXISTS users (
                                     id INT PRIMARY KEY AUTO_INCREMENT,
                                     username VARCHAR(50) NOT NULL UNIQUE,
                                     email VARCHAR(100) NOT NULL UNIQUE,
                                     role_id INT,
                                     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                                     FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE IF NOT EXISTS logs (
                                    id INT PRIMARY KEY AUTO_INCREMENT,
                                    user_id INT,
                                    action VARCHAR(100),
                                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                                    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO roles (name) VALUES ('admin')

INSERT INTO permissions (name) VALUES ('view_users'), ('create_user');

INSERT INTO roles_permissions (role_id, permission_id) VALUES
                                                           (1,1),
                                                           (1,2)