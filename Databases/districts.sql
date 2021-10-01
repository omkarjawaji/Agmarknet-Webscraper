-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: options
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `districts`
--

DROP TABLE IF EXISTS `districts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `districts` (
  `d_id` bigint DEFAULT NULL,
  `district_Id` bigint DEFAULT NULL,
  `district_Name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `districts`
--

LOCK TABLES `districts` WRITE;
/*!40000 ALTER TABLE `districts` DISABLE KEYS */;
INSERT INTO `districts` VALUES (1,1,'Ahmednagar'),(2,2,'Akola'),(3,3,'Amarawati'),(4,19,'Aurangabad'),(5,20,'Bandra(E)'),(6,21,'Beed'),(7,22,'Bhandara'),(8,4,'Buldhana'),(9,23,'Chandrapur'),(10,26,'Dharashiv(Usmanabad)'),(11,5,'Dhule'),(12,24,'Gadchiroli'),(13,34,'Gondiya'),(14,35,'Hingoli'),(15,6,'Jalana'),(16,7,'Jalgaon'),(17,8,'Kolhapur'),(18,9,'Latur'),(19,10,'Mumbai'),(20,11,'Nagpur'),(21,25,'Nanded'),(22,12,'Nandurbar'),(23,13,'Nashik'),(24,36,'Osmanabad'),(25,27,'Parbhani'),(26,14,'Pune'),(27,28,'Raigad'),(28,29,'Ratnagiri'),(29,15,'Sangli'),(30,30,'Satara'),(31,16,'Sholapur'),(32,31,'Sindhudurg'),(33,17,'Thane'),(34,33,'Vashim'),(35,18,'Wardha'),(36,32,'Yavatmal');
/*!40000 ALTER TABLE `districts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-01  6:35:08
