#include <DHT.h>

#define red 6  //RGB red pin
#define blue 7  //RGB blue pin
#define green 8  //RGB green pin
#define soil_sensor A1 //Soil Humidity Sensor pin
#define light_sensor A2 //Light Sensor pin
#define DHTPIN 2 //air temp, humidity Sensor pin
#define DHTTYPE DHT22
#define GPS_RX 3 //GPS RX pin
#define GPS_TX 4 //GPS TX pin

int soil_ec = 0, soil_temp = 0, soil_hum = 0, air_temp = 0 , air_hum = 0 , soil_hum = 0 , light = 0 ; //sensor data

void setup() {

  Serial.begin(9600);
  digitalWrite(red,OUTPUT);
  digitalWrite(blue,OUTPUT);
  digitalWrite(green,OUTPUT);

  DHT dht(DHTPIN, DHTTYPE); //air temp, humidity Sensor
  Serial.println("System Start...");

  //LED Test

  digitalWrite(red,HIGH);
  digitalWrite(blue,LOW);
  digitalWrite(green,LOW);
  delay(100);
  digitalWrite(red,LOW);
  digitalWrite(blue,HIGH);
  digitalWrite(green,LOW);
  delay(100);
  digitalWrite(red,LOW);
  digitalWrite(blue,LOW);
  digitalWrite(green,HIGH);
  delay(100);
  digitalWrite(green,LOW);
  digitalWrite(blue,HIGH);
}

void loop() {
  if(serial.available() > 0){
    char c = serial.read();
    if(c == '1'){
      air_temp = dht.readTemperture(); //read air temp
      air_hum = dht.readHumidity(); //read air humidity
      soil_hum = analogRead(soil_sensor); //read soil humidity
      light = analogRead(light_sensor); //read light

      Serial.print("soil_ec:" + soil_ec); //send soil ec
      Serial.print("soil_temp:" + soil_temp); //send soil temp
      Serial.print("soil_hum:" + soil_hum); //send soil humidity
      Serial.print("Air Temperature: " + air_temp); //send air temp
      Serial.print(", Air Humidity: " + air_hum); //send air humidity
      Serial.print(", Soil Humidity: " + soil_hum); //send soil humidity
      Serial.println(", Light: " + light); //send light
      
      digitalWrite(red,LOW);
      digitalWrite(blue,LOW);
      digitalWrite(green,HIGH);
      delay(100);
      digitalWrite(green,LOW);

    }
    if(c == '2'){
      
    }
  }
}
