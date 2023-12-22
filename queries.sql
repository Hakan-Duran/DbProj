ALTER TABLE archive.country_data
MODIFY COLUMN ISO3 VARCHAR(3),
MODIFY COLUMN Country VARCHAR(100),
MODIFY COLUMN hdicode VARCHAR(10),
MODIFY COLUMN region VARCHAR(3),
MODIFY COLUMN hdi_rank_2021 INT;

ALTER TABLE archive.co2_production
MODIFY COLUMN ISO3 VARCHAR(3),
MODIFY COLUMN Country VARCHAR(100),
MODIFY COLUMN hdicode VARCHAR(10),
MODIFY COLUMN region VARCHAR(3),
MODIFY COLUMN hdi_rank_2021 INT;

ALTER TABLE archive.gross_national_income_per_capital
MODIFY COLUMN ISO3 VARCHAR(3),
MODIFY COLUMN Country VARCHAR(100),
MODIFY COLUMN hdicode VARCHAR(10),
MODIFY COLUMN region VARCHAR(3),
MODIFY COLUMN hdi_rank_2021 INT;

ALTER TABLE archive.human_development_index
MODIFY COLUMN ISO3 VARCHAR(3),
MODIFY COLUMN Country VARCHAR(100),
MODIFY COLUMN hdicode VARCHAR(10),
MODIFY COLUMN region VARCHAR(3),
MODIFY COLUMN hdi_rank_2021 INT;

ALTER TABLE archive.life_expectancy_by_birth
MODIFY COLUMN ISO3 VARCHAR(3),
MODIFY COLUMN Country VARCHAR(100),
MODIFY COLUMN hdicode VARCHAR(10),
MODIFY COLUMN region VARCHAR(3),
MODIFY COLUMN hdi_rank_2021 INT;

ALTER TABLE archive.country_data
ADD PRIMARY KEY (ISO3);

ALTER TABLE archive.co2_production
ADD PRIMARY KEY (ISO3);

ALTER TABLE archive.gross_national_income_per_capital
ADD PRIMARY KEY (ISO3);

ALTER TABLE archive.human_development_index
ADD PRIMARY KEY (ISO3);

ALTER TABLE archive.life_expectancy_by_birth
ADD PRIMARY KEY (ISO3);

CREATE INDEX idxiso ON archive.country_data(ISO3);
CREATE INDEX idxcountry ON archive.country_data(Country);
CREATE INDEX idxreg ON archive.country_data(region);
CREATE INDEX idxhdi ON archive.country_data(hdicode);
CREATE INDEX idxhdirank ON archive.country_data(hdi_rank_2021);

ALTER TABLE archive.co2_production
ADD FOREIGN KEY (ISO3)
REFERENCES archive.country_data(ISO3)
ON DELETE RESTRICT
ON UPDATE RESTRICT;

ALTER TABLE archive.co2_production
ADD FOREIGN KEY (Country)
REFERENCES archive.country_data(Country)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.co2_production
ADD FOREIGN KEY (region)
REFERENCES archive.country_data(region)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.co2_production
ADD FOREIGN KEY (hdicode)
REFERENCES archive.country_data(hdicode)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.co2_production
ADD FOREIGN KEY (hdi_rank_2021)
REFERENCES archive.country_data(hdi_rank_2021)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.gross_national_income_per_capital
ADD FOREIGN KEY (ISO3)
REFERENCES archive.country_data(ISO3)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.gross_national_income_per_capital
ADD FOREIGN KEY (Country)
REFERENCES archive.country_data(Country)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.gross_national_income_per_capital
ADD FOREIGN KEY (region)
REFERENCES archive.country_data(region)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.gross_national_income_per_capital
ADD FOREIGN KEY (hdicode)
REFERENCES archive.country_data(hdicode)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.gross_national_income_per_capital
ADD FOREIGN KEY (hdi_rank_2021)
REFERENCES archive.country_data(hdi_rank_2021)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.human_development_index
ADD FOREIGN KEY (ISO3)
REFERENCES archive.country_data(ISO3)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.human_development_index
ADD FOREIGN KEY (Country)
REFERENCES archive.country_data(Country)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.human_development_index
ADD FOREIGN KEY (region)
REFERENCES archive.country_data(region)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.human_development_index
ADD FOREIGN KEY (hdicode)
REFERENCES archive.country_data(hdicode)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.human_development_index
ADD FOREIGN KEY (hdi_rank_2021)
REFERENCES archive.country_data(hdi_rank_2021)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.life_expectancy_by_birth
ADD FOREIGN KEY (ISO3)
REFERENCES archive.country_data(ISO3)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.life_expectancy_by_birth
ADD FOREIGN KEY (Country)
REFERENCES archive.country_data(Country)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.life_expectancy_by_birth
ADD FOREIGN KEY (region)
REFERENCES archive.country_data(region)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.life_expectancy_by_birth
ADD FOREIGN KEY (hdicode)
REFERENCES archive.country_data(hdicode)
ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE archive.life_expectancy_by_birth
ADD FOREIGN KEY (hdi_rank_2021)
REFERENCES archive.country_data(hdi_rank_2021)
ON DELETE RESTRICT
ON UPDATE CASCADE;

UPDATE `archive`.`country_data` SET `Country` = 'Ivory Coast' WHERE (`ISO3` = 'CIV');
UPDATE `archive`.`country_data` SET `Country` = 'Turkey' WHERE (`ISO3` = 'TUR');



