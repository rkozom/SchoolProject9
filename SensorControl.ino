#include "DHT.h"

#define DHTPIN 4     // Номер пина, к которому подключен сенсор на плате
#define DHTTYPE DHT22   // Тип сенсора

// Инициализация сенсора
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Действия при старте программы
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Ждем 3 секунды перед очередным считыванием данных с сенсора
  delay(3000);

  // Получаем данные по влажности
  float h = dht.readHumidity();
  // Получаем даные по температуре в градусах цельсия
  float t = dht.readTemperature();

  // Проверяем, все ли данные удалось прочитать. Если не удалось,
  // то выполняем ранний выход из цикла, чтобы попробовать еще раз
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Serial.print(F("h="));
  Serial.print(h);
  Serial.print(F(";"));
  Serial.println(t);
}
