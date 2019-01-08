//RFID     -3.3V-RST-GND-IRQ-MISO-MOSI-SCK-SDA ----RFID腳位接下方Arduino腳位
//接Arduino-3.3V-A0 -GND- 空-12  - 11 -13 -10  ----Arduino接腳
//////////////////////////////////////////////////////////////////////////

//RFID套件-start
#include <SPI.h>
#include <MFRC522.h>     // 引用程式庫 
#define RST_PIN      9        // 讀卡機的重置腳位
#define SS_PIN       10        // 晶片選擇腳位
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件
//RFID套件-end



void setup() {
  Serial.begin(9600);  // 設定串列通訊速率
  Serial.println("RFID-LCD reader is ready!");
  //RFID載入-start
  SPI.begin();   // 設定  SPI bus
  mfrc522.PCD_Init();   // 初始化MFRC522讀卡機模組
  //RFID載入-end

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
 
   Serial.println("Test1");
   }
   if  (content.substring(1) == "46 DB 52 A3") 
   {
      Serial.println("Test2");
   }
     delay(3000);
     
 
} //main end
