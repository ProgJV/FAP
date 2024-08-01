CREATE TABLE consultorio(
	ID_consultorio INT AUTO_INCREMENT UNIQUE,
    nome_sala_consultorio (VARCHAR(16)) NOT NULL,
    PRIMARY KEY(ID_consultorio),
    FOREIGN KEY(ID_prestador) REFERENCES prestador(ID_prestador),
    FOREIGN KEY(ID_atendimento) REFERENCES atendimento(ID_atendimento),
    FOREIGN KEY(ID_paciente) REFERENCES paciente(ID_paciente)
);

CREATE TABLE ambulatorio (
	ID_ambulatorio int AUTO_INCREMENT UNIQUE,
    poltrona INT NOT NULL,
    nome_sala_ambulatorio (VARCHAR(16)) NOT NULL,
    PRIMARY KEY(ID_ambulatorio),
    FOREIGN KEY(ID_consultorio) REFERENCES consultorio(ID_consultorio),
    FOREIGN KEY(ID_prestador) REFERENCES prestador(ID_prestador),
    FOREIGN KEY(ID_paciente) REFERENCES paciente(ID_paciente)
);