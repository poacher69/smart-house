//从接收部分代码
#include <IRremote.h>
int RECV_Pin = 11; //define input pin on Arduino
IRrecv irrecv(RECV_Pin);
decode_results results;
void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}
void loop() 
{
  if (irrecv.decode(&results)) 
  {
   Serial.println(results.value, HEX);
   irrecv.resume(); // Receive the next value
  }
}
