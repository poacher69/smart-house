//需先上方Sketch->Include Libray->拉到最下看有沒tm1638-libray
//如果沒有Sketch->Include Libray->Add.ZIP libray

#include <TM1638.h>
// define a module on data pin 8, clock pin 7 and strobe pin 6
TM1638 module(8, 7, 6);  //定義DIO-8,CLK-7,STB-6
void setup() {

  // display a hexadecimal number and set the left 4 dots
  //module.setDisplayToHexNumber(0x1234ABCD, 0xF0);
   //module.setDisplayToHexNumber(0x1111, 0x00);//(16進位顯示,16進位小數點顯示位置)
    module.setDisplayToDecNumber(0, 0x00);//(10進位顯示,16進位小數點顯示位置)
}

void loop() {
  byte keys = module.getButtons();
  // light the first 4 red LEDs and the last 4 green LEDs as the buttons are pressed

  module.setLEDs(((keys & 0xF0) << 8) | (keys & 0xF));
  for (int i=0; i < 9999; i ++) 
   {
     module.setDisplayToDecNumber(i, 0x00);//(10進位顯示,16進位小數點顯示位置)
     delay(200);        //延遲
   }  

}
