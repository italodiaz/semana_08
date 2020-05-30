-- DATABASE NAME : reto_semana8
DROP TABLE IF EXISTS alquiler;
DROP TABLE IF EXISTS lector;
DROP TABLE IF EXISTS libro;
DROP TABLE IF EXISTS editorial;
DROP TABLE IF EXISTS autor;

create table editorial(
	id serial primary key not null,
	nombre text not null
);

create table autor(
	id serial primary key not null,
	nombre text not null
);

create table libro(
	id serial primary key not null,
	titulo text not null,
	stock integer not null,
	id_editorial integer not null references editorial(id),
	id_autor integer not null references autor(id)
);
create table lector(
	id serial primary key not null,
	nombre text not null,
	apellido_paterno text not null,
	apellido_materno text not null default '',
	correo text not null default '',
	dni text not null,
	fecha_registro timestamp without time zone not null default now()
);

create table alquiler(
	id serial primary key not null,
	id_libro integer not null references libro(id),
	id_lector integer not null references lector(id),
	fecha_prestamo timestamp without time zone not null,
	fecha_devolucion timestamp without time zone, -- Inicialmente nulo se actualiza con devolución
	limite_entrega date not null
);

/*
NOTAS:

El calculo del stock actual se hara en base a la cantidad de libros
que aun no han sido devueltos en la tabla "alquiler"

Es decir, 
stock_actual = (tabla "libro_editorial" columna stock) - (cantidad sin devolver tabla "alquiler")

*/