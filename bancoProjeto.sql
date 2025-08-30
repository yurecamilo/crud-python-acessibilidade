create database projeto;
use projeto;

create table locais (
	idLocal int primary key auto_increment,
    nome varchar (80),
    endereco varchar (256) not null,
    tipo varchar (50) not null
);


