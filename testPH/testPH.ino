//const double m = -18.75;
//const double b = 15.53;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

float mapfloat(long x, long in_min, long in_max, long out_min, long out_max)
{
 return (float)(x - in_min) * (out_max - out_min) / (float)(in_max - in_min) + out_min;
}

void loop() {
  // put your main code here, to run repeatedly:
int x = analogRead(A0);
//double y = (x)* m + b;
float y = mapfloat(x, 0, 1023, 14, 0); 

Serial.print("ph waarde: ");
Serial.print(y);
Serial.println(" ");
}
