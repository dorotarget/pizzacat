-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 14. Apr 2020 um 15:24
-- Server-Version: 10.4.11-MariaDB
-- PHP-Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `pizzastars`
--
CREATE DATABASE IF NOT EXISTS `pizzastars` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `pizzastars`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `adresse`
--

CREATE TABLE `adresse` (
  `adresse_id` int(11) NOT NULL,
  `strasse` varchar(200) NOT NULL,
  `hausnummer` int(11) NOT NULL,
  `postleitzahl` int(20) NOT NULL,
  `ort` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='adressenverwaltung';

--
-- Daten für Tabelle `adresse`
--

INSERT INTO `adresse` (`adresse_id`, `strasse`, `hausnummer`, `postleitzahl`, `ort`) VALUES
(1, 'Blumenweg', 17, 12345, 'Blumendorf'),
(2, 'Kauzgasse', 3, 98765, 'Weizensee'),
(3, 'Wasseralle', 37, 73984, 'Tropfe'),
(4, 'Kuckucksstraße', 99, 29475, 'Kuckingen'),
(5, 'Huhnweg', 5, 94328, 'Huhnululu'),
(6, 'Kurzweg', 81, 12355, 'Dorfingen'),
(7, 'Schotterweg', 234, 94856, 'Schottern'),
(8, 'Suppenstraße', 22, 32455, 'Lucksig'),
(9, 'Sommeralle', 77, 739, 'Sommerfels'),
(10, 'Huchweg', 98, 98766, 'Huchingen');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `bestellung`
--

CREATE TABLE `bestellung` (
  `bestellung_id` int(11) NOT NULL,
  `kunde_id` int(11) NOT NULL,
  `datum` timestamp NOT NULL DEFAULT current_timestamp(),
  `adresse_id` int(11) NOT NULL,
  `bestellsumme` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='bestellungverwaltung';

--
-- Daten für Tabelle `bestellung`
--

INSERT INTO `bestellung` (`bestellung_id`, `kunde_id`, `datum`, `adresse_id`, `bestellsumme`) VALUES
(1, 3, '2020-04-14 13:14:52', 3, '11'),
(2, 2, '2020-04-14 13:17:22', 2, '16');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kunde`
--

CREATE TABLE `kunde` (
  `kunde_id` int(11) NOT NULL,
  `vorname` varchar(100) NOT NULL,
  `nachname` varchar(100) NOT NULL,
  `adresse_id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kundenverwaltung';

--
-- Daten für Tabelle `kunde`
--

INSERT INTO `kunde` (`kunde_id`, `vorname`, `nachname`, `adresse_id`, `email`) VALUES
(1, 'Hans', 'Müller', 1, 'mueller@web.de'),
(2, 'Susi', 'Strolch', 2, 'susi@strolch.io'),
(3, 'Toni', 'Trampler', 3, 'trampel@ton.de'),
(4, 'Ferdinand', 'Pferd', 4, 'ferdinand@pferd.de'),
(5, 'Larissa', 'Schmied', 5, 'larissa@schmied.de'),
(6, 'Peter', 'Hase', 6, 'peter@hase.de'),
(7, 'Anna', 'Peterson', 7, 'anna@peterson.de'),
(8, 'Kalle', 'Blomquist', 8, 'kalle@blomquist.de'),
(9, 'Carl', 'Schneider', 9, 'carl@schneider.de'),
(10, 'Sarah', 'Friedrich', 10, 'sarah@friedrich.io');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `pizza`
--

CREATE TABLE `pizza` (
  `pizza_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `groesze` varchar(20) NOT NULL,
  `beschreibung` varchar(1500) NOT NULL,
  `preis` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='pizzenverwaltung';

--
-- Daten für Tabelle `pizza`
--

INSERT INTO `pizza` (`pizza_id`, `name`, `groesze`, `beschreibung`, `preis`) VALUES
(1, 'Margarita', '24', 'der Klassiker in kleiner Größe', 4),
(2, 'Margarita', '28', 'der Klassiker in klassischer Größe', 4.5),
(3, 'Brokkolipizza', '28', 'mit extra viel Brokkoli', 5.7),
(4, 'Gemüsepizza', '28', 'Champignons, Tomate, Zucchini, Spinat, Peperoni, Paprika und Spargel', 11.7),
(5, 'Pizza Quatro Formaggi vegan', '24', 'mit veganem Cheddar, Parmesan, Gorgonzola und Mozzarella', 7),
(6, 'Pizza Quatro Formaggi vegan', '28', 'mit veganem Cheddar, Parmesan, Gorgonzola und Mozzarella, in groß', 10.1),
(7, 'Tofupizza mit Tomate', '24', 'mit geräuchertem Tofu', 7.1),
(8, 'Tofupizza mit Tomate', '28', 'mitgeräuchertem Tofu, in groß', 8.9),
(9, 'Riesenpizza', '39', 'für den großen Hunger, mit veganem Käse, Tofu, Gemüse, veganer Salami und Basilikum', 17.3),
(10, 'Nachtischpizza', '24', 'mit Schokosoße, geriebener weißer Schokolade, Waffelteig und Keksbelag', 12.3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `wird_bestellt`
--

CREATE TABLE `wird_bestellt` (
  `id_bestellung` int(11) NOT NULL,
  `id_pizza` int(11) NOT NULL,
  `anzahl` int(100) NOT NULL,
  `zwischenpreis` double(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='waswirdbestellt';

--
-- Daten für Tabelle `wird_bestellt`
--

INSERT INTO `wird_bestellt` (`id_bestellung`, `id_pizza`, `anzahl`, `zwischenpreis`) VALUES
(1, 1, 1, 4),
(1, 5, 1, 7),
(2, 7, 1, 7),
(2, 8, 1, 9);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `adresse`
--
ALTER TABLE `adresse`
  ADD PRIMARY KEY (`adresse_id`);

--
-- Indizes für die Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  ADD PRIMARY KEY (`bestellung_id`);

--
-- Indizes für die Tabelle `kunde`
--
ALTER TABLE `kunde`
  ADD PRIMARY KEY (`kunde_id`);

--
-- Indizes für die Tabelle `pizza`
--
ALTER TABLE `pizza`
  ADD PRIMARY KEY (`pizza_id`);

--
-- Indizes für die Tabelle `wird_bestellt`
--
ALTER TABLE `wird_bestellt`
  ADD PRIMARY KEY (`id_bestellung`,`id_pizza`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `adresse`
--
ALTER TABLE `adresse`
  MODIFY `adresse_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT für Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  MODIFY `bestellung_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT für Tabelle `kunde`
--
ALTER TABLE `kunde`
  MODIFY `kunde_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT für Tabelle `pizza`
--
ALTER TABLE `pizza`
  MODIFY `pizza_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
