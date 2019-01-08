//溫度感測,溫度顯示在LCD上
//I2C LCD  -GND-VCC-SDA-SCL   ---LCD腳位接下Arduino腳位
//接Arduino-GND-5V -A4 -A5    ---Arduino接腳
//DS18B20溫度感知sensor +接5V,-接GND,OUT接Arduino第2腳

//溫度感知套件-start
#include <OneWire.h>  // 匯入程式庫標頭檔 
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 2  // Arduino數位腳位2(DIGITAL)接到OUT
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
//溫度感知套件-end

float val;

//LCD套件-start
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
//LCD套件-end

void setup() {
  Serial.begin(9600);      // 監控視窗波特率为9600
  Serial.println("Temperature Sensor start");
  sensors.begin();    // 初始化 

   // 初始化 LCD，一行 16 的字元，共 2 行，預設開啟背光
lcd.begin(16, 2);

// 閃爍三次
for(int i = 0; i < 3; i++) {
lcd.backlight(); // 開啟背光
delay(250);
lcd.noBacklight(); // 關閉背光
delay(250);
}
lcd.backlight();
}

void loop() {
// 要求匯流排上的所有感測器進行溫度轉換（不過我只有一個） 
  sensors.requestTemperatures();//原始檔
val = sensors.getTempCByIndex(0) ; // 參數0代表匯流排上第0個1-Wire裝置 
  Serial.println(val);//直接顯示溫度
lcd.setCursor(0, 0); // 設定游標位置在第一行行首
lcd.print("temperature");
lcd.setCursor(0, 1); // 設定游標位置在第二行行首
lcd.print(val);

}
