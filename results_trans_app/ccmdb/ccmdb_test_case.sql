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
-- Table structure for table `test_case`
--

DROP TABLE IF EXISTS `test_case`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_case` (
  `case_id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `component_id` int(11) NOT NULL,
  `case_name` varchar(45) NOT NULL,
  `package_name` varchar(45) DEFAULT NULL,
  `status` tinyint(3) NOT NULL DEFAULT '1',
  `log` text,
  `note` varchar(255) DEFAULT 'No note',
  PRIMARY KEY (`case_id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_case`
--

LOCK TABLES `test_case` WRITE;
/*!40000 ALTER TABLE `test_case` DISABLE KEYS */;
INSERT INTO `test_case` VALUES (1,10,1,'case1','pk1',0,'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddtttttttttttttttttttttttttttttttttttttttttttttttttttttttfffffffffffffffffffffffffffffffffffffffffffff','not impact'),(2,10,2,'case2','pk2',1,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhggggggggggggggggggggg',NULL),(3,10,3,'case3','pk3',1,NULL,'standard'),(4,10,4,'case4','pk4',2,'dfefssdfsdfsdfsdfdsfsdfefefsfsdfsdfsdfdsfsdfsdfsd',NULL),(5,10,5,'case5','pk5',2,NULL,NULL),(6,10,6,'case6','pk1',1,'33333333333333333333333333333333333333333',NULL),(7,10,1,'case7','pk1',0,NULL,NULL),(8,10,2,'case8','pk2',1,'3333333333333333333333333333333',NULL),(9,10,3,'case9','pk2',1,NULL,NULL),(10,10,4,'case10','pk3',0,NULL,NULL),(11,10,5,'case11','pk3',1,NULL,NULL),(12,10,6,'case12','pk4',0,NULL,NULL),(13,10,1,'case13','pk5',1,NULL,NULL),(14,10,2,'case14','pk5',1,NULL,NULL),(15,10,3,'case15','pk5',1,NULL,NULL),(16,10,4,'case16','pk5',0,NULL,NULL),(17,10,5,'case17','pk4',1,NULL,NULL),(18,10,6,'case18','pk3',1,NULL,NULL),(19,10,1,'case19','pk3',1,NULL,NULL),(20,10,2,'case20','pk3',1,NULL,NULL),(21,1,3,'case21','pk2',1,NULL,NULL),(22,1,4,'case22','pk2',1,NULL,NULL),(23,1,5,'case23','pk1',1,NULL,NULL),(24,1,6,'case24','pk1',1,NULL,NULL),(25,1,1,'case25','pk1',0,NULL,NULL),(26,1,2,'case26','pk1',0,NULL,NULL),(27,1,3,'case27','pk2',1,NULL,NULL),(28,1,4,'case28','pk5',1,NULL,NULL),(29,1,5,'case29','pk5',2,NULL,NULL),(30,1,5,'case30','pk1',2,NULL,NULL),(31,1,5,'case31','pk1',0,NULL,'not impact'),(32,1,5,'case32','pk2',1,NULL,NULL),(33,1,5,'case33','pk3',1,NULL,NULL),(34,1,3,'case34','pk4',2,NULL,NULL),(35,1,3,'case35','pk5',2,NULL,NULL),(36,1,3,'case36','pk1',1,NULL,NULL),(37,1,3,'case37','pk1',0,NULL,NULL),(38,1,6,'case38','pk2',1,NULL,NULL),(39,1,6,'case39','pk2',1,NULL,NULL),(40,1,6,'case40','pk3',0,NULL,NULL),(41,1,6,'case41','pk3',1,NULL,NULL),(42,1,2,'case42','pk4',0,NULL,NULL),(43,1,2,'case43','pk5',1,NULL,NULL),(44,1,2,'case44','pk5',1,NULL,NULL),(45,1,2,'case45','pk5',1,NULL,NULL),(46,1,2,'case46','pk5',0,NULL,NULL),(47,1,2,'case47','pk4',1,NULL,NULL),(48,1,2,'case48','pk3',1,NULL,NULL),(49,1,2,'case49','pk3',1,NULL,NULL),(50,1,2,'case50','pk3',1,NULL,NULL),(51,1,2,'case51','pk2',1,NULL,NULL),(52,1,2,'case52','pk2',1,NULL,NULL),(53,1,2,'case53','pk1',1,NULL,NULL),(54,1,4,'case54','pk1',1,NULL,NULL),(55,1,4,'case55','pk1',0,NULL,NULL),(56,1,4,'case56','pk1',0,NULL,NULL),(57,1,4,'case57','pk2',1,NULL,NULL),(58,1,1,'case58','pk5',1,NULL,NULL),(59,1,1,'case59','pk5',2,NULL,NULL),(60,1,1,'case60','pk1',2,NULL,NULL),(61,1,1,'case61','pk7',1,NULL,NULL);
/*!40000 ALTER TABLE `test_case` ENABLE KEYS */;
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
