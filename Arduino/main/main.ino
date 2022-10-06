#include <DHT.h>
#include <SoftwareSerial.h>
#include <Wire.h>

#define red 7  //RGB red pin
#define blue 8  //RGB blue pin
#define green 9  //RGB green pin
#define soil_sensor A1 //Soil Humidity Sensor pin
#define light_sensor A2 //Light Sensor pin
#define DHTPIN 2 //air temp, humidity Sensor pin
#define DHTTYPE DHT22
#define GPS_RX 3 //GPS RX pin
#define GPS_TX 4 //GPS TX pin

int soil_ec = 0, soil_temp = 0, soil_hum = 0, air_temp = 0 , air_hum = 0 , soil_hum = 0 , light = 0 ; //sensor data

SoftwareSerial gpsSerial(6,5); //GPS 모듈
// RX = 6
// TX = 5

char c = ""; // \n 인지 구분 및 str에 저장
String str = ""; // \n 전까지 c 값을 저장
String targetStr = "GPGGA"; // str의 값이 NMEA의 GPGGA 값인지 지정

void led() { //녹색 LED 깜빡임
  digitalWrite(red,LOW);
  digitalWrite(blue,LOW);
  digitalWrite(green,HIGH);
  delay(100);
  digitalWrite(green,LOW);
  delay(100);
  digitalWrite(green,HIGH);
  delay(100);
  digitalWrite(green,LOW);
}

void setup() {
  Wire.begin();
  gpsSerial.begin(9600);
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
      Serial.print(" soil_temp:" + soil_temp); //send soil temp
      Serial.print(" soil_hum:" + soil_hum); //send soil humidity
      Serial.print(" Air Temperature: " + air_temp); //send air temp
      Serial.print(" Air Humidity: " + air_hum); //send air humidity
      Serial.print(" Soil Humidity: " + soil_hum); //send soil humidity
      Serial.println(" Light: " + light); //send light
      
      led();

    }
    if(c == '2'){
        if(gpsSerial.available()) // gps 센서 통신 가능 여부 확인
    {
      c = gpsSerial.read(); //gps 센서 값 읽기
      
      if(c == '\n')// \n 일시. 지금까지 저장된 str 값이 targetStr과 맞는지 구분
        { 
        
        if(targetStr.equals(str.substring(1, 6))) // NMEA 의 GPGGA 값일시
          { 
          // Serial.println(str); //디버깅용, 파싱 전 값 출력
          
          // , 기준 파싱
          int first = str.indexOf(",");
          int two = str.indexOf(",", first+1);
          int three = str.indexOf(",", two+1);
          int four = str.indexOf(",", three+1);
          int five = str.indexOf(",", four+1);

          // index 추출
          String Lat = str.substring(two+1, three);
          String Long = str.substring(four+1, five);

          // 앞값과 뒷값을 구분
          String Lat1 = Lat.substring(0, 2);
          String Lat2 = Lat.substring(2);

          // 앞값과 뒷값을 구분
          String Long1 = Long.substring(0, 3);
          String Long2 = Long.substring(3);

          // 좌표 계산
          double LatF = Lat1.toDouble() + Lat2.toDouble()/60;
          float LongF = Long1.toFloat() + Long2.toFloat()/60;

          // 좌표 출력
          Serial.print("latitude: ");
          Serial.println(LatF, 15);
          Serial.print("longitude: ");
          Serial.println(LongF, 15);
        }

        // str 값 초기화 
        str = "";
        
      } else // \n 아닐시, str에 문자를 계속 더하기
        { 
        str += c;
      }

      led();
    
    }
  }
}
