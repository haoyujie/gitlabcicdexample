CREATE DATABASE  IF NOT EXISTS `ccmdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ccmdb`;
-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ccmdb
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `case_component`
--

DROP TABLE IF EXISTS `case_component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `case_component` (
  `component_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `component_name` varchar(45) NOT NULL,
  `report_id` int(11) NOT NULL,
  `total_case` int(11) NOT NULL DEFAULT '0',
  `execute_case` int(11) NOT NULL DEFAULT '0',
  `pass_case` int(11) NOT NULL DEFAULT '0',
  `fail_case` int(11) NOT NULL DEFAULT '0',
  `blocked_case` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`component_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `case_component`
--

LOCK TABLES `case_component` WRITE;
/*!40000 ALTER TABLE `case_component` DISABLE KEYS */;
INSERT INTO `case_component` VALUES (1,'cm1',10,2000,1900,1850,50,0),(2,'cm2',10,1500,1500,1400,0,100),(3,'cm3',10,1550,1000,1000,500,50),(4,'cm4',10,900,880,850,30,0),(5,'cm5',10,1101,800,780,0,20),(6,'cm6',10,450,450,0,0,450),(7,'cm7',10,780,780,760,20,0);
/*!40000 ALTER TABLE `case_component` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-26 15:09:14
