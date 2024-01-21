#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Adafruit_GFX.h>
#include <DHT.h>
#include <Adafruit_ILI9341.h>
#include <BluetoothSerial.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include "MAX30105.h"

#define ONE_WIRE_BUS 4 // GPIO pin to which DS18B20 is connected

MAX30105 particleSensor;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

BluetoothSerial SerialBT;

DHT dht(DHT_PIN, DHT_TYPE);

int heartrate;
int data[2] = {-1, -1};

void setup() {
  Serial.begin(115200);
  SerialBT.begin("Water Part");

  esp_bd_addr_t address;
  esp_err_t ret = esp_efuse_mac_get_default(address);
  
  if (ret != ESP_OK) {
    Serial.println("Failed to get Bluetooth address");
  } else {
    Serial.printf("Bluetooth Address: %02X:%02X:%02X:%02X:%02X:%02X\n",
                  address[0], address[1], address[2],
                  address[3], address[4], address[5]);
  }

  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30105 was not found. Please check wiring/power.");
    while (1);
  }
  
  particleSensor.setup();
  particleSensor.setPulseAmplitudeRed(0x0A);
  particleSensor.setPulseAmplitudeGreen(0);

  dht.begin();
  sensors.begin();
}

void loop() {
  delay(1000);  // Wait for 1 seconds between measurements

  if (particleSensor.available()) {
    int heartRate = particleSensor.getHeartRate();
    int spo2 = particleSensor.getSpO2();

    data[0] = heartRate;
  }
  else {
    data[0] = NULL;
  }

  sensors.requestTemperatures();

  float temperatureCelsius = sensors.getTempCByIndex(0);

  if (temperatureCelsius != DEVICE_DISCONNECTED_C) {
    data[1] = temperatureCelsius;
  } else {
    Serial.println("Error reading temperature");
  }

  char buffer[20];
  sprintf(buffer, "%d#--#%d", data[0], data[1]);

  SerialBT.println(buffer);
}
