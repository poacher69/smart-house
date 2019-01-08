//I2C LCD  -GND-VCC-SDA-SCL   ---LCD腳位
//接Arduino-GND-5V -A4 -A5    ---Arduino接腳

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
// 設定 LCD I2C 位址
// Set the pins on the I2C chip used for LCD connections:
// addr, en,rw,rs,d4,d5,d6,d7,bl,blpol
//LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);//原檔案
LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
void setup() {
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

// 輸出初始化文字
lcd.setCursor(0, 0); // 設定游標位置在第一行行首
lcd.print("ICshop&MakerPRO");
delay(1000);
lcd.setCursor(0, 1); // 設定游標位置在第二行行首
lcd.print("Hello, Maker!");
delay(8000);
lcd.clear(); //顯示清除

}

void loop() {
 lcd.setCursor(0, 0); // 設定游標位置在第一行行首
lcd.print("ICshop&MakerPRO");
lcd.setCursor(0, 1); // 設定游標位置在第二行行首
lcd.print(millis()/1000);   //millis() 函式會回傳 Arduino 從開始執行程式一直到目前為止的千分之一秒數值


}
