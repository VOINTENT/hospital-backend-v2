CREATE SEQUENCE account_id_seq START 1;
CREATE SEQUENCE patient_id_seq START 1;
CREATE SEQUENCE doctor_id_seq START 1;
CREATE SEQUENCE speciality_id_seq START 1;
CREATE SEQUENCE department_id_seq START 1;
CREATE SEQUENCE cabinet_id_seq START 1;
CREATE SEQUENCE service_id_seq START 1;
CREATE SEQUENCE service_category_id_seq START 1;
CREATE SEQUENCE price_id_seq START 1;
CREATE SEQUENCE reception_plan_id_seq START 1;
CREATE SEQUENCE reception_line_id_seq START 1;
CREATE SEQUENCE register_id_seq START 1;
CREATE SEQUENCE register_out_plan_id_seq START 1;
CREATE SEQUENCE doctor_service_id_seq START 1;
CREATE SEQUENCE doctor_cabinet_seq START 1;

CREATE TABLE account (
    id BIGINT NOT NULL DEFAULT nextval('account_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    email VARCHAR(50) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    is_active BOOLEAN NOT NULL,
    user_type VARCHAR(7) NOT NULL CHECK (user_type = 'patient' or user_type = 'doctor') DEFAULT 'patient'
);

CREATE TABLE speciality (
    id BIGINT NOT NULL DEFAULT nextval('speciality_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE department (
    id BIGINT NOT NULL DEFAULT nextval('department_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE patient (
    id BIGINT NOT NULL DEFAULT nextval('patient_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    account_id BIGINT NOT NULL UNIQUE REFERENCES account(id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    gender SMALLINT NOT NULL CHECK (gender = 1 OR gender = 2 OR gender = 3),
    birth_date timestamp without time zone,
    snils VARCHAR(14) UNIQUE,
    policy VARCHAR(16) UNIQUE
);

CREATE TABLE doctor (
    id BIGINT NOT NULL DEFAULT nextval('doctor_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    account_id BIGINT UNIQUE REFERENCES account(id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    gender SMALLINT NOT NULL CHECK (gender = 1 OR gender = 2 OR gender = 3) DEFAULT 3,
    birth_date timestamp without time zone,
    speciality_id BIGINT REFERENCES speciality(id),
    department_id BIGINT REFERENCES department(id)
);

CREATE TABLE cabinet (
    id BIGINT NOT NULL DEFAULT nextval('cabinet_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    number VARCHAR(10) UNIQUE NOT NULL,
    department_id BIGINT NOT NULL REFERENCES department(id)
);

CREATE TABLE service (
    id BIGINT NOT NULL DEFAULT nextval('service_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    service_category_id BIGINT REFERENCES service_category(id),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    service_time SMALLINT NOT NULL DEFAULT 30
);

CREATE TABLE service_category (
    id BIGINT NOT NULL DEFAULT nextval('service_category_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE price (
    id BIGINT NOT NULL DEFAULT nextval('price_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    service_id BIGINT NOT NULL UNIQUE REFERENCES service(id),
    cost INTEGER NOT NULL DEFAULT 0,
    date_approval timestamp without time zone NOT NULL DEFAULT current_timestamp
);

CREATE TABLE reception_plan (
    id BIGINT NOT NULL DEFAULT nextval('reception_plan_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    service_id BIGINT NOT NULL REFERENCES service(id),
    doctor_id BIGINT NOT NULL REFERENCES doctor(id),
    date DATE NOT NULL
);

CREATE TABLE reception_line (
    id BIGINT NOT NULL DEFAULT nextval('reception_line_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    reception_plan_id BIGINT NOT NULL REFERENCES reception_plan(id),
    time TIME NOT NULL
);

CREATE TABLE register (
    id BIGINT NOT NULL DEFAULT nextval('register_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    reception_line_id BIGINT REFERENCES reception_line(id),
    patient_id BIGINT REFERENCES patient(id)
);

CREATE TABLE register_out_plan (
    id BIGINT NOT NULL DEFAULT nextval('register_out_plan_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    reception_plan_id BIGINT NOT NULL REFERENCES reception_plan(id),
    patient_id BIGINT REFERENCES patient(id),
    time TIME NOT NULL
);

CREATE TABLE doctor_service (
    id BIGINT NOT NULL DEFAULT nextval('doctor_service_id_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    doctor_id BIGINT NOT NULL REFERENCES doctor(id),
    service_id BIGINT NOT NULL REFERENCES service(id)
    CONSTRAINT UNIQUE (doctor_id, service_id)
);

CREATE TABLE doctor_cabinet (
    id BIGINT NOT NULL DEFAULT nextval('doctor_cabinet_seq') PRIMARY KEY,
    created_at timestamp without time zone NOT NULL DEFAULT current_timestamp,
    doctor_id BIGINT NOT NULL REFERENCES doctor(id),
    cabinet_id BIGINT NOT NULL REFERENCES cabinet(id),
    CONSTRAINT UNIQUE (doctor_id, cabinet_id)
);