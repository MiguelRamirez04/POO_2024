-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 09-08-2024 a las 16:16:56
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agencia_autos_datos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autos`
--

CREATE TABLE `autos` (
  `matricula` varchar(7) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `modelo` int(4) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  `nif` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `autos`
--

INSERT INTO `autos` (`matricula`, `marca`, `modelo`, `color`, `nif`) VALUES
('GAB0001', 'nissan', 2004, 'ROJO', 4),
('GAB0002', 'NISSAN', 2005, 'NEGRO', 4),
('GAF0001', 'VOLKSWAGEN', 2000, 'ROJO', 1),
('NFA0001', 'VOLKSWAGEN', 2001, 'NEGRO', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `nif` int(5) NOT NULL,
  `nombre` varchar(60) DEFAULT 'Escribe aqui el nombre',
  `direccion` varchar(60) DEFAULT NULL,
  `ciudad` varchar(20) DEFAULT NULL,
  `tel` bigint(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`nif`, `nombre`, `direccion`, `ciudad`, `tel`) VALUES
(1, 'MANUEL PEREZ', 'EDUARDO MARTINEZ #300', 'SANTIAGO', 6181001010),
(2, 'DANIEL GUZMAN', 'COL. CENTRO S/N', 'DURANGO', 6181001011),
(3, 'DAVID HERNANDEZ', 'COL. MADERO S/N', 'LERDO', 6181001012),
(4, 'LUIS GUZMAN', 'COL. CENTRO S/N', 'DURANGO', 6181001013),
(5, 'TOMAS GOMEZ', 'COL. CENTRO S/N', 'SANTIAGO', 6181001014);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `revisiones`
--

CREATE TABLE `revisiones` (
  `no_revision` int(5) NOT NULL,
  `cambiofiltro` varchar(1) DEFAULT NULL,
  `cambioaceite` varchar(1) DEFAULT NULL,
  `cambiofrenos` varchar(1) DEFAULT NULL,
  `otros` varchar(60) DEFAULT NULL,
  `matricula` varchar(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `revisiones`
--

INSERT INTO `revisiones` (`no_revision`, `cambiofiltro`, `cambioaceite`, `cambiofrenos`, `otros`, `matricula`) VALUES
(10001, 'S', 'S', 'N', 'ROTACION DE LLANTAS', 'GAB0001'),
(10002, 'N', 'S', 'N', 'ROTACIÓN DE LLANTAS', 'GAB0001'),
(10003, 'N', 'N', 'N', 'REVISIÓN DE NIVELES', 'GAB0001');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autos`
--
ALTER TABLE `autos`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `nif` (`nif`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`nif`);

--
-- Indices de la tabla `revisiones`
--
ALTER TABLE `revisiones`
  ADD PRIMARY KEY (`no_revision`),
  ADD KEY `matricula` (`matricula`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `autos`
--
ALTER TABLE `autos`
  ADD CONSTRAINT `fk_clientes_autos` FOREIGN KEY (`nif`) REFERENCES `clientes` (`nif`);

--
-- Filtros para la tabla `revisiones`
--
ALTER TABLE `revisiones`
  ADD CONSTRAINT `fk_autos_revisiones` FOREIGN KEY (`matricula`) REFERENCES `autos` (`matricula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
