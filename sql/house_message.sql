
DROP TABLE IF EXISTS `house_message`;

CREATE TABLE `house_message` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `picture` varchar(100) DEFAULT NULL,
  `name` varchar(80) DEFAULT NULL,
  `area` varchar(20) DEFAULT NULL,
  `unit_price` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `community_name` varchar(100) DEFAULT NULL,
  `community_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
