#include <Adafruit_Sensor.h>
#include <SoftwareSerial.h>
#include <DHT.h>
#include <Wire.h>

#define soil_sensor A1 //Soil Humidity Sensor pin
#define light_sensor A2 //Light Sensor pin
#define soil_sensor A1
#define DHTPIN 2

int GPS_RX = 3, GPX_TX = 4;

int soil_ec = 0;
int soil_temp = 0; 
int soil_hum = 0;
int air_temp = 0; 
int air_hum = 0; 
int light = 0 ; //sensor data

SoftwareSerial gpsSerial(6,5); //GPS 모듈
// RX = 6
// TX = 5

DHT dht(DHTPIN, DHT22); //air temp, humidity Sensor

char c = ""; // \n 인지 구분 및 str에 저장
String str = ""; // \n 전까지 c 값을 저장
String targetStr = "GPGGA"; // str의 값이 NMEA의 GPGGA 값인지 지정

double LatF = 0.0;
float LongF = 0.0;

void led() { //녹색 LED 깜빡임
  digitalWrite(7,LOW);
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  delay(100);
  digitalWrite(9,LOW);
  delay(100);
  digitalWrite(9,HIGH);
  delay(100);
  digitalWrite(9,LOW);
  delay(100);
  digitalWrite(8,HIGH);
}

void gps(){
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
        }

        // str 값 초기화 
        str = "";
        
      } else // \n 아닐시, str에 문자를 계속 더하기
        { 
        str += c;
      }
    }
}

void setup() {
  
  Wire.begin();
  gpsSerial.begin(9600);
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);

  //LED Test
  digitalWrite(7,HIGH);
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
  delay(100);
  digitalWrite(7,LOW);
  digitalWrite(8,HIGH);
  digitalWrite(9,LOW);
  delay(100);
  digitalWrite(7,LOW);
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  delay(100);
  digitalWrite(9,LOW);
  digitalWrite(8,HIGH);
}

void loop() {

  int h = dht.readTemperature();
  int t = dht.readHumidity();
  
  if(h < 0){
    h = h*(-1); 
  }
  if(h > 0 && t > 0) { 
    air_temp = h; //read air temp
    air_hum = t; //read air humidity
  }
  soil_hum = analogRead(soil_sensor); //read soil humidity
  soil_hum = map(soil_hum, 170, 1023, 100, 0); // %
  light = analogRead(light_sensor); //read light
  
  if(Serial.available()){
    char cmd = Serial.read();
    if(cmd == 'g'){
      Serial.println(soil_ec); //send soil ec
      Serial.println(soil_temp); //send soil temp
      Serial.println(soil_hum); //send soil humidity
      Serial.println(air_temp); //send air temp
      Serial.println(air_hum); //send air humidity
      Serial.println(light); //send light
      gps();
      Serial.println(LatF, 15); //send latitude
      Serial.println(LongF, 15); //send longitude

      led();
    }
  }

}
