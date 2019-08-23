-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 23 Août 2019 à 16:52
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `seqbox`
--

-- --------------------------------------------------------

--
-- Structure de la table `batch`
--

CREATE TABLE IF NOT EXISTS `batch` (
  `id_batch` varchar(30) NOT NULL,
  `name_batch` varchar(50) NOT NULL,
  `date_batch` date NOT NULL,
  `instrument` varchar(250) NOT NULL,
  `primer` varchar(100) NOT NULL,
  PRIMARY KEY (`id_batch`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `batch`
--

INSERT INTO `batch` (`id_batch`, `name_batch`, `date_batch`, `instrument`, `primer`) VALUES
('5222mmm', 'palu01', '2018-05-04', 'sa', 'gggg'),
('555558', 'test', '2018-08-04', 'dddd', 'ccccc');

-- --------------------------------------------------------

--
-- Structure de la table `location`
--

CREATE TABLE IF NOT EXISTS `location` (
  `id_location` varchar(25) NOT NULL,
  `continent` varchar(80) NOT NULL,
  `country` varchar(60) NOT NULL,
  `province` varchar(40) NOT NULL,
  `city` varchar(50) NOT NULL,
  PRIMARY KEY (`id_location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `location`
--

INSERT INTO `location` (`id_location`, `continent`, `country`, `province`, `city`) VALUES
('1 Yec Xanh', 'Asia', 'Vietnam', 'Hai Bà Trung', 'Hanoi'),
('34 NGO AU CO', 'Asia', 'Vietnam', 'TAY HO', 'Hanoi');

-- --------------------------------------------------------

--
-- Structure de la table `result1`
--

CREATE TABLE IF NOT EXISTS `result1` (
  `id_result1` int(50) NOT NULL AUTO_INCREMENT,
  `qc` varchar(60) NOT NULL,
  `ql` varchar(60) NOT NULL,
  `description` varchar(250) NOT NULL,
  `snapper_variants` int(40) DEFAULT NULL,
  `snapper_ignored` int(50) DEFAULT NULL,
  `num_heterozygous` int(30) DEFAULT NULL,
  `mean_depth` double DEFAULT NULL,
  `coverage` double DEFAULT NULL,
  PRIMARY KEY (`id_result1`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Contenu de la table `result1`
--

INSERT INTO `result1` (`id_result1`, `qc`, `ql`, `description`, `snapper_variants`, `snapper_ignored`, `num_heterozygous`, `mean_depth`, `coverage`) VALUES
(1, 'ISO/CEI', 'isoprpyl', 'ggggg', 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `result2`
--

CREATE TABLE IF NOT EXISTS `result2` (
  `id_result2` int(10) NOT NULL AUTO_INCREMENT,
  `mykrobe_version` varchar(50) NOT NULL,
  `phylo_grp` varchar(60) NOT NULL,
  `phylo_grp_covg` double DEFAULT NULL,
  `phylo_grp_depth` double DEFAULT NULL,
  `species` varchar(50) NOT NULL,
  `species_covg` double DEFAULT NULL,
  `species_depth` double DEFAULT NULL,
  `lineage` varchar(50) NOT NULL,
  `lineage_covg` double DEFAULT NULL,
  `lineage_depth` double DEFAULT NULL,
  `susceptibility` varchar(50) NOT NULL,
  `variants` varchar(80) NOT NULL,
  `genes` varchar(100) NOT NULL,
  `drug` varchar(90) NOT NULL,
  PRIMARY KEY (`id_result2`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `result2`
--

INSERT INTO `result2` (`id_result2`, `mykrobe_version`, `phylo_grp`, `phylo_grp_covg`, `phylo_grp_depth`, `species`, `species_covg`, `species_depth`, `lineage`, `lineage_covg`, `lineage_depth`, `susceptibility`, `variants`, `genes`, `drug`) VALUES
(2, 'tuberculosis', 'Escherichia coli', 0, 0, '80', 0, 0, '', 0, 0, '', '', '', '');

-- --------------------------------------------------------

--
-- Structure de la table `sample`
--

CREATE TABLE IF NOT EXISTS `sample` (
  `id_sample` varchar(20) NOT NULL,
  `num_seq` varchar(60) NOT NULL,
  `date_time` datetime NOT NULL,
  `organism` varchar(30) NOT NULL,
  `batch` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `path_r1` varchar(40) NOT NULL,
  `path_r2` varchar(40) NOT NULL,
  `result1` int(11) DEFAULT NULL,
  `result2` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_sample`),
  KEY `result1` (`result1`),
  KEY `sample_ibfk_1` (`result2`),
  KEY `batch` (`batch`),
  KEY `location` (`location`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `sample`
--

INSERT INTO `sample` (`id_sample`, `num_seq`, `date_time`, `organism`, `batch`, `location`, `path_r1`, `path_r2`, `result1`, `result2`) VALUES
('05', 'ok', '2019-08-15 00:00:00', 'kkk', NULL, NULL, 'jj', '', NULL, NULL),
('45p', 'ii', '0000-00-00 00:00:00', '', NULL, NULL, '', '', NULL, NULL),
('as', 'gg', '0000-00-00 00:00:00', '', '555558', '34 NGO AU CO', '', '', NULL, 2),
('faas', 'lll', '0000-00-00 00:00:00', '', NULL, '1 Yec Xanh', '', '<input id="path_r2" name="path_r2" type=', 1, 2),
('fff', 'fff855', '0000-00-00 00:00:00', '', '555558', '1 Yec Xanh', '', '', 1, 2),
('hh', 'tt', '0000-00-00 00:00:00', '', '555558', '34 NGO AU CO', '', '<input id="path_r2" name="path_r2" type=', 1, 2),
('ko', '333', '0000-00-00 00:00:00', '', '555558', '34 NGO AU CO', '', '<input id="path_r2" name="path_r2" type=', 1, 2),
('ssssss', '46', '0000-00-00 00:00:00', '', '555558', '34 NGO AU CO', '', '<input id="path_r2" name="path_r2" type=', 1, 2),
('sz', 'az', '0000-00-00 00:00:00', '', '555558', '34 NGO AU CO', '', '', 1, 2);

-- --------------------------------------------------------

--
-- Structure de la table `sample_study`
--

CREATE TABLE IF NOT EXISTS `sample_study` (
  `id_sample` varchar(40) NOT NULL,
  `id_study` varchar(50) NOT NULL,
  PRIMARY KEY (`id_sample`,`id_study`),
  KEY `sample_study_ibfk_1` (`id_sample`) USING BTREE,
  KEY `id_study` (`id_study`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `study`
--

CREATE TABLE IF NOT EXISTS `study` (
  `id_study` varchar(50) NOT NULL,
  `date_study` date NOT NULL,
  `result_study` varchar(80) NOT NULL,
  PRIMARY KEY (`id_study`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `study`
--

INSERT INTO `study` (`id_study`, `date_study`, `result_study`) VALUES
('Palsmodium', '2019-04-23', 'negatif2'),
('treee', '0000-00-00', ''),
('Treponema ', '2018-12-04', 'positif');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Contenu de la table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password_hash`) VALUES
(1, 'lydia', 'lydiaiskounene@gmail.com', 'pbkdf2:sha256:50000$OT6jDS6i$10f37e0ce7dcc63116d2d91902893249e3cab8a64919982553ed965b33ae3ea5'),
(2, 'sara', 'kessar@hotmail.fr', 'pbkdf2:sha256:50000$AXNCuVWg$5516fb99126389c76b7f6db9b6708827c92ce3e8bd63511f6b5c8b45dc0d1352'),
(3, 'hai', 'f.iskounen@gmail.com', 'pbkdf2:sha256:50000$Gwt35BcP$61d2bb05afae1a7a4ae88d69091e807d5b3febf14b34f967f910a9ad6a718d8d'),
(4, 'oucru', 'jjjjjj@hotmail.fr', 'pbkdf2:sha256:50000$ANHi7VhE$b8b2ba0d1a177becbc00a982f754b2c91f7b0e43bf9f5b717eb4693e9dc21743');

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `sample`
--
ALTER TABLE `sample`
  ADD CONSTRAINT `sample_ibfk_4` FOREIGN KEY (`result2`) REFERENCES `result2` (`id_result2`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `sample_ibfk_1` FOREIGN KEY (`location`) REFERENCES `location` (`id_location`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `sample_ibfk_2` FOREIGN KEY (`batch`) REFERENCES `batch` (`id_batch`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `sample_ibfk_3` FOREIGN KEY (`result1`) REFERENCES `result1` (`id_result1`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Contraintes pour la table `sample_study`
--
ALTER TABLE `sample_study`
  ADD CONSTRAINT `sample_study_ibfk_2` FOREIGN KEY (`id_sample`) REFERENCES `sample` (`id_sample`),
  ADD CONSTRAINT `sample_study_ibfk_1` FOREIGN KEY (`id_study`) REFERENCES `study` (`id_study`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
