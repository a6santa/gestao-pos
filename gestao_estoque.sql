CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255),
  `password` varchar(255),
  `name` varchar(255),
  `email` varchar(255),
  `permission` enum('admin','operator'),
  `created_at` timestamp,
  `update_at` timestamp,
  `status` boolean
);

CREATE TABLE `supplier` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `document` varchar(255),
  `address` varchar(255),
  `number` int,
  `city` varchar(255),
  `state` varchar(2),
  `zip_code` varchar(14),
  `created_at` timestamp,
  `updated_at` timestamp,
  `status` boolean,
  `register_by` varchar(255)
);

CREATE TABLE `customer` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `source_id` varchar(255),
  `source` varchar(255),
  `name` varchar(255),
  `address` varchar(255),
  `number` int,
  `city` varchar(255),
  `state` varchar(2),
  `zip_code` varchar(14),
  `register_by` varchar(255)
);

CREATE TABLE `terminal` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `brand` varchar(255),
  `model` varchar(255),
  `terminal_type_id` int,
  `supplier_id` int,
  `serial_number` varchar(255),
  `status` boolean,
  `terminal_state_id` int,
  `purchase_price` decimal,
  `created_at` timestamp,
  `update_at` timestamp,
  `register_by` varchar(255)
);

CREATE TABLE `terminal_state` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `register_by` varchar(255)
);

CREATE TABLE `terminal_type` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `register_by` varchar(255)
);

CREATE TABLE `terminal_movement` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `terminal_id` int,
  `customer_id` int,
  `price` decimal,
  `start_date` timestamp,
  `end_date` timestamp,
  `movement_type` enum('venda', 'aluguel','manutenção'),
  `register_by` varchar(255)
);

CREATE TABLE `supplies` (
  `id` int AUTO_INCREMENT,
  `name` varchar(255),
  `brand` varchar(255),
  `supplier_id` int,
  `purchase_price` decimal,
  `qtd` int,
  `created_at` timestamp,
  `update_at` timestamp,
  `register_by` varchar(255),
  PRIMARY KEY (`id`, `name`, `brand`)
);

CREATE TABLE `supplier_movement` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `supplies_id` int,
  `customer_id` int,
  `created_at` timestamp,
  `qtd` int,
  `price` decimal,
  `register_by` varchar(255)
);

ALTER TABLE `terminal` ADD FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`);

ALTER TABLE `terminal` ADD FOREIGN KEY (`terminal_state_id`) REFERENCES `terminal_state` (`id`);

ALTER TABLE `terminal` ADD FOREIGN KEY (`terminal_type_id`) REFERENCES `terminal_type` (`id`);

ALTER TABLE `terminal_movement` ADD FOREIGN KEY (`terminal_id`) REFERENCES `terminal` (`id`);

ALTER TABLE `terminal_movement` ADD FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

ALTER TABLE `supplies` ADD FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`);

ALTER TABLE `supplier_movement` ADD FOREIGN KEY (`supplies_id`) REFERENCES `supplies` (`id`);

ALTER TABLE `supplier_movement` ADD FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

