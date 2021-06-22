-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 11, 2019 at 03:26 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grupo19`
--

-- --------------------------------------------------------

--
-- Table structure for table `asistencias`
--

CREATE TABLE `asistencias` (
  `id_taller_asist` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(255) NOT NULL,
  `estudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `asistencias`
--

INSERT INTO `asistencias` (`id_taller_asist`, `fecha`, `estado`, `estudiante`) VALUES
(1, '2019-04-02', '1', 6),
(1, '2019-02-04', '2', 1),
(1, '2019-02-04', '3', 6),
(1, '2019-02-04', '4', 12),
(6, '2019-08-19', '4', 1);

-- --------------------------------------------------------

--
-- Table structure for table `barrio`
--

CREATE TABLE `barrio` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `barrio`
--

INSERT INTO `barrio` (`id`, `nombre`) VALUES
(1, 'Barrio Náutico'),
(2, 'Barrio Obrero'),
(3, 'Berisso'),
(4, 'Barrio Solidaridad'),
(5, 'Barrio Obrero'),
(6, 'Barrio Bco. Pcia.'),
(7, 'Barrio J.B. Justo'),
(8, 'Barrio Obrero'),
(9, 'El Carmen'),
(10, 'El Labrador'),
(11, 'Ensenada'),
(12, 'La Hermosura'),
(13, 'La PLata'),
(14, 'Los Talas'),
(15, 'Ringuelet'),
(16, 'Tolosa'),
(17, 'Villa Alba'),
(18, 'Villa Arguello'),
(19, 'Villa B. C'),
(20, 'Villa Elvira'),
(21, 'Villa Nueva'),
(22, 'Villa Paula'),
(23, 'Villa Progreso'),
(24, 'Villa San Carlos'),
(25, 'Villa Zula');

-- --------------------------------------------------------

--
-- Table structure for table `ciclo_lectivo`
--

