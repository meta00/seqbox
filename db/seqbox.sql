-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  mar. 18 juin 2019 à 09:20
-- Version du serveur :  5.7.24
-- Version de PHP :  7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `seqbox`
--

-- --------------------------------------------------------

--
-- Structure de la table `batch`
--

DROP TABLE IF EXISTS `batch`;
CREATE TABLE IF NOT EXISTS `batch` (
  `id_batch` varchar(30) NOT NULL,
  `name_batch` varchar(50) DEFAULT NULL,
  `date_batch` date DEFAULT NULL,
  `instrument` varchar(250) DEFAULT NULL,
  `primes` varchar(100) DEFAULT NULL,
  `location` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id_batch`),
  KEY `location` (`location`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `batch`
--

INSERT INTO `batch` (`id_batch`, `name_batch`, `date_batch`, `instrument`, `primes`, `location`) VALUES
('palu01', 'Paludism', '2019-06-03', 'phagothérapie', NULL, '34 NGO AU C0'),
('TRE02', 'Treponema', '2019-02-06', NULL, 'pallidum', '1 Yec Xanh');

-- --------------------------------------------------------

--
-- Structure de la table `location`
--

DROP TABLE IF EXISTS `location`;
CREATE TABLE IF NOT EXISTS `location` (
  `id_location` varchar(25) NOT NULL,
  `continent` varchar(80) NOT NULL,
  `country` varchar(60) NOT NULL,
  `province` varchar(40) NOT NULL,
  `city` varchar(50) NOT NULL,
  PRIMARY KEY (`id_location`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `location`
--

INSERT INTO `location` (`id_location`, `continent`, `country`, `province`, `city`) VALUES
('34 NGO AU CO', 'Asia', 'Vietnam', 'TAY HO', 'HANOI'),
('1 Yec Xanh', 'Asia', 'Vietnam', 'Hai Bà Trung', 'Hanoi');

-- --------------------------------------------------------

--
-- Structure de la table `result1`
--

DROP TABLE IF EXISTS `result1`;
CREATE TABLE IF NOT EXISTS `result1` (
  `id_result1` int(50) NOT NULL AUTO_INCREMENT,
  `qc` varchar(60) DEFAULT NULL,
  `ql` varchar(60) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `snapper_variants` int(40) DEFAULT NULL,
  `snapper_ignored` int(50) DEFAULT NULL,
  `num_heterozygous` int(30) DEFAULT NULL,
  `mean_depth` double DEFAULT NULL,
  `coverage` double DEFAULT NULL,
  PRIMARY KEY (`id_result1`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `result1`
--

INSERT INTO `result1` (`id_result1`, `qc`, `ql`, `description`, `snapper_variants`, `snapper_ignored`, `num_heterozygous`, `mean_depth`, `coverage`) VALUES
(1, 'ISO/CEI', 'isoprpyl', NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `result2`
--

DROP TABLE IF EXISTS `result2`;
CREATE TABLE IF NOT EXISTS `result2` (
  `id_result2` int(10) NOT NULL AUTO_INCREMENT,
  `mykrobe_version` varchar(50) DEFAULT NULL,
  `phylo_grp` varchar(60) DEFAULT NULL,
  `phylo_grp_covg` double DEFAULT NULL,
  `phylo_grp_depth` double DEFAULT NULL,
  `species` varchar(50) DEFAULT NULL,
  `species_covg` double DEFAULT NULL,
  `species_depth` double DEFAULT NULL,
  `lineage` varchar(50) DEFAULT NULL,
  `lineage_covg` double DEFAULT NULL,
  `lineage_depth` double DEFAULT NULL,
  `susceptibility` varchar(50) DEFAULT NULL,
  `variants` varchar(80) DEFAULT NULL,
  `genes` varchar(100) DEFAULT NULL,
  `drug` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id_result2`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `result2`
--

INSERT INTO `result2` (`id_result2`, `mykrobe_version`, `phylo_grp`, `phylo_grp_covg`, `phylo_grp_depth`, `species`, `species_covg`, `species_depth`, `lineage`, `lineage_covg`, `lineage_depth`, `susceptibility`, `variants`, `genes`, `drug`) VALUES
(2, 'tuberculosis', 'Escherichia coli', -1.79769, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `sample`
--

DROP TABLE IF EXISTS `sample`;
CREATE TABLE IF NOT EXISTS `sample` (
  `id_sample` varchar(20) NOT NULL,
  `num_seq` varchar(60) NOT NULL,
  `date_time` datetime NOT NULL,
  `organism` varchar(30) DEFAULT NULL,
  `batch` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `path_r1` varchar(40) DEFAULT NULL,
  `path_r2` varchar(40) DEFAULT NULL,
  `result1` int(60) DEFAULT NULL,
  `result2` int(60) DEFAULT NULL,
  PRIMARY KEY (`id_sample`),
  KEY `result1` (`result1`),
  KEY `result2` (`result2`),
  KEY `location` (`location`),
  KEY `batch` (`batch`)
) ENGINE=MyISAM AUTO_INCREMENT=1131 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `sample`
--

INSERT INTO `sample` (`id_sample`, `num_seq`, `date_time`, `organism`, `batch`, `location`, `path_r1`, `path_r2`, `result1`, `result2`) VALUES
('malaria01', 'M01', '2018-04-04 16:19:41', 'LABDiderot', 'palu01', '34 NGO AU C0', 'palsmodium falciparum', NULL, 1, NULL),
('syphilis02', 'S02', '2019-01-09 10:11:00', 'LABECE', 'TRE02', '1 Yec Xanh', NULL, 'Treponema pallidum', NULL, 2);

-- --------------------------------------------------------

--
-- Structure de la table `sample_study`
--

DROP TABLE IF EXISTS `sample_study`;
CREATE TABLE IF NOT EXISTS `sample_study` (
  `id_sample` varchar(40) NOT NULL,
  `id_study` varchar(50) NOT NULL,
  PRIMARY KEY (`id_sample`,`id_study`),
  KEY `id_study` (`id_study`),
  KEY `id_sample` (`id_sample`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `sample_study`
--

INSERT INTO `sample_study` (`id_sample`, `id_study`) VALUES
('malaria01', 'Palsmodium'),
('syphilis02', 'Treponema ');

-- --------------------------------------------------------

--
-- Structure de la table `study`
--

DROP TABLE IF EXISTS `study`;
CREATE TABLE IF NOT EXISTS `study` (
  `id_study` varchar(50) NOT NULL,
  `date_study` date DEFAULT NULL,
  `result_study` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_study`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `study`
--

INSERT INTO `study` (`id_study`, `date_study`, `result_study`) VALUES
('Palsmodium', '2019-04-23', 'negatif'),
('Treponema ', '2018-12-04', 'positif');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
