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
-- Table structure for table `commodities`
--

DROP TABLE IF EXISTS `commodities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commodities` (
  `C_id` bigint DEFAULT NULL,
  `Commodity_Id` bigint DEFAULT NULL,
  `Commodity_Name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodities`
--

LOCK TABLES `commodities` WRITE;
/*!40000 ALTER TABLE `commodities` DISABLE KEYS */;
INSERT INTO `commodities` VALUES (1,137,'Ajwan'),(2,281,'Alasande Gram'),(3,325,'Almond(Badam)'),(4,166,'Alsandikai'),(5,86,'Amaranthus'),(6,130,'Ambada Seed'),(7,355,'Amla(Nelli Kai)'),(8,102,'Amphophalus'),(9,209,'Antawala'),(10,379,'Anthorium'),(11,17,'Apple'),(12,326,'Apricot(Jardalu/Khumani)'),(13,140,'Arecanut(Betelnut/Supari)'),(14,49,'Arhar (Tur/Red Gram)(Whole)'),(15,260,'Arhar Dal(Tur Dal)'),(16,83,'Ashgourd'),(17,232,'Astera'),(18,269,'Avare Dal'),(19,28,'Bajra(Pearl Millet/Cumbu)'),(20,274,'Balekai'),(21,204,'Bamboo'),(22,19,'Banana'),(23,90,'Banana - Green'),(24,29,'Barley (Jau)'),(25,321,'Bay leaf (Tejpatta)'),(26,94,'Beans'),(27,262,'Beaten Rice'),(28,157,'Beetroot'),(29,263,'Bengal Gram Dal (Chana Dal)'),(30,6,'Bengal Gram(Gram)(Whole)'),(31,357,'Ber(Zizyphus/Borehannu)'),(32,143,'Betal Leaves'),(33,41,'Betelnuts'),(34,85,'Bhindi(Ladies Finger)'),(35,113,'Big Gram'),(36,51,'Binoula'),(37,81,'Bitter gourd'),(38,8,'Black Gram (Urd Beans)(Whole)'),(39,264,'Black Gram Dal (Urd Dal)'),(40,38,'Black pepper'),(41,380,'BOP'),(42,189,'Borehannu'),(43,82,'Bottle gourd'),(44,290,'Bran'),(45,35,'Brinjal'),(46,293,'Broken Rice'),(47,320,'Broomstick(Flower Broom)'),(48,214,'Bull'),(49,284,'Bullar'),(50,224,'Bunch Beans'),(51,272,'Butter'),(52,154,'Cabbage'),(53,215,'Calf'),(54,354,'Camel Hair'),(55,205,'Cane'),(56,164,'Capsicum'),(57,40,'Cardamoms'),(58,375,'Carnation'),(59,153,'Carrot'),(60,238,'Cashew Kernnel'),(61,133,'Cashewnuts'),(62,36,'Cashewnuts'),(63,270,'Castor Oil'),(64,123,'Castor Seed'),(65,34,'Cauliflower'),(66,188,'Chakotha'),(67,169,'Chapparad Avare'),(68,241,'Chennangi (Whole)'),(69,295,'Chennangi Dal'),(70,328,'Cherry'),(71,71,'Chikoos(Sapota)'),(72,26,'Chili Red'),(73,88,'Chilly Capsicum'),(74,167,'Chow Chow'),(75,402,'Chrysanthemum'),(76,231,'Chrysanthemum(Loose)'),(77,316,'Cinamon(Dalchini)'),(78,105,'Cloves'),(79,80,'Cluster beans'),(80,315,'Coca'),(81,368,'Cock'),(82,104,'Cocoa'),(83,138,'Coconut'),(84,37,'Coconut'),(85,266,'Coconut Oil'),(86,112,'Coconut Seed'),(87,45,'Coffee'),(88,318,'Colacasia'),(89,129,'Copra'),(90,43,'Coriander(Leaves)'),(91,108,'Corriander seed'),(92,15,'Cotton'),(93,99,'Cotton Seed'),(94,212,'Cow'),(95,92,'Cowpea (Lobia/Karamani)'),(96,89,'Cowpea(Veg)'),(97,159,'Cucumbar(Kheera)'),(98,42,'Cummin Seed(Jeera)'),(99,352,'Custard Apple (Sharifa)'),(100,382,'Daila(Chandni)'),(101,91,'Dal (Avare)'),(102,273,'Dalda'),(103,410,'Delha'),(104,69,'Dhaincha'),(105,168,'Drumstick'),(106,132,'Dry Chillies'),(107,345,'Dry Fodder'),(108,278,'Dry Grapes'),(109,370,'Duck'),(110,163,'Duster Beans'),(111,367,'Egg'),(112,361,'Egypian Clover(Barseem)'),(113,296,'Elephant Yam (Suran)'),(114,64,'Field Pea'),(115,221,'Fig(Anjura/Anjeer)'),(116,206,'Firewood'),(117,366,'Fish'),(118,365,'Flower Broom'),(119,121,'Foxtail Millet(Navane)'),(120,298,'French Beans (Frasbean)'),(121,350,'Galgal(Lemon)'),(122,25,'Garlic'),(123,249,'Ghee'),(124,276,'Gingelly Oil'),(125,27,'Ginger(Dry)'),(126,103,'Ginger(Green)'),(127,364,'Gladiolus Bulb'),(128,363,'Gladiolus Cut Flower'),(129,219,'Goat'),(130,353,'Goat Hair'),(131,359,'Gram Raw(Chholia)'),(132,294,'Gramflour'),(133,22,'Grapes'),(134,165,'Green Avare (W)'),(135,87,'Green Chilli'),(136,346,'Green Fodder'),(137,9,'Green Gram (Moong)(Whole)'),(138,265,'Green Gram Dal (Moong Dal)'),(139,50,'Green Peas'),(140,267,'Ground Nut Oil'),(141,268,'Ground Nut Seed'),(142,10,'Groundnut'),(143,314,'Groundnut (Split)'),(144,312,'Groundnut pods (raw)'),(145,75,'Guar'),(146,413,'Guar Seed(Cluster Beans Seed)'),(147,185,'Guava'),(148,74,'Gur(Jaggery)'),(149,279,'Gurellu'),(150,252,'Haralekai'),(151,216,'He Buffalo'),(152,369,'Hen'),(153,125,'Hippe Seed'),(154,236,'Honey'),(155,124,'Honge seed'),(156,119,'Hybrid Cumbu'),(157,299,'Indian Beans (Seam)'),(158,344,'Indian Colza(Sarson)'),(159,256,'Isabgul (Psyllium)'),(160,182,'Jack Fruit'),(161,406,'Jaffri'),(162,151,'Jaggery'),(163,175,'Jamamkhan'),(164,184,'Jamun(Narale Hannu)'),(165,376,'Jarbara'),(166,229,'Jasmine'),(167,250,'Javi'),(168,5,'Jowar(Sorghum)'),(169,16,'Jute'),(170,210,'Jute Seed'),(171,362,'Kabuli Chana(Chickpeas-White)'),(172,317,'Kacholam'),(173,230,'Kakada'),(174,233,'Kankambra'),(175,115,'Karamani'),(176,187,'Karbuja(Musk Melon)'),(177,305,'Kartali (Kantola)'),(178,61,'Kharif Mash'),(179,372,'Khoya'),(180,336,'Kinnow'),(181,177,'Knool Khol'),(182,117,'Kodo Millet(Varagu)'),(183,243,'Kuchur'),(184,114,'Kulthi(Horse Gram)'),(185,155,'Ladies Finger'),(186,96,'Lak(Teora)'),(187,171,'Leafy Vegetable'),(188,310,'Lemon'),(189,63,'Lentil (Masur)(Whole)'),(190,378,'Lilly'),(191,180,'Lime'),(192,67,'Linseed'),(193,280,'Lint'),(194,351,'Litchi'),(195,302,'Little gourd (Kundru)'),(196,304,'Long Melon(Kakri)'),(197,403,'Lotus'),(198,339,'Lotus Sticks'),(199,337,'Lukad'),(200,107,'Mace'),(201,411,'Mahedi'),(202,335,'Mahua'),(203,371,'Mahua Seed(Hippe seed)'),(204,288,'Maida Atta'),(205,4,'Maize'),(206,20,'Mango'),(207,172,'Mango (Raw-Ripe)'),(208,225,'Maragensu'),(209,181,'Marasebu'),(210,407,'Marget'),(211,235,'Marigold(Calcutta)'),(212,405,'Marigold(loose)'),(213,60,'Mash'),(214,340,'Mashrooms'),(215,259,'Masur Dal'),(216,93,'Mataki'),(217,47,'Methi Seeds'),(218,46,'Methi(Leaves)'),(219,237,'Millets'),(220,360,'Mint(Pudina)'),(221,258,'Moath Dal'),(222,95,'Moath Dal'),(223,77,'Mousambi(Sweet Lime)'),(224,12,'Mustard'),(225,324,'Mustard Oil'),(226,142,'Myrobolan(Harad)'),(227,245,'Nargasi'),(228,222,'Nearle Hannu'),(229,126,'Neem Seed'),(230,223,'Nelli Kai'),(231,98,'Niger Seed (Ramtil)'),(232,106,'Nutmeg'),(233,23,'Onion'),(234,358,'Onion Green'),(235,18,'Orange'),(236,381,'Orchid'),(237,97,'Other Pulses'),(238,213,'Ox'),(239,414,'Paddy(Dhan)(Basmati)'),(240,2,'Paddy(Dhan)(Common)'),(241,72,'Papaya'),(242,313,'Papaya (Raw)'),(243,404,'Patti Calcutta'),(244,331,'Peach'),(245,330,'Pear(Marasebu)'),(246,308,'Peas cod'),(247,174,'Peas Wet'),(248,347,'Peas(Dry)'),(249,301,'Pegeon Pea (Arhar Fali)'),(250,109,'Pepper garbled'),(251,110,'Pepper ungarbled'),(252,327,'Persimon(Japani Fal)'),(253,220,'Pigs'),(254,21,'Pineapple'),(255,329,'Plum'),(256,303,'Pointed gourd (Parval)'),(257,240,'Polherb'),(258,190,'Pomegranate'),(259,24,'Potato'),(260,84,'Pumpkin'),(261,254,'Pundi'),(262,128,'Pundi Seed'),(263,161,'Raddish'),(264,30,'Ragi (Finger Millet)'),(265,409,'Raibel'),(266,248,'Rajgir'),(267,282,'Ram'),(268,307,'Rat Tail Radish (Mogari)'),(269,65,'Raya'),(270,7,'Red Gram'),(271,322,'Resinwood'),(272,62,'Riccbcan'),(273,3,'Rice'),(274,160,'Ridge gourd(Tori)'),(275,374,'Rose(Local)'),(276,228,'Rose(Loose)'),(277,373,'Rose(Tata)'),(278,306,'Round gourd'),(279,111,'Rubber'),(280,291,'Sabu Dana'),(281,59,'Safflower'),(282,338,'Saffron'),(283,271,'Sajje'),(284,122,'Same/Savi'),(285,247,'Sarasum'),(286,277,'Season Leaves'),(287,253,'Seegu'),(288,176,'Seemebadnekai'),(289,201,'Seetafal'),(290,11,'Sesamum(Sesame,Gingelly,Til)'),(291,217,'She Buffalo'),(292,283,'She Goat'),(293,218,'Sheep'),(294,183,'Siddota'),(295,226,'Skin And Hide'),(296,156,'Snake gourd'),(297,135,'Soanf'),(298,207,'Soapnut(Antawala/Retha)'),(299,286,'Soji'),(300,246,'Sompu'),(301,13,'Soyabean'),(302,342,'Spinach'),(303,311,'Sponge gourd'),(304,332,'Squash(Chappal Kadoo)'),(305,48,'Sugar'),(306,150,'Sugarcane'),(307,14,'Sunflower'),(308,285,'Sunflower Seed'),(309,139,'Sunhemp'),(310,242,'Suram'),(311,300,'Surat Beans (Papadi)'),(312,255,'Suva (Dill Seed)'),(313,178,'Suvarna Gadde'),(314,152,'Sweet Potato'),(315,173,'Sweet Pumpkin'),(316,120,'T.V. Cumbu'),(317,261,'Tamarind Fruit'),(318,208,'Tamarind Seed'),(319,100,'Tapioca'),(320,76,'Taramira'),(321,44,'Tea'),(322,200,'Tender Coconut'),(323,116,'Thinai (Italian Millet)'),(324,170,'Thogrikai'),(325,162,'Thondekai'),(326,349,'Tinda'),(327,141,'Tobacco'),(328,78,'Tomato'),(329,323,'Torchwood'),(330,66,'Toria'),(331,234,'Tube Flower'),(332,401,'Tube Rose(Double)'),(333,408,'Tube Rose(Loose)'),(334,377,'Tube Rose(Single)'),(335,39,'Turmeric'),(336,309,'Turmeric (raw)'),(337,341,'Turnip'),(338,343,'Walnut'),(339,73,'Water Melon'),(340,1,'Wheat'),(341,287,'Wheat Atta'),(342,412,'White Peas'),(343,158,'White Pumpkin'),(344,203,'Wood'),(345,348,'Wool'),(346,244,'Yam'),(347,297,'Yam (Ratalu)');
/*!40000 ALTER TABLE `commodities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-01  6:35:35
