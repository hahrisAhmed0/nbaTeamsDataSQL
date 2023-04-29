from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc

from basketball_reference_scraper.box_scores import get_all_star_box_score
# TeamName(primary key)
# Year(primary key)
# Location
# Won_ChampionShip
# Wins
# Payroll

teamAbbrev = {"ATLANTA HAWKS" : "ATL",
"ST. LOUIS HAWKS" : "SLH",
#"MILWAUKEE HAWKS" : "MIL", # dupe milwaukee
"TRI-CITIES BLACKHAWKS" : "TCB",
"BOSTON CELTICS" : "BOS",
"BROOKLYN NETS" : "BRK",
"NEW JERSEY NETS" : "NJN",
"CHICAGO BULLS" : "CHI", #dupe chicago
"CHARLOTTE HORNETS": "CHH",
"CHARLOTTE HORNETS": "CHO",
"CHARLOTTE BOBCATS" : "CHA",
"CLEVELAND CAVALIERS" : "CLE",
"DALLAS MAVERICKS" : "DAL",
"DENVER NUGGETS" : "DEN",
"DETROIT PISTONS" : "DET",
"FORT WAYNE PISTONS" : "FWP",
"GOLDEN STATE WARRIORS" : "GSW",
"SAN FRANCISCO WARRIORS" : "SFW",
"PHILADELPHIA WARRIORS" : "PHI",#dupe philly
"HOUSTON ROCKETS" : "HOU",
"INDIANA PACERS" : "IND", #dupe indianapolis
"LOS ANGELES CLIPPERS" : "LAC",
"SAN DIEGO CLIPPERS" : "SDC",
"BUFFALO BRAVES" : "BUF",
"LOS ANGELES LAKERS" : "LAL",
"MINNEAPOLIS LAKERS" : "MIN", #dupe mineeapolis
"MEMPHIS GRIZZLIES" :"MEM",
"VANCOUVER GRIZZLIES" : "VAN",
"MIAMI HEAT" : "MIA",
"MILWAUKEE BUCKS" : "MIL", #dupe milwaukee
"MINNESOTA TIMBERWOLVES" : "MIN", #dupe minnesota
"NEW ORLEANS PELICANS" : "NOP",
"NEW ORLEANS/OKLAHOMA CITY HORNETS" : "NOK",
"NEW ORLEANS HORNETS" : "NOH",
"NEW YORK KNICKS" : "NYK",
"OKLAHOMA CITY THUNDER" : "OKC",
"SEATTLE SUPERSONICS" : "SEA",
"ORLANDO MAGIC" : "ORL",
"PHILADELPHIA 76ERS" : "PHI",
"SYRACUSE NATIONALS" : "SYR",
"PHOENIX SUNS" : "PHO",
"PORTLAND TRAIL BLAZERS" : "POR",
"SACRAMENTO KINGS" : "SAC",
#"KANSAS CITY KINGS" : "KCK", #dupe kansas city
#"KANSAS CITY-OMAHA KINGS" : "KCK", #dupe kansas city
"CINCINNATI ROYALS" : "CIN",
"ROCHESTER ROYALS" : "ROR",
"SAN ANTONIO SPURS" : "SAS",
"TORONTO RAPTORS" : "TOR",
"UTAH JAZZ" : "UTA",
"NEW ORLEANS JAZZ" : "NOJ",
"WASHINGTON WIZARDS" : "WAS",#dupe
"WASHINGTON BULLETS" : "WAS",#dupe
"CAPITAL BULLETS" : "CAP",
"BALTIMORE BULLETS" : "BAL",
#"CHICAGO ZEPHYRS" : "CHI", #dupe chicago
#"CHICAGO PACKERS" : "CHI",#dupe chicago
"ANDERSON PACKERS" : "AND",
#"CHICAGO STAGS" : "CHI", #dupe chicago
#"INDIANAPOLIS OLYMPIANS" : "IND", #dupe Indianapolis
"SHEBOYGAN RED SKINS" : "SRS",
"ST. LOUIS BOMBERS" : "SLB",
"WASHINGTON CAPITOLS" : "WAS",#dupe washington
#"WATERLOO HAWKS" : "WAT",#dupe waterloo
"SAN DIEGO ROCKETS" : "SDR"}

#example = get_team_misc("OKC" ,2010)
#print(example)


