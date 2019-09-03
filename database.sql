-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: cookbook
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1,'a6'),(3,'the chicken rice man'),(5,'PippingHot'),(6,'hokkien club');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuisine`
--

DROP TABLE IF EXISTS `cuisine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cuisine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuisine_type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuisine`
--

LOCK TABLES `cuisine` WRITE;
/*!40000 ALTER TABLE `cuisine` DISABLE KEYS */;
INSERT INTO `cuisine` VALUES (1,'American'),(2,'British'),(3,'Caribbean'),(4,'Chinese'),(5,'French'),(6,'Greek'),(7,'Indian'),(8,'Italian'),(9,'Japanese'),(10,'Mediterranean'),(11,'Mexican'),(12,'Moroccan'),(13,'Spanish'),(14,'Thai'),(15,'Turkish'),(16,'Vietnamese');
/*!40000 ALTER TABLE `cuisine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredient` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ingred_name_id` int(11) NOT NULL,
  `ingred_serving` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_ingredient__ingred_name_id` (`ingred_name_id`),
  CONSTRAINT `fk_ingredient__ingred_name_id` FOREIGN KEY (`ingred_name_id`) REFERENCES `ingredient_name` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (1,1,'a4'),(20,36,'1 whole'),(21,37,'1 bowl'),(22,38,'1 bottle'),(23,39,'1 bottle'),(24,40,'1 tube'),(25,41,'1 pack'),(26,42,'1 kg'),(27,43,'300 g'),(28,44,'300 g'),(29,45,'1 pack x 500g'),(30,46,'1 pack x 500g'),(31,47,'1 pack x 1 kg');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient_name`
--

DROP TABLE IF EXISTS `ingredient_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredient_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ingred_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient_name`
--

LOCK TABLES `ingredient_name` WRITE;
/*!40000 ALTER TABLE `ingredient_name` DISABLE KEYS */;
INSERT INTO `ingredient_name` VALUES (1,'a3'),(2,'b3'),(3,'c3'),(4,'d3'),(5,'hello'),(6,'hello'),(7,'hello'),(8,'hello'),(21,'beef'),(22,'noodle'),(27,'chicken'),(28,'chicken'),(29,'rice'),(30,'chicken rice sauce'),(31,'chicken'),(32,'rice'),(33,'chicken rice sauce'),(34,'dark soy sauce'),(35,'spinach'),(36,'chicken'),(37,'rice'),(38,'chicken rice sauce'),(39,'dark soy sauce'),(40,'spinach'),(41,'hokkien noodle'),(42,'prawns'),(43,'beansprouts'),(44,'lean pork'),(45,'spaghetti'),(46,'lean beef'),(47,'tomato');
/*!40000 ALTER TABLE `ingredient_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient_recipe`
--

DROP TABLE IF EXISTS `ingredient_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredient_recipe` (
  `ingredient` int(11) NOT NULL,
  `recipe` int(11) NOT NULL,
  PRIMARY KEY (`ingredient`,`recipe`),
  KEY `idx_ingredient_recipe` (`recipe`),
  CONSTRAINT `fk_ingredient_recipe__ingredient` FOREIGN KEY (`ingredient`) REFERENCES `ingredient` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ingredient_recipe__recipe` FOREIGN KEY (`recipe`) REFERENCES `recipe` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient_recipe`
--

LOCK TABLES `ingredient_recipe` WRITE;
/*!40000 ALTER TABLE `ingredient_recipe` DISABLE KEYS */;
INSERT INTO `ingredient_recipe` VALUES (20,3),(21,3),(22,3),(23,3),(24,3),(29,5),(30,5),(31,5),(25,6),(26,6),(27,6),(28,6);
/*!40000 ALTER TABLE `ingredient_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_title` varchar(255) NOT NULL,
  `recipe_desc` varchar(255) NOT NULL,
  `recipe_methods` varchar(255) NOT NULL,
  `recipe_image` varchar(255) DEFAULT NULL,
  `cuisine_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_recipe__author_id` (`author_id`),
  KEY `idx_recipe__cuisine_id` (`cuisine_id`),
  CONSTRAINT `fk_recipe__author_id` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_recipe__cuisine_id` FOREIGN KEY (`cuisine_id`) REFERENCES `cuisine` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (3,'Chicken Rice','A flavorful Asian dish that combines several simple ingredients.','step 1 : slice the chicken\r\nstep 2: slice the spinach',NULL,4,3),(5,'Beef Bolognese','A warm western that commonly prepared by families across the globe. The ingredients consist of beef, spaghetti, and most importantly, the tomato sauce that brings out the essence of the dish.','step 1: smash the tomato and cook it into sauce\r\nstep 2: wash, slice and prepare the lean beef\r\nstep 3: wash and cook the spaghetti until its piping hot',NULL,1,5),(6,'Hokkien Noodle','A hokkien dish like no other.','step 1: slice the lean pork into pieces\r\nstep 2: cook the noodle\r\nstep 3: remove the beansprout roots\r\nstep 4: wash the prawns',NULL,4,6);
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-03 10:15:00
