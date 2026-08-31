#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include "HX711.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

const char* WIFI_SSID = "YOUR_WIFI";
const char* WIFI_PASS = "YOUR_PASSWORD";
const char* MQTT_HOST = "192.168.10.30";

WiFiClient net;
PubSubClient mqtt(net);
HX711 scale;
Adafruit_MPU6050 mpu;

constexpr int HX_DOUT = 4;
constexpr int HX_SCK  = 5;
constexpr int PRESENCE_PIN = 27;

float calibration_factor = -7050.0f;

void connect_wifi() {
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) delay(300);
}

void connect_mqtt() {
  while (!mqtt.connected()) {
    mqtt.connect("ESP32-SORTING-CELL");
    delay(500);
  }
}

float read_weight_kg() {
  if (!scale.is_ready()) return -1.0f;
  return max(0.0f, (float)scale.get_units(3) / 1000.0f);
}

float vibration_rms() {
  sensors_event_t a, g, t;
  mpu.getEvent(&a, &g, &t);
  const float mag = sqrt(a.acceleration.x*a.acceleration.x +
                         a.acceleration.y*a.acceleration.y +
                         a.acceleration.z*a.acceleration.z);
  return fabs(mag - 9.81f);
}

void publish_telemetry() {
  float weight = read_weight_kg();
  float vib = vibration_rms();
  int presence = digitalRead(PRESENCE_PIN);

  char payload[256];
  snprintf(payload, sizeof(payload),
    "{\"device\":\"ESP32-01\",\"weight_kg\":%.3f,\"vibration_rms\":%.3f,\"presence\":%d}",
    weight, vib, presence);

  mqtt.publish("factory/cell01/telemetry", payload);
}

void setup() {
  Serial.begin(115200);
  pinMode(PRESENCE_PIN, INPUT_PULLUP);

  scale.begin(HX_DOUT, HX_SCK);
  scale.set_scale(calibration_factor);
  scale.tare();

  if (!mpu.begin()) {
    Serial.println("MPU6050 not detected");
  }

  connect_wifi();
  mqtt.setServer(MQTT_HOST, 1883);
}

void loop() {
  if (!mqtt.connected()) connect_mqtt();
  mqtt.loop();

  static uint32_t last = 0;
  if (millis() - last > 1000) {
    last = millis();
    publish_telemetry();
  }
}
