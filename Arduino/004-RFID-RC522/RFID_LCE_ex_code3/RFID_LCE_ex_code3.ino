//RFID     -3.3V-RST-GND-IRQ-MISO-MOSI-SCK-SDA ----RFID腳位
//接Arduino-3.3V-A0 -GND- 空-12  - 11 -13 -10  ----Arduino接腳

//RFID套件-start
#include <SPI.h>
#include <MFRC522.h>     // 引用程式庫 
#define RST_PIN      A0        // 讀卡機的重置腳位
#define SS_PIN       10        // 晶片選擇腳位
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件
//RFID套件-end

//溫度感知套件-start
#include <OneWire.h>  // 匯入程式庫標頭檔 
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 2  // Arduino數位腳位2(DIGITAL)接到OUT
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
//溫度感知套件-end

void setup() {
  Serial.begin(9600);  // 設定串列通訊速率
  Serial.println("RFID reader is ready!");
  //RFID載入-start
  SPI.begin();   // 設定  SPI bus
  mfrc522.PCD_Init();   // 初始化MFRC522讀卡機模組
  //RFID載入-end

  //LCD載入-start
sensors.begin();  // LCD初始化  
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
    lcd.setCursor(0, 0); // 設定游標位置在第一行行首
    lcd.print("111111");
    lcd.setCursor(0, 1); // 設定游標位置在第二行行首
    lcd.print("222222");
   }
   if  (content.substring(1) == "46 DB 52 A3") 
   {
     lcd.setCursor(0, 0); // 設定游標位置在第一行行首
    lcd.print("333333");
    lcd.setCursor(0, 1); // 設定游標位置在第二行行首
    lcd.print("444444");
   }
     delay(3000);
 
} //main end
