#include <DHT.h>

#define red 6  //RGB red pin
#define blue 7  //RGB blue pin
#define green 8  //RGB green pin
#define soil_sensor A1 //Soil Humidity Sensor pin
#define DHTPIN 2 //air temp, humidity Sensor pin
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
  int soil_hum = analogRead(soil_sensor);
  

  delay(1500);
  

}
