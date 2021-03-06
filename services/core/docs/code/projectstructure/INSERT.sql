INSERT INTO service_category(name) VALUES
('Диагностика'),
('Анализы'),
('Лечение');

INSERT INTO service(service_category_id, name) VALUES
(1, 'Первичный осмотр'),
(1, 'Вторичный осмотр'),
(1, 'Процедура лечения'),
(2, 'Сдача анализов'),
(3, 'Медицинские процедуры'),


INSERT INTO doctor(first_name, last_name, middle_name, gender) VALUES
('Иванов', 'Иван', 'Иванович', 1),
('Петров', 'Петр', 'Петрович', 1),

('Сергеев', 'Сергей', 'Сергеевич'),
('Викторов', 'Виктор', 'Викторович'),

('Денисов', 'Денис', 'Денисович', 1),
('Васильев', 'Василий', 'Васисльевич', 1);


INSERT INTO doctor_service(doctor_id, service_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 1);


INSERT INTO reception_plan(service_id, doctor_id, date) VALUES
(1, 1, '2020-06-18'),
(2, 2, '2020-06-18'),
(3, 3, '2020-06-18'),
(4, 4, '2020-06-18'),
(5, 5, '2020-06-18'),
(1, 6, '2020-06-18');


INSERT INTO reception_line(reception_plan_id, time) VALUES
(2, '08:00'),
(2, '08:30'),
(2, '09:00'),
(2, '09:30'),
(2, '10:00'),
(2, '10:30'),
(2, '11:00'),
(2, '11:30');