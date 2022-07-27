#include <Servo.h>
Servo myservo;
Servo myservo1;
const int D0 = 2;       //Raspberry pin 27    LSB
const int D1 = 3;       //Raspberry pin 25
const int D2 = 4;       //Raspberry pin 23
const int D3 = 5;       //Raspberry pin 24    MSB

int sv1 = 11;
int led1 = 9;
int cam = 12;
int a,b,c,d,data;
int pos = 0;
void setup() {

pinMode(D0, INPUT_PULLUP);
pinMode(D1, INPUT_PULLUP);
pinMode(D2, INPUT_PULLUP);
pinMode(D3, INPUT_PULLUP);

pinMode(led1, OUTPUT);
pinMode(sv1,OUTPUT);
pinMode(cam,OUTPUT);
myservo1.attach(led1);
myservo.attach(cam);

}

void Data()
{
   a = digitalRead(D0);
   b = digitalRead(D1);
   c = digitalRead(D2);
   d = digitalRead(D3);

   data = 8*d+4*c+2*b+a;
}

void Servo1()
{
  myservo.write(0);// off cam
  
  }
void Servo2()
{
  myservo.write(122); // on cam
  }
void Servo3()
{
  myservo1.write(55); // chua phanh
  }
void Servo4()
{
  myservo1.write(15);// da phanh
  }
void Servo5()
{
  digitalWrite(sv1,HIGH); // den on
  }
void Servo6()
{
  digitalWrite(sv1,LOW); // den off
  }
void Servo7()
{
  myservo.write(70);
  }
void Servo8()
{
  myservo.write(80);
  }
void Servo9()
{
  myservo.write(90);
  }
void Servo10()
{
  myservo.write(100);
  }
void Servo11()
{
  myservo.write(112);
  }
void Servo12()
{
  myservo.write(114);
}
void Servo13()
{
  myservo.write(117);
  }
void Servo14()
{
  myservo.write(118);
  }
void Servo15()
{
  myservo.write(155);
  }
void Servo16()
{
  myservo.write(160);
  }
void Servo17()
{
  myservo.write(170);
  }
void Servo18()
{
  myservo.write(179);
  }



void LedPhai()
{
  digitalWrite(led1,HIGH);
  delay(1000);
  digitalWrite(led1,LOW);
  delay(1000);
  }

void loop()
{
  Data();
  if(data==1)
  {
    Servo1();
    }
  else if(data==2)
  {
    Servo2();
    }
  else if(data==3)
  {
    Servo3();
    }
  else if(data==4)
  {
    Servo4();
    }
  else if(data==5)
  {
    Servo5();
    }
  else if(data==6)
  {
    Servo6();
    }
  else if(data==7)
  {
    Servo7();
    }
  else if(data==8)
  {
    Servo8();
    }
  else if(data==9)
  {
    Servo9();
    }
  else if(data==10)
  {
    Servo10();
    }
  else if(data==11)
  {
    Servo11();
    }
  else if(data==12)
  {
    Servo12();
    }
  else if(data==13)
  {
    Servo13();
    }
  else if(data==14)
  {
    Servo14();
    }
  else if(data==15)
  {
    Servo15();
    }
  else if(data==16)
  {
    Servo16();
    }
  else if(data==17)
  {
    Servo17();
    }
  else
  {
    Servo18();
    }
  }
