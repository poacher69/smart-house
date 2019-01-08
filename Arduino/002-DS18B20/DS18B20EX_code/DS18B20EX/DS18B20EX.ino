//DS18B20溫度感知sensor +接5V,-接GND,OUT接Arduino第2腳
#include <OneWire.h>  // 匯入程式庫標頭檔 
#include <DallasTemperature.h>


#define ONE_WIRE_BUS 2  // Arduino數位腳位2(DIGITAL)接到OUT

// 運用程式庫建立物件
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
float val;
void setup(void)
{
  //Serial.begin(115200);
  Serial.begin(9600);      // 監控視窗波特率为9600
  Serial.println("Temperature Sensor start");
  sensors.begin();    // 初始化 
}

void loop(void)
{
  // 要求匯流排上的所有感測器進行溫度轉換（不過我只有一個） 
  sensors.requestTemperatures();//原始檔

  // 取得溫度讀數（攝氏）並輸出，
  
  //Serial.println(sensors.getTempCByIndex(0));//原始檔
  val = sensors.getTempCByIndex(0) ; // 參數0代表匯流排上第0個1-Wire裝置 
  Serial.println(val);//直接顯示溫度
  if(val > 26 && val <= 27)
  {
    Serial.println("溫度大於26度");
  }
    else if (val > 27 && val <= 28)
    {
     Serial.println("溫度大於27度");
    }
     else if (val > 28 && val <= 29)
    {
     Serial.println("溫度大於29度");
    }
     else if (val > 29 && val <= 30)
    {
     Serial.println("溫度大於30度");
    }
  
 
  delay(1000);
}
