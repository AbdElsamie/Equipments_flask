-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2023 at 11:40 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jobsdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `equipment_table`
--

CREATE TABLE `equipment_table` (
`id` INT(11) NOT NULL AUTO_INCREMENT ,
`name_equipment` VARCHAR(24) NOT NULL ,
 `type_equipment` VARCHAR(24) NOT NULL ,
  `make_country` VARCHAR(24) NOT NULL ,
   `price` INT(11) NOT NULL ,
    `purpose` VARCHAR(24) NOT NULL ,
     `trainer_name` VARCHAR(24) NOT NULL ,
      `class_name` VARCHAR(24) NOT NULL , 
      `room` INT(11) NOT NULL , 
      `time_of_class` VARCHAR(24) NOT NULL , 
      PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
