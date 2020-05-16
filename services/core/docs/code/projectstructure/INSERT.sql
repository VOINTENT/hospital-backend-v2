INSERT INTO service_category(name) VALUES
('Диагностика'),
('Анализы'),
('Похороны');

INSERT INTO service(service_category_id, name) VALUES
(_, 'Первичный осмотр'),
(_, 'Вторичный осмотр'),
(_, 'Процедура лечения'),
(_, 'Закопать, чтоб не мучился'),


INSERT INTO doctor(first_name, last_name, middle_name, gender, specialty_id, department_id) VALUES
('Иванов', 'Иван', 'Иванович', 1, _, _),
('Петров', 'Петр', 'Петрович', 1, _, _),

('Сергеев', 'Сергей', 'Сергеевич', 1, _, _),
('Викторов', 'Виктор', 'Викторович', 1, _, _),

('Денисов', 'Денис', 'Денисович', 1, _, _),
('Васильев', 'Василий', 'Васисльевич', 1, _, _);


INSERT INTO doctor_service(doctor_id, service_id) VALUES
(_, _),
(_, _),
(_, _),
(_, _),
(_, _),
(_, _),