# {year: [[]]}
wonChamp = {
2022: "GOLDEN STATE WARRIORS",
2021: "MILWAUKEE BUCKS",
2020:	"LOS ANGELES LAKERS",
2019:	"TORONTO RAPTORS"	,
2018:	"GOLDEN STATE WARRIORS",	
2017:	"GOLDEN STATE WARRIORS"	,
2016:	"CLEVELAND CAVALIERS"	,
2015:	"GOLDEN STATE WARRIORS",	
2014:	"SAN ANTONIO SPURS"	,
2013:	"MIAMI HEAT"	,
2012:	"MIAMI HEAT"	,
2011:"DALLAS MAVERICKS",
2010:	"LOS ANGELES LAKERS",	
2009:	"LOS ANGELES LAKERS",	
2008	:"BOSTON CELTICS",
2007:	"SAN ANTONIO SPURS",	
2006:	"MIAMI HEAT"	,
2005:	"SAN ANTONIO" ,
2004:	"DETROIT PISTONS",	
2003:	"SAN ANTONIO SPURS",	
2002:	"LOS ANGELES LAKERS",	
2001:	"LOS ANGELES LAKERS",	
2000:	"LOS ANGELES LAKERS",	
1999:	"SAN ANTONIO SPURS"	,
1998:	"CHICAGO BULLS"	,
1997:	"CHICAGO BULLS"	,
1996:	"CHICAGO BULLS"	,
1995:	"HOUSTON ROCKETS",	
1994:	"HOUSTON ROCKETS"	,
1993:	"CHICAGO BULLS"	,
1992:	"CHICAGO BULLS"	,
1991:	"CHICAGO BULLS"	,
1990:	"DETROIT PISTONS",	
1989:	"DETROIT PISTONS"	,
1988:	"LOS ANGELES LAKERS",	
1987:	"LOS ANGELES LAKERS",
1986:	"BOSTON CELTICS",	
1985:	"LOS ANGELES LAKERS",	
1984:	"BOSTON CELTICS",	
1983:	"PHILADELPHIA 76ERS",	
1982:	"LOS ANGELES LAKERS",	
1981:	"BOSTON CELTICS",	
1980:	"LOS ANGELES LAKERS",	
1979:	"SEATTLE SUPERSONICS",	
1978:	"WASHINGTON BULLETS",	
1977:	"PORTLAND TRAIL BLAZERS",	
1976:	"BOSTON CELTICS",	
1975:	"GOLDEN STATE WARRIORS",
1974:	"BOSTON CELTICS",	
1973:	"NEW YORK KNICKS",	
1972:	"LOS ANGELES LAKERS",	
1971:	"MILWAUKEE BUCKS",	
1970:	"NEW YORK KNICKS",	
1969:	"BOSTON CELTICS",	
1968:	"BOSTON CELTICS",		
1967:	"PHILADELPHIA 76ERS",
1966:	"BOSTON CELTICS",		
1965:	"BOSTON CELTICS",		
1964:	"BOSTON CELTICS",		
1963:	"BOSTON CELTICS",	
1962:	"BOSTON CELTICS",		
1961:	"BOSTON CELTICS",
1960:	"BOSTON CELTICS",		
1959:	"BOSTON CELTICS",	
1958:	"ST. LOUIS HAWKS",		
1957:	"BOSTON CELTICS",		
1956:	"PHILADELPHIA WARRIORS",		
1955:	"SYRACUSE NATIONALS",		
1954:	"MINNEAPOLIS LAKERS",		
1953:	"MINNEAPOLIS LAKERS",	
1952:	"MINNEAPOLIS LAKERS",		
1951:	"ROCHESTER ROYALS",	
1950:	"MINNEAPOLIS LAKERS" 
}

DDL_Text = """CREATE TABLE IF NOT EXISTS Teams(
	        Team_Name CHAR(25),
	        yr INT,
	        Location CHAR(25),
          Wins REAL,
	        Won_Championship BOOLEAN,
	        PRIMARY KEY(Team_Name, yr)
	        \n\n\n ); \n"""
Inserts = "INSERT INTO Teams(Team_Name, yr, Location, Wins, Won_Championship) VALUES\n"
teamData = {}
champ = "N"
file = open("teams.sql", "w")
file.write(DDL_Text+Inserts)

count = 0
for year in range(2022,2023):
  teamInfo = {}
  for team in teamAbbrev.keys():
      abbrev = teamAbbrev[team]
      try:
        example = get_team_misc(abbrev,year)
      except :
        continue
      else:
        dataFrame = get_team_misc(abbrev,year)
        if(dataFrame[0] is not None):
          if(year>=1998 and abbrev == "WAS"):
            
            team = "WASHINGTON WIZARDS"
            
          elif(year<=1951 and abbrev == "WAS"):
            team = "WASHINGTON CAPITOLS"
          elif(year<1998 and abbrev == "WAS"):
            team = "WASHINGTON BULLETS"
          elif(year>=1961 and abbrev == "MIN"):
            team = "MINNESOTA TIMBERWOLVES"
          elif(year<1961 and abbrev == "MIN"):
            team = "MINNEAPOLIS LAKERS"
          elif(year<1964 and abbrev == "PHI"):
            team = "PHILADELPHIA WARRIORS"
          elif(year>=1964 and abbrev == "PHI"):
            team = "PHILADELPHIA 76ERS"
          location = team.split()
          team_list = team.split(" ")
          location = ""
          for i in range(0, len(team_list) - 1):
            location += team_list[i] + " "
          if (location[0:-1] =="GOLDEN STATE"):
            location = "SAN FRANCISCO "
          elif (location[0:-1] == "PORTLAND TRAIL"):
            location = "PORTLAND "
          champ= False
          if(team == wonChamp[year]):
            champ = True
          if(team in teamInfo):
            continue
          #('Team_Name', Year, 'Location', Wins, 'Won_Championship')
	        #(0, 'Alaa', 'Abdelnaby', '1968-06-24,', False, 'F-C', 82, 1991),
          inputTxt = team_list[-1], year,location[0:-1], dataFrame[1],champ,
          inputTxt = str(inputTxt)
          if(year==2022 and team == "WASHINGTON WIZARDS"):
            file.write(inputTxt+ "\n")
          else:
            file.write(inputTxt+ ","+ "\n")
	        
            
          teamInfo[team] = [team_list[-1],year, location[0:-1],dataFrame[1],champ] # add 0 or 1 at the end
          teamData[year] = teamInfo
          count = 0

#print("hello")
file.close()
#print(get_team_misc("ATL",2022))
finalValues = list(teamData.values())
count = 0
for x in finalValues:
  final = list(x.values())
  for y in final:
    print(y)
  print("          ")
 




          
        
  
        
    
  



