int Led=13;//定義LED接腳
int Shock=3;//定義震動傳感器接腳
int val; 
void setup()
{
  pinMode(Led,OUTPUT);//定義LED 為輸出接口
  pinMode(Shock,INPUT);//定義震動傳感器為輸出接口
}
void loop()
{
  val=digitalRead(Shock);//讀取震動傳感器數值送到val
  if(val==HIGH) digitalWrite(Led,LOW);  //當震動傳感器檢測有信號時, LED 閃爍
   else digitalWrite(Led,HIGH);
}



