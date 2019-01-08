-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: localhost
-- 產生時間： 2018 年 12 月 14 日 09:50
-- 伺服器版本: 10.1.23-MariaDB-9+deb9u1
-- PHP 版本： 7.0.30-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `mydatabase`
--

-- --------------------------------------------------------

--
-- 資料表結構 `rfid`
--

CREATE TABLE `rfid` (
  `id` int(20) UNSIGNED NOT NULL,
  `name` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `rfid`
--

INSERT INTO `rfid` (`id`, `name`, `date`, `time`) VALUES
(1, '333', '', '0000-00-00 00:00:00'),
(2, 'lala', '2018-10-10', '12:23:50'),
(3, '111', '222', '333'),
(4, '', 'None', ''),
(5, '123', 'None', '567'),
(6, '787', '2018/12/6', '999'),
(7, '', '2018/12/6', '15:41:37'),
(8, '', '2018/12/7', '10:24:20'),
(9, 'LISA                ', '2018/12/7', '11:41:33'),
(10, 'LISA                ', '2018/12/7', '11:41:33'),
(11, 'LISA                ', '2018/12/7', '11:41:33'),
(12, 'LISA                ', '2018/12/7', '11:44:16'),
(13, 'POLY                ', '2018/12/7', '11:44:50'),
(14, 'LISA                ', '2018/12/7', '11:45:23'),
(15, 'LISA                ', '2018/12/7', '13:58:8'),
(16, 'POLY                ', '2018/12/7', '13:58:34'),
(17, 'LISA                ', '2018/12/7', '13:59:35'),
(18, 'POLA                ', '2018/12/10', '16:7:43'),
(19, 'Jayjay              ', '2018/12/10', '16:16:26'),
(20, 'Jayjay              ', '2018/12/10', '16:17:49'),
(21, 'bluecard            ', '2018/12/12', '13:45:55'),
(22, 'bluecard            ', '2018/12/12', '13:48:59'),
(23, 'bluecard            ', '2018/12/12', '13:50:8'),
(24, 'bluecard            ', '2018/12/12', '14:5:36'),
(25, 'Mick                ', '2018/12/12', '14:5:56'),
(26, 'Mick                ', '2018/12/12', '14:6:2'),
(27, 'Mick                ', '2018/12/12', '14:6:6'),
(28, 'Jerry               ', '2018/12/12', '14:6:19'),
(29, 'Mick                ', '2018/12/12', '14:6:28'),
(30, 'Jerry               ', '2018/12/12', '14:6:35'),
(31, 'Mick                ', '2018/12/12', '14:19:21'),
(32, 'Mick                ', '2018/12/12', '15:58:59');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `rfid`
--
ALTER TABLE `rfid`
  ADD PRIMARY KEY (`id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `rfid`
--
ALTER TABLE `rfid`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
