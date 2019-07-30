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
