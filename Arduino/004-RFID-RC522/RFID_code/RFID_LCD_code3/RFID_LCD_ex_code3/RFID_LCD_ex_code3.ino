//RFID     -3.3V-RST-GND-IRQ-MISO-MOSI-SCK-SDA ----RFID腳位接下方Arduino腳位
//接Arduino-3.3V-A0 -GND- 空-12  - 11 -13 -10  ----Arduino接腳
//////////////////////////////////////////////////////////////////////////
//I2C LCD  -GND-VCC-SDA-SCL   ---LCD腳位接下方Arduino腳位
//接Arduino-GND-5V -A4 -A5    ---Arduino接腳
/////////////////////////////////////////////////////////////////////////
//RFID套件-start
#include <SPI.h>
#include <MFRC522.h>     // 引用程式庫 
#define RST_PIN      A0        // 讀卡機的重置腳位
#define SS_PIN       10        // 晶片選擇腳位
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件
//RFID套件-end

//LCD套件-start
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
//LCD套件-end

void setup() {
  Serial.begin(9600);  // 設定串列通訊速率
  Serial.println("RFID-LCD reader is ready!");
  //RFID載入-start
  SPI.begin();   // 設定  SPI bus
  mfrc522.PCD_Init();   // 初始化MFRC522讀卡機模組
  //RFID載入-end

  //LCD載入-start
lcd.begin(16, 2); // 初始化 LCD，一行 16 的字元，共 2 行
lcd.backlight();  //開啟背光
  //LCD載入-end
}

void loop() {
  if ( ! mfrc522.PICC_IsNewCardPresent()) // 是否為新卡？
  {
    return;
  }

  if ( ! mfrc522.PICC_ReadCardSerial())   // 選擇一張卡
  {
    return;
  }
  //Show UID on serial monitor
  Serial.print("Card No. :");
  String content = "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print(" Message : ");
  content.toUpperCase();

   if (content.substring(1) == "10 77 4F A8")
   {
    lcd.clear();  //清除螢幕顯示的資料
    lcd.setCursor(0, 0); // 設定游標位置在第一行行首(
    lcd.print("Hello! Jayjay");
    lcd.setCursor(0, 1); // 設定游標位置在第二行行首
    lcd.print("Room 888 Unlock");
   }
   if  (content.substring(1) == "46 DB 52 A3") 
   {
    lcd.clear();  //清除螢幕顯示的資料
    lcd.setCursor(0, 0); // 設定游標位置在第一行行首(第幾字元開始顯示,0第1行)
    lcd.print("Hello! Patty");
    lcd.setCursor(0, 1); // 設定游標位置在第二行行首(第幾字元開始顯示,1第2行)
    lcd.print("Room 999 Unlock");
   }
     delay(3000);
     
 
} //main end
