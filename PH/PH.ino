#include <Wire.h>

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Wire.begin(8);                // join i2c bus with address #8
Wire.onRequest(requestEvent); // register event

}

float mapfloat(long x, long in_min, long in_max, long out_min, long out_max)
{
 return (float)(x - in_min) * (out_max - out_min) / (float)(in_max - in_min) + out_min;
}

byte y;

void loop() {
  // put your main code here, to run repeatedly:
int x = analogRead(A0);
//double y = (x)* m + b;
y = map(x, 0, 1023, 255, 0); 

Serial.print("ph waarde: ");
Serial.print(y);
Serial.println(" ");
}

void requestEvent() {
  Wire.write(y); // respond with message of 6 bytes
  // as expected by master
}
