# Школьный проект по информатике 9 класс
## Описание проекта
Проект состоит из нескольких частей и предназначен для сбора данных с датчиков Arduino и помещения этих данных в специализированную базу данных.
## Составные части проекта
### Управляющий код для Arduino (SensorControl.ino)
Скетч, написанный на языке C++, считывающий данные о температуре и влажности с датчика DHT-11 или DHT-22, и передающий их в поток в определенном формате.
### Модуль чтения данных из потока (ReadSerial)
Программа, написанная на Python и запускающаяся из командной строки, производит чтение данных из COM-порта, производит верификацию полученных данных и отправляет их по протоколу HTTP в базу данных.
### База данных и API для хранения данных (DataProcessor)
Для хранения данных, полученных с датчиков и для организаци API, используется фреймворк Django.