-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-08-2024 a las 08:09:58
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `personal_finances`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `category`
--

CREATE TABLE `category` (
  `category_id` smallint(3) NOT NULL,
  `category_name` varchar(50) DEFAULT NULL,
  `category_description` varchar(120) DEFAULT NULL,
  `category_status` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `category`
--

INSERT INTO `category` (`category_id`, `category_name`, `category_description`, `category_status`) VALUES
(1, 'Salario', 'Mi salario mensual en mi trabajo', 1),
(2, 'Arriendo', 'Pago por servicios de arriendo', 1),
(3, 'Comida', 'alimentacion diaria', 1),
(32, 'Entretenimiento', 'diversion', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modules`
--

CREATE TABLE `modules` (
  `module_name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `modules`
--

INSERT INTO `modules` (`module_name`) VALUES
('roles'),
('transacciones'),
('usuarios');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permissions`
--

CREATE TABLE `permissions` (
  `rol_name` varchar(15) NOT NULL,
  `module_name` varchar(15) NOT NULL,
  `p_select` tinyint(1) DEFAULT 1,
  `p_insert` tinyint(1) DEFAULT 1,
  `p_update` tinyint(1) DEFAULT 1,
  `p_delete` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `permissions`
--

INSERT INTO `permissions` (`rol_name`, `module_name`, `p_select`, `p_insert`, `p_update`, `p_delete`) VALUES
('Admin', 'roles', 0, 0, 0, 0),
('Admin', 'transacciones', 1, 1, 0, 0),
('Admin', 'usuarios', 1, 1, 0, 0),
('Cliente', 'roles', 0, 0, 0, 0),
('Cliente', 'transacciones', 1, 1, 1, 1),
('Cliente', 'usuarios', 0, 0, 0, 0),
('SuperAdmin', 'roles', 1, 1, 1, 1),
('SuperAdmin', 'transacciones', 1, 1, 0, 0),
('SuperAdmin', 'usuarios', 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `rol_name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`rol_name`) VALUES
('Admin'),
('Cliente'),
('Super Admin'),
('SuperAdmin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transactions`
--

CREATE TABLE `transactions` (
  `transactions_id` int(10) UNSIGNED NOT NULL,
  `user_id` char(30) DEFAULT NULL,
  `category_id` smallint(3) DEFAULT NULL,
  `amount` float(10,2) DEFAULT NULL,
  `t_description` varchar(120) DEFAULT NULL,
  `t_type` enum('revenue','expenses') DEFAULT NULL,
  `t_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `user_id` char(30) NOT NULL,
  `full_name` varchar(80) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `passhash` varchar(140) DEFAULT NULL,
  `user_role` varchar(15) DEFAULT NULL,
  `user_status` tinyint(1) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`user_id`, `full_name`, `mail`, `passhash`, `user_role`, `user_status`, `created_at`, `updated_at`) VALUES
('831361cIb17YWnadqfOhJkK2kwRQe6', 'Maribel Obando', 'maribel@gmail.com', '$2b$12$xVePF0W7EK8DLnWwNzygTewluxj5fG82BM2M6L31S7hbsEj4pXGvO', 'SuperAdmin', 1, '2024-08-20 04:23:38', '2024-08-19 23:23:38'),
('9sRDlfqsGAZLyMLemwjR76Ek670ZC7', 'Miguel Angel', 'miguelito@gmail.com', '$2b$12$JazJo4nvHfrEnw14KXjgGu397kbi6tQnp/R0XWi4VDFnzrNIgjENa', 'Admin', 1, '2024-08-20 04:26:43', '2024-08-19 23:26:43'),
('fxMbFnLSoWfDkQ3qgyyR2OVCoV777G', 'Vanesa Ortega', 'vanesa@gmail.com', '$2b$12$OzGAmqRVudDcDJAO5Ox4wubUGxFACU0h4mHq4J2xJXTEU2aOHhD92', 'Cliente', 1, '2024-08-20 04:27:25', '2024-08-19 23:27:25'),
('p0opfX13aQO0trgjvll48jNhIHGUPY', 'Jenifer Lopez', 'lopezjen@gmail.com', '$2b$12$p0gDv6KDFwMckMdFZwklSusbp89wIBtpHZPCCpo8G1eT7SUy90fXO', 'Cliente', 1, '2024-08-20 04:30:21', '2024-08-19 23:30:21'),
('PM7AQ14zUbruOjHyR7WCNwHQ3sRHZL', 'Valeria Carvajal', 'vale02@gmail.com', '$2b$12$TaGXQ0dAPrVmOrj6xf5Eg.OdQY5wRVKU1eakE1TYXRcPUjZKx3iRm', 'Cliente', 1, '2024-08-20 04:29:42', '2024-08-19 23:29:42'),
('TrreYlVRWzV0zbTFHBrJ4uZT1D4usd', 'Sebastian Usma', 'usma2024@gmail.com', '$2b$12$kVVN3ouSqlP1QrPKQEmKNezT1nQMMUaUCOM8lkO3DxGa7I7Vd87.S', 'Admin', 1, '2024-08-20 04:25:58', '2024-08-19 23:25:58');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indices de la tabla `modules`
--
ALTER TABLE `modules`
  ADD PRIMARY KEY (`module_name`);

--
-- Indices de la tabla `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`rol_name`,`module_name`),
  ADD KEY `module_name` (`module_name`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`rol_name`);

--
-- Indices de la tabla `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`transactions_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `mail` (`mail`),
  ADD KEY `user_role` (`user_role`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `category`
--
ALTER TABLE `category`
  MODIFY `category_id` smallint(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `transactions`
--
ALTER TABLE `transactions`
  MODIFY `transactions_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `permissions`
--
ALTER TABLE `permissions`
  ADD CONSTRAINT `permissions_ibfk_1` FOREIGN KEY (`rol_name`) REFERENCES `roles` (`rol_name`),
  ADD CONSTRAINT `permissions_ibfk_2` FOREIGN KEY (`module_name`) REFERENCES `modules` (`module_name`);

--
-- Filtros para la tabla `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`);

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_role`) REFERENCES `roles` (`rol_name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
