int relay1 = 8; //继电器1导通触发信号-高电平有效； 
int relay2 = 9; //继电器2导通触发信号-高电平有效； 
void setup() 
{ 
  pinMode(relay1,OUTPUT); //定义端口属性为输出； 
  pinMode(relay2,OUTPUT); 
} 
void loop() 
{ 
  digitalWrite(relay1,HIGH); //继电器1导通； 
  digitalWrite(relay2,LOW); //继电器2开关断开；
  delay(1000); digitalWrite(relay1,LOW); //继电器1开关断开； 
  digitalWrite(relay2,HIGH); //继电器2导通； 
  delay(1000); 
}

