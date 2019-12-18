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
-- Table structure for table `test_report`
--

DROP TABLE IF EXISTS `test_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `report_name` varchar(255) NOT NULL,
  `rcpl` tinyint(3) NOT NULL,
  `report_date` timestamp(6) NOT NULL,
  `project_id` int(11) NOT NULL,
  `execute_case` int(11) NOT NULL DEFAULT '0',
  `total_case` int(11) NOT NULL DEFAULT '0',
  `pass_case` int(11) NOT NULL DEFAULT '0',
  `fail_case` int(11) NOT NULL DEFAULT '0',
  `blocked_case` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_report`
--

LOCK TABLES `test_report` WRITE;
/*!40000 ALTER TABLE `test_report` DISABLE KEYS */;
INSERT INTO `test_report` VALUES (1,'WRL8_RCPL30_07082019',30,'2019-07-07 16:00:00.000000',1,240,260,200,15,5),(2,'WRL8_RCPL30_07092019',30,'2019-07-08 16:00:00.000000',1,280,300,280,0,20),(3,'WRL8_RCPL30_07102019',30,'2019-07-09 16:00:00.000000',1,300,300,300,0,0),(4,'WRL8_RCPL30_07112019',30,'2019-07-10 16:00:00.000000',1,450,450,450,0,0),(5,'WRL8_RCPL30_08082019',30,'2019-08-07 16:00:00.000000',1,800,850,790,10,0),(6,'WRL8_RCPL30_08092019',30,'2019-08-08 16:00:00.000000',1,700,750,690,0,10),(7,'WRL8_RCPL29_07082019',29,'2019-07-07 16:00:00.000000',1,680,680,680,0,0),(8,'WRL8_RCPL31_07082019',31,'2019-07-07 16:00:00.000000',1,540,550,535,5,0),(9,'WRL8_RCPL30_10082019',30,'2019-10-07 16:00:00.000000',1,590,600,580,5,5),(10,'WRL8_RCPL30_11132019',30,'2019-12-13 16:00:00.000000',1,1000,1100,1000,1000,50),(11,'WRL8_RCPL29_11132019',29,'2019-11-28 16:00:00.000000',1,1080,1080,1070,50,100),(12,'WRL8_RCPL29_11232019',29,'2019-11-22 16:00:00.000000',1,800,800,800,120,20),(13,'WRL8_RCPL29_11232019',29,'2019-11-19 16:00:00.000000',1,900,900,900,30,30),(14,'WRL8_RCPL29_11232019',29,'2019-11-18 16:00:00.000000',1,850,850,850,100,100),(15,'WRL8_RCPL29_11232019',29,'2019-11-17 16:00:00.000000',1,900,900,900,90,20),(16,'WRL8_RCPL29_11232019',29,'2019-11-16 16:00:00.000000',1,850,850,850,55,100),(17,'WRL8_RCPL29_11232019',29,'2019-11-15 16:00:00.000000',1,800,800,800,10,100),(18,'WRL8_RCPL29_11232019',29,'2019-11-14 16:00:00.000000',1,700,700,700,30,16),(19,'WRL8_RCPL29_11232019',29,'2019-11-13 16:00:00.000000',1,750,750,750,33,22),(20,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,1000,1000,1000,0,0),(21,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(22,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(23,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(24,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(25,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(26,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(27,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(28,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(29,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0),(30,'WRL8_RCPL29_11232019',29,'2019-11-12 16:00:00.000000',1,800,800,800,0,0);
/*!40000 ALTER TABLE `test_report` ENABLE KEYS */;
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
