CREATE DATABASE sistema_hospitalar;

-- Usar a base de dados
USE sistema_hospitalar;

-- Criar a tabela paciente
CREATE TABLE paciente (
    ID_Paciente INT AUTO_INCREMENT UNIQUE,
    Nome VARCHAR(128) NOT NULL,
    CPF VARCHAR(14) NOT NULL UNIQUE,
    Data_Nascimento DATETIME NOT NULL,
    Tipo_Sanguineo VARCHAR(3),
    Telefone VARCHAR(17) NOT NULL,
    Endereco VARCHAR(64) NOT NULL,
    Genero VARCHAR(10) NOT NULL,
    PRIMARY KEY (ID_Paciente)
);

-- Criar a tabela prestador
CREATE TABLE prestador (
    ID_Prestador INT AUTO_INCREMENT,
    Nome VARCHAR(128) NOT NULL,
    CPF VARCHAR(14) UNIQUE,
    Data_Nascimento DATE NOT NULL,
    Tipo_Sanguineo VARCHAR(3),
    Telefone VARCHAR(17),
    Endereco VARCHAR(64),
    Genero VARCHAR(10) NOT NULL,
    Especialidade VARCHAR(20) NOT NULL,
    Tipo_Prestador VARCHAR(15) NOT NULL,
    PRIMARY KEY (ID_Prestador)
);

-- Criar a tabela Usuario
CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT UNIQUE,
    ID_Prestador INT,
    Tipo_Prestador VARCHAR(15),
    Senha VARCHAR(8) NOT NULL,
    Status BOOLEAN NOT NULL,
    Perfil VARCHAR(30) NOT NULL,
    PRIMARY KEY (ID_Usuario),
    FOREIGN KEY (ID_Prestador) REFERENCES prestador(ID_Prestador)
);

-- Criar a tabela Prontuario
CREATE TABLE Prontuario (
    ID_Prontuario INT AUTO_INCREMENT UNIQUE,
    ID_Prestador INT,
    ID_Paciente INT,
    Pressao VARCHAR(16),
    Tipo_Atendimento VARCHAR(64),
    Nome_Medicamento VARCHAR(128),
    Receber_Medicacao BOOLEAN,
    Data DATETIME,
    PRIMARY KEY (ID_Prontuario),
    FOREIGN KEY (ID_Prestador) REFERENCES prestador(ID_Prestador),
    FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID_Paciente)
);

-- Criar a tabela atendimento
CREATE TABLE atendimento (
    ID_Atendimento INT AUTO_INCREMENT,
    ID_Prestador INT,
    ID_Prontuario INT,
    ID_Paciente INT,
    Tipo_Atendimento VARCHAR(64),
    Prioridade VARCHAR(16),
    Data DATETIME,
    Pressao VARCHAR(16),
    PRIMARY KEY (ID_Atendimento),
    FOREIGN KEY (ID_Prestador) REFERENCES prestador(ID_Prestador),
    FOREIGN KEY (ID_Prontuario) REFERENCES prontuario(ID_Prontuario),
    FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID_Paciente)
);

-- Criar a tabela consultorio
CREATE TABLE consultorio (
    ID_Consultorio INT AUTO_INCREMENT UNIQUE,
    Nome_Sala VARCHAR(16) NOT NULL,
    ID_Prestador INT,
    ID_Atendimento INT,
    ID_Paciente INT,
    PRIMARY KEY (ID_Consultorio),
    FOREIGN KEY (ID_Prestador) REFERENCES prestador(ID_Prestador),
    FOREIGN KEY (ID_Atendimento) REFERENCES atendimento(ID_Atendimento),
    FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID_Paciente)
);

-- Criar a tabela ambulatorio
CREATE TABLE ambulatorio (
    ID_Ambulatorio INT AUTO_INCREMENT UNIQUE,
    Poltrona INT NOT NULL,
    Nome_Ambulatorio VARCHAR(16) NOT NULL,
    ID_Consultorio INT,
    ID_Prestador INT,
    ID_Paciente INT,
    PRIMARY KEY (ID_Ambulatorio),
    FOREIGN KEY (ID_Consultorio) REFERENCES consultorio(ID_Consultorio),
    FOREIGN KEY (ID_Prestador) REFERENCES prestador(ID_Prestador),
    FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID_Paciente)
);
