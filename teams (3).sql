CREATE TABLE IF NOT EXISTS Teams(
	        Team_Name CHAR(25),
	        yr INT,
	        Location CHAR(25),
          Wins REAL,
	        Won_Championship BOOLEAN,
	        PRIMARY KEY(Team_Name, yr)
	        


 ); 
INSERT INTO Teams(Team_Name, yr, Location, Wins, Won_Championship) VALUES
('HAWKS', 2022, 'ATLANTA', 43.0, False),
('CELTICS', 2022, 'BOSTON', 51.0, False),
('NETS', 2022, 'BROOKLYN', 44.0, False),
('BULLS', 2022, 'CHICAGO', 46.0, False),
('HORNETS', 2022, 'CHARLOTTE', 43.0, False),
('CAVALIERS', 2022, 'CLEVELAND', 44.0, False),
('MAVERICKS', 2022, 'DALLAS', 52.0, False),
('NUGGETS', 2022, 'DENVER', 48.0, False),
('PISTONS', 2022, 'DETROIT', 23.0, False),
('WARRIORS', 2022, 'SAN FRANCISCO', 53.0, True),
('76ERS', 2022, 'PHILADELPHIA', 51.0, False),
('ROCKETS', 2022, 'HOUSTON', 20.0, False),
('PACERS', 2022, 'INDIANA', 25.0, False),
('CLIPPERS', 2022, 'LOS ANGELES', 42.0, False),
('LAKERS', 2022, 'LOS ANGELES', 33.0, False),
('TIMBERWOLVES', 2022, 'MINNESOTA', 46.0, False),
('GRIZZLIES', 2022, 'MEMPHIS', 56.0, False),
('HEAT', 2022, 'MIAMI', 53.0, False),
('BUCKS', 2022, 'MILWAUKEE', 51.0, False),
('PELICANS', 2022, 'NEW ORLEANS', 36.0, False),
('KNICKS', 2022, 'NEW YORK', 37.0, False),
('THUNDER', 2022, 'OKLAHOMA CITY', 24.0, False),
('MAGIC', 2022, 'ORLANDO', 22.0, False),
('SUNS', 2022, 'PHOENIX', 64.0, False),
('BLAZERS', 2022, 'PORTLAND', 27.0, False),
('KINGS', 2022, 'SACRAMENTO', 30.0, False),
('SPURS', 2022, 'SAN ANTONIO', 34.0, False),
('RAPTORS', 2022, 'TORONTO', 48.0, False),
('JAZZ', 2022, 'UTAH', 49.0, False),
('WIZARDS', 2022, 'WASHINGTON', 35.0, False)
