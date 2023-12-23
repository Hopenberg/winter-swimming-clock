#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Adafruit_GFX.h>
#include <DHT.h>
#include <Adafruit_ILI9341.h>

#define DHT_PIN 2  
#define DHT_TYPE DHT22

DHT dht(DHT_PIN, DHT_TYPE);

int heartrate;
int data[2];

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  delay(2000);  // Wait for 2 seconds between measurements

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");
}

int readHeartrate() {
  return random(10);
}

void sendData(int *data) {

}