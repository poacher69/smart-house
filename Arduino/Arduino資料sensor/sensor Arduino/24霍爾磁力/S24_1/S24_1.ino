int Led=13;//定義LED 接口
int SENSOR=3;//定義霍爾磁力傳感器接口
int val;//定義數字變量val
void setup()
{
  pinMode(Led,OUTPUT);//定義LED 為輸出接口
  pinMode (SENSOR,INPUT);//定義霍爾磁力傳感器為輸出接口
}
void loop()
{
  val=digitalRead(SENSOR);//將數字接口3 的值讀取賦給val
  if(val==HIGH)//當霍爾磁力傳感器檢測有信號時, LED 亮
       { digitalWrite(Led, HIGH);}
  else { digitalWrite(Led, LOW); }
}

