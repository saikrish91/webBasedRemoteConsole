-- MySQL dump 10.13  Distrib 5.1.58, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: wbrc
-- ------------------------------------------------------
-- Server version	5.1.58-1ubuntu1

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
-- Table structure for table `ENDUSER`
--

DROP TABLE IF EXISTS `ENDUSER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ENDUSER` (
  `REGNO` int(11) NOT NULL,
  `USERID` varchar(40) DEFAULT NULL,
  `PWD` varchar(40) DEFAULT NULL,
  `FIRSTNAME` varchar(20) DEFAULT NULL,
  `LASTNAME` varchar(20) DEFAULT NULL,
  `SECQN` varchar(200) DEFAULT NULL,
  `SECANS` varchar(200) DEFAULT NULL,
  `MOBILE` varchar(50) DEFAULT NULL,
  `EMAIL` varchar(100) DEFAULT NULL,
  `THEME` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`REGNO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ENDUSER`
--

LOCK TABLES `ENDUSER` WRITE;
/*!40000 ALTER TABLE `ENDUSER` DISABLE KEYS */;
INSERT INTO `ENDUSER` VALUES (1,'demo','demo','Demonstration','User','Whats demo used for','demonstration is demo','9999999999','demo@example.com','blitzer');
/*!40000 ALTER TABLE `ENDUSER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOSTS`
--

DROP TABLE IF EXISTS `HOSTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HOSTS` (
  `HOSTID` int(11) NOT NULL,
  `REGNO` int(11) DEFAULT NULL,
  `IPADDR` varchar(100) DEFAULT NULL,
  `HOSTNAME` varchar(200) DEFAULT NULL,
  `HPWD` varchar(200) DEFAULT NULL,
  `PFNO` int(11) DEFAULT NULL,
  PRIMARY KEY (`HOSTID`),
  KEY `REGNO` (`REGNO`),
  KEY `PFNO` (`PFNO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOSTS`
--

LOCK TABLES `HOSTS` WRITE;
/*!40000 ALTER TABLE `HOSTS` DISABLE KEYS */;
INSERT INTO `HOSTS` VALUES (1,1,'localhost','localhost','root',1);
/*!40000 ALTER TABLE `HOSTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOGTAB`
--

DROP TABLE IF EXISTS `LOGTAB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LOGTAB` (
  `TXNID` int(11) NOT NULL AUTO_INCREMENT,
  `HOSTID` int(11) DEFAULT NULL,
  `USERID` varchar(100) DEFAULT NULL,
  `TIMESTAMP` date DEFAULT NULL,
  `TASK` varchar(500) DEFAULT NULL,
  `OUTCOME` varchar(1000) DEFAULT NULL,
  `STATUS` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`TXNID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOGTAB`
--

LOCK TABLES `LOGTAB` WRITE;
/*!40000 ALTER TABLE `LOGTAB` DISABLE KEYS */;
/*!40000 ALTER TABLE `LOGTAB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLATFORM`
--

DROP TABLE IF EXISTS `PLATFORM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PLATFORM` (
  `PFNO` int(11) NOT NULL,
  `PLATFORM` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PFNO`),
  UNIQUE KEY `PLATFORM` (`PLATFORM`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLATFORM`
--

LOCK TABLES `PLATFORM` WRITE;
/*!40000 ALTER TABLE `PLATFORM` DISABLE KEYS */;
INSERT INTO `PLATFORM` VALUES (1,'UBUNTU'),(2,'REDHAT'),(3,'SOLARIS'),(4,'openSUSE'),(5,'DEBIAN');
/*!40000 ALTER TABLE `PLATFORM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SENIORUSER`
--

DROP TABLE IF EXISTS `SENIORUSER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SENIORUSER` (
  `REGNO` int(11) NOT NULL,
  `USERID` varchar(40) DEFAULT NULL,
  `PWD` varchar(40) DEFAULT NULL,
  `FIRSTNAME` varchar(20) DEFAULT NULL,
  `LASTNAME` varchar(20) DEFAULT NULL,
  `SECQN` varchar(200) DEFAULT NULL,
  `SECANS` varchar(200) DEFAULT NULL,
  `MOBILE` varchar(50) DEFAULT NULL,
  `EMAIL` varchar(100) DEFAULT NULL,
  `THEME` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SENIORUSER`
--

LOCK TABLES `SENIORUSER` WRITE;
/*!40000 ALTER TABLE `SENIORUSER` DISABLE KEYS */;
INSERT INTO `SENIORUSER` VALUES (1,'SENIOR','demo','','','','','','','ui-darkness');
/*!40000 ALTER TABLE `SENIORUSER` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-04-15 20:41:36
