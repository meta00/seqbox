-- Create a new database called 'oucru_robot'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'oucru_robot'
)
CREATE DATABASE oucru_robot;
GO
-- Create a new table called 'sample' in schema 'SchemaOucru'
-- Create the table in the specified schema
CREATE TABLE SchemaOucru.sample
(
    id_sample VARCHAR(50)  PRIMARY KEY, -- primary key column
    num_sequence VARCHAR(50),
    date_time  DATETIME,
    organism  VARCHAR(50),
    batch VARCHAR(50),
    location VARCHAR(50),
    path_r1 VARCHAR(50),
    path_r2 VARCHAR(50),
    result1 INTEGER,
    result2 INTEGER,
    FOREIGN KEY (result1) REFERENCES result1 (id_result1),
    FOREIGN KEY (result2) REFERENCES result2 (id_result2),
    FOREIGN KEY (location) REFERENCES location (id_location),
    FOREIGN KEY (batch)  REFERENCES batch (id_batch), 

    
);
GO

-- Create a new table called 'batch' in schema 'SchemaOucru'
-- Create the table in the specified schema
CREATE TABLE SchemaOucru.batch
(
    id_batch INT NOT NULL PRIMARY KEY, -- primary key column
    name_batch VARCHAR(50),
    date_batch DATE,
    instrument VARCHAR(50),
    primes VARCHAR(50),
    location VARCHAR(50),

);
GO

-- Create a new table called 'location' in schema 'SchemaOucru'

-- Create the table in the specified schema
CREATE TABLE SchemaOucru.location
(
    id_location INT NOT NULL PRIMARY KEY, -- primary key column
    continent VARCHAR(50),
    country VARCHAR(50),
    province VARCHAR(50),
    city VARCHAR(50),
);
GO

-- Create a new table called 'result1' in schema 'SchemaOucru'
-- Create the table in the specified schema
CREATE TABLE SchemaOucru.result1
(
    id_result1 INT NOT NULL PRIMARY KEY, -- primary key column
    qc VARCHAR(50),
    ql VARCHAR(50),
    description VARCHAR(50),
    mean_depth  DOUBLE PRECISION,
    coverage  DOUBLE PRECISION,
    snapper_variants INTEGER,
    snapper_ignored INTEGER,
    num_heterozygous INTEGER,

);
GO

-- Create a new table called 'result2' in schema 'SchemaOucru'
-- Create the table in the specified schema
CREATE TABLE SchemaOucru.result2
(
    id_result2 INT NOT NULL PRIMARY KEY, -- primary key column
    mykrobe_version VARCHAR(50),
    phylo_grp VARCHAR(50),
    phylo_grp_covg DOUBLE PRECISION,
    phylo_grp_depth DOUBLE PRECISION,
    species  VARCHAR(50),
    species_covg DOUBLE PRECISION,
    species_depth DOUBLE PRECISION,
    lineage VARCHAR(50),
    lineage_covg DOUBLE PRECISION,
    lineage_depth DOUBLE PRECISION,
    susceptibility VARCHAR(50),
    variants VARCHAR(50),
    genes VARCHAR(50),
    drug VARCHAR(50),
);
GO

-- Create a new table called 'study' in schema 'SchemaOucru'
-- Create the table in the specified schema
CREATE TABLE SchemaOucru.study
(
    id_study VARCHAR(50) NOT NULL PRIMARY KEY, -- primary key column
    date_study DATE,
    result_study VARCHAR(50),    
);
GO

-- Create a new table called 'sample_study' in schema 'SchemaOucru'
-- Create the table in the specified schema
CREATE TABLE SchemaOucru.sample_study
(
    id_sample VARCHAR(50) NOT NULL PRIMARY KEY, -- primary key column
    id_study VARCHAR(50)  NOT NULL PRIMARY KEY,
    FOREIGN KEY (id_sample) REFERENCES sample,
    FOREIGN KEY (id_study) REFERENCES study,
    
);
GO