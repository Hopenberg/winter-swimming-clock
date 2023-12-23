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
int data[2] = {-1, -1};

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  delay(2000);  // Wait for 2 seconds between measurements

  data[0] = readHeartrate();

  if (isnan(data[0]) || isnan(data[1])) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  sendData(data);

  Serial.print("Heartrate: ");
  Serial.print(data[0]);
  Serial.print("Temperature: ");
  Serial.print(data[1]);
  Serial.println("°C");
}

int readHeartrate() {
  return random(10);
}

void sendData(int *data) {

}