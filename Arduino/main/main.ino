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

int air_temp = 0 , air_hum = 0 , soil_hum = 0 , light = 0 ;

void setup() {

  Serial.begin(9600);
  digitalWrite(red,OUTPUT);
  digitalWrite(blue,OUTPUT);
  digitalWrite(green,OUTPUT);

  DHT dht(DHTPIN, DHTTYPE);
  Serial.println("System Start...");

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
  
  digitalWrite(green,LOW);
  digitalWrite(blue,HIGH);
}

void loop() {
  if(serial.available() > 0){
    char c = serial.read();
    if(c == '1'){
      air_temp = dht.readTemperture();
      air_hum = dht.readHumidity();
      soil_hum = analogRead(soil_sensor);
      light = analogRead(light_sensor);

      Serial.print("Air Temperature: " + air_temp);
      Serial.print(", Air Humidity: " + air_hum);
      Serial.print(", Soil Humidity: " + soil_hum);
      Serial.println(", Light: " + light);
      
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
