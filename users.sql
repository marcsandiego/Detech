-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 29, 2021 at 09:04 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `detech`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `name` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `confirm_password` varchar(30) NOT NULL,
  `store_name` varchar(50) NOT NULL DEFAULT 'Name of the store',
  `store_type` varchar(30) NOT NULL DEFAULT 'Type of store',
  `address` varchar(50) NOT NULL DEFAULT 'N/A',
  `city` varchar(30) NOT NULL DEFAULT 'N/A',
  `country` varchar(30) NOT NULL DEFAULT 'N/A'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`name`, `username`, `email`, `password`, `confirm_password`, `store_name`, `store_type`, `address`, `city`, `country`) VALUES
('marclsd', 'admin', 'marclsandiego23@gmail.com', '', '', '', '', '', '', ''),
('marcs', '', '1@gmail.com', 'admin111', 'admin111', '', '', '', '', ''),
('marc', '123', '123@gmail.com', 'admins123', 'admins123', '', '', '', '', ''),
('marc', '1', '12@gmail.com', 'admin12345', 'admin12345', '', '', '', '', ''),
('marc sandiego', '', 'mlsd@gmail.com', 'admin123', 'admin123', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('addasd', '', '21@gmail.com', 'sandiego082399', 'sandiego082399', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('addasd', '', '123456@gmail.com', 'sandiego082399', 'sandiego082399', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('mich', 'mich', 'mich@gmail.com', '', '', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('Marc lawrence', 'marc', 'mc@gmail.com', '', '', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('dasdasdas', '', 'admin12345@gmail.com', 'admin12345', 'admin12345', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('marc', '', 'admin01@gmail.com', 'admin01', 'admin01', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('marco123', '', 'marco123@gmail.com', 'marco123', 'marco123', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A'),
('msar', '', 'msar@g.com', 'msar', 'msar', 'Name of the store', 'Type of store', 'N/A', 'N/A', 'N/A');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