CREATE TABLE `ciclo_lectivo` (
  `id` int(11) NOT NULL,
  `fecha_ini` datetime DEFAULT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `semestre` tinyint(1) NOT NULL DEFAULT 1,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `ciclo_lectivo`
--

INSERT INTO `ciclo_lectivo` (`id`, `fecha_ini`, `fecha_fin`, `semestre`, `year`) VALUES
(2, '2019-01-31 00:00:00', '2019-07-12 00:00:00', 1, 2019),
(3, '2019-08-19 00:00:00', '2019-12-20 00:00:00', 2, 2019),
(4, '2020-01-09 00:00:00', '2020-07-15 00:00:00', 1, 2020),
(5, '2021-02-02 00:00:00', '2021-06-25 00:00:00', 1, 2021);

-- --------------------------------------------------------

--
-- Table structure for table `ciclo_lectivo_taller`
--

CREATE TABLE `ciclo_lectivo_taller` (
  `taller_id` int(11) NOT NULL,
  `ciclo_lectivo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `ciclo_lectivo_taller`
--

INSERT INTO `ciclo_lectivo_taller` (`taller_id`, `ciclo_lectivo_id`) VALUES
(1, 2),
(2, 2),
(3, 2),
(4, 2),
(3, 3),
(4, 3),
(2, 4),
(1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `docente`
--

CREATE TABLE `docente` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `localidad_id` int(11) NOT NULL,
  `domicilio` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `genero_id` int(11) DEFAULT NULL,
  `tipo_doc_id` int(11) NOT NULL,
  `numero` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `docente`
--

INSERT INTO `docente` (`id`, `apellido`, `nombre`, `fecha_nac`, `localidad_id`, `domicilio`, `genero_id`, `tipo_doc_id`, `numero`, `tel`, `email`) VALUES
(5, 'Perez', 'Pablo', '1980-05-05', 6, 'Rancho 2554', NULL, 1, '1234567', '0221420333', 'pablo@mail.com'),
(6, 'Fernandez', 'Roberto', '1961-02-05', 12, 'Mitre 1250', NULL, 1, '7654321', '0221420334', 'roberto@mail.com'),
(7, 'Fezor', 'Elpro', '1990-08-12', 2, 'Belgrano 123', NULL, 5, 'ATR12345', '0221420335', 'profe@mail.com'),
(8, 'Juarez', 'Maria', '1930-01-01', 5, 'Mitre 1260', NULL, 3, '12456478790', '0221420336', 'mari@mail.com'),
(9, 'Linder', 'Juana', '1907-02-05', 9, 'Belgrano 2233', NULL, 2, '765432123', '0221420337', 'juana@mail.com');

-- --------------------------------------------------------

--
-- Table structure for table `docente_responsable_taller`
--

CREATE TABLE `docente_responsable_taller` (
  `id_drt` int(11) NOT NULL,
  `docente_id` int(11) NOT NULL,
  `ciclo_lectivo_id` int(11) NOT NULL,
  `taller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `escuela`
--

CREATE TABLE `escuela` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telefono` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `escuela`
--

INSERT INTO `escuela` (`id`, `nombre`, `direccion`, `telefono`) VALUES
(1, '502', NULL, NULL),
(2, 'Albert Thomas', NULL, NULL),
(3, 'Anexa', NULL, NULL),
(4, 'Anexo T. Speroni', NULL, NULL),
(5, 'Basiliana', NULL, NULL),
(6, 'Basiliano', NULL, NULL),
(7, 'Bellas Artes', NULL, NULL),
(8, 'Canossiano', NULL, NULL),
(9, 'Castañeda', NULL, NULL),
(10, 'Col. Nacional', NULL, NULL),
(11, 'Conquista Cristiana', NULL, NULL),
(12, 'Dardo Rocha N° 24', NULL, NULL),
(13, 'E.E.M.N° 2', NULL, NULL),
(14, 'E.M. N°26', NULL, NULL),
(15, 'E.P. Municipal N° 2', NULL, NULL),
(16, 'EE N° 2', NULL, NULL),
(17, 'EEE N° 501', NULL, NULL),
(18, 'EEE N°501', NULL, NULL),
(19, 'EEM N° 1', NULL, NULL),
(20, 'EEM N° 26 L.P', NULL, NULL),
(21, 'EEM N°128', NULL, NULL),
(22, 'EEM N°2', NULL, NULL),
(23, 'EES N° 10', NULL, NULL),
(24, 'EES N° 14', NULL, NULL),
(25, 'EES N° 4', NULL, NULL),
(26, 'EES N° 4 Berisso', NULL, NULL),
(27, 'EES N° 4 El Pino', NULL, NULL),
(28, 'EEST N° 1 bsso', NULL, NULL),
(29, 'EET Nº 1', NULL, NULL),
(30, 'EET Nº1', NULL, NULL),
(31, 'EGB N°25', NULL, NULL),
(32, 'EM N° 2', NULL, NULL),
(33, 'EMM N° 3', NULL, NULL),
(34, 'EP N° 1 L.P-', NULL, NULL),
(35, 'EP N° 11', NULL, NULL),
(36, 'EP N° 129', NULL, NULL),
(37, 'EP N° 14', NULL, NULL),
(38, 'EP N° 15', NULL, NULL),
(39, 'EP N° 17', NULL, NULL),
(40, 'EP N° 18', NULL, NULL),
(41, 'EP N° 19', NULL, NULL),
(42, 'EP N° 2', NULL, NULL),
(43, 'EP N° 20', NULL, NULL),
(44, 'EP N° 22', NULL, NULL),
(45, 'EP N° 25', NULL, NULL),
(46, 'EP N° 27', NULL, NULL),
(47, 'EP N° 3', NULL, NULL),
(48, 'EP N° 37 LP', NULL, NULL),
(49, 'EP N° 43', NULL, NULL),
(50, 'EP N° 45', NULL, NULL),
(51, 'EP N° 5', NULL, NULL),
(52, 'EP N° 6', NULL, NULL),
(53, 'EP N° 65 La Plata', NULL, NULL),
(54, 'EP N° 7', NULL, NULL),
(55, 'EPB N° 10', NULL, NULL),
(56, 'EPB N° 14', NULL, NULL),
(57, 'EPB N° 15', NULL, NULL),
(58, 'EPB N° 19', NULL, NULL),
(59, 'EPB N° 2', NULL, NULL),
(60, 'EPB N° 20', NULL, NULL),
(61, 'EPB N° 24', NULL, NULL),
(62, 'EPB N° 25', NULL, NULL),
(63, 'EPB N° 45', NULL, NULL),
(64, 'EPB N° 5', NULL, NULL),
(65, 'EPB N° 55', NULL, NULL),
(66, 'EPB N° 6', NULL, NULL),
(67, 'EPB N° 65', NULL, NULL),
(68, 'EPB N° 8', NULL, NULL),
(69, 'ESB N° 10', NULL, NULL),
(70, 'ESB N° 11', NULL, NULL),
(71, 'ESB N° 14', NULL, NULL),
(72, 'ESB N° 3', NULL, NULL),
(73, 'ESB N° 61', NULL, NULL),
(74, 'ESB N° 66', NULL, NULL),
(75, 'ESB N° 8', NULL, NULL),
(76, 'ESB N° 9', NULL, NULL),
(77, 'ESC N° 10', NULL, NULL),
(78, 'ESC N° 13', NULL, NULL),
(79, 'ESC N° 19', NULL, NULL),
(80, 'ESC N° 2', NULL, NULL),
(81, 'ESC N° 20', NULL, NULL),
(82, 'ESC N° 22', NULL, NULL),
(83, 'ESC N° 23', NULL, NULL),
(84, 'ESC N° 24', NULL, NULL),
(85, 'ESC N° 25', NULL, NULL),
(86, 'ESC N° 27', NULL, NULL),
(87, 'ESC N° 3', NULL, NULL),
(88, 'ESC N° 43', NULL, NULL),
(89, 'ESC N° 45', NULL, NULL),
(90, 'ESC N° 5', NULL, NULL),
(91, 'ESC N° 501', NULL, NULL),
(92, 'ESC N° 6', NULL, NULL),
(93, 'ESC N° 66', NULL, NULL),
(94, 'ESC N° 7', NULL, NULL),
(95, 'ESC N° 8', NULL, NULL),
(96, 'ESC N°11', NULL, NULL),
(97, 'ESC N°17', NULL, NULL),
(98, 'ESC N°19', NULL, NULL),
(99, 'ESC N°3', NULL, NULL),
(100, 'ESC N°7', NULL, NULL),
(101, 'ESC de Arte', NULL, NULL),
(102, 'ESS N° 4', NULL, NULL),
(103, 'Enseñanza Media', NULL, NULL),
(104, 'Especial N° 502', NULL, NULL),
(105, 'Estrada', NULL, NULL),
(106, 'FACULTAD', NULL, NULL),
(107, 'INDUSTRIAL', NULL, NULL),
(108, 'Italiana', NULL, NULL),
(109, 'J 904', NULL, NULL),
(110, 'J. Manuel Strada', NULL, NULL),
(111, 'Jacarandá', NULL, NULL),
(112, 'Jardín Euforion', NULL, NULL),
(113, 'Jardín N° 903', NULL, NULL),
(114, 'Jardín N° 907', NULL, NULL),
(115, 'JoaquinV.Gonzalez', NULL, NULL),
(116, 'Lola Mora sec', NULL, NULL),
(117, 'Lujan Sierra', NULL, NULL),
(118, 'MUNICIOAL 11', NULL, NULL),
(119, 'María Auxiliadora', NULL, NULL),
(120, 'María Reina', NULL, NULL),
(121, 'Media 2 España', NULL, NULL),
(122, 'Media N 1', NULL, NULL),
(123, 'Mercedita de S.Martin', NULL, NULL),
(124, 'Monseñor Alberti', NULL, NULL),
(125, 'Mtro Luis MKEY', NULL, NULL),
(126, 'Mñor. Rasore', NULL, NULL),
(127, 'N1 Francisco', NULL, NULL),
(128, 'Normal 2', NULL, NULL),
(129, 'Normal 3 LP', NULL, NULL),
(130, 'Normal n 2', NULL, NULL),
(131, 'Ntra Sra Lourdes', NULL, NULL),
(132, 'Ntra. Sra. del Valle', NULL, NULL),
(133, 'PSICOLOGIA', NULL, NULL),
(134, 'Parroquial', NULL, NULL),
(135, 'Pasos del Libertedor', NULL, NULL),
(136, 'Ped 61', NULL, NULL),
(137, 'Pedagogica', NULL, NULL),
(138, 'SEC N° 8', NULL, NULL),
(139, 'SEC N°17', NULL, NULL),
(140, 'San Simón', NULL, NULL),
(141, 'Santa Rosa', NULL, NULL),
(142, 'Sra de Fátima', NULL, NULL),
(143, 'Sta Margarita', NULL, NULL),
(144, 'Sta Ro. de Lima', NULL, NULL),
(145, 'Sta Rosa', NULL, NULL),
(146, 'Sta Rosa Lima', NULL, NULL),
(147, 'Sta. R. de Lima', NULL, NULL),
(148, 'Sta. Rosa de lima', NULL, NULL),
(149, 'Técnica N° 1', NULL, NULL),
(150, 'Técnica N° 1 Berisso', NULL, NULL),
(151, 'Técnica N° 5', NULL, NULL),
(152, 'Técnica N° 7', NULL, NULL),
(153, 'UCALP', NULL, NULL),
(154, 'UNLP', NULL, NULL),
(155, 'UTN', NULL, NULL),
(156, 'Universitas', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `estudiante`
--

CREATE TABLE `estudiante` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `localidad_id` int(11) NOT NULL,
  `nivel_id` int(11) NOT NULL,
  `domicilio` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `genero_id` int(11) NOT NULL,
  `escuela_id` int(11) NOT NULL,
  `tipo_doc_id` int(11) NOT NULL,
  `numero` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `barrio_id` int(11) NOT NULL,
  `responsable` int(3) NOT NULL,
  `lugar_nac` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `estudiante`
--

INSERT INTO `estudiante` (`id`, `apellido`, `nombre`, `fecha_nac`, `localidad_id`, `nivel_id`, `domicilio`, `genero_id`, `escuela_id`, `tipo_doc_id`, `numero`, `tel`, `barrio_id`, `responsable`, `lugar_nac`) VALUES
(14, 'Dominguez', 'Martin', '2001-05-20', 2, 1, 'Sarmiento 123', 1, 8, 1, '40342552', '123456', 4, 0, 'Nueve de Julio'),
(15, 'Juarez', 'Carlos', '1998-10-12', 12, 3, 'Cabildo 1234', 1, 7, 1, '9786456456', '0221420441', 14, 1, 'La Matanza'),
(16, 'Miglia', 'Mirtha', '2000-10-29', 3, 4, 'Belgrano 123', 2, 3, 1, '489465132', '1231245', 4, 2, 'Junin'),
(17, 'Sanchez', 'Maca', '1997-09-18', 8, 7, 'Rancho 2554', 3, 12, 1, '46543133', '0221420123', 15, 1, 'Mar del Plata');

-- --------------------------------------------------------

--
-- Table structure for table `estudiante_taller`
--

CREATE TABLE `estudiante_taller` (
  `estudiante_id` int(11) NOT NULL,
  `ciclo_lectivo_id` int(11) NOT NULL,
  `taller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `genero`
--

CREATE TABLE `genero` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `genero`
--

INSERT INTO `genero` (`id`, `nombre`) VALUES
(1, 'Masculino'),
(2, 'Femenino'),
(3, 'Otro');

-- --------------------------------------------------------

--
-- Table structure for table `horarios`
--

CREATE TABLE `horarios` (
  `id` int(11) NOT NULL,
  `taller_responsable` int(11) NOT NULL,
  `nucleo_id` int(11) NOT NULL,
  `dia` int(11) NOT NULL,
  `inicio` time NOT NULL,
  `fin` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `horarios`
--

INSERT INTO `horarios` (`id`, `taller_responsable`, `nucleo_id`, `dia`, `inicio`, `fin`) VALUES
(1, 1, 1, 3, '19:30:10', '20:30:10'),
(2, 5, 1, 1, '14:00:00', '15:00:00'),
(3, 1, 1, 2, '14:00:00', '15:00:00'),
(4, 6, 1, 1, '19:16:00', '19:18:00'),
(5, 1, 1, 1, '19:00:00', '17:00:00'),
(6, 1, 1, 1, '19:00:00', '17:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `informacion`
--

CREATE TABLE `informacion` (
  `titulo` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `contacto` varchar(70) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `cantidadfilas` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `informacion`
--

INSERT INTO `informacion` (`titulo`, `descripcion`, `contacto`, `habilitado`, `cantidadfilas`) VALUES
('Orquesta Escuela de Berisso', 'Descripcion de la Orquesta Escuela de Berisso', 'info@orquestaescuelaberisso.com', 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `instrumento`
--

CREATE TABLE `instrumento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_id` int(11) NOT NULL,
  `n_inventario` int(30) NOT NULL,
  `longitud` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `latitud` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `id_alumno` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `instrumento`
--

INSERT INTO `instrumento` (`id`, `nombre`, `tipo_id`, `n_inventario`, `longitud`, `latitud`, `id_alumno`) VALUES
(290, 'Bateria', 3, 1, ' -57.954769', '-34.921267', 14),
(291, 'Gibson Les Paul', 2, 2, ' -57.942281', '-34.920739', 16),
(292, 'Flauta Traversa', 1, 3, ' -57.947559', '-34.915496', 15);

-- --------------------------------------------------------

--
-- Table structure for table `nivel`
--

CREATE TABLE `nivel` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `nivel`
--

INSERT INTO `nivel` (`id`, `nombre`) VALUES
(1, 'I'),
(2, 'II'),
(3, 'III'),
(4, 'IV'),
(5, 'V'),
(6, 'VI'),
(7, 'VII'),
(8, 'VIII'),
(9, 'IX'),
(10, 'X'),
(11, 'XI'),
(12, 'XII');

-- --------------------------------------------------------

--
-- Table structure for table `nucleo`
--

CREATE TABLE `nucleo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `latitud` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `longitud` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `nucleo`
--

INSERT INTO `nucleo` (`id`, `nombre`, `direccion`, `telefono`, `latitud`, `longitud`) VALUES
(1, 'escuela primaria 7', '151 entre 8 y 9', '2214098345', '-34.883888', '-57.898451'),
(2, 'Escuela Primaria N°6 ', 'Calle 8 y Calle 158', '1234', '-34.876277', '-57.892960'),
(3, 'Escuela Primaria N°6 ', 'Calle 8 y Calle 158', '1234', '-34.876277', '-57.892960'),
(4, 'Escuela Primaria N°8', 'Calle 6 y Calle 125', '1234', '-34.906617', '-57.921674'),
(5, 'Escuela Primaria N°8', 'Calle 6 y Calle 125', '1234', '-34.906617', '-57.921674'),
(6, 'Parroquia San Miguel Arcángel', 'Calle 6 y Calle 124', '1234', '-34.907421', '-57.922068'),
(7, 'Parroquia San Miguel Arcángel', 'Calle 6 y Calle 124', '1234', '-34.907421', '-57.922068'),
(8, 'Escuela Primaria N° 22', 'Calle 32 y Calle 173', '1234', '-34.876491', '-57.855908'),
(9, 'Escuela Primaria N° 22', 'Calle 32 y Calle 173', '1234', '-34.876491', '-57.855908'),
(10, 'Escuela Primaria N° 20', 'Ruta 11 km13 - Pje La Hermosura', '1234', '-34.958005', '-57.817772'),
(11, 'Escuela Primaria N° 20', 'Ruta 11 km13 - Pje La Hermosura', '1234', '-34.958005', '-57.817772');

-- --------------------------------------------------------

--
-- Table structure for table `permiso`
--

CREATE TABLE `permiso` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `permiso`
--

INSERT INTO `permiso` (`id`, `nombre`) VALUES
(1, 'usuario_crear'),
(2, 'usuario_borrar'),
(3, 'usuario_modificar'),
(4, 'usuario_leer'),
(5, 'configuracion_configurar'),
(6, 'estudiante_crear'),
(7, 'estudiante_borrar'),
(8, 'estudiante_show'),
(9, 'estudiante_update'),
(10, 'docente_show'),
(11, 'docente_crear'),
(12, 'docente_borrar'),
(13, 'docente_update'),
(14, 'administrativo_crear'),
(15, 'administrativo_show'),
(16, 'administrativo_borrar'),
(17, 'administrativo_update'),
(18, 'instrumento_crear'),
(19, 'instrumento_update'),
(20, 'instrumento_borrar'),
(21, 'instrumento_show');

-- --------------------------------------------------------

--
-- Table structure for table `preceptor`
--

CREATE TABLE `preceptor` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `preceptor_nucleo`
--

CREATE TABLE `preceptor_nucleo` (
  `preceptor_id` int(11) NOT NULL,
  `nucleo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rol`
--

CREATE TABLE `rol` (
  `id` int(5) NOT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rol`
--

INSERT INTO `rol` (`id`, `nombre`) VALUES
(1, 'administrador'),
(2, 'preceptor'),
(3, 'profesor');

-- --------------------------------------------------------

--
-- Table structure for table `rol_tiene_permiso`
--

CREATE TABLE `rol_tiene_permiso` (
  `rol_id` int(11) NOT NULL,
  `permiso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rol_tiene_permiso`
--

INSERT INTO `rol_tiene_permiso` (`rol_id`, `permiso_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(1, 19),
(1, 20),
(1, 21),
(2, 8),
(2, 9),
(2, 10),
(2, 15),
(2, 21),
(3, 8),
(3, 9),
(3, 10),
(3, 15);

-- --------------------------------------------------------

--
-- Table structure for table `taller`
--

CREATE TABLE `taller` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre_corto` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `taller`
--

INSERT INTO `taller` (`id`, `nombre`, `nombre_corto`) VALUES
(1, 'flauta traverso', 'fla_tra'),
(2, 'clarinete', 'clarin'),
(3, 'oboe', 'obo'),
(4, 'violin', 'violeta');

-- --------------------------------------------------------

--
-- Table structure for table `tipo_instrumento`
--

CREATE TABLE `tipo_instrumento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tipo_instrumento`
--

INSERT INTO `tipo_instrumento` (`id`, `nombre`) VALUES
(1, 'Viento'),
(2, 'Cuerda'),
(3, 'Percusión');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `firstname` varchar(25) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(256) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1,
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`firstname`, `lastname`, `email`, `password`, `activo`, `updated_at`, `created_at`, `id`) VALUES
('Andres', 'Marconi', 'andressandro@gmail.com', '$2b$12$UwORvthnn6FsnTNolxlcZ.g7G48QHoqr.iaWyV0A1SMF84UaDHUbW', 1, '2019-10-29 19:54:10', '2019-10-29 19:54:10', 1),
('Federico', 'Perroni', 'fede@mail.com', '$2b$12$FZG.KCYxGWN4VA1PNfoSn.iH0XgWU8IKYbSzX4PjdQHlp8OXsRq5u', 1, '2019-10-29 21:07:38', '2019-10-29 21:07:38', 2),
('Guillermo', 'Villareal', 'guille@mail.com', '$2b$12$W8a7s00bWsEbmciyVdgyR.lsN1WVR6TypE23e1ojvm3oqwLkvnVGG', 1, '2019-10-29 21:08:10', '2019-10-29 21:08:10', 3),
('Juana', 'Linder', 'juana@mail.com', '$2b$12$34vwcCHyIy2Cb/DX8Z1nEuND7i8kk7m.pB6YGwb02wp4uTe4I9NUO', 1, '2019-12-11 11:00:40', '2019-12-11 11:00:40', 35),
('Maria', 'Juarez', 'mari@mail.com', '$2b$12$EkWjOrPYIkleKkLqR5Kkpe3qMfQ1ohZXPCvGOPAVqibnhvMuSdWr6', 1, '2019-12-11 10:59:38', '2019-12-11 10:59:38', 34),
('Pablo', 'Perez', 'pablo@mail.com', '$2b$12$3Thg4APTbZr0hi39qOJGiuzU9z4jHZWrHRH3aLZRRMpBnCM3/XAie', 1, '2019-12-11 10:56:27', '2019-12-11 10:56:27', 31),
('Elpro', 'Fezor', 'profe@mail.com', '$2b$12$Qt1n1VsHQW.Rtw1p1.VIyutDuMrhESNUyoDf18SJmJ4IpQe2AMtp2', 1, '2019-12-11 10:58:31', '2019-12-11 10:58:31', 33),
('Roberto', 'Fernandez', 'roberto@mail.com', '$2b$12$S8xMLZc0cFkDBnoz7gtLFOKiRkCARhkKXAXjeeD5VeZ.ReelgRJcq', 1, '2019-12-11 10:57:15', '2019-12-11 10:57:15', 32),
('Roberto', 'Sanchez', 'sandro@gitano.com', '$2b$12$gYCsqSUr1bmFdXwYo6K81.Phu1S0zgASNx0Z1GF00L.FkQKPvRaL6', 1, '2019-10-30 14:26:44', '2019-10-30 14:26:44', 22);

-- --------------------------------------------------------

--
-- Table structure for table `usuario_tiene_rol`
--

CREATE TABLE `usuario_tiene_rol` (
  `usuario_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usuario_tiene_rol`
--

INSERT INTO `usuario_tiene_rol` (`usuario_id`, `rol_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(22, 3),
(28, 0),
(28, 3),
(29, 0),
(29, 3),
(31, 0),
(31, 3),
(32, 0),
(32, 3),
(33, 0),
(33, 3),
(34, 0),
(34, 3),
(35, 0),
(35, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barrio`
--
ALTER TABLE `barrio`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ciclo_lectivo`
--
ALTER TABLE `ciclo_lectivo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ciclo_lectivo_taller`
--
ALTER TABLE `ciclo_lectivo_taller`
  ADD PRIMARY KEY (`ciclo_lectivo_id`,`taller_id`),
  ADD KEY `FK_ciclo_lectivo_taller_taller_id` (`taller_id`);

--
-- Indexes for table `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_genero_docente_id` (`genero_id`);

--
-- Indexes for table `docente_responsable_taller`
--
ALTER TABLE `docente_responsable_taller`
  ADD PRIMARY KEY (`id_drt`),
  ADD UNIQUE KEY `docente_id` (`docente_id`,`ciclo_lectivo_id`,`taller_id`) USING BTREE,
  ADD KEY `FK_docente_responsable_taller_ciclo_lectivo_id` (`ciclo_lectivo_id`),
  ADD KEY `FK_docente_responsable_taller_taller_id` (`taller_id`);

--
-- Indexes for table `escuela`
--
ALTER TABLE `escuela`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_nivel_id` (`nivel_id`),
  ADD KEY `FK_genero_estudiante_id` (`genero_id`),
  ADD KEY `FK_escuela_id` (`escuela_id`),
  ADD KEY `FK_barrio_id` (`barrio_id`);

--
-- Indexes for table `estudiante_taller`
--
ALTER TABLE `estudiante_taller`
  ADD PRIMARY KEY (`estudiante_id`,`ciclo_lectivo_id`,`taller_id`),
  ADD KEY `FK_estudiante_taller_ciclo_lectivo_id` (`ciclo_lectivo_id`),
  ADD KEY `FK_estudiante_taller_taller_id` (`taller_id`);

--
-- Indexes for table `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `n_inventario` (`n_inventario`),
  ADD KEY `FK_tipo_instrumento_id` (`tipo_id`);

--
-- Indexes for table `nivel`
--
ALTER TABLE `nivel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nucleo`
--
ALTER TABLE `nucleo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `permiso`
--
ALTER TABLE `permiso`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `preceptor`
--
ALTER TABLE `preceptor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `preceptor_nucleo`
--
ALTER TABLE `preceptor_nucleo`
  ADD PRIMARY KEY (`preceptor_id`,`nucleo_id`),
  ADD KEY `FK_nucleo_id` (`nucleo_id`);

--
-- Indexes for table `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD PRIMARY KEY (`rol_id`,`permiso_id`);

--
-- Indexes for table `taller`
--
ALTER TABLE `taller`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tipo_instrumento`
--
ALTER TABLE `tipo_instrumento`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `usuario_tiene_rol`
--
ALTER TABLE `usuario_tiene_rol`
  ADD PRIMARY KEY (`usuario_id`,`rol_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barrio`
--
ALTER TABLE `barrio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `ciclo_lectivo`
--
ALTER TABLE `ciclo_lectivo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `docente`
--
ALTER TABLE `docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `docente_responsable_taller`
--
ALTER TABLE `docente_responsable_taller`
  MODIFY `id_drt` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `escuela`
--
ALTER TABLE `escuela`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=157;

--
-- AUTO_INCREMENT for table `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `horarios`
--
ALTER TABLE `horarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `instrumento`
--
ALTER TABLE `instrumento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=293;

--
-- AUTO_INCREMENT for table `nivel`
--
ALTER TABLE `nivel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `nucleo`
--
ALTER TABLE `nucleo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `preceptor`
--
ALTER TABLE `preceptor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `taller`
--
ALTER TABLE `taller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tipo_instrumento`
--
ALTER TABLE `tipo_instrumento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ciclo_lectivo_taller`
--
ALTER TABLE `ciclo_lectivo_taller`
  ADD CONSTRAINT `FK_ciclo_lectivo_taller_ciclo_lectivo_id` FOREIGN KEY (`ciclo_lectivo_id`) REFERENCES `ciclo_lectivo` (`id`),
  ADD CONSTRAINT `FK_ciclo_lectivo_taller_taller_id` FOREIGN KEY (`taller_id`) REFERENCES `taller` (`id`);

--
-- Constraints for table `docente`
--
ALTER TABLE `docente`
  ADD CONSTRAINT `FK_genero_docente_id` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`);

--
-- Constraints for table `docente_responsable_taller`
--
ALTER TABLE `docente_responsable_taller`
  ADD CONSTRAINT `FK_docente_responsable_taller_ciclo_lectivo_id` FOREIGN KEY (`ciclo_lectivo_id`) REFERENCES `ciclo_lectivo` (`id`),
  ADD CONSTRAINT `FK_docente_responsable_taller_docente_id` FOREIGN KEY (`docente_id`) REFERENCES `docente` (`id`),
  ADD CONSTRAINT `FK_docente_responsable_taller_taller_id` FOREIGN KEY (`taller_id`) REFERENCES `taller` (`id`);

--
-- Constraints for table `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `FK_barrio_id` FOREIGN KEY (`barrio_id`) REFERENCES `barrio` (`id`),
  ADD CONSTRAINT `FK_escuela_id` FOREIGN KEY (`escuela_id`) REFERENCES `escuela` (`id`),
  ADD CONSTRAINT `FK_genero_estudiante_id` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`),
  ADD CONSTRAINT `FK_nivel_id` FOREIGN KEY (`nivel_id`) REFERENCES `nivel` (`id`);

--
-- Constraints for table `estudiante_taller`
--
ALTER TABLE `estudiante_taller`
  ADD CONSTRAINT `FK_estudiante_taller_ciclo_lectivo_id` FOREIGN KEY (`ciclo_lectivo_id`) REFERENCES `ciclo_lectivo` (`id`),
  ADD CONSTRAINT `FK_estudiante_taller_id` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiante` (`id`),
  ADD CONSTRAINT `FK_estudiante_taller_taller_id` FOREIGN KEY (`taller_id`) REFERENCES `taller` (`id`);

--
-- Constraints for table `instrumento`
--
ALTER TABLE `instrumento`
  ADD CONSTRAINT `FK_tipo_instrumento_id` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_instrumento` (`id`);

--
-- Constraints for table `preceptor_nucleo`
--
ALTER TABLE `preceptor_nucleo`
  ADD CONSTRAINT `FK_nucleo_id` FOREIGN KEY (`nucleo_id`) REFERENCES `nucleo` (`id`),
  ADD CONSTRAINT `FK_preceptor_id` FOREIGN KEY (`preceptor_id`) REFERENCES `preceptor` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
