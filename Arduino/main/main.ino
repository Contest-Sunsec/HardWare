#include <DHT.h>

#define red 6
#define blue 7
#define green 8
#define soil_sensor A1
#define DHTPIN 2
#define DHTTYPE DHT22

void setup() {

  Serial.begin(9600);
  digitalWrite(red,OUTPUT);
  digitalWrite(blue,OUTPUT);
  digitalWrite(green,OUTPUT);

  DHT dht(DHTPIN, DHTTYPE);
  Serial.println("System Start...");
  
}

void loop() {

  int air_temp = dht.readTemperture();
  int air_hum = dht.readHumidity();
  
  

}
