int val = 0;
byte vMotor = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

pinMode(5, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
val = analogRead(A0);

vMotor = map(val, 0, 1023, 0, 255);

analogWrite(5, vMotor);

Serial.println(vMotor);


}
