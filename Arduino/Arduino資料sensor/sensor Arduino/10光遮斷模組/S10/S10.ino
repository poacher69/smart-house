int Led=13;//定義LED接口
int buttonpin=3; //定義光遮斷傳感器接口
int val;//定義數字變量val
void setup()
{
pinMode(Led,OUTPUT);//定義LED為輸出接口
pinMode(buttonpin,INPUT);//定義光遮斷傳感器為輸出接口
}
void loop()
{
val=digitalRead(buttonpin);//將數字接口3的值讀取賦給val
if(val==HIGH)//當光遮斷傳感器檢測有信號時, LED 閃爍
{
digitalWrite(Led,HIGH);
}
else
{
digitalWrite(Led,LOW);
}
}